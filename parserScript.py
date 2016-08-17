#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#Parsing Log Information
with open("Log.txt", "r") as f:
    
    file = open(("LogParseado.txt"), 'w')   
    
    for line in f:
        parts = line.split('|')
        if(parts[0] == 'Failed'):                     
            #file.write("Status: " + parts[0] + " | " + "Test name: " + parts[1] + "\n")
            file.write(parts[1] + "\n")
                        
    file.write(parts[0]) #Last log line                               
            
                        
file.close()


#Automated sendmail
fromaddr = "mailToSend"
toaddr = "mailToReceive"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "mailSubject"
 

body = "Message to attach on body"
 
msg.attach(MIMEText(body, 'plain'))
filename = "LogParseado.txt"
attachment = open("LogParseado.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.Server', 587)
server.starttls()
server.login(fromaddr, "mailPassword")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
                    
