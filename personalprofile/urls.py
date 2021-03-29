from django.urls import path
from . import views

app_name = 'personalprofile'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('profiles/', views.AllProfilesView.as_view(), name='profiles'),
    path('<int:pk>/', views.InfoView.as_view(), name='info'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete')
]