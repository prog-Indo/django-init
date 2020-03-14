def serialize_user(data):
    return {
        "id": data.id,
        "is_superuser": data.is_superuser,
        "username": data.username,
        "mobile_number": data.mobile_number,
        "email": data.email,
        "first_name": data.first_name,
        "last_name": data.last_name,
        "role": data.role,
        "membership": data.membership.name if data.membership else "",
        "is_active": data.is_active,
        "last_login": data.last_login,
    }

def serialize_author(data):
    return {
        "id": data.id,
        "email": data.email,
        "first_name": data.first_name,
        "last_name": data.last_name,
    }
