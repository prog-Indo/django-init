import os
from datetime import datetime as _datetime

import phonenumbers
import requests
from django.apps.registry import apps
from django.contrib.auth import login
from django.core.exceptions import FieldError
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.utils import timezone

get_model = apps.get_model


# from sequences import get_next_value
class FilenameGenerator(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        today = timezone.localtime(timezone.now()).date()

        filepath = os.path.basename(filename)
        filename, extension = os.path.splitext(filepath)
        filename = slugify(filename)

        path = "/".join([
            'media',
            self.prefix,
            str(today.year),
            str(today.month),
            # str(today.day),
            filename + extension
        ])
        return path
try:
    from django.utils.deconstruct import deconstructible
    FilenameGenerator = deconstructible(FilenameGenerator)
except ImportError:
    pass


def normalize_phone(number):
    number = number[1:] if number[:1] == '0' else number
    parse_phone_number = phonenumbers.parse(number, 'ID')
    phone_number = phonenumbers.format_number(
        parse_phone_number, phonenumbers.PhoneNumberFormat.E164)
    return phone_number

def prepare_datetime_range(start, end, tzinfo=None):
    start = _datetime.combine(start, _datetime.min.time())
    start = timezone.localtime(timezone.make_aware(start))
    end = _datetime.combine(end, _datetime.max.time())
    end = timezone.localtime(timezone.make_aware(end))
    return start, end

def prepare_start_date(date, tzinfo=None):
    start = _datetime.combine(date, _datetime.min.time())
    start = timezone.localtime(timezone.make_aware(start))
    return start

def prepare_end_date(date, tzinfo=None):
    end = _datetime.combine(date, _datetime.max.time())
    end = timezone.localtime(timezone.make_aware(end))
    return end


def force_login(request, user):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

def send_sms(message, number):
    url = 'https://reguler.zenziva.net/apps/smsapi.php?userkey=3crpu7&passkey=ljopk3ks5r&nohp=' + \
        number + '&pesan=' + message
    headers = {'accept': 'application/xml;q=0.9, */*;q=0.8'}
    response = requests.get(url, headers=headers)
    print(response.text)
    return response.text


def filter_obj(objects, GET):
    sort = GET.get('sort', '-id')
    limit = int(GET.get("limit", 30))
    offset = int(GET.get("offset", 0))
    extra_filter = {}
    for key, value in GET.items():
        try:
            if "," in value:
                value = value.split(",")
            if value == "True":
                value = True
            elif value == "False":
                value = False
            
            extra_filter = {key: value}
            if key and value:
                extra_filter = {key: value}
            objects = objects.filter(**extra_filter)
        except FieldError:
            pass
    if sort:
        sort = sort.split(",")
        objects = objects.order_by(*sort)
    return objects.all()[offset:limit]

def indoDate(date):
    months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    date = "%s %s %s" % (date.day, months[date.month - 1], date.year)
    return date
