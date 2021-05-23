import pandas as pd
import psycopg2
import gspread
import datetime
import csv
import os
from oauth2client.service_account import ServiceAccountCredentials

# Connect to the database "dvdrental"
connection =psycopg2.connect(host='localhost',database='dvdrental',user='postgres',password='admin')

cursor = connection.cursor()
query ="select rental_id,inventory_id,customer_id from rental limit 5"
# Excecute The query
cursor.execute(query)
# fetch data using fetchall() function
rows = cursor.fetchall()
data = []
# Append list of rows to data
for row in rows:
    data.append([row[0],row[1],row[2]])

# Assign Headers for each column
headers = [i[0] for i in cursor.description]


if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

# Save Scope
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
# Create Service Account and connect to the sheet
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client = gspread.authorize(creds)
sheet = client.open('Rental').sheet1

# insert Headers for each column
sheet.insert_row(headers,1)
# Get length of rows in the sheet
x = len(sheet.get_all_values())
# Insert set of rows from x + 1
sheet.insert_rows(data,x+1)

