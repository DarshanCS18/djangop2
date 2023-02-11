from django.contrib import admin
from django.urls import path,re_path,include
from std_details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home,name='home'),
    re_path(r'^reg',views.reg,name='reg'),
    re_path(r'^detail',views.detail,name='detail')

]
