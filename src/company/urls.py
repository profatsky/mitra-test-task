from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]
