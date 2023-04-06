from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('bargains/', views.BargainsListView.as_view(), name='bargains'),
    path('documents/', views.DocumentsListView.as_view(), name='documents'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]
