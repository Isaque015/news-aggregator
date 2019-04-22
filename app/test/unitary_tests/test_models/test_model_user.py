from test_base import BaseTest

from app.models.user import User


class TestModelUser(BaseTest):

    def test_save_user(self):
        user = User()
        user.name = 'isaque'
        user.nickname = 'primeiroTeste'
        user.last_name = 'felizardo'
        user.email = 'segundoTeste@segundoTeste.com'
        user.password = 'sasasa'

        esperado = {'status': True, 'msg': 'user save success'}
        resposta_teste = user.save()
        self.assertEqual(resposta_teste, esperado)

    def test_save_fields_exists_unique_true(self):
        user = User()
        user.name = 'isaque'
        user.nickname = 'primeiro_teste_unique'
        user.last_name = 'felizardo'
        user.email = 'primeirounique@primeirounique.com'
        user.password = 'sasasa'
        user.save()

        duplicate_nickname_user = User()
        duplicate_nickname_user.name = 'isaque'
        duplicate_nickname_user.nickname = 'primeiro_teste_unique'
        duplicate_nickname_user.last_name = 'felizardo'
        duplicate_nickname_user.email = 'unique_two@unique.com'
        duplicate_nickname_user.password = 'sasasa'
        duplicate_nickname_user.save()

        esperado = {
            'status': False,
            'msg': 'the primeiro_teste_unique already exists in nickname'
        }

        resposta_teste = duplicate_nickname_user.save()
        self.assertEqual(resposta_teste, esperado)

        duplicate_nickname_user.nickname = 'segundo_teste_unique'
        duplicate_nickname_user.email = 'primeirounique@primeirounique.com'

        esperado['msg'] = 'the primeirounique@primeirounique.com already exists in email'

    def test_save_user_without_fields_with_nullable_false(self):

        user = User()
        user.name = 'isaque'
        user.last_name = 'felizardo'
        user.email = 'terceiroTeste@terceiroTeste.com'
        user.password = 'sasasa'

        esperado = {
            'status': False,
            'msg': 'nickname not allow blank'
        }

        resposta = user.save()

        self.assertEqual(resposta, esperado)

        user_without_email = User()
        user_without_email.name = 'isaque'
        user_without_email.nickname = 'test_without_email'
        user_without_email.last_name = 'felizardo'
        user_without_email.password = 'sasasa'

        esperado['msg'] = 'email not allow blank'
        resposta = user_without_email.save()

        self.assertEqual(resposta, esperado)

        user_without_password = User()
        user_without_password.name = 'isaque'
        user_without_password.nickname = 'test_without_password'
        user_without_password.email = 'test_without_password@test.com'
        user_without_password.last_name = 'felizardo'

        esperado['msg'] = 'password not allow blank'
        resposta = user_without_password.save()

        self.assertEqual(resposta, esperado)

    def test_save_with_wrong_email(self):
        user = User()
        user.name = 'isaque'
        user.nickname = 'primeiro_teste_email'
        user.last_name = 'felizardo'
        user.email = '@primeiro_teste_email.com'
        user.password = 'sasasa'

        esperado = {
            'status': False,
            'msg': 'Invalid email, subdomain is empty'
        }

        resposta = user.save()
        self.assertEqual(resposta, esperado)

        user.email = 'primeiro_teste_email@'
        esperado['msg'] = 'Invalid email, domain is empty'

        resposta = user.save()
        self.assertEqual(resposta, esperado)

        user.email = 'primeiro_teste_email@primeiro_teste_email'
        esperado['msg'] = 'Invalid domain'

        resposta = user.save()
        self.assertEqual(resposta, esperado)

        user.email = 'primeiro_teste_emailprimeiro_teste_email'
        esperado['msg'] = 'Invalid email, no @'

        resposta = user.save()
        self.assertEqual(resposta, esperado)
