import hashlib
import secrets
from collections import defaultdict

from flask import Flask, jsonify, request, redirect
import requests
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/get_key', methods=['POST'])
def homepage():
    """Возвращет пользователю - уникальный сгенерированный URL"""
    webhook = request.get_json(force=False)
    webhook_account_name = webhook['account_name']
    webhook_event_name = webhook['event_name']
    salt = secrets.token_hex(16) + webhook_account_name
    url = 'https://api.ecomru.ru/jivo'
    url_key = hashlib.sha256(salt.encode('utf-8')).hexdigest()
    result_url = f'{url}/{webhook_event_name}/{url_key}'
    print(result_url)
    return result_url


# @app.route('/', methods=['POST'])
# def homepage():
#     webhook = request.get_json(force=False)
#     if webhook:
#         if webhook['event_name'] == 'chat_finished':
#             return webhook
#         elif webhook['event_name'] == 'offline_message':
#             return webhook
#         elif webhook['event_name'] == 'chat_accepted':
#             return webhook
#         elif webhook['event_name'] == 'chat_assigned':
#             return webhook
#         elif webhook['event_name'] == 'chat_updated':
#             return webhook
#         elif webhook['event_name'] == 'call_event':
#             return webhook
#         else:
#             return webhook

@app.route('/call_event/<url_key>', methods=['POST'])
def webhook_call_event():
    """Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка."""
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'call_event':
            data = {}
            result_list = defaultdict(list)
            for k, v in webhook.items():
                if type(v) == dict:
                    for key, value in v.items():
                        if type(value) == dict:
                            for key1, value1 in value.items():
                                result_list[key1].append(str(value1))
                        else:
                            result_list[key].append(str(value))
                else:
                    result_list[k].append(str(v))

            result_list.pop('user_agent')

            data['data'] = [result_list]
            return data


@app.route('/chat_accepted/<url_key>', methods=['POST'])
def webhook_accepted():
    """Событие возникает в момент приема запроса диалога оператором."""
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_accepted':
            data = {}
            result_list = defaultdict(list)
            for k, v in webhook.items():
                if type(v) == dict:
                    for key, value in v.items():
                        if type(value) == dict:
                            for key1, value1 in value.items():
                                result_list[key1].append(str(value1))
                        else:
                            result_list[key].append(str(value))
                else:
                    result_list[k].append(str(v))

            result_list.pop('user_agent')

            data['data'] = [result_list]
            return data


@app.route('/chat_assigned/<url_key>', methods=['POST'])
def webhook_assigned():
    """Событие отправляется когда чат прикрепляется к карточке в CRM, используя параметр
    "crm_link" из ответа на событие chat_accepted. """
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_assigned':
            data = {}
            result_list = defaultdict(list)
            for k, v in webhook.items():
                if type(v) == dict:
                    for key, value in v.items():
                        if type(value) == dict:
                            for key1, value1 in value.items():
                                result_list[key1].append(str(value1))
                        else:
                            result_list[key].append(str(value))
                else:
                    result_list[k].append(str(v))

            result_list.pop('user_agent')

            data['data'] = [result_list]
            return data


@app.route('/chat_finished/<url_key>', methods=['POST'])
def webhook_finished():
    """Событие отправляется при закрытии чата в приложении оператора."""
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_finished':
            data = {}
            result_list = defaultdict(list)
            for k, v in webhook.items():
                if type(v) == dict:
                    for key, value in v.items():
                        if type(value) == dict:
                            for key1, value1 in value.items():
                                result_list[key1].append(str(value1))
                        else:
                            result_list[key].append(str(value))
                else:
                    result_list[k].append(str(v))

            result_list.pop('messages')

            result_list.pop('user_agent')

            data['data'] = [result_list]
            return data


@app.route('/chat_updated/<url_key>', methods=['POST'])
def webhook_updated():
    """Событие будет отправлено в случае, если информация о посетителе была обновлена . """
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_updated':
            data = {}
            result_list = defaultdict(list)
            for k, v in webhook.items():
                if type(v) == dict:
                    for key, value in v.items():
                        if type(value) == dict:
                            for key1, value1 in value.items():
                                result_list[key1].append(str(value1))
                        else:
                            result_list[key].append(str(value))
                else:
                    result_list[k].append(str(v))

            data['data'] = [result_list]
            return data


@app.route('/offline_message/<url_key>', methods=['POST'])
def webhook_offline():
    """Событие будет отправлено в момент отправки сообщения через оффлайн-форму. """
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'offline_message':
            data = {}
            result_list = defaultdict(list)
            for k, v in webhook.items():
                if type(v) == dict:
                    for key, value in v.items():
                        if type(value) == dict:
                            for key1, value1 in value.items():
                                result_list[key1].append(str(value1))
                        else:
                            result_list[key].append(str(value))
                else:
                    result_list[k].append(str(v))

            result_list.pop('user_agent')
            data['data'] = [result_list]

            return data
