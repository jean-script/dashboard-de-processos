


#  validações
def campo_vazio(campo):
    return not campo.strip()

def senha_nao_sao_iguais(senha, senha2):
    return senha != senha2
   