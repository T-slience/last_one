import json

from django.shortcuts import render
import django_redis
# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        response = HttpResponse('ok')

        # 写cookie
        # response.set_cookie('hello', 'django', max_age=60 * 60 * 24 * 7)

        # 读[],get()
        hello = request.COOKIES.get('hello', 'redis')
        print(request.COOKIES.get('hello'))
        # print(hello)

        return response

    def post(self, request):
        # a = request.body.decode()
        # b = json.loads(a)
        # a = b['a']
        a = json.loads(request.body.decode()).get('a')
        return HttpResponse(a)


class SessionView(View):
    def get(self, request):
        # request.session['abc']=2000
        # # a= request.session['a']
        # # a = request.session.get('ab')
        # # print(a)
        del request.session['dala']
        return HttpResponse('OK')
