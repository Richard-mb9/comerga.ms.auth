create_user_validator = {
    'nome': {
        'type': 'string',
        'required': True
    },
    'email': {
        'type': 'string',
        'required': True
    },
    'senha': {
        'type': 'string',
        'required': True
    },
    'sobrenome': {
        'type': 'string',
        'required': True
    }
}

list_coins_validator = {
    'name': {
        'type': 'string'
    }
}

calculate_price_validator = {
    'from': {
        'type': 'string',
        'required': True
    },
    'to': {
        'type': 'string',
        'required': True
    },
    'amount': {
        'type': 'number',
        'required': True
    }
}