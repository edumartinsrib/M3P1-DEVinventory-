from marshmallow import Schema, ValidationError, fields, validates

from src.app.models.permission import Permission
from src.app.models.role import Role
from src.app.models.schemas.error_messages import set_error_message


class RoleValidateSchema(Schema):
    description = fields.Str(
        required=True, error_messages=set_error_message('description')
    )
    name = fields.Str(required=True, error_messages=set_error_message('name'))
    permissions = fields.List(
        fields.Integer(),
        required=True,
        error_messages=set_error_message('permissions'),
    )

    @validates('description')
    def validate_description(self, value):
        if Role.query.filter_by(description=value).first():
            raise ValidationError('Descrição já registrada')

    @validates('name')
    def validate_name_role(self, value):
        if Role.query.filter_by(name=value).first():
            raise ValidationError('Função já registrada')

    @validates('permissions')
    def validate_permissions(self, value):
        for permission_id in value:
            if not Permission.query.filter_by(id=permission_id).first():
                raise ValidationError(
                    f'{permission_id} - Permissão não encontrada'
                )
        if type(value) is not list:
            raise ValidationError('Permissões inválidas, deve ser uma lista')
        if len(value) > 5:
            raise ValidationError('Função com mais de 5 permissões')


user_validate_schema = RoleValidateSchema()
