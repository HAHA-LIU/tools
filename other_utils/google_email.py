# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/10/26 11:00
# describe: 谷歌邮箱发送邮件
import smtplib

GMAIL_USERNAME = "LWYCAP@gmail.com"
GMAIL_PASSWORD = "lwy19961229"
email_subject = "Hello"
recipient = "1091761664@qq.com"
body_of_email = "hi"


# The below code never changes, though obviously those variables need values.
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                       "subject: " + email_subject,
                       "to: " + recipient,
                       "mime-version: 1.0",
                       "content-type: text/html"])

# body_of_email can be plaintext or html!
content = headers + "\r\n\r\n" + body_of_email
session.sendmail(GMAIL_USERNAME, recipient, content)
