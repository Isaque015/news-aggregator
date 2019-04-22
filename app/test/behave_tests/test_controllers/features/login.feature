# language:pt

Funcionalidade: login


Cenário: nickname vazio
    Dado que irei fazer login no sistema
    Quando fazer um login sem nickname na url "/login"
    Então a resposta deve ser
    """
    {
        "code": 401,
        "msg": "the nickname field can not be empty",
        "status": False
    }
    """
