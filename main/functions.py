import re


def clean_string(value):
    return re.sub('[^A-Za-z0-9]+', '', value)