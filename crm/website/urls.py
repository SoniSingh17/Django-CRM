
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name='home'),
    #path('login/',views.login_user,name='login'),

    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>/',views.record_user,name='record'),
    path('delete_record/<int:pk>/',views.delete_record_user,name='delete_record'),
    path('add_record/',views.add_record_user,name='add_record'),
    path('update_record/<int:pk>/',views.update_record_user,name='update_record'),
    
]
