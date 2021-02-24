from marshmallow import Schema, fields, validates, ValidationError
from allcities import cities


class RunRequestSchema(Schema):

    city = fields.Str(required=True)

    @validates('city')
    def valid_city(self, value):
        if len(cities.filter(name=value)) == 0:
            raise ValidationError("Can't find this city!")