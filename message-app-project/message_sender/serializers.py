from rest_framework import serializers

from .models import MessageSenderModel, MessageModel


class MessageSenderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSenderModel
        fields = [
            'id', 'start_datetime', 'end_datetime', 'message', 'client_tag'
        ]

class MessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = [
            'id', 'datetime_stamp', 'status', 'message_sender_id', 'client_id'
        ]