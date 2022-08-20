from datetime import datetime
from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import MessageModel, MessageSenderModel
from .serializers import MessageSenderModelSerializer, MessageModelSerializer


class MessageSenderViewSet(viewsets.ModelViewSet):
    queryset = MessageSenderModel.objects.all()
    serializer_class = MessageSenderModelSerializer

class MessageSenderStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MessageSenderModel.objects.all()
    serializer_class = MessageSenderModelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        for d in serializer.data:
            messages_obj = MessageModel.objects.filter(message_sender_id=d.get('id'))
            related_count = messages_obj.filter(status=True).count()
            d['sended_messages'] = related_count
            d['messages'] = MessageModelSerializer(messages_obj, many=True).data
            
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(obj)
        modified_data = {}
        messages_obj = MessageModel.objects.filter(message_sender_id=pk)
        related_count = messages_obj.filter(status=True).count()
        modified_data['sended_messages'] = related_count
        modified_data['messages'] = MessageModelSerializer(messages_obj, many=True).data
        modified_data.update(serializer.data)
        
        return Response(modified_data)
