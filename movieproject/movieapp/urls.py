from . import views
from django.urls import path
app_name='movieapp' 

urlpatterns = [
    
    path('',views.first,name='first'),
    path('index/',views.index,name='index'),

    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    #path('register/', views.register, name='register'),
    #path('login/',views.login,name='login' ),
    #path('logout/',views.logout,name='logout')
    

]
