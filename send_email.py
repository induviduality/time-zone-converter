import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='abcxyz@gmail.com',
    to_emails='receiver@gmail.com',
    subject='Hello from the other side',
    html_content='<strong>I must have called a thousand times</strong>')

sg = sendgrid.SendGridAPIClient(api_key='totallyNotAnAPIKey')
response = sg.send(message)
print(response.status_code, response.body, response.headers)
