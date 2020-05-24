import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def mandar_email():
    sender_email = "hh.covid.alerta@gmail.com"
    receiver_email = "luisa42.rodrigues@gmail.com" #email
    #thiagomoutinho19@poli.ufrj.br
    message = MIMEMultipart("alternative")
    message['subject']= "Covid alerta tem um aviso para você"
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "hh.covid.alerta@gmail.com"
    password = "covidzeca"

    nome = "thiaguinho"
    data = "20/05"
        
    text = """\
    Caro """ + nome + """,

        Nós do grupo Covid Alerta gostariamos de informar que no dia """ + data + """ você esteve em contato com um caso confirmado de COVID-19 por meio de uma entrega realizada em sua residência.
        Em vista disso, é necessário redobrar seus cuidados de isolamento pelos próximos 15 dias (ou pelo menos 15 dias desde a entrega), até mesmo dentro de sua casa, para que a doença não seja transmitida. 

        Fique antento aos sintomas nos próximos dias, que podem incluir:

        -Febre
        -Dor no Corpo 
        -Tosse 
        -Dificuldade Respiratória

        Para mais informações sobre a doença e procedimentos, acessar o site abaixo:

        https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente


        É importante também lembrar que as empresas, restaurantes, entregadores e etc, não carregam a culpa da transmissão.
        O novo Coronavirus é uma doença altamente contagiosa e pode ser pega até mesmo por aqueles que tomam os devidos cuidados.
        Esses trabalhadores estão se arriscando para que ainda possamos ter acesso a aquilo que precisamos e nós devemos ter respeito pela coragem deles.
        
        Nosso projeto visa a sua segurança e bem estar, assim como daqueles próximos a você. Sua participação é essencial para que possamos vencer o coronavírus e voltar à normalidade o mais rápido possivel. 
        Mais detalhes sobre nosso projeto e nossas parcerias podem ser encontradas por meio de nosso site, encaminhado abaixo.

        https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente


        Agradecemos sua colaboração,
        Equipe Covid Alerta."""

    html = """\
    <html>
    <head style= "background-color: #e8eded;">
    <style>
    div {
        width: 550px;
        margin-left:auto;
        margin-right:auto;
    }
    .caro
    {
        margin-left: 3%;
        font-size: 17px;
    }

    </style>


    <body style="font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;  font-size:15px; color:#000000; background-color:#e8f1fc">
    <div style= "text-align: center;"> VAMOS VENCER O CORONA! </div>
    <div>
        <div style="margin: 0 auto;"> <img src="https://i.ibb.co/SsS57pW/capa-logo-tamanho-novo.png" alt="Logo" title="Logo" style="display:block" width="550" height="170" /></div><br>

        <div class="caro" style= "font-weight: bold; margin-left: 4%;"> Caro """ + nome + """,</div> 
        <p style="text-align: left; margin: 5%;">
        Nós do grupo Covid Alerta gostariamos de informar que no dia """ + data + """ você esteve em contato com um caso confirmado de COVID-19 por meio de uma entrega realizada em sua residência.<br>
        Em vista disso, é necessário redobrar seus cuidados de isolamento pelos próximos 15 dias (ou pelo menos 15 dias desde a entrega), até mesmo dentro de sua casa, para que a doença não seja transmitida. 
        Fique antento aos sintomas nos próximos dias, que podem incluir:<br>
        </p>
        <div style= "font-weight: bold; margin-left: 6%;">
        <ul>
        <li> Febre </li>
        <li> Dor no Corpo </li>
        <li> Tosse </li> 
        <li> Dificuldade Respiratória </li>
        </ul> 
        </div>

        <p style="text-align: left; margin: 5%;">Para mais informações sobre a doença e procedimentos, acessar o site abaixo:</p>
    
        <a href="https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente" style="text-align: left; margin-left: 10%; font-weight: bold; text-size: 30px;"> Informativo Covid-19
        </a><br>

        <p style="text-align: left; margin: 5%;"> É importante também lembrar que as empresas, restaurantes, entregadores e etc, não carregam a culpa da transmissão.
        O novo Coronavirus é uma doença altamente contagiosa e pode ser pega até mesmo por aqueles que tomam os devidos cuidados.
        Esses trabalhadores estão se arriscando para que ainda possamos ter acesso a aquilo que precisamos e nós devemos ter respeito pela coragem deles.</p>
        <p style="text-align: left; margin: 5%;"> Nosso projeto visa a sua segurança e bem estar, assim como daqueles próximos a você. Sua participação é essencial para que possamos vencer o coronavírus e voltar à normalidade o mais rápido possivel. 
        Mais detalhes sobre nosso projeto e nossas parcerias podem ser encontradas por meio de nosso site, encaminhado abaixo.</p>
        <a href="https://coronavirus.saude.gov.br/sobre-a-doenca#se-eu-ficar-doente" style="text-align: left; margin-left: 10%; font-weight: bold; text-size: 30px;"> Nosso Site </a> <br> 

        <p style="text-align: left; margin: 5%;"> Agradecemos sua solaboração, <br>
        Equipe Covid Alerta.</p><br>
        </div>
    </body>

    </head>
    </html>
    """

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
mandar_email()