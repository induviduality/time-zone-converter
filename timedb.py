import requests
import time
import json

#API key LL848IAQ75FZ
from requests.models import Response

r = requests.get("http://worldtimeapi.org/api/timezone")

count = 1
for i in range(0, len(r.json())):
    if count < 5:
        print(str(i+1)+". "+r.json()[i].ljust(30), end="\t")
        count += 1
    else:
        if count == 5:
            print(i, ".", r.json()[i])
            count = 1

from_ind = int(input('\n\nEnter serial number of origin time zone: '))
from_index = from_ind - 1
to_ind = int(input('Enter serial number of destination time zone: '))
to_index = to_ind - 1

in_time_date = str(input('Enter origin date and time in "yyyy-mm-dd hh:mm:ss": '))
date_time_obj = time.strptime(in_time_date, '%Y-%m-%d %H:%M:%S')
conv_in_time = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date={0}".format(in_time_date))
#input time converted to unix timestamp

r2 = requests.get("http://api.timezonedb.com/v2.1/convert-time-zone?key=LL848IAQ75FZ&format=json&from={0}&to={1}&time={2}".format( r.json()[from_index], r.json()[to_index], conv_in_time.json()))
incomplete_out_time = r2.json()
#time is converted but it is considered as GMT although it is actually the desired output

r3 = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/fromunixtimestamp?UnixTimeStamp={0}".format(incomplete_out_time["toTimestamp"]))
conv_out_time = r3.json() #formatting the time without any timezone data

print('When it is', in_time_date, 'in', r.json()[from_index], 'it is', conv_out_time['Datetime'], 'in', r.json()[to_index])


