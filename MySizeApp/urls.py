from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name = "home"),
    path('top', views.topView, name = "topView"),
    path('mypage', views.mypage, name = "mypage"),
    path('compare/<int:id>', views.compareView, name = "compareView" ),
    path('editMypage/<int:editsize_pk>', views.editMypage, name="editMypage"),
   
]