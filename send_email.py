# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='induja.shankar@gmail.com',
    to_emails='induja.exe@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = sendgrid.SendGridAPIClient(api_key='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')
response = sg.send(message)
print(response.status_code, response.body, response.headers)