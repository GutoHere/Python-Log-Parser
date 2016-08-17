#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#Parseando as informacoes do Log
with open("Log.txt", "r") as f:
    
    file = open(("LogParseado.txt"), 'w')   
    
    for line in f:
        parts = line.rsplit('|', 3)
        if(parts[3] == 'Failed\r\n'):                     
            #file.write("Status: " + parts[0] + " | " + "Teste: " + parts[1] + "\n")
            file.write(parts[0] + "\n")
        #print parts                
    #file.write(parts[0]) #Ultima linha do log                               
            
            
            

file.close()

''' 
#Envio de email automatico
fromaddr = "luizgf@inatel.br"
toaddr = "rogerio.chagas@inatel.br"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "EOC/CIR Regression Testing Results - Develop Branch"
 
body = "Bom dia Rogerio," + "\n" + "Segue o log anexado do Full Stack." + "\n" + "Att," + "\n" + "Luiz Gustavo"
 
msg.attach(MIMEText(body, 'plain'))

filename = "LogParseado.txt"
attachment = open("LogParseado.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromaddr, "132511lgf")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


'''                    
            
