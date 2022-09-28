from src.app import DB, MA
from src.app.models.permission import permissions_share_schema

roles_permissions = DB.Table("roles_permissions",
    DB.Column("role_id", DB.Integer, DB.ForeignKey("roles.id")),
    DB.Column("permission_id", DB.Integer, DB.ForeignKey("permissions.id")))

class Role(DB.Model):
    __tablename__ = 'roles'
    id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
    description = DB.Column(DB.String(128), nullable = False)
    name = DB.Column(DB.String(128), nullable = False)
    permissions = DB.relationship("Permission", secondary=roles_permissions, backref="roles")
    
    
    @classmethod
    def seed(cls, description, name , permissions):
        role = Role(
            description=description,
            name=name,
            permissions = permissions
        )
        role.save()
        return role
    
    def save(self):
        DB.session.add(self)
        DB.session.commit()

class RoleSchema(MA.Schema):
    permissions = MA.Nested(permissions_share_schema)
    class Meta: 
        fields = ('id', 'description', 'name' , 'permissions')

role_share_schema = RoleSchema()
roles_share_schema = RoleSchema(many = True)