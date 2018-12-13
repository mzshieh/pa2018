import requests

res = requests.get('http://sip.einvoice.nat.gov.tw/ods-main/ODS308E/download/3886F055-EB77-4DF9-98E2-F3F49A7D3434/1/845E38D0-76D4-4B49-922A-96F41705F175/0/?fileType=csv')
rows = res.text.strip().split('\n')
rows = [row.strip('\ufeff').strip().split(',') for row in rows]

張數 = {}
金額 = {}
for row in rows[1:]:
    year = int(row[0].split('/')[0])
    if year < 2014 or year > 2017: continue
    行業類別 = row[1]
    張數.setdefault(行業類別, 0)
    張數[行業類別] += int(row[2])
    金額.setdefault(行業類別, 0)
    金額[行業類別] += int(row[3])

with open('task-4-4.csv','w') as out:
    for 行業類別 in 張數.keys():
        # print(行業類別,'之平均客單價:{:.2f}'.format(金額[行業類別]/張數[行業類別]))
        print(行業類別,'{:.2f}'.format(金額[行業類別]/張數[行業類別]),sep=",",file=out)

























