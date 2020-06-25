import os
from DB.bin.DB import DB
from DB.bin.ES import ES
import csv
import yaml
from datetime import datetime
from elasticsearch import Elasticsearch
from Utils.setup_logger import logger
import unittest
import pytest
from configparser import ConfigParser
import pandas as pd

class CrossDataValidator():
    def __init__(self,sqldb, elasticdb, email,request_type,testsuite ):
        super(CrossDataValidator,self).__init__()
        logger.info("Initilaized CrossDataValidator")
        self.sqldb=sqldb
        self.elasticdb=elasticdb
        self.email = email
        self.request_type=request_type
        self.testsuite=os.path.abspath(testsuite)
        self.writer = None
        logger.info("Making connection to DB")
        #Make connection to DB
        db_con = DB(host=self.sqldb)
        config = ConfigParser()
        report_file = os.path.abspath("outfile/DBCompareReport_" + str(datetime.now()) + ".xlsx")
        self.writer= pd.ExcelWriter(report_file,engine='xlsxwriter')



        # Make connection to ES
        logger.info("Making connection to ES")
        es_con = ES(host=self.elasticdb)

        #Start the execution based on the request_type
        if self.request_type=='environment_shakeout':
            config.read(self.testsuite)
            testcaseNames=config.sections()
            #testsuiteDict=print({s:dict(config.items(s)) for s in config.sections()})
            for row in testcaseNames:

                assert(db_con.get_row(config.get(row, 'db_query')), es_con.get_row(config.get(row, 'es_query')))






            #for row in testsuiteDict:
            #    print (row)

            #pd.DataFrame.from_dict(self.db_con(query),orient='columns'))















    # def __init__(self,srcdb=None, tgtdb=None, target_file_dir=None, exceptions=None, execute_only=None, print_only=False, srcdb_type=None, tgtdb_type=None, start_time=None):
    #     super(CrossDataValidator,self).__init__(debug)
    #     logger.info("")
    #     self.srcdb=srcdb
    #     self.tgtdb=tgtdb
    #     self.execute_only = execute_only
    #     self.print_only=print_only
    #     self.srcdb_type=srcdb_type
    #     self.tgtdb_type=tgtdb_type
    #     self.start_time=start_time
    #     self.summary=self.init_summary()
    #     self.src_release_label=None
    #     self.tgt_release_label = None
    #     self.passlist=[]
    #     self.completelist=[]
    #     self.target_file_dir=target_file_dir
    #     self.results_file_path= ("/".join(target_file_dir.split('/')[:-1])+'Deploy/log/AutomationData.csv')
    #     self.msgs=[]
    #     with open(("/".join(target_file_dir.split('/')[:-1])+'/DB/config/db_conf.yml'), 'r') as file:
    #         config_file = yaml.load(file, Loader=yaml.Loader)
    #     with open(self.results_file_path,'w') as newFile:
    #         newFileWriter = csv.writer(newFile)
    #         newFileWriter.writerow(['test_type','app', 'branch','env', 'exec_date','platform','duration','tc_count','tc_pass', 'tc_fail', 'report_location'])
    #
    #     if (srcdb_type=='es'):
    #         self.es_host = self.srcdb
    #     elif (srcdb_type=='es'):
    #         self.es_host = self.srcdb
    #
    #
    # def get_count(self):
    #     pass








