import random


CHARS = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
MAX_LENGTH = 15
MIN_LENGTH = 6
DOMAINS = [
    'ya.ru',
    'gmail.com',
    'list.ru'
]


def password_or_name_generator():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    result = ''
    for i in range(length):
        result += random.choice(CHARS)
    return result


def mail_generator():
    return password_or_name_generator() + '@' + random.choice(DOMAINS)
