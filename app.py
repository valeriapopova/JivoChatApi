import json

from flask import Flask, jsonify
import requests
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/jivo/webhook_call_event')
def webhook_call_event():
    """Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка."""
    r = requests.get('http://lk.ecomru.ru/jivo/webhook/test.php')
    webhook = r.status_code
    # webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'call_event':
            values = webhook
            print(values)
            return values


@app.route('/jivo/webhook_accepted')
def webhook_accepted():
    """Событие возникает в момент приема запроса диалога оператором."""
    r = requests.get('http://lk.ecomru.ru/jivo/webhook/test.php')
    webhook = r.status_code
    # webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_accepted':
            values = webhook
            print(values)
            return values


@app.route('/jivo/webhook_assigned')
def webhook_assigned():
    """Событие отправляется когда чат прикрепляется к карточке в CRM, используя параметр
    "crm_link" из ответа на событие chat_accepted. """
    r = requests.get('http://lk.ecomru.ru/jivo/webhook/test.php')
    webhook = r.json()
    # webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_assigned':
            values = webhook
            print(values)
            return values


@app.route('/jivo/webhook_finished')
def webhook_finished():
    """Событие отправляется при закрытии чата в приложении оператора."""
    r = requests.get('http://lk.ecomru.ru/jivo/webhook/test.php')
    webhook = r.json()
    # webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_finished':
            values = webhook
            print(values)
            return values


@app.route('/jivo/webhook_updated')
def webhook_updated():
    """Событие будет отправлено в случае, если информация о посетителе была обновлена . """
    r = requests.get('http://lk.ecomru.ru/jivo/webhook/test.php')
    webhook = r.json()
    # webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'chat_updated':
            values = webhook
            print(values)
            return values


@app.route('/jivo/webhook_offline')
def webhook_offline():
    """Событие будет отправлено в момент отправки сообщения через оффлайн-форму. """
    r = requests.get('http://lk.ecomru.ru/jivo/webhook/test.php')
    webhook = jsonify(r.content)
    print(webhook)
    # webhook = request.get_json(force=False)
    if webhook:
        if webhook['event_name'] == 'offline_message':
            values = webhook["visitor"]
            print(values)
            return values





