from django.urls import path, include
from rest_framework.routers import DefaultRouter
from performer.views import PerformerViewSet, ArtistViewSet, BandViewSet

# Use a router to automatically generate routes for the viewset
router = DefaultRouter()
router.register(r'all', PerformerViewSet, basename= 'performers')
router.register(r'artists', ArtistViewSet)
router.register(r'bands', BandViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]