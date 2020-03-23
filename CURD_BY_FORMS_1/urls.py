from django.conf.urls import url
from django.contrib import admin
from CurdFormsApp import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$',views.home_page,name=''),
url(r'create/',views.create_view, name='create'),
url(r'update/',views.update_view,name='update'),
url(r'retrieve/',views.retrieve_view, name='retrieve'),
url(r'delete/',views.delete_view,name='delete')
]
