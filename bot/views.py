from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests;

HAOSHUO_CLIENT_ID = getattr(settings, 'HAOSHUO_CLIENT_ID', None)
HAOSHUO_TOKEN = getattr(settings, 'HAOSHUO_BOT_USER_TOKEN', None)
HAOSHUO_API = getattr(settings, 'HAOSHUO_API', None)


class Bot(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data
        print(message.get('token'))
        print(HAOSHUO_TOKEN)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + HAOSHUO_TOKEN,
        }

        r = requests.post(HAOSHUO_API + 'chat/send', data={'type': 'text', 'content': '你好，我是bot', 'channel_id': '277'},
                          headers=headers)
        print(r)
        print(headers)
        retarray = [int(i) for i in r.content]
        print('123')
        print(retarray)
        if message.get('token') != HAOSHUO_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_200_OK)
