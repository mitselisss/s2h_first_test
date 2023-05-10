from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [

    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),

    path('Users', views.Users, name='Users'),
    path('UsersProfile', views.UsersProfile, name='UsersProfile'),
    path('IdUserProfile/<str:pk>/', views.IdUserProfile, name='IdUserProfile'),
    path('<str:pk>/NPs', views.NPs, name='NPs'),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    path('MealsApi', views.MealsApi, name='MealsApi'),
]