import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email = "hh.covid.alerta@gmail.com"
receiver_email = "luisa42.rodrigues@gmail.com"
#thiagomoutinho19@poli.ufrj.br
message = MIMEMultipart("alternative")
msg = msg_content = MIMEText('send with attachment...', 'plain', 'utf-8')
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "hh.covid.alerta@gmail.com"
password = "covidzada"



text = """\
Caro fulano, 

	Nós do grupo Covid Alerta gostariamos de informar que no dia DATA você esteve em contato com um caso confirmado deCOVID-19 por meio de uma entrega realizada à(s) HORA
 	É necessário redobrar seus cuidados de isolamento pelos próximos HOJE-ENTREGA dias, até mesmo dentro de sua casa, para que a doença não seja transmitida. 

	Fique antento aos sintomas nos próximos dias, que podem incluir:

	-Febre
	-Dor no Corpo 
	-Tosse 
	-Dificuldade Respiratória

	Para mais informações sobre a doença e procedimentos, acessar o site abaixo:

	https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente


	Nosso projeto visa a sua segurança e bem estar, assim como daqueles próximos a você. Sua participação é essencial para que possamos vencer o coronavírus e voltar à normalidade o mais rápido possivel. Mais detalhes sobre nosso projeto e nossas parcerias podem ser encontradas por meio de nosso site, encaminhado abaixo.
	
	Contamos com sua ajuda,
	Covid Alerta."""

html ="""<html>
<body>
    <img src="https://pngimage.net/wp-content/uploads/2018/05/cidade-alerta-png-2.png" alt="Logo" title="Logo" style="display:block" width="200" height="87" /> 
    <p>Caro Thiago,<br>
    Nós do grupo Covid Alerta gostariamos de informar que no dia 23/05 você esteve em contato com um caso confirmado de COVID-19 por meio de uma entrega realizada à(s) 13:00 em sua residência.<br>
    Em vista disso, é necessário redobrar seus cuidados de isolamento pelos próximos 15 dias, até mesmo dentro de sua casa, para que a doença não seja transmitida. 
	Fique antento aos sintomas nos próximos dias, que podem incluir:<br>
    </p>
    <ul>
	<li> Febre </li>
	<li> Dor no Corpo </li>
	<li> Tosse </li> 
	<li> Dificuldade Respiratória </li>
    </ul>

	<p>Para mais informações sobre a doença e procedimentos, acessar o site abaixo:</p> <br>

	<a href="https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente">Informativo SUS</a><br>

    <p>Nosso projeto visa a sua segurança e bem estar, assim como daqueles próximos a você. Sua participação é essencial para que possamos vencer o coronavírus e voltar à normalidade o mais rápido possivel. Mais detalhes sobre nosso projeto e nossas parcerias podem ser encontradas por meio de nosso site, encaminhado abaixo.</p><br>
    <a href="https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente"> Nosso Site </a><br> 
  </body>
</html>"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)


# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 