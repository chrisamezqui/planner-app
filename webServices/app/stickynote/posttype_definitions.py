ALLOWED_FIELDS = ["title", "message", "schedule", "reminder", "list", "checklist", "refresh"]
TYPES = ["memo"]
PUBLIC_USER_ID = '_'
META_FIELDS = ["note_id", "type_id", "user_id"]

POSTTYPE_DEFINITIONS = [
    {
    "type_id":0,
    "display_name":"Memo",
    "type_fields": [
        "title",
        "message"
    ]
    }
]
