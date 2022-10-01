payload_configs_and_types = [
    {
        "key": "product_category_id",
        "value": 1,
        "type": int,
        "required": True,
        "unique": False,
    },
    {
        "key": "title",
        "value": "Smart TV LED 43 - TEST Post_Inventory",
        "type": str,
        "required": True,
        "unique": False,
    },
    {
        "key": "product_code",
        "value": 12345,
        "type": int,
        "required": True,
        "unique": True,
    },
    {"key": "user_id", "value": 1, "type": int, "required": False, "unique": False},
    {
        "key": "value",
        "value": 1169.00,
        "type": float,
        "required": True,
        "unique": False,
    },
    {
        "key": "brand",
        "value": "Samsung",
        "type": str,
        "required": True,
        "unique": False,
    },
    {
        "key": "template",
        "value": "https://m.media-amazon.com/images/I/61-RpcaVQcL._AC_SL1000_.jpg",
        "type": str,
        "required": True,
        "unique": False,
    },
    {
        "key": "description",
        "value": "Samsung Smart TV 43 Crystal UHD 4K BU8000 2022 43",
        "type": str,
        "required": True,
        "unique": False,
    },
]

payload_just_values_and_keys = {}
for payload_config in payload_configs_and_types:
    payload_just_values_and_keys[payload_config["key"]] = payload_config["value"]