from django.urls import path

from . import views

app_name = 'lol'

urlpatterns = [
    path('', views.index, name='index'),
     # ex: /lol/5/
    path('<int:game_id>/', views.detail, name='detail'),
    # ex: /lol/5/vote/
    path('register/', views.registerview, name='registerview'),

    path('login/', views.login, name='login'),

	path('registerdata/', views.register, name='register'),

	path('profile/', views.profile, name='profile'),

	path('logout/', views.logout, name='logout'),

	path('uploadImage/', views.uploadImage, name='uploadImage'),

	path('registergame/', views.registergame, name='registergame')
]
