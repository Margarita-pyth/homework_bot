# API "homework_bot"
#### Проверяет статус проверки домашней работы в "Яндекс.Практикум".

##### Краткое описание функционала API:
- Данный Api-сервис делает запрос к единственному эндпоинту - "Яндекс.Практикум" и возвращает  соответствующий вердикту ответ. 
- Содержит следующие функции:
- - get_api_answer: делаем запрос и возвращаем (преобразованный из формата JSON к типам данных Python) ответ API.
- - check_response: проверяем ответ API на корректность.
- - parse_status: извлекаем статус конкретной домашней работы 
(ответ соотвествующего статуса проверки домашней работы)
- - send_message: отправляем сообщение в Telegram чат.
    Принимает на вход два параметра: экземпляр класса Bot и строку сообщения.
- - check_tokens(): проверяем доступность переменных окружения.

✨Magic ✨Python

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
https://github.com/Margarita-pyth/homework_bot
```sh
cd homework_bot
```
Cоздать и активировать виртуальное окружение:
```sh
python3 -m venv env
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Не забудьте запросить TOKEN у своего телеграмм-бота через @BotFather,а также ID telegram-чата (отправьте сообщение @userinfobot) и запросите TOKEN у сервиса, к которому будем отправлять запрос, затем в терминале выполните команду:
```sh
export TOKEN=123.....
export TOKEN_TLG=123.....
export CHAT_ID=123.....
```
Таким образом у нас будет доступ к глобальным переменным окружения из кода 
(методом getenv из встроенного модуля os).
Программа готова к использованию!

## Plugins
| GitHub | | Django | 
| formatter | | os |
| Python |  | logger |

## Лицензия
MIT
**Разработано програмистом 
Margarita-pyth**
____________________________________________________________________________________
# API "homework_bot"
#### Checks the status of checking homework in "Yandex.Workshop".

##### Brief description of API functionality:

- This Api-service makes a request to a single endpoint - "Yandex.Practice" and returns a response corresponding to the verdict.
- Contains the following features:
- - get_api_answer: make a request and return (converted from JSON format to Python data types) an API response.
- - check_response: check the API response for correctness.
- - parse_status: Retrieve the status of a specific homework
(response of appropriate homework check status)
- - send_message: send a message to Telegram chat.
    It takes two parameters as input: an instance of the Bot class and a message string.
- - check_tokens(): check the availability of environment variables.

✨Magic ✨Python

## How to run the project:
Clone the repository and change into it on the command line:
https://github.com/Margarita-pyth/homework_bot
```sh
cd homework_bot
```
Create and activate virtual environment:
```sh
python3 -m venv env
source env/Scripts/activate
```
Install dependencies from requirements.txt file:
```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Don't forget to request a TOKEN from your telegram bot via @BotFather, as well as a telegram chat ID (send a message to @userinfobot) and request a TOKEN from the service to which we will send the request, then run the command in the terminal:
```sh
export TOKEN=123.....
export TOKEN_TLG=123.....
export CHAT_ID=123.....
```
This way we will have access to the global environment variables from the code
(using the getenv method from the built-in os module).
The program is ready to use!

## Plugins
| GitHub | | Django | 
| formatter | | os |
| Python |  | logger |

## License
MIT
**Designed by programmer
Margarita-pyth**

