import datetime as dt
today = dt.datetime.today()

waktu = ''
if 4 <= today.hour < 10:
    waktu = 'Pagi'
elif 10 <= today.hour < 15:
    waktu = 'Siang'
elif 15 <= today.hour < 19:
    waktu = 'Sore'
else:
    waktu = 'Malam'