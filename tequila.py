#!/usr/bin/env python
import getpass, imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login("gjxlu92@gmail.com", getpass.getpass())
M.select()
typ, data = M.search(None, '(UNSEEN)')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])
M.close()
M.logout()
