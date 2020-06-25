import pymysql
import configparser
import pymysql.cursors
import os

class TooManyRowsException(Exception):
    def __init__(self,sql, num_rows):
        self.sql=sql
        self.num_rows = num_rows

    def __str__(self):
        error_msg = 'Expected one row from SQL %s got %s' %(self.sql, self.num_rows)
        return repr(error_msg)


class SQLExecutionException(object):
    def __init__(self, sql, db_error):
        self.sql = sql
        self.db_error = db_error

    def __str__(self):
        error_msg = 'Expected %s for SQL %s' %(self.db_error, self.sql)
        return repr(error_msg)


class DB:
    def __init__(self,host=None, config=os.path.abspath("DB/config/db.conf"), db_name=None, db_port=None, ssl=None):
        self.host= host
        self.config=config
        self.db_name=db_name
        self.db_port = db_port
        self.ssl = ssl
        self.get_options()
        self.connect_to_mysql_db()

    def get_options(self):
        parser = configparser.RawConfigParser()
        parser.read(self.config)
        if self.host != None:
            self.user = parser.get(self.host,'user')
            self.passwd = parser.get(self.host, 'passwd')
            if self.db_name:
                self.database = self.db_name
            else:
                self.database = parser.get(self.host, 'db')
        else:
            for attr in ['host','user', 'database','passwd']:
                setattr(self,attr,None)
        self.parser=parser

    def connect_to_mysql_db(self):
        if self.host != None:
            self.db= pymysql.connect(host=self.host,
                                     user=self.user,
                                     passwd=self.passwd,
                                     db=self.database,
                                     port=self.db_port,
                                     ssl=self.ssl)
        else:
            self.db = None

    def get_cursor(self):
        db=self.db
        if db !=None:
            return db.cursor(pymysql.cursors.DictCursor)
        else:
            print("No db object found")

    def execute(self,sql):
        rv = -1
        try:
            cur = self.get_cursor()
            cur.execute('BEGIN')
            cur.execute(sql)
            self.db.commit()
            rv = 0
        except Exception as e:
            self.db.rollback()
            raise SQLExecutionException(sql,e)
        return rv

    def execute_without_commit(self,sql):
        rv = -1
        try:
            cur = self.get_cursor()
            cur.execute(sql)
            rv = 0
        except Exception as e:
            self.db.rollback()
            raise SQLExecutionException(sql,e)
        return rv

    def commit(self):
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()

    def executemany(self,sql,list):
        rv = -1
        try:
            cur = self.get_cursor()
            cur.executemany(sql,list)
            self.db.commit()
            rv = 0
        except Exception as e:
            self.db.rollback()
            raise SQLExecutionException(sql,e)
        return rv

    def get_rows(self, sql):
        data = []
        datareal = []
        try:
            cur = self.get_cursor()
            cur.execute(sql)
            for row in cur.fetchall():
                if isinstance(row,dict):
                    datareal.append(dict(row))
                data.append(row)
        except Exception as e:
            raise SQLExecutionException(sql,e)
        self.db.commit()
        return data

    def get_row(self, sql):
        rows = self.get_rows(sql)
        if len(rows) > 1:
            raise TooManyRowsException(sql, len(rows))
        elif len(rows) == 1:
            return rows[0]
        else:
            return {}

    def list_config_hosts(self):
        for host in self.parser.sections():
            print(host)

    def close(self):
        try:
            cur =self.get_cursor()
            cur.execute(sql)
        except Exception as e:
            raise SQLExecutionException(sql,e)
        self.db.commit()
        

    