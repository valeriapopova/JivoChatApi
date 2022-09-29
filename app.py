import json

from flask import Flask, jsonify, request, redirect
import requests
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/', methods=['POST'])
def homepage():
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_finished':
            r = requests.post(' https://api.ecomru.ru/jivo/chat_finished', json=webhook)
            return r.json()
        elif webhook['event_name'] == 'offline_message':
            r = requests.post(' https://api.ecomru.ru/jivo/chat_finished', json=webhook)
            return r.json()
        elif webhook['event_name'] == 'chat_accepted':
            r = requests.post(' https://api.ecomru.ru/jivo/chat_finished', json=webhook)
            return r.json()
        elif webhook['event_name'] == 'chat_assigned':
            r = requests.post(' https://api.ecomru.ru/jivo/chat_finished', json=webhook)
            return r.json()
        elif webhook['event_name'] == 'chat_updated':
            r = requests.post(' https://api.ecomru.ru/jivo/chat_finished', json=webhook)
            return r.json()
        elif webhook['event_name'] == 'call_event':
            r = requests.post(' https://api.ecomru.ru/jivo/chat_finished', json=webhook)
            return r.json()
        else:
            pass


@app.route('/webhook_call_event', methods=['POST'])
def webhook_call_event():
    """Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка."""
    # r = requests.get('http://api.ecomru.ru/jivo')
    # webhook = r.status_code
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'call_event':
            values = webhook
            print(values)
            return values


@app.route('/webhook_accepted', methods=['POST'])
def webhook_accepted():
    """Событие возникает в момент приема запроса диалога оператором."""
    # r = requests.get('http://api.ecomru.ru/jivo')
    # webhook = r.status_code
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_accepted':
            values = webhook
            print(values)
            return values


@app.route('/webhook_assigned', methods=['POST'])
def webhook_assigned():
    """Событие отправляется когда чат прикрепляется к карточке в CRM, используя параметр
    "crm_link" из ответа на событие chat_accepted. """
    # r = requests.get('http://api.ecomru.ru/jivo')
    # webhook = r.json()
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_assigned':
            values = webhook
            print(values)
            return values


@app.route('/webhook_finished', methods=['POST'])
def webhook_finished():
    """Событие отправляется при закрытии чата в приложении оператора."""
    # r = requests.get('http://api.ecomru.ru/jivo')
    # webhook = r.json()
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_finished':
            values = webhook
            print(values)
            return values


@app.route('/webhook_updated', methods=['POST'])
def webhook_updated():
    """Событие будет отправлено в случае, если информация о посетителе была обновлена . """
    # r = requests.get('http://api.ecomru.ru/jivo')
    # webhook = r.json()
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_updated':
            values = webhook
            print(values)
            return values


@app.route('/webhook_offline', methods=['POST'])
def webhook_offline():
    """Событие будет отправлено в момент отправки сообщения через оффлайн-форму. """
    # r = requests.get('http://api.ecomru.ru/jivo')
    # webhook = jsonify(r.content)
    # print(webhook)
    webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'offline_message':
            values = webhook["visitor"]
            print(values)
            return values





