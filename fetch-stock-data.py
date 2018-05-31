#!/usr/bin/env python3

import requests
import json
import prettytable
import random
import time
import pandas as pd
import time

from requests.auth import HTTPBasicAuth
from influxdb import InfluxDBClient
from datetime import date
from datetime import timedelta

from flask import Flask

app = Flask(__name__)

url_get_historical_data = 'https://api.intrinio.com/historical_data?identifier='
url_get_companies = 'https://api.intrinio.com/companies'
auth_user = '48e36a026502830319d748727218a21f'
auth_pass = 'f671948d2171caac783fa422dfa42bfe'
database_name = "demo"
companies_of_interest = ["AAC", "AAL", "AAMC", "AAME", "AAPL"]


#Fetch all companies available in intrino's API
request_obj = requests.get(url_get_companies, auth=HTTPBasicAuth(auth_user, auth_pass))
companies = json.loads(request_obj.text)

@app.route('/create-grafana-dashboard', methods = ['POST'])
def create_dashboard():
	request.headers['	

@app.route('/get-stocks-data')
def get_data():

	client = InfluxDBClient(host='localhost', port=8086)
	client.switch_database(database_name)
	
	#Read each of the 5 companies
	for company in companies_of_interest:

		#Initializing the start date of fetching stocks data to January 1st, 2010
		start_date = date(2015,1,1)
		
		#Initializing the end date to be 100 days from the start date as that's how much
		#data permits us to retrieve at a time
		end_date = start_date + timedelta(days = 100)
		
		for j in range(24):

			request_obj = requests.get(url_get_historical_data + company + '&item=pricetoearnings&start_date=' + str(start_date) + '&end_date=' + str(end_date), auth=HTTPBasicAuth(auth_user, auth_pass))

			json_data = json.loads(request_obj.text)
			series = []

			print (len(json_data["data"]))

			for i in range(len(json_data["data"])):
		
				stock_value = 0.0
				print("{} {}\n".format(json_data["data"][i]["date"], json_data["data"][i]["value"]))

				try:
				    stock_value = float(json_data["data"][i]["value"])
				except ValueError:
				    print("Not a number found.. continuing")
				    continue

				pointValues = {
				    "time": json_data["data"][i]["date"],
				    "measurement": 'stocks5',
				    "tags": {
					"Symbol" : company,
				    },
				    "fields": {
					"Stock" : company,
					"Stock Value" : stock_value
				    }
				}
				series.append(pointValues)

			print(series)
			client.write_points(series)
			print ("Data written to InfluxDB to database demo and series stocks {} {}".format(company,len(series)))
			start_date = end_date
			end_date = end_date + timedelta(days = 30)
			time.sleep(1)
		
	return ("Stocks data has been written to InfluxDB.")


if __name__ == '__main__':
	app.run(debug=True)
