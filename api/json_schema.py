GET_LIST_USER_SCHEMA = {

# Fit to validate list of users or single user
# /api/users, /api/users?page=[int], /api/user/2

    "type": "object",
    "properties": {
        "page": {"type": "integer", "minimum": 0},
        "per_page": {"type": "integer", "minimum": 0},
        "total": {"type": "integer", "minimum": 0},
        "total_pages": {"type": "integer", "minimum": 0},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string", "format": "email"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string", "format": "uri"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"],
                "additionalProperties": False
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"],
            "additionalProperties": False
        }
    },
    "required": ["data", "support"],
    "additionalProperties": False
}
