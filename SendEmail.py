import smtplib

class emailconfig:
    def sendemail(msg):
       server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
       #Next, log in to the server
       server.login("abc@gmail.com", "*****")

       #Send the mail
       server.sendmail("*******@gmail.com", "abc@gmail.com", msg) 
       return "Email Sent. Bon Appetit!"