# mandar email 
#teste
# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# create message object instance
class Send():
    def sendMessage(self,senha,email):
        

        msg = MIMEMultipart()
        
        message = "Caro" + nome + "Nós do grupo Covid Alerta gostariamos de informar que no dia" + data + "você esteve em contato com um caso confirmado de COVID-19 por meio de uma entrega realizada à(s)" + hora + ".Deve-se redobrar os cuidados de isolamento pelos proximos" + HJ-ENTREGA+ "dias. Fique antento aos sintomas nos próximos dias e siga as instruções da OMS" + link + 
        
        # setup the parameters of the message
        password = "covidzada"
        msg['From'] = "hh.covid.alerta@gmail.com"
        msg['To'] = email
        msg['Subject'] = "A Covid Alerta tem um aviso para você."
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        server.quit()
        
        print ("successfully sent email to %s:" % (msg['To']))