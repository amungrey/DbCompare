from elasticsearch import Elasticsearch
import configparser
import os

class ES:
    def __init__(self,host=None, es_port=None, config=os.path.abspath("DB/config/es.conf")):
        self.host= host
        self.es_port=es_port
        self.config=config
        #self.es_index=es_index
        #self.es_doc_type = es_doc_type
        #self.es_query = es_query
        self.get_options()
        self.connect_to_es()

    def get_options(self):
        parser = configparser.RawConfigParser()
        parser.read(self.config)
        if self.host != None:
            self.es_port=parser.get(self.host,'es_port')
            self.es_index = parser.get(self.host,'es_index')
            self.es_doc_type = parser.get(self.host, 'es_doc_type')
        else:
            for attr in ['host','es_port','es_index', 'es_doc_type']:
                setattr(self,attr,None)
        self.parser=parser

    def connect_to_es(self):
        if self.host != None:
            self.connection = Elasticsearch([{'host': self.host, 'port': self.es_port}])

    def get_row(self,es_query):

        results = []
        response = self.connection.search(index=self.es_index, doc_type=self.es_doc_type, body=es_query)
        #response = self.connection.search(index=es_index, doc_type=es_doc_type, body=es_query)
        output = response['hits'].get('total')
        output=output['value']

        if (isinstance(output, int)):
            es_result = output
        else:
            for doc in output:
                results.append(doc)
            es_result = results[0].get('version')
        return es_result;





