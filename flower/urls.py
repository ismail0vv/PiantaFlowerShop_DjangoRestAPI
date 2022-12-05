from django.urls import path
from flower import views

urlpatterns = [
    path('flowers/<int:cat_id>/', views.FlowerListApiView.as_view(), name='flower list')
]