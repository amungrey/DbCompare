# DbCompare
Python based framework that allows to compare between any 2 types of the DB. This framework can be used for DB testing such as Data Warehourse or Data migration

To test this on your local, you will need MYSQL and Elastic search:

#How to install and Run MYSQL:
https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html

Once the pkg file downloaded and installed , run:
/usr/local/mysql/bin/mysql -u root -p
Root1234

#How to install Elastic search on local:
https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html

#How to start the ES server:
akshays-mbp:~ akshaymungrey$ cd Downloads/tools/elasticsearch-7.8.0/
akshays-mbp:elasticsearch-7.8.0 akshaymungrey$  cd bin $ ./elasticsearch

The below URL will host the ES on your local:
localhost:9200

To test the data across the ES and Mysql, you will need some sample data
Downlaod the Cars data:
https://corgis-edu.github.io/corgis/csv/cars/

#How to upload the csv to your ES server:
elasticsearch_loader --index cars --type cars csv ~/Downloads/tools/cars.csv

#How to make the MYSQL table per CSV:
csvsql --dialect mysql --snifflimit 100000  ~/Downloads/tools/cars.csv > maketable.sql

#How to load the data to Mysql :
mysqlimport --ignore-lines=1 \
            --fields-terminated-by=, \
            --local -u root \
            -p test \
             cars.csv
