
def send_aviso():
    nome_e = "Lucio Costa"
    cpf = "167.876.352-14"

    # tratar dados
    cpf = cpf.replace('.', '')
    cpf = int(cpf.replace('-', ''))

    aviso = {"nome": nome_e, "cpf": cpf}

    return aviso