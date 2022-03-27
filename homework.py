import time
import requests
import os
from dotenv import load_dotenv
import telegram
import logging
from logging import StreamHandler

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = StreamHandler()
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

PRACTICUM_TOKEN = os.getenv('TOKEN')
TELEGRAM_TOKEN = os.getenv('TOKEN_TLG')
TELEGRAM_CHAT_ID = os.getenv('Chat_id')

RETRY_TIME = 600
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}


HOMEWORK_STATUSES = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}


def send_message(bot, message):
    """Отправляет сообщение в Telegram чат."""
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
        logger.info('Сообщение отправлено в чат {TELEGRAM_CHAT_ID}: {message}')
    except Exception:
        logger.error('Ошибка отправки сообщения в чат')


def get_api_answer(current_timestamp):
    """Запрос к эндпоинту API-сервиса."""
    timestamp = current_timestamp or int(time.time())
    params = {'from_date': timestamp}
    try:
        homework_statuses = requests.get(ENDPOINT, headers=HEADERS,
                                         params=params)
        status_code = homework_statuses.status_code
    except Exception as error:
        logging.error(f'Ошибка запроса к эндпоинту {error}')
        raise Exception(f'Ошибка запроса к эндпоинту {error}')
    if status_code != 200:
        raise ValueError(f"Эндпоинт недоступен {status_code}")
    return homework_statuses.json()


def check_response(response):
    """Проверяет ответ API на корректность."""
    if type(response) is not dict:
        raise TypeError('Ответ API не содержит словарь')
    try:
        list_homeworks = response['homeworks']
        homework = list_homeworks[0]
    except IndexError:
        logger.error('Пуст список работ')
        raise IndexError('Пуст список работ')
    return homework


def parse_status(homework):
    """Извлекает из информации о конкретной домашней работе.
    Статус конкретной работы.
    """
    if 'homework_name' not in homework:
        raise KeyError('Отсутствует ключ homework_name')
    homework_name = homework['homework_name']
    homework_status = homework['status']
    if homework_status not in HOMEWORK_STATUSES:
        raise Exception(f'Неизвестный статус {homework_status}')
    verdict = HOMEWORK_STATUSES[homework_status]
    return f'Изменился статус проверки работы "{homework_name}". {verdict}'


def check_tokens():
    """Проверяет доступность переменных окружения."""
    if all([PRACTICUM_TOKEN, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID]):
        return True


def main():
    """Основная логика работы бота."""
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    current_timestamp = int(time.time())
    # Проверка переменных окружения
    if not check_tokens():
        logger.critical('Отсутствуют переменные окружения')
        raise Exception('Отсутствуют переменные окружения')
    while True:
        try:
            # Запрос и проверка ответа
            response = get_api_answer(current_timestamp)
            current_timestamp = response.get('current_date')
            message = parse_status(check_response(response))
            if message != STATUS:  # Проверка статуса и отправка сообщения
                send_message(bot, message)
                STATUS = message
            time.sleep(RETRY_TIME)
        except Exception as error:
            message = f'{error}'
            send_message(bot, message)
        time.sleep(RETRY_TIME)


if __name__ == '__main__':
    main()
