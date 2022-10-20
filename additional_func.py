import re
from kopeechka import Mail_activations
from conf import KP_API


def check(email: str):
    """Функция для валидации email"""

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return email


def parse_facebook(text: str) -> str:
    """Парсинг письма с Facebook"""

    result = re.findall(r'>(?P<code>\d{8})<', text)
    return result[0][:8]


def mailbox_reorder(token, site, email, api='2.0') -> dict:
    """Повторный запрос активации с этой почтой на kopeechka"""

    body = Mail_activations(token=token)
    return body.mailbox_reorder(site, email, api)


def mailbox_message(token, full, id, api='2.0') -> str:

    body = Mail_activations(token=token)
    return body.mailbox_get_message(full, id, api)
    

# print(mailbox_reorder(KP_API, site='facebook.com', email='derczachicsetz1982@outlook.com'))
# print(mailbox_message(KP_API, full='0', id='1440700785'))


