from unittest import TestCase

from app.controllers.login import login


class TestLogin(TestCase):

    def test_login(self):
        self.assertEqual(login(), 'hello world bottle')
