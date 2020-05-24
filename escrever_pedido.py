import simplejson as json
from datetime import date


nome_c = "Marcos Andrade"
email = "marcos.andr@hotmail.com"
telefone = 5521985009719

nome_e = "Lucio Costa"
cpf = "167.876.352-14"

# tratar dados
cpf = cpf.replace('.', '')
cpf = int(cpf.replace('-', ''))
telefone = int(telefone)

pedido = {"data": date.today(), "cliente":[nome_c, email, telefone], "entregador":[nome_e, cpf]}


file_name = "novo_pedido.json"

with open(file_name, 'w ') as outfile:
    json.dump(pedido, outfile)

 
 





