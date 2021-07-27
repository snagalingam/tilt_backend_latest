import os

from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from users.views import blank_response


ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')

if ENVIRONMENT == 'development':
    urlpatterns = [
        path("teamtilt", admin.site.urls),
        path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
        re_path(".*", blank_response, name="blank")
    ]

if ENVIRONMENT == 'production':
    urlpatterns = [
        path("teamtilt", admin.site.urls),
        path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=False))),
        re_path(".*", blank_response, name="blank")
    ]
