#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


def _format_add(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header("name", "utf-8").encode(),
        addr,
    ))

mail_text = """
<h2>This is a hewen email!</h2>
<h2>Python is a fucking useful coding language.</h2>
"""

SENDER = "wuqiangroy@live.com"
PASSWORD = os.getenv("password")
RECEIVER = "wuqiangroy@gmail.com"
SMTP_SERVER = "smtp-mail.outlook.com:587"

msg = MIMEMultipart()
msg["from"] = _format_add("A Pythonnor<{}>".format(SENDER))
msg["To"] = _format_add("A Fucking Study man<{}>".format(RECEIVER))
msg["subject"] = Header("Welcome to coding world!").encode()
msg.attach(MIMEText(mail_text, "html", "utf-8"))

# 添加附件

mime = MIMEText(open("/home/wq/work_test/hewen.txt", "rb").read(), "base64", "utf-8")
# 设置发送出去附件的格式
mime["Content-Type"] = "application/octet-stream"
mime["Content-Disposition"] = "attachment; filename = 'hewen.txt'"
msg.attach(mime)

server = smtplib.SMTP(SMTP_SERVER)
server.ehlo()
server.starttls()
try:
    server.login(SENDER, PASSWORD)
    server.sendmail(SENDER, RECEIVER, msg.as_string())
    print("send mail successful")
except Exception as e:
    print("debug", e)
finally:
    server.close()

