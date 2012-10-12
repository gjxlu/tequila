#!/usr/bin/env python
import getpass, imaplib,pyttsx

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login("gjxlu92@gmail.com", getpass.getpass())
M.select()
typ, data = M.search(None, '(UNSEEN)')
for num in data[0].split():
        typ, data = M.fetch(num, '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')
        message = data[0][1].lstrip('Subject: ').strip()
        print message
        engine=pyttsx.init()
        engine.say(message)
        engine.runAndWait()
M.close()
M.logout()
