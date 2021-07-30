from .views import UserViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path(r'', include(router.urls)),
]
