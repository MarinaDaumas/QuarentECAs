# Covid Alerta - 2020
### QuarentECAs / Logística

![logo](https://i.ibb.co/QNWdW5d/logo-sem-bolaa.png)

#### Apresentação 

Com  necessidade de distanciamento social decorrente da pandemia da doença pelo novo coronavirus (Covid-19), as pessoas passaram a recorrer a serviços de entrega para os mais variados produtos. Embora seja uma solução mais segura do que sair à rua para compras, existe um risco de contágio decorrente do contato com o entregador e objetos que são compartilhados por ambos, como as máquinas de cartão de crédito.

Se o entregador apresentar sintomas compatíveis com a Covid-19, é importante que seja imediatamente afastado do trabalho e que os clientes que tiveram contato com ele a partir de 2¹ dias antes do início dos sintomas sejam notificados.
O isolamento dos casos e daqueles que estiveram em contato, mesmo sem apresentar sintomas, é comprovadamente uma das medidas mais efetivas para combater o avanço do novo coronavírus.
O objetivo do Covid-Alerta é alertar aqueles que estiveram em contato com pessoas infectadas para que possam avaliar seu risco de infecção e assim tomar os cuidados necessários para seu própria saúde e proteger aqueles que amam, iniciando o autoisolamento e monitoramento de sintomas, quando indicado.



#### O Produto

O nosso serviço é voltado para empresas, de qualquer ramo, que trabalhem com entregadores. Com um sistema simples, realizamos algo único no mercado, auxiliando empresas no controle da epidemia, reconhecendo seu comprometimento com essa causa.  O sistema é dividido em três partes:

- 1ª Parte

Utilizando nosso servidor, as empresas nos mandam mensagens informando sobre novas entregas ou novos casos suspeitos de Covid entre seus entregadores.

- 2ª Parte

Com essas mensagens, atualizamos nosso banco de dados e resgatamos o contato de clientes que tiveram contato com o entregador até 2 dias antes do início dos sintomas. 

- 3ª Parte 

É enviado automaticamente um email para esses clientes, informando sobre o ocorrido e dando orientações.


#### Informações adicionais 



A vantagem para a empresa consiste em ser reconhecida pela sua transparência e respeito ao consumidor, através do recebimento do Selo de Comprometimento de Combate ao Covid.




#### Instruções para teste do MVP

Siga os passos abaixo para testar:

- 1°- Baixe ou clone o repositório em uma pasta
- 2°- Abra duas abas do seu terminal e entre na pasta em que está o arquivo
- 3°- Abra o seu visualizador de código e vá no final do código de client.py e escolha qual função deseja fazer inicialmente
- 4°- Volte para os terminais e digite em um o seguinte comando:
    - python3 server.py
    - Ele te dará um ip que deve ser copiado e colado no arquivo client.py na linha que tem escrito server='algum numero' e que não está comentada
    - Após isso cancele o processo no seu terminal e rode de novo o mesmo comando
    - No segundo terminal digite o seguinte comando:
        python3 client.py
    - Após preencher a primeira vez,volte em client.py, descomente a última linha e comente a de cima então rode o comando à cima no segundo terminal
 
 Obs: Deve ser utilizado o python 3 para rodar os arquivo, além disso pode ser que no seu computador só seja necessário escrever py na hora de digitar o código



#### Bibliografia

1 - [OMS, Cosiderations in the investigation of cases and clusters of COVID-19](https://apps.who.int/iris/bitstream/handle/10665/331668/WHO-2019-nCoV-cases_clusters_investigation-2020.2-eng.pdf?sequence=1&isAllowed=y)
 

2 -[Estadão, Pessoas não diagnosticadas com novo coronavírus são as maiores responsáveis por disseminar a pandemia](https://saude.estadao.com.br/noticias/geral,pessoas-nao-diagnosticadas-com-novo-coronavirus-sao-as-maiores-responsaveis-por-disseminar-epidemia,70003235348)
