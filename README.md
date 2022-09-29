
***/jivo*** доступ к JivoSite webhook api

___POST___

_/jivo/webhook_call_event_ -  Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка.

Responses 200 успешно

___POST___

_/jivo/webhook_accepted_ -  Оператор принял запрос диалога от клиента (нажал в программе кнопку Ответить)

Responses 200 успешно



___POST___

_/jivo/webhook_assigned_ -  Диалог был прикреплен к карточке в CRM

Responses 200 успешно


___POST___

_/jivo/webhook_finished_  -   Диалог завершился (был закрыт в программе либо нажатием на крестик рядом с именем клиента, либо автоматически после того, как клиент покинул сайт)

Responses 200 успешно



___POST___

_/jivo/webhook_updated_ -  Обновились контактные данные о клиенте (либо клиент представился, либо оператор сам внёс контакты в программе)

Responses 200 успешно


___POST___

_/jivo/webhook_offline_ -   Было отправлено оффлайн-сообщение, когда не было операторов онлайн.


Responses 200 успешно

возвращает json вида:

```
{'data': [defaultdict(<class 'list'>,
                      {'campaign': ['campaign_name'],
                       'chats_count': ['1'],
                       'city': ['San Francisco'],
                       'content': ['banner'],
                       'country': ['United States'],
                       'country_code': ['US'],
                       'description': ['Description text'],
                       'email': ['email@example.com'],
                       'event_name': ['offline_message'],
                       'ip_addr': ['208.80.152.201'],
                       'latitude': ['37.7898'],
                       'longitude': ['-122.3942'],
                       'medium': ['cpc'],
                       'message': ['Message text'],
                       'name': ['John Smith'],
                       'number': ['2198'],
                       'offline_message_id': ['2806'],
                       'organization': ['Wikimedia Foundation'],
                       'phone': ['+14084987855'],
                       'region': ['California'],
                       'region_code': ['CA'],
                       'source': ['google'],
                       'term': ['...'],
                       'title': ['Page title'],
                       'url': ['http://example.com/'],
                       'utm': ['source=google|medium=cpc|content=banner|campaign=campaign_name'],
                       'widget_id': ['3948']})]}

```