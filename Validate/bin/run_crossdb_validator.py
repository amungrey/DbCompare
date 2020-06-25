from datetime import datetime
from optparse import OptionParser
from Validate.lib.crossdata_validator import CrossDataValidator

def get_options(parser):
    parser.add_option('-v', '--sqldb', dest ='sqldb', help='SQL database')
    parser.add_option('-s', '--elasticdb', dest='elasticdb', help='ES instance')
    parser.add_option('-f', '--email', type='string', action='callback', callback=option_callback)
    parser.add_option('-t','--request_type', dest='request_type', help='request_type',default='')
    parser.add_option('-z', '--testsuite', dest='testsuite', help='path of the testsuite like Validate/testsuite/carsSuite.conf')

    (options, args)=parser.parse_args()
    return options

def option_callback(option, opt, value, parser):
    setattr(parser.values, option.dest,value.split(','))


def check_options(options,parser):
    for option in ['sqldb']:
        if getattr(options,option) != None:
            parser.error("Missing required argument %s" %option)
    for option in ['elasticdb']:
        if getattr(options,option) != None:
            parser.error("Missing required argument %s" %option)
    for option in ['testsuite']:
        if getattr(options,option) != None:
            parser.error("Missing required argument %s" %option)


# def check_options(options,parser):
#     db_cnt=0
#     for option in ['sqldb', 'elasticdb1']:
#         if getattr(options,option) != None:
#             db_cnt +=1
#     for option in ['execute_only']:
#         if getattr(options,option) == None:
#             parser.error("YAML validation file is a mandatory option to run this script %s" %option)
#     if((db_cnt==0) or (db_cnt > 2)):
#         parser.error("You have to give one or two databases to run this script:\n %s" % options)
#
#
# def check_source_target_dbs(options, parser):
#     for option in ['elasticdb1']:
#         if getattr(options,option) != None:
#             elasticdb_cnt +=1

def main():
    parser = OptionParser()
    options = get_options(parser)
    #check_options(options,parser)
    #check_source_target_dbs(options,parser)

    d= CrossDataValidator(
        sqldb=options.sqldb,
        elasticdb=options.elasticdb,
        email=options.email,
        request_type=options.request_type,
        testsuite=options.testsuite
         )


if __name__ == '__main__':
    start_time = datetime.now()
    main()
