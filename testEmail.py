import smtplib
import json

with open('recipentList.json') as data_file:    
    recipentList = json.load(data_file)

sender = "test@gmail.com" # Your email address
password = "password" # Your password for your email

for recipentEmail in recipentList:
    recipient = recipentEmail["email"]
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(sender, password)

    subject = "Test email from Python" # Email subject
    text = recipentEmail["salutation"] + " Test Body message" # Email main message. Edit the Test body message portion

    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_server.sendmail(sender, recipient, message)
smtp_server.close()
