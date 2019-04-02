from re import search, findall


class GetErrorException(object):

    def unique_constraint(self, erro):
        msg_search = search(
            r'(\([\w|\.|\@]+\))=(\([\w|@|\.]+\))+([\s|\w]+\.)',
            erro
        ).group()

        msg_list = findall(r'[\w|\@|\.]+', msg_search)
        msg = ' '.join(msg_list)
        return msg

    def nullable_contraint(self, erro):
        msg_search = search(r'("[\w]+")', erro).group()
        msg_list = findall(r'[\w]+', msg_search)
        msg = ''.join(msg_list)
        msg = f'o campo {msg} não pode estar vazio'
        return msg

    def despacho_func(self, erro):
        if 'unique' in erro:
            resposta = self.unique_constraint(erro)
        elif 'null' in erro:
            resposta = self.nullable_contraint(erro)
        return resposta
