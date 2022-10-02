payload_configs_and_types = [
    {
        'key': 'product_category_id',
        'value': 1,
        'type': int,
        'required': True,
        'unique': False,
        'patch': False,
    },
    {
        'key': 'title',
        'value': 'Smart TV LED 43 - TEST Post_Inventory',
        'type': str,
        'required': True,
        'unique': False,
        'patch': True,
    },
    {
        'key': 'product_code',
        'value': 12345,
        'type': int,
        'required': True,
        'unique': True,
        'patch': False,
    },
    {
        'key': 'user_id',
        'value': 1,
        'type': int,
        'required': False,
        'unique': False,
        'patch': True,
    },
    {
        'key': 'value',
        'value': 1169.00,
        'type': float,
        'required': True,
        'unique': False,
        'patch': True,
    },
    {
        'key': 'brand',
        'value': 'Samsung',
        'type': str,
        'required': True,
        'unique': False,
        'patch': True,
    },
    {
        'key': 'template',
        'value': 'https://m.media-amazon.com/images/I/61-RpcaVQcL._AC_SL1000_.jpg',
        'type': str,
        'required': True,
        'unique': False,
        'patch': True,
    },
    {
        'key': 'description',
        'value': 'Samsung Smart TV 43 Crystal UHD 4K BU8000 2022 43',
        'type': str,
        'required': True,
        'unique': False,
        'patch': True,
    },
]

configs = {
    'url_base': '/inventory/',
    'url_product_code': '/inventory/1',
    'product_code': 1,
}


def headers(logged_in_client):
    return {'Authorization': f'Bearer {logged_in_client}'}


payload_just_values_and_keys = {}
for payload_config in payload_configs_and_types:
    payload_just_values_and_keys[payload_config['key']] = payload_config[
        'value'
    ]


def delete_keys_by_atribute(payload, atributo, valor):
    payload_deleted_keys = {}
    payload_base = [
        payload_config
        for payload_config in payload_configs_and_types
        if payload_config['key'] in payload.keys()
    ]
    payload_copy = payload.copy()
    for payload_config in payload_base:
        if payload_config[atributo] == valor:
            del payload_copy[payload_config['key']]
        else:
            payload_deleted_keys[payload_config['key']] = payload_config[
                'value'
            ]

    return payload_deleted_keys
