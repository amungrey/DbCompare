import os
from DB.bin.DB import DB
import csv
import yaml
from datetime import datetime
from elasticsearch import Elasticsearch
from Utils.setup_logger import logger
import unittest

class CrossDataValidator():
    def __init__(self,srcdb=None, tgtdb=None, target_file_dir=None, exceptions=None, execute_only=None, print_only=False, srcdb_type=None, tgtdb_type=None, start_time=None):
        super(CrossDataValidator,self).__init__(debug)
        logger.info("")
        self.srcdb=srcdb
        self.tgtdb=tgtdb
        self.execute_only = execute_only
        self.print_only=print_only
        self.srcdb_type=srcdb_type
        self.tgtdb_type=tgtdb_type
        self.start_time=start_time
        self.summary=self.init_summary()
        self.src_release_label=None
        self.tgt_release_label = None
        self.passlist=[]
        self.completelist=[]
        self.target_file_dir=target_file_dir
        self.results_file_path= ("/".join(target_file_dir.split('/')[:-1])+'Deploy/log/AutomationData.csv')
        self.msgs=[]
        with open(("/".join(target_file_dir.split('/')[:-1])+'/DB/config/db_conf.yml'), 'r') as file:
            config_file = yaml.load(file, Loader=yaml.Loader)
        with open(self.results_file_path,'w') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(['test_type','app', 'branch','env', 'exec_date','platform','duration','tc_count','tc_pass', 'tc_fail', 'report_location'])

        if (srcdb_type=='es'):
            self.es_host = self.srcdb
        elif (srcdb_type=='es'):
            self.es_host = self.srcdb


    def get_count(self):
        pass







