# Covid Alerta - 2020
### QuarentECAs / Logística

![logo](https://i.ibb.co/QNWdW5d/logo-sem-bolaa.png)

#### Apresentação 

Com  necessidade de distanciamento social decorrente da pandemia da doença pelo novo coronavirus (Covid-19), as pessoas passaram a recorrer a serviços de entrega para os mais variados produtos. Embora seja uma solução mais segura do que sair à rua para compras, existe um risco de contágio decorrente do contato com o entregador e objetos que são compartilhados por ambos, como as máquinas de cartão de crédito.

Se o entregador apresentar sintomas compatíveis com a Covid-19, é importante que seja imediatamente afastado do trabalho e que os clientes que tiveram contato com ele a partir de 2¹ dias antes do início dos sintomas sejam notificados.
O isolamento dos casos e daqueles que estiveram em contato, mesmo sem apresentar sintomas, é comprovadamente uma das medidas mais efetivas para combater o avanço do novo coronavírus.
O objetivo do Covid-Alerta é alertar aqueles que estiveram em contato com pessoas infectadas para que possam avaliar seu risco de infecção e assim tomar os cuidados necessários para seu própria saúde e proteger aqueles que amam, iniciando o autoisolamento e monitoramento de sintomas, quando indicado.



#### O Produto

O nosso serviço é voltado para empresas, de qualquer ramo, que trabalhem com entregadores. Com um sistema simples, realizamos algo único no mercado, auxiliando empresas no controle da epidemia, reconhecendo seu comprometimento com essa causa. O sistema é dividido em três partes:

- 1ª Parte

Utilizando nosso servidor, as empresas nos mandam mensagens informando sobre novas entregas ou novos casos suspeitos de Covid entre seus entregadores.

- 2ª Parte

Com essas mensagens, atualizamos nosso banco de dados e resgatamos o contato de clientes que tiveram contato com o entregador até 2 dias antes do início dos sintomas. 

- 3ª Parte 

É enviado automaticamente um email para esses clientes, informando sobre o ocorrido e dando orientações.


#### Informações adicionais 



A vantagem para a empresa consiste em ser reconhecida pela sua transparência e respeito ao consumidor, através do recebimento do Selo de Comprometimento de Combate ao Covid.

![selo](https://i.ibb.co/1J7J6zJ/selo-ECA-de-Qualidade.png)




#### Instruções para teste do MVP

Exemplo do que aconteceria no caso de um entregador doente logo após a entrega de um pedido.

Siga os passos abaixo para testar:

- 1°- Baixe ou clone o repositório em uma pasta.
- 2°- Abra duas abas do seu terminal.
- 3°- Escreva em um terminal o seguinte comando, ele retornará seu ip que será necessário na próxima etapa.
     - OBS: a forma do número é XXX.X.X.X.
```bash 
python3 server.py

```
- 4°- Abra o outro terminal, digite o seguinte código e responda as perguntas esses dados serão os dados do cliente.
```bash
python3 client.py
```
- 5°- Ao final desse proscesso você deve receber um email com o aviso.

 Obs1: Deve ser utilizado o python 3 para rodar os arquivo, além disso pode ser que no seu computador só seja necessário escrever py na hora de digitar o código.

 Obs2: Para editar outros dados, como os dados do entregador, modifique as funções escrever_aviso.py ou escrever_pedido.py


#### Bibliografia

1 - [OMS, Cosiderations in the investigation of cases and clusters of COVID-19](https://apps.who.int/iris/bitstream/handle/10665/331668/WHO-2019-nCoV-cases_clusters_investigation-2020.2-eng.pdf?sequence=1&isAllowed=y)
 

2 -[Estadão, Pessoas não diagnosticadas com novo coronavírus são as maiores responsáveis por disseminar a pandemia](https://saude.estadao.com.br/noticias/geral,pessoas-nao-diagnosticadas-com-novo-coronavirus-sao-as-maiores-responsaveis-por-disseminar-epidemia,70003235348)


