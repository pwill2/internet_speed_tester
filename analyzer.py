import csv
from matplotlib import pyplot

file_name = 'runs.csv'
all_data = []
download_data = []
upload_data = []
with open(file_name, mode='r', encoding='utf-8-sig') as f:
  r = csv.DictReader(f)
  for row in r:
    all_data_item = {}
    all_data_item['timestamp'] = row['Timestamp']
    all_data_item['download'] = float(row['Download Speed'])
    all_data_item['upload'] = float(row['Upload Speed'])
    all_data.append(all_data_item)

    download_data_item = {}
    download_data_item['timestamp'] = row['Timestamp']
    download_data_item['download'] = float(row['Download Speed'])
    download_data.append(download_data_item)

    upload_data_item = {}
    upload_data_item['timestamp'] = row['Timestamp']
    upload_data_item['upload'] = float(row['Upload Speed'])
    upload_data.append(upload_data_item)

print("Total Data Points:", len(all_data))

for download_data_dict in download_data:
  x = download_data_dict['timestamp']
  y = download_data_dict['download']
  pyplot.scatter(x,y)

pyplot.show()


for upload_data_dict in upload_data:
  x = upload_data_dict['timestamp']
  y = upload_data_dict['upload']
  pyplot.scatter(x,y)

pyplot.show()

sum_download = 0
for download_data_dict in download_data:
  sum_download = sum_download + download_data_dict['download']

# print(sum_download)
print("Average Download: ", sum_download / len(download_data))

sum_upload = 0
for upload_data_dict in upload_data:
  sum_upload = sum_upload + upload_data_dict['upload']

# print(sum_upload)
print("Average Upload: ", sum_upload / len(upload_data))