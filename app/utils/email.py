from re import match


def tratar_email(normalize_email):

    def validar_email(self, *args):
        email_funcao_decorada = getattr(self, 'email')
        email_e_valido = {}

        if not email_funcao_decorada:
            email_e_valido['status'] = False
            email_e_valido['msg'] = 'E-mail esta vazio'
        else:

            resultado_match_email = match(
                r'^([\w\.\-]+)@([\w]+)(\.)(\w*)((\.(\w*))?)$',
                email_funcao_decorada
            )

            if resultado_match_email:
                email_e_valido['status'] = True
                email_e_valido['msg'] = 'E-mail é valido'

            elif '@' in email_funcao_decorada:
                nick, domain_name = email_funcao_decorada.split('@')

                if not domain_name:
                    email_e_valido['status'] = False
                    email_e_valido['msg'] = 'E-mail invalido, não tem dominio'

                elif '.' not in domain_name:
                    email_e_valido['status'] = False
                    email_e_valido['msg'] = 'Dominio invalido'
            else:
                email_e_valido['status'] = False
                email_e_valido['msg'] = 'E-mail invalido, não tem @'

        return normalize_email(self, email_e_valido)

    return validar_email
