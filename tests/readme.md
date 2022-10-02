# Execução de testes da aplicação
A presente aplicação conta com uma suíte de testes para os principais endpoints, veja-se:

# Configurações
Para rodar os testes é necessário que a aplicação esteja devidamente instalada e o ambiente de banco de dados configurados para os testes.
Para instalação da aplicação:

    poetry install && poetry run flask db init && poetry run flask db migrate && poetry run flask db upgrade && poetry run flask populate_db
ou via Makefile

    Make install && Make db
Para rodar os testes, os comandos abaixos devem ser utilizados:

    poetry run pytest -v
ou, também via Makefile:

    make test

|Testes Disponíveis|
|--|
| test_app_not_is_name_failed |
|test_config_is_loaded |
|test_request_returns_404| 
|test_get_inventory_success_status_200| 
|test_get_inventory_fail_with_invalid_token| 
|test_get_inventory_results_success_status_200 |
|test_get_inventory_success_with_name_filter| 
|test_get_inventory_fail_invalid_with_name_not_found| 
|test_get_inventory_success_with_paginate_validate| 
|test_get_inventory_fail_with_paginate_invalid| 
|test_get_inventory_success_with_item_in_company| 
|test_get_inventory_success_with_item_in_user| 
|test_get_inventory_with_item_in_user_keys_requireds| 
|test_get_inventory_num_items_in_page| 
|test_get_inventory_without_paginate| 
|test_get_inventory_by_id_success| 
|test_get_inventory_by_id_fail| 
|test_get_inventory_fields_returned| 
|test_get_inventory_result_type_of_data| 
|test_get_inventory_download_template_url| 
|test_patch_inventory_success_status_204| 
|test_patch_inventory_fail_invalid_token| 
|test_patch_inventory_fail_without_permission| 
|test_patch_inventory_fail_without_payload| 
|test_patch_inventory_success_with_parcial_fields| 
|test_patch_inventory_fail_with_invalid_fields| 
|test_patch_inventory_fail_with_invalid_payload_values| 
|test_patch_inventory_fail_with_invalid_payload_value_null| 
|test_patch_inventory_fail_with_invalid_payload_value_negative| 
|test_post_inventory_success_status_200| 
|test_post_inventory_fail_user_not_authorized_status_403| 
|test_post_inventory_fail_with_invalid_token| 
|test_post_inventory_fail_with_invalid_payload| 
|test_post_inventory_fail_missing_fields_requireds| 
|test_post_inventory_fail_with_type_wrong| 
|test_post_inventory_fail_with_product_code_unique| 
|test_post_inventory_fail_with_invalid_value_null| 
|test_post_inventory_fail_with_invalid_value_negative| 
|test_get_users_success_status_200| 
|test_get_users_fail_with_invalid_token| 
|test_get_user_success_with_name| 
|test_get_user_fail_with_name_not_found| 
|test_patch_user_success| 
|test_patch_user_fail_with_invalid_token| 
|test_patch_user_fail_invalid_field| 
|test_patch_user_fail_not_found| 
|test_patch_user_success_with_not_required_fields| 
|test_patch_user_fail_with_email_registered| 
|test_patch_user_fail_without_permission| 
|test_post_user_success| 
|test_post_user_fail_invalid_token| 
|test_post_user_success_without_not_requireds_fields| 
|test_post_user_fail_with_email_already_exists| 
|test_post_user_fail_invalid_permission_user| 
|test_post_user_fail_invalid_payload| 
|test_post_user_fail_invalid_payload_password| 
|test_post_user_fail_with_invalid_payload_telephone| 
|test_post_user_fail_with_invalid_payload_email| 
|test_post_user_fail_with_invalid_payload_age| 
|test_post_user_fail_with_invalid_payload_city_id| 
|test_post_user_fail_with_invalid_payload_gender_id| 
|test_post_user_fail_role_with_success_create_role| 
|test_post_user_fail_role_with_invalid_payload_create_role| 
|test_post_user_fail_role_with_invalid_payload_create_role_permissions| 
|test_post_user_fail_role_with_invalid_create_role_with_existing_name_and_description| 
|test_post_user_fail_role_with_invalid_permission_user| 
