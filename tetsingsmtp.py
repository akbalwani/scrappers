import smtplib, ssl

port = 1025  # For SSL
smtp_server = "localhost"
sender_email = "arpitbalwani.ab@gmail.com"  # Enter your address
receiver_email = "arpitbalwani.ab@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)