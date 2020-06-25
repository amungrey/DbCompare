import json, ast
from optparse import OptionParser
from datetime import datetime
from elasticsearch import Elasticsearch



def get_options():
    parser=OptionParser()
    parser.add_option('-s', '--es-host', dest='es_host', help='ES host name')
    parser.add_option('-o', dest='es_output', help='ES Output file name')
    (options, args) = parser.parse_args()

    for arg in required_args():
        if getattr(options, arg) is None:
            parser.error('Missing required argument %s' %arg)

    return options

def required_args():
    return ['es_host']

if __name__ == '__main__':
    start_time = datetime.now()
    options = get_options()



