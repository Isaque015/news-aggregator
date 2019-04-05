from unittest import TestCase, main

from app import app


class BaseTest(TestCase):

    def setUp(self):
        self.app = app
        self.app.config['sqlite.db'] = 'sqlite:////tmp/sqlite.db'


if __name__ == '__main__':
    main()
