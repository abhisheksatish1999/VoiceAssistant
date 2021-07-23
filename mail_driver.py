import smtplib, ssl

class send_mail_driver:
    def _init__(self):
       self.username=""
       self.password=""


    def credentials(self,username,password):
        self.username=username
        self.password=password

    def send(self,reciever_email,subject,message):
       compiled_message="""Subject: """+subject+"""\n\n"""+message
       context = ssl.create_default_context()
       #print("Trying to send with \n"+reciever_email+"\n"+compiled_message)
       try :
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, reciever_email, compiled_message)
            #print("Done")
            return tuple([1,"Email successfully sent"])
       except Exception as E:
            print(E)
            return tuple([0,E])









