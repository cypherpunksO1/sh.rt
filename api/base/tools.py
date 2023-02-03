import random
import string


def make_link_key() -> str:
    letters = str(string.ascii_lowercase + string.ascii_uppercase)
    numbers = '1234567890'

    symbols = letters + numbers
    key = ''.join([random.choice(symbols) for _ in range(10)])
    return key


def get_client_ip(request) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
