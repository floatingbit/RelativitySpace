#!/usr/bin/env python3

import requests
import json
import prettytable
import random
import time
import pandas as pd

from requests.auth import HTTPBasicAuth
from influxdb import InfluxDBClient
from datetime import date

from flask import Flask

app = Flask(__name__)

url_get_historical_data = 'https://api.intrinio.com/historical_data?identifier='
url_get_companies = 'https://api.intrinio.com/companies'
url_
auth_user = '48e36a026502830319d748727218a21f'
auth_pass = 'f671948d2171caac783fa422dfa42bfe'
database_name = "demo"
company_counter = 0

request_obj = requests.get(url_get_companies, auth=HTTPBasicAuth(auth_user, auth_pass))
companies = json.loads(request_obj.text)

@app.route('/get-stocks-data')
def get_data():

	global company_counter
	global companies

	client = InfluxDBClient(host='localhost', port=8086)
	client.switch_database(database_name)
	
	#Read the next 10 company names 
	for i in range(10):

		request_obj = requests.get(url_get_historical_data + companies["data"][company_counter]["ticker"] + '&item=pricetoearnings&start_date=2015-01-01&end_date=2018-01-01', auth=HTTPBasicAuth(auth_user, auth_pass))

		json_data = json.loads(request_obj.text)
		series = []

		print (len(json_data["data"]))

		for i in range(len(json_data["data"])):
		
			stock_value = 0.0
		
			try:
			    stock_value = float(json_data["data"][i]["value"])
			except ValueError:
			    print("Not a number found.. continuing")
			    continue

			pointValues = {
			    "time": json_data["data"][i]["date"],
			    "measurement": 'stocks4',
			    "tags": {
				"Symbol" : companies["data"][company_counter]["ticker"],
			    },
			    "fields": {
				"Stock" : companies["data"][company_counter]["ticker"],
				"Stock Value" : stock_value
			    }
			}
			series.append(pointValues)

		print(series)
		client.write_points(series)
		company_counter = company_counter + 1
		print ("Data written to InfluxDB to database demo and series stocks {} {} {}".format(companies["data"][company_counter]["ticker"], companies["data"][company_counter]["name"],len(series)))
		
	return ("Stocks data has been written to InfluxDB.")


if __name__ == '__main__':
	app.run(debug=True)
