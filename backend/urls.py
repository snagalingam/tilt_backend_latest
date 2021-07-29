from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('teamtilt', admin.site.urls),
    path('api/v1/', include('api.urls')),
]
