from src.app import DB, MA
from src.app.models.state import State, state_share_schema


class City(DB.Model):
    __tablename__ = 'cities'
    id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    state_id = DB.Column(DB.Integer, DB.ForeignKey(State.id), nullable=False)
    name = DB.Column(DB.String(128), nullable=False)

    state = DB.relationship('State', foreign_keys=[state_id])

    @classmethod
    def seed(cls, state_id, name):
        city = City(state_id=state_id, name=name)
        city.save()
        return city

    def save(self):
        DB.session.add(self)
        DB.session.commit()


class CitySchema(MA.Schema):
    state = MA.Nested(state_share_schema)

    class Meta:
        fields = ('id', 'description', 'state')


city_share_schema = CitySchema()
cities_share_schema = CitySchema(many=True)
