from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('test3/',test3,name='test3'),
    path('test4/',test4,name='test4'),
    path('test5/',test5,name='test5'),
]