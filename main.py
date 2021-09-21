import os
import time
import requests

import pandas as pd
import datetime
from apiclient.discovery import build

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import numpy as np

dt_now = datetime.datetime.now()





# 設定
json_file = 'spreadsheet-326710-56876663fcc9.json'
file_name = 'youtube_list'
sheet_name1 = 'シート1'
csv_file_name = 'videos.csv'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# スプレッドシートにアクセス
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(credentials)
sh = gc.open(file_name)
wks = sh.worksheet(sheet_name1)

API_KEY = ""
#CHANNEL_ID = 'UCFKOVgVbGmX65RxO3EtH3iw'
#0期生
sora = 'UCp6993wxpyDPHUpavwDFqgg'
azuki = 'UC0TXe_LYZ4scaW2XMyi5_kw'
roboco = 'UCDqI2jOz0weumE8s7paEk6g'
miko = 'UC-hM6YJuNYVAmUWxeIr9FeA'
suisei = 'UC5CwaMl1eIgY8h02uZw7u8A'

#1期生
mel = 'UCD8HOxPs4Xvsm8H0ZxXGiBw'
aki = 'UCFTLzh12_nrtzqBPsTCqenA'
haato = 'UC1CfXB_kRs3C-zaeTG3oGyg'
hubuki = 'UCdn5BQ06XqgXoAxIhbqw5Rg'
matsuri = 'UCQ0UDLQCjY0rmuxCDE38FGg'

#2期生
akua = 'UC1opHUrw8rvnsadT-iGp7Cg'
shion = 'UCXTpFs_3PqI41qX2d9tL2Rw'
ayame = 'UC7fk0CB07ly8oSl0aqKkqFg'
tyoko = 'UC1suqwovbL1kzsoaZgFZLKg'
subaru = 'UCvzGlP9oQwU--Y0r9id_jnA'

#ゲーマーズ
mio = 'UCp-5t9SrOQwXMU7iIjQfARg'
okayu = 'UCvaTdHTWBGv3MKj3KVqJVCw'
korone = 'UChAnqc_AY5_I3Px5dig3X1Q'

#3期生
peko = 'UC1DCedRgGHBdm81E1llLhOQ'
rushia = 'UCl_gCybOJRIgOXw6Qb4qJzQ'
hurea = 'UCvInZx9h3jC2JzsIzoOebWg'
noeru = 'UCdyqAaZDKHXg4Ahi7VENThQ'
marin = 'UCCzUftO8KOVkV4wQG1vkUvg'

#4期生
kanata = 'UCZlDXzGoo7d44bwdNObFacg'
watame = 'UCqm3BQLlJfvkTsX_hvm0UmA'
towa = 'UC1uv2Oq6kNxgATlCiez59hw'
luna = 'UCa9Y57gfeY0Zro_noHRVrnw'

#5期生
lamy ='UCFKOVgVbGmX65RxO3EtH3iw'
nene = 'UCAWSyEs_Io8MtpY3m-zqILA'
botan = 'UCUKD-uaobj9jiqB-VXt71mA'
polka = 'UCK9V2B22uJYu3N7eR_BT9QA'





CHANNEL_ID_LIST = [sora,azuki,roboco,miko,suisei, mel,aki,haato,hubuki,matsuri ,akua,shion,ayame,tyoko,subaru ,mio,okayu,korone ,peko,rushia,hurea,noeru,marin ,kanata,watame,towa,luna ,lamy,nene,botan,polka]
youtube = build('youtube', 'v3', developerKey=API_KEY)
base_url = 'https://www.googleapis.com/youtube/v3'
url = base_url + '/search?key=%s&channelId=%s&part=snippet,id&order=date&maxResults=50'
infos = []

list_ = []
for CHANNEL_ID in CHANNEL_ID_LIST:
    response = requests.get(url % (API_KEY, CHANNEL_ID))
    id_list = []
    if response.status_code != 200:
        print('エラーで終わり')
        #break
    else:
        result = response.json()
        for item in result['items']:
             if item['id']['kind'] == 'youtube#video':
                 s = item['snippet']['publishedAt']
                 target = 'T'
                 idx = s.find(target)
                 day = s[:idx]
                 idx = s.find(target)
                 time = s[idx+1:]
                 time = time.replace('Z', '')
                 date_str = day+" "+time
                 tdatetime = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                 td = dt_now - tdatetime
                 if td.total_seconds() <= 86400:
                     response = youtube.videos().list(part = 'snippet,statistics',id = item['id']['videoId']).execute()
                     item = response.get("items", [])[0]
                     if item['snippet']['liveBroadcastContent'] == "none":
                         viewCount = item['statistics']['viewCount']
                         title = item['snippet']['title']
                         channelTitle = item['snippet']['channelTitle']
                         id = item['id']
                         id_list.append([channelTitle,title,str(viewCount),"https://youtu.be/"+id])
                         #print(channelTitle+title+str(viewCount))
    list_.extend(id_list)

videos = pd.DataFrame(list_, columns=['channelTitle', 'title', 'viewCount', 'url'])
videos.to_csv('videos.csv', index=None)

sh.values_clear(f"{sheet_name1}!A1:F300")
wks.update(list(csv.reader(open(csv_file_name, encoding='UTF-8'))))
