import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "jclaville93@gmail.com"
password = "lzpj nmzz bssg sstc"

receiver = "thenewlaville@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: You have a nice booty!
Booty Booty Booty
Rocking everywhere!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)