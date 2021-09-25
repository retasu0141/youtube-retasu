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
sheet_name2 = 'シート2'
csv_file_name = 'videos.csv'
csv_file_name2 = 'videos2.csv'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# スプレッドシートにアクセス
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(credentials)
sh = gc.open(file_name)
wks = sh.worksheet(sheet_name1)
wks2 = sh.worksheet(sheet_name2)

#CHANNEL_ID = 'UCFKOVgVbGmX65RxO3EtH3iw'

#ホロライブ

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

#にじさんじ
CHANNEL_ID_LIST2 = [
kuzuha = 'UCSFCh5NL4qXrAy9u-u2lX3g',
kanae = 'UCspv01oxUFf_MTSipURRhkA',
tsukino = 'UCD-miitqNY3nyukJ4Fnf4_A',
himawari = 'UC0g1AE0DOjBYnLhkgoRWN1w',
sasaki = 'UCoztvTULBYd3WmStqYeoHcA',
hoshikawa = 'UC9V3Y3_uzU5e-usObb6IE1w',
lize = 'UCZ1xuCK1kNmn5RzPYIZop3w',
ange = 'UCHVXbQzkl3rDfsXWo8xi2qw',
ars = 'UCdpUojq0KWZCN9bxXnZwz5w',
chihiro = 'UCLO9QDxVL4bnvRRsz6K4bsQ',
shiina = 'UC_4tXjqecqox5Uc05ncxpxg',
inui = 'UCXRlIK3Cw_TJIQC5kSJJQMg',
kizuku = 'UCKMYISTJAQ8xTplUPHiABlA',
ryushen = 'UCt5-0i4AVHXaWJrL8Wql3mw',
utako = 'UCwokZsOK_uEre70XayaFnzA',
mayuzumi = 'UCb5JxV6vKlYVknoJB8TnyYg',
kenmochi = 'UCv1fFr156jc65EMiLbaLImw',
kaede = 'UCsg-YqdqQ-KFF0LNk23BY4A',
mikoto = 'UCPvGypSgfDkVe7JG2KygK7A',
fuwa = 'UC6wvdADTJ88OfIbJYIpAaDA',
hayato = 'UCmovZ2th3Sqpd00F5RdeigQ',
debiru = 'UCjlmCrq4TP1I4xguOtJ-31w',
rion = 'UCV5ZZlLjk5MKGg3L0n0vbzw',
sukoya = 'UC8C1LLhBhf_E2IBPLSDJXlQ',
chima = 'UCo7TRj3cS-f_1D9ZDmuTsjw',
ibrahim = 'UCmZ1Rbthn-6Jm_qOGjYsh5A',
belmond = 'UCbc8fwhdUNlqi-J99ISYu4A',
akina = 'UCNW1Ex0r6HsWRD4LCtPwvoQ',
claire = 'UC1zFJrfEKvCixhsjNSb1toQ',
furen = 'UCuep1JCrMvSxOGgGhBfJuYw',
yorumi = 'UCL34fAoFim9oHLbVzMKFavQ',
gundou = 'UCeShTCVgZyq2lsBW9QwIJcw',
amamiya = 'UCkIimWZ9gBJRamKF0rmPU8w',
rin = 'UC6oDys1BGgBsIC3WhG1BovQ',
roa = 'UCCVwhI5trmaSxfcze_Ovzfw',
sociere = 'UCUc8GZfFxtmk7ZwSO7ccQ0g',
petit = 'UCIG9rDtgR45VCZmYnd-4DUw',
maimoto = 'UCJubINhCcFXlsBwnHp0wl_g',
melissa = 'UCwcyyxn6h9ex4sMXGtpQE_g',
chaika = 'UCsFn_ueskBkMCEyzCEqAOvg',
joe = 'UChUJbHiTVeGrSkTdBzVfNCQ',
shirayuki = 'UCuvk5PilcvDECU7dDZhQiEw',
hakase = 'UCGYAYLDE7TZiiC8U6teciDQ',
kaida = 'UCo2N7C-Z91waaR6lF3LL_jw',
gwelu = 'UC1QgXt46-GEvtNjEC1paHnw',
tamaki = 'UCBiqkFJljoxAj10SoP2w2Cg',
albio = 'UCIytNcoz4pWzXfLda0DoULQ',
doal = 'UC53UDnhAAYwvNO7j_2Ju1cQ',
uiha = 'UCnRQYHTnRLSF0cLJwMnedCg',
mashiro = 'UCfki3lMEF6SGBFiFfo9kvUA',
chigusa = 'UCkngxfPbmGyGl_RIq4FA3MQ',
yumeoi = 'UCTIE7LM5X15NVugV7Krp9Hw',
ririmu = 'UC9EjSJ8pvxtvPdxLOElv73w',
morinaka = 'UCtpB6Bvhs1Um93ziEDACQ8g',
naraka = 'UC-o-E6I3IC2q8sAoAuM6Umg',
levi = 'UCtnO2N4kPTXmyvedjGWdx3Q',
lain = 'UCRm6lqtdxs_Qo6HeL-SRQ-w',
alice = 'UCt0clH12Xk1-Ej5PXKGfdPA',
leos = 'UC-6rZgmxZSIbq786j3RD5ow',
meiji = 'UCveZ9Ic1VtcXbsyaBgxPMvg',
shellin = 'UCHBhnG2G-qN0JrrWmMO2FTA',
elu = 'UCYKP16oMX9KKPbrNgo_Kgag',
nagao = 'UCXW4MqCQn-jCaxlX-nn-BYg',
mao = 'UCerkculBD7YLc_vOGrF7tKg',
riri = 'UC48jH1ul-6HOrcSSfoR02fQ',
sakura = 'UCfQVs_KuXeNAlGa3fb8rlnQ',
genzuki = 'UCGw7lrT-rVZCWHfdG9Frcgg',
kanda = 'UCWz0CSYCxf4MhRKPDm220AQ',
lauren = 'UCgmFrRcyH7d1zR9sIVQhFow',
hayama = 'UCfipDDn7wY-C-SoUChgxCQQ',
emma = 'UCl1oLKcAq93p-pwKfDGhiYQ',
suzuki = 'UCryOPk2GZ1meIDt53tL30Tw',
hayase = 'UC2OacIzd2UxGHRGhdHl1Rhw',
uzuki = 'UC3lNFeJiTq6L3UWoz4g1e-A',
axia = 'UC8oPnditPSp5lZu45fnXWCA',
hisui = 'UCRqBKoKuX30ruKAq05pCeRQ',
sango = 'UCL_O_HXgLJx3Auteer0n0pA',
luisu = 'UCb6ObE-XGCctO3WrjRZC-cw',
fumi = 'UCwrjITPwG4q71HzihV2C7Nw',
shiba = 'UCmeyo5pRj_6PXG-CsGUuWWg',
onomachi = 'UCg63a3lk6PNeWhVvMRM_mrQ',
gaku = 'UCXU7YYxy_iQd3ulXyO-zC2w',
aizono = 'UC0WwEfE-jOM2rzjpdfhTzZA',
youko = 'UCBi8YaVyZpiKWN3_Z0dCTfQ',
mugi = 'UC_GCs6GARLxEHxy1w40d6VQ',
ichigo = 'UCmUjjW5zF1MMOhYUwwwQv9Q',
eli = 'UCpNH2Zk2gw3JBjWAKSyZcQQ',
karuta = 'UCllKI7VjyANuS1RXatizfLQ',
amemori = 'UCRWOdwLRsenx2jLaiCAIU4A',
seto = 'UCHK5wkevfaGrPr7j3g56Jmw',
oliver = 'UCqjTqdVlvIipZXIKeCkHKUA',
shibuya = 'UCeK9HFcRZoTrvqcUCtccMoQ',
moira = 'UCvmppcdYf4HOv-tFQhHHJMA',
kirame = 'UC_82HBGtvwN1hcGeOGHzUBQ',
yukishiro = 'UCHX7YpFG8rVwhsHCx34xt7w',
natsume = 'UCRcLAVTbmx2-iNcXSsupdNA',
suzuri = 'UCpnvhOIJ6BN-vPkYU9ls-Eg',
asahina = 'UCe_p3YEuYJb8Np0Ip9dk-FQ',
todoroki = 'UCRV9d6YCYIMUszK-83TwxVA',
gilzaren = 'UCUzJ90o1EjqUbk2pBAy0_aw',
azuti = 'UC6TfqY40Xt1Y0J-N18c85qQ',
asuka = 'UCiSRx1a2k-0tOg-fs6gAolQ',
naruse = 'UCoM_XmK45j504hfUWvN06Qg',
kohaku = 'UCebT4Aq-3XWb5je1S1FvR_A',
harusaki = 'UCtAvQ5U0aXyKwm2i4GqFgJg',
yaguruma = 'UCvzVB-EYuHFXHZrObB8a_Og',
tsumugu = 'UCufQu4q65z63IgE4cfKs1BQ'
]

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
                url_data = iframe_titel.attrs["href"]
                target = '?v='
                idx = url_data.find(target)
                video_id = url_data[idx+len(target):]
                #print(video_id)
                video_url = "https://youtu.be/" + video_id
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

infos = []

list_ = []
for CHANNEL_ID in CHANNEL_ID_LIST2:
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
                url_data = iframe_titel.attrs["href"]
                target = '?v='
                idx = url_data.find(target)
                video_id = url_data[idx+len(target):]
                #print(video_id)
                video_url = "https://youtu.be/" + video_id
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
videos.to_csv('videos2.csv', index=None)

sh.values_clear(f"{sheet_name2}!A1:F300")
wks2.update(list(csv.reader(open(csv_file_name2, encoding='UTF-8'))))
