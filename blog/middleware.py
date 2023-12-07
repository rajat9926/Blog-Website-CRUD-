from django.http import HttpResponseRedirect
from django.shortcuts import render

class Underconstmidware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('call from middleware')
        response = render(request,'blog/underconst.html')
        # response = self.get_response(request)
        print('After View midware')
        return response