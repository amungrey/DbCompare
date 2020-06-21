from elasticsearch import Elasticsearch
import configparser
import os

class ES:
    def __init__(self,host=None, config=os.path.abspath("DB/es.conf"), es_index=None, es_doc_type=None, es_query=None):
        self.host= host
        self.config=config
        self.es_index=es_index
        self.es_doc_type = es_doc_type
        self.es_query = es_query
        self.get_options()
        self.connect_to_es()

    def get_options(self):
        parser = configparser.RawConfigParser()
        parser.read(self.config)
        if self.host != None:
            self.es_index = parser.get(self.es_index,'es_index')
            self.es_doc_type = parser.get(self.es_doc_type, 'es_doc_type')
        else:
            for attr in ['host','es_index', 'es_doc_type']:
                setattr(self,attr,None)
        self.parser=parser

    def connect_to_es(self):
        results = []
        Connection = Elasticsearch([{'host': self.host, 'port': 9200}])
        response = Connection.search(index=self.es_index, doc_type=self.es_doc_type, body=self.es_query)
        output = response['hits'].get('total')

        if (isinstance(output, int)):
            es_result = output
        else:
            for doc in output:
                results.append(doc)
            es_result = results[0].get('version')
        return es_result;




