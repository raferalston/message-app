from posixpath import basename
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from clients.views import ClientViewSet
from message_sender.views import MessageSenderViewSet, MessageSenderStatisticsViewSet


router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('messages', MessageSenderViewSet, basename='messages')
router.register('messages-statistics', MessageSenderStatisticsViewSet, basename='messages-statistics')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
