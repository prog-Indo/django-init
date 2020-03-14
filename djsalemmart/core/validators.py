from django.core.exceptions import ValidationError

from phonenumbers import parse, phonenumberutil
from django.core.validators import validate_email as django_validate_email


def validate_mobile_number(phone_number):
    if str(phone_number[0]) == "0":
        phone_number = "+62" + phone_number[1:]
    try:
        number = parse(phone_number)
    except phonenumberutil.NumberParseException:
        raise ValidationError('please input valid mobile number')

    if number:
        return True

    raise ValidationError('please input valid mobile number')


def validate_email_address(email):
    django_validate_email(email)

    if email.endswith('.'):
        raise ValidationError(
            "email doesn't end by (.) dot, please input valid email")
    else:
        return True
