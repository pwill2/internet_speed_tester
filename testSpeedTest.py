#! /Users/parkerwilliams/.virtualenvs/speedtester/bin/python

import speedtest
from datetime import datetime
import time
from csv import writer

def append_list_as_row(file_name, data):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(data)

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

start_time = time.time()
st = speedtest.Speedtest()
best_server = st.get_best_server()
download = st.download()
upload = st.upload()
execution_time = (time.time() - start_time)

file_name = '/Users/parkerwilliams/Desktop/speedtester/runs.csv'
data = [dt_string, round(download/1000000, 2), round(upload/1000000, 2), best_server['url'], best_server['lat'], best_server['lon'], best_server['name'], best_server['country'], best_server['sponsor'], best_server['id'], best_server['latency'], str(round(execution_time, 2))]

append_list_as_row(file_name, data)

# print('Data written to file.')
# * * * * * /Users/parkerwilliams/.virtualenvs/speedtester/bin/python /Users/parkerwilliams/Desktop/speedtester/testSpeedTest.py > /Users/parkerwilliams/Documents/python_cron_jobs/cron/cron.txt