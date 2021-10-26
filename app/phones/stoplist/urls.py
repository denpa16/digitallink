from django.urls import path
from . import views

app_name = 'stoplist'

urlpatterns = [
    path('phone/', views.PhoneView.as_view(), name='phones'),
    path('phone_add/', views.PhoneAddView.as_view(), name='phone_add'),
    path('upload/', views.FileUploadView.as_view(), name='upload')
]