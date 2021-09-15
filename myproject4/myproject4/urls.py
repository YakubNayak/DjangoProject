from django.conf.urls import url
from myapp4 import views
urlpatterns = [
    url(r'^$',views.homev),
    url(r'page1',views.aboutv,name='Aboutl'),
    url(r'page2',views.contactv,name='Contactl'),
url(r'page3',views.donatev,name='Donatel'),

]
