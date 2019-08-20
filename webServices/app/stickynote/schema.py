from marshmallow import Schema, fields, validate
from .posttype_definitions import *
#
class PosttypeDataSchema(Schema):
    type_id = fields.Int(required=True)
    display_name = fields.Str(required=True)
    type_fields = fields.List(fields.String(validate=validate.OneOf(ALLOWED_FIELDS)))

class PosttypeSchema(PosttypeDataSchema):
    user_id = fields.Str(required=True)

class PostdataSchema(Schema):
    note_id = fields.Int(required=True)
    type_id = fields.Int()
    # title = fields.Str()
    message = fields.Str()
    # schedule = fields.Str()

class StickynoteSchema(PostdataSchema):
    # user_id = fields.Email(required=True)
    user_id = fields.Str(required=True)
