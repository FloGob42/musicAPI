from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.MusicViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('performers/', include('performer.urls')),
]