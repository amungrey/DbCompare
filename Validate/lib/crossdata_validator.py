import os
from DB.bin.DB import DB
from DB.bin.ES import ES
from datetime import datetime
from elasticsearch import Elasticsearch
from Utils.setup_logger import logger
from configparser import ConfigParser
import pandas as pd
from Utils.send_email_util import send_mail

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
        try:

            #Make connection to DB
            db_con = DB(host=self.sqldb)
            config = ConfigParser()
            report_file = os.path.abspath("outfile/DBCompareReport_" + str(datetime.now()) + ".xlsx")
            self.writer= pd.ExcelWriter(report_file,engine='xlsxwriter')

            #Read the testsuite
            config.read(self.testsuite)
            testcaseNames = config.sections()
            testResults = []

            #Start the execution based on the request_type
            if self.request_type=='environment_shakeout':
                # Make connection to ES
                logger.info("Making connection to ES")
                es_con = ES(host=self.elasticdb)

                #testsuiteDict=print({s:dict(config.items(s)) for s in config.sections()})
                for row in testcaseNames:
                    db_result = db_con.get_row(config.get(row, 'db_query'))['value']

                    es_result = es_con.get_row(config.get(row, 'es_query'))
                    if db_result==es_result:
                        test_result = "PASS"
                    else:
                        test_result = "FAIL"
                    testResults.append({'test_case_id' : row,'db_query': config.get(row, 'db_query'),'db_result' : db_result, 'es_query':config.get(row, 'es_query'), 'es_result': es_result, 'test_result': test_result})
                logger.info(testResults)
            es_con.transport.connection_pool.close()
            db_con.close()

            if self.request_type == 'data_integrity':
                for row in testcaseNames:
                    db_result = db_con.get_row(config.get(row, 'db_query'))['value']

                    testResults.append({'test_case_id': row, 'db_query': config.get(row, 'db_query'), 'db_result': db_result})
                logger.info(testResults)

            db_con.close()

        except:
            testResults.append({'error':'issue with the connections'})

        finally:
            pd.DataFrame.from_dict(testResults, orient='columns')
            send_mail('DBCompare','DBCompare', self.email,[report_file] )









            #for row in testsuiteDict:
            #    print (row)

            #pd.DataFrame.from_dict(self.db_con(query),orient='columns'))





















