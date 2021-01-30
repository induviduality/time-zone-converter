# Cross-time zone Converter and Reminder App
Save the APAC friendos. End time zone cruelty.

## What is this?
This is a time zone converter at present. My idea for Hack APAC is to make a cross-timezone reminder app that automatically converts timezones and sets a reminder. I believe this would be a desktop app of sorts. Run the `timedb.py` file to see the time converter in action! 

## Why did I build this?
I'm a newbie to hackathons and in my first hackathon (which was LHD: Build), people from the APAC region including myself were exhausted from catching up with the event being halfway across the Earth. I found myself and fellow APAC hackers pulling all-nighters just to show up at events at 2:00 am or 4:00 am. It was choas trying to catch up with events when you haven't slept for days. When HackAPAC came along, I took this chance to make an app that'd be an International Hacker's compass. Hence this Cross-timezone reminder app.

## How did I build this? 
I have always heard about APIs and the vast range of possibilities it opens up. Despite being a beginner, I decided to try out APIs and build something out of it. For this project, I have used 3 APIs.

 - http://worldtimeapi.org/
 - https://unixtime.co.za/
 - https://timezonedb.com/
 
I used the Timezonedb API to handle the conversions of time, as it'd be impossible for me to tackle each time zone manually. To use the API, I needed the origin and destination time zone data along with the time to convert as well. But the API was limited to returning only the Unix Timestamps of the converted time, so I needed help to convert the Timestamps to human readable time. I used the Unix Time API to accompolish this. 

## What else?
Currently, my project can convert between timezones. The recipient.json and send_email.py files are still under work. I'm trying to figure to create reminders and trigger an email. Yet to implement a reminder function and a GUI.
