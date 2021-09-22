import os
import time
import requests

import pandas as pd
import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import numpy as np
import lxml
from requests_html import HTMLSession

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

session = requests.Session()
#Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 '} #ユーザーエージェント情報
session = HTMLSession()



CHANNEL_ID_LIST = [sora,azuki,roboco,miko,suisei, mel,aki,haato,hubuki,matsuri ,akua,shion,ayame,tyoko,subaru ,mio,okayu,korone ,peko,rushia,hurea,noeru,marin ,kanata,watame,towa,luna ,lamy,nene,botan,polka]

infos = []

list_ = []
for CHANNEL_ID in CHANNEL_ID_LIST:
    time.sleep(3)
    url = 'https://www.youtube.com/channel/{}/videos'.format(CHANNEL_ID)
    r = session.get(url,headers=headers)
    #print(url)
    #soup = bs(r.html.html, "html.parser")
    id_list = []
    if r.status_code != 200:
        print('エラーで終わり')
        #break
    else:
        r.html.render(timeout=30)

        iframe_rows_titel = r.html.find("#video-title")
        #print(iframe_rows_titel)
        #iframe_rows_metadata = r.html.find("#metadata-line")
        for iframe_titel in iframe_rows_titel:
            data = iframe_titel.attrs["aria-label"]
            if "Streamed" in data:
                title = iframe_titel.attrs["title"]
                video_url = "https://www.youtube.com" + iframe_titel.attrs["href"]
                if "hours ago" in data:
                    print(data)
                    #print(title)
                    target = 'by '
                    idx = data.find(target)
                    ch_name_data = data[idx+len(target):]
                    target = "Streamed"
                    idx = ch_name_data.find(target)
                    ch_name = ch_name_data[:idx]
                    print(ch_name)

                    idx = data.find(target)
                    time_data = data[idx+len(target):]
                    target ="ago"
                    idx = time_data.find(target)
                    time_ = time_data[:idx]
                    print(time_)
                    idx = data.find(target)
                    v_time_data = data[idx+len(target):]
                    target ="minutes"
                    idx = v_time_data.find(target)
                    v_time = v_time_data[:idx+len(target)]
                    print(v_time)
                    target = v_time
                    idx = data.find(target)
                    viewCount = data[idx+len(v_time):]
                    if len(viewCount) >= 20:
                        target ="minute"
                        idx = v_time_data.find(target)
                        v_time = v_time_data[:idx+len(target)]
                        print(v_time)
                        target = v_time
                        idx = data.find(target)
                        viewCount = data[idx+len(v_time):]
                    print(viewCount)
                    id_list.append([ch_name,title,time_,v_time,viewCount,video_url])
            else:
                pass
                         #print(channelTitle+title+str(viewCount))
    list_.extend(id_list)
print("EXIT")
#print(list_)
videos = pd.DataFrame(list_, columns=['チャンネル名', '動画タイトル', '経過時間', '動画時間', '視聴回数', 'URL'])
videos.to_csv('videos.csv', index=None)

sh.values_clear(f"{sheet_name1}!A1:F300")
wks.update(list(csv.reader(open(csv_file_name, encoding='UTF-8'))))


