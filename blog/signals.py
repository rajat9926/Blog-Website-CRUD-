from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user, **kwargs):
    ipadd = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ipadd
    a = cache.get('count',default=0, version=user.id)
    newcount = a + 1
    cache.set('count',newcount,60*60*24, version=user.id)