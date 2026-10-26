from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('', views.login_view, name='login'),
    path('painel/', views.adminpage, name='adminpage'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]