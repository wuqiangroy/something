#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from smtplib import SMTP
from poplib import POP3
import time

SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

OrigHdrs = ['From: wesley@python.is.cool',
            'TO: wesley@python.is.cool',
            'Subject: test msg',]
OrigBody = ['xxx', 'yyy', 'zzz']
OrigMsg = '\r\n\r\n'.join(['\r\n'.join(OrigHdrs), '\r\n'.join(OrigBody)])

# SMTP
SendSvr = SMTP(SMTPSVR)
errs = SendSvr.sendmail('wesley@python.is.cool',
                        ('wesley@python.is.cool',), OrigMsg)
SendSvr.quit()
assert len(errs) == 0, errs
# wait for mail to be delivered
time.sleep(10)

# POP3
RecvSvr = POP3(POP3SVR)
RecvSvr.user('wesley')
RecvSvr.pass_('youllNeverGuess')
rsp, msg, siz = RecvSvr.retr(RecvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
RecvSvrBody = msg[sep+1:]
# assert identical
assert OrigBody == RecvSvrBody

