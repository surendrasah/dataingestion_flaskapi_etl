# Data Engineer Challenge

How you implement the challenge is up to you. The only requirements are that the code must run with minimal setup on our own machines and that the code is clean and well abstracted.

1. Create an ingestion system for two data streams. It must accept HTTP messages. Example files are provided for both streams. The first stream named 'metrics.json' is an example of machine data. The second, 'workorder.json', defines what product ran when and how much output was produced. Persist this data. (time relates the two data sources)

2. Create an ETL pipeline that reads the data from step 1, and finds the top three parameters that correlate to the production output of each product, and output them in a static report.

Document any design considerations and how to run your code.
You may use the provided files to test but your entire system will be tested on a different set of files.

## Steps to execute the program:

At first, delete the databaseb: data.db
Install the necessary libraries like Flask, flask_sqlalchemy, SQLAlchemy, requests

now run the ingestion program, then run post program and etl program.

python3 data_app_ingestion.py : web api flask server proram

python3 data_post_request.py : load the data to database using post request

python3 data_store_etl.py : Etl program to read the data and correlation between product and production output


