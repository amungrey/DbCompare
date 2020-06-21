# DbCompare
Python based framework that allows to compare between any 2 types of the DB. This framework can be used for DB testing such as Data Warehourse or Data migration

/usr/local/mysql/bin/mysql -u root -p
Root1234

Elastic search
How to start
akshays-mbp:~ akshaymungrey$ cd Downloads/tools/elasticsearch-7.8.0/
akshays-mbp:elasticsearch-7.8.0 akshaymungrey$  cd bin $ ./elasticsearch


URL:
localhost:9200


Cars: data:
https://corgis-edu.github.io/corgis/csv/cars/


elasticsearch_loader --index cars --type cars csv ~/Downloads/tools/cars.csv

How to make 
csvsql --dialect mysql --snifflimit 100000  ~/Downloads/tools/cars.csv > maketable.sql



mysqlimport --ignore-lines=1 \
            --fields-terminated-by=, \
            --local -u root \
            -p test \
             cars.csv
