from django.contrib import admin
from django.urls import include, path, re_path
from users.views import blank_response


urlpatterns = [
    path('teamtilt', admin.site.urls),
    path('api/v1/', include('api.urls')),
    re_path(".*", blank_response, name="blank")
]
