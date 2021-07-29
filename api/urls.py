from .views import UserViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
    path(r'', include(router.urls)),
]
