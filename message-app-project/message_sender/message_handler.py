import requests
import json
from datetime import datetime

# from .models import MessageModel
from clients.models import ClientModel


def send_message(pk, phone, text):
    url = f'https://probe.fbrq.cloud/v1/send/{pk}'
    data = {
        'id': pk,
        'phone': phone,
        'text': text
    }
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIzNjAyMTUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IlBodWtldFRhYmxldG9wIn0.uPZEV_Ic1pKSMR10q3pJoBVdgUjkjx3Lsmu96dLha0Y',
        'Content-Type': 'application/json'
    }
    r = requests.post(url, json=data, headers=headers)
    status = r.json().get('message', False)
    # TODO: spending to much time to convert response date time, decide to use basic python object
    # really dont bother about accurate time right now.
    date_time = datetime.now() 
    return status, date_time

def start_messaging(model_object, end_time):
    from .models import MessageModel, MessageSenderModel
    model_object = MessageSenderModel.objects.get(id=model_object)
    model = MessageModel
    clients = ClientModel.objects.filter(tag=model_object.client_tag)
    if clients:
        for client in clients:
            #TODO: Тут будут проблемы с временем и таймзоной. Не успевал реализовать.
            if datetime.now() > datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ'):
                break
            message_model = model.objects.create(
                datetime_stamp=datetime.now(),
                message_sender_id=model_object,
                client_id = client
            )

            status, date_time = send_message(
                pk=client.id, 
                phone=client.phone, 
                text=model_object.message
                )
            if status == 'OK':
                message_model.status = True
                message_model.datetime_stamp = date_time
                message_model.save()
        return True
    return False