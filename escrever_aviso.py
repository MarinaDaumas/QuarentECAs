import simplejson as json


nome_e = "Lucio Costa"
cpf = "167.876.352-14"

# tratar dados
cpf = cpf.replace('.', '')
cpf = int(cpf.replace('-', ''))
telefone = int(telefone)

aviso = {"nome": nome, "cpf": cpf}


file_name = "novo_aviso.json"

with open(file_name, 'w ') as outfile:
    json.dump(aviso, outfile)