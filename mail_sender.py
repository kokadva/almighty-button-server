import ssl
import smtplib

def send_main():
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "almightybuttoninfo@gmail.com"
    sender_password = "ASDasd123."
    receiver_email = "cdval13@freeuni.edu.ge"
    message = 'Gasswore davalebebi daidos qulebi'
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        return {"Message": "Mail has been sent."}
    except Exception as e:
        print(e)
        return {"Message": "Error occurred while sending mail."}
    finally:
        server.quit()