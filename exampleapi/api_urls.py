from django.conf import settings
from django.conf.urls import include, url
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.schemas import get_schema_view

from rest_framework import permissions, response, schemas
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)

urlpatterns = [
    url(r'^characters/', include('characters.urls')),
]


swagger_settings = getattr(settings, 'SWAGGER_SETTINGS', None)

schema_view = get_schema_view(title="Star Wars Character API",
                              renderer_classes=[OpenAPIRenderer,
                                                SwaggerUIRenderer])

urlpatterns += [url(r'^docs/',
                schema_view)]
