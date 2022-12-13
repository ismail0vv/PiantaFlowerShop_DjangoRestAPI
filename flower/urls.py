from django.urls import path, include
from flower import views
from rest_framework.routers import SimpleRouter
ROUTER = SimpleRouter()
ROUTER.register('flower-crud', views.FlowerViewSet)
ROUTER.register('category-crud', views.CategoryViewSet)
ROUTER.register('color-crud', views.ColorViewSet)
ROUTER.register('photo-crud', views.PhotoViewSet)
ROUTER.register('review-crud', views.ReviewViewSet)
urlpatterns = [
    path('flowers/', views.FlowerListApiView.as_view(), name='flower list'),
    path('flower-detail/<int:pk>/', views.FlowerDetailApiView.as_view()),
    path('flower-best/', views.FlowerBestApiView.as_view()),
    path('flower-browses/', views.FlowerAlsoBrowsedApiView.as_view()),
    path('', include(ROUTER.urls)),
    path('category/', views.CategoryListApiView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    path('reviews/', views.ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/', views.ReviewItemUpdateDeleteAPIView.as_view()),
]