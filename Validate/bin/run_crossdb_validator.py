from datetime import datetime
from optparse import OptionParser

def get_options(parser):
    parser.add_option('-v', '--sqldb', dest ='sqldb', help='SQL database')
    parser.add_option('-s', '--elasticdb1', dest='elasticdb1', help='ES instance')

    (options, args)=parser.parse_args()
    return options

def check_options(options,parser):
    db_cnt=0
    for option in ['sqldb', 'elasticdb1']:
        if getattr(options,option) != None:
            db_cnt +=1
    for option in ['execute_only']:
        if getattr(options,option) == None:
            parser.error("YAML validation file is a mandatory option to run this script %s" %option)

def check_source_target_dbs(options, parser):
    for options in ['elasticdb1']:
        pass

def main():
    parser = OptionParser()
    options = get_options(parser)
    check_options(options,parser)
    check_source_target_dbs()


if __name__ == '__main__':
    start_time = datetime.now()