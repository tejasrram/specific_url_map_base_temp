from django.urls import path
from app1.views import *
app_name='nothing'

urlpatterns=[
    path('test1/',test1,name='test1'),
    path('test2/',test2,name='test2'),
    path('test3/',test3,name='test3'),
]