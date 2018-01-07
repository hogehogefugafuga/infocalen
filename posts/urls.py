from django.conf.urls import url
from . import views

app_name = 'posts'


# viewsのindex関数をみにいっている
urlpatterns = [url(r'^$', views.index, name='index')]
