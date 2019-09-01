from django.urls import path
# re_path 정규표현식 사용

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('result', views.result, name='result'),

]