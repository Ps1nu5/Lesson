import wget
import requests
import time

# with open('target.txt', 'r') as file:
#     url = file.read()
download_url = 'https://ayaznal.ru'



# wget.download(url, 'output.txt')
# time.sleep(5)



target_line = ''
target_list = []
with open('output.txt', 'rb') as f:
    for char in f.read().decode('utf-8'):
        target_line += char

target_list = target_line.split('\n')

urls_str = ''
for line in target_list:
    if 'photoUrls: ' in line:
        urls_str = '{'+line.replace('photoUrls', '"photoUrls"')+'}'

print(urls_str)
urls_str = urls_str.replace('null', '"null"')

urls_dict = eval(urls_str)
urls_dict = urls_dict['photoUrls']['1']
print(urls_dict)
finally_complete_fucking_parser = []
for i in urls_dict:
    finally_complete_fucking_parser.append(i[1])

print(finally_complete_fucking_parser)

urls_list = finally_complete_fucking_parser

for i in urls_list:
    wget.download(download_url+i)