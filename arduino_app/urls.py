from django.urls import path
from . import views
from .views import send_bulk_email_view
urlpatterns = [
    path('', views.home, name='main'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('send_emails/', send_bulk_email_view, name='send_emails'),
    path('prolan/', views.prolan, name='prolan'),
    path('update/', views.update, name='update'),
    path('python_programming/<str:language_name>/', views.python_programming, name='python_programming'),
    path('tech_updates/<str:update_name>/', views.tech_updates, name='tech_updates'),
    path('privacy policy/', views.privacy_policy, name='privacy_policy'),
]
