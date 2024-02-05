from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mail import views

router = DefaultRouter()
router.register(r'letters', views.LetterViewSet)
router.register(r'parcels', views.ParcelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
