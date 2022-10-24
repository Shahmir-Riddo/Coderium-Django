from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('signup/', views.signup, name="signup"),
   path('login/', views.login, name="login"),
   path('logout/', views.logout, name="logout"),
   path('profile/', views.profile, name="profile"),
   path('editprofile/', views.editprofile, name="editprofile"),
   path('htmleditor/', views.htmleditor, name="htmleditor"),
   path('logout/', views.logout, name="logout"),
   path('error/', views.error, name="error"),
   path('login/error/', views.loginerror, name="loginerror"),
   
]