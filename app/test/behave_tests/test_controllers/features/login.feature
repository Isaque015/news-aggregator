# language:pt

Funcionalidade: login


Cenário: nickname vazio
    Quando fazer um login no sistema
    """
    {
        "nickname": "",
        "password": 123
    }
    """
    Então a resposta deve ser
    """
    {
        "code": 401,
        "msg": "the nickname field can not be empty",
        "status": false
    }
    """


Cenário: password vazia
    Quando fazer um login no sistema
    """
    {
        "nickname": "teste",
        "password": ""
    }
    """
    Então a resposta deve ser
    """
    {
        "code": 401,
        "msg": "the password field can not be empty",
        "status": false
    }
    """


Cenário: Usuario não existe
    Dado que o usuário teste não exista
    Quando fazer um login no sistema
    """
    {
        "nickname": "teste",
        "password": "123456"
    }
    """
    Então a resposta deve ser
    """
    {
        "code": 404,
        "msg": "User not found",
        "status": false
    }
    """


Cenário: Senha incorreta
    Dado que o usuário teste1 exista
    Quando fazer um login no sistema
    """
    {
        "nickname": "teste1",
        "password": "123456"
    }
    """
    Então a resposta deve ser
    """
    {
        "code": 404,
        "msg": "Wrong password",
        "status": false
    }
    """

Cenário: Autenticação correta
    Dado que o usuário teste1 exista
    Quando fazer um login no sistema
    """
    {
        "nickname": "teste1",
        "password": "123456789"
    }
    """
    Então a resposta deve ser
    """
    {
        "code": 200,
        "msg": "User has been logged in",
        "status": true
    }
    """
