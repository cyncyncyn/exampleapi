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




#@api_view()
#@permission_classes([permissions.AllowAny])
#@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
#def schema_view(request):
#    generator = schemas.SchemaGenerator(title='Example API')
#    return response.Response(generator.get_schema(request=request))
#

from django.conf import settings

swagger_settings  =  getattr(settings, 'SWAGGER_SETTINGS', None)
class CustomRenderer(OpenAPIRenderer):
    def get_customizations(self):
        """
        Adds settings, overrides, etc. to the specification.
        """
        data = super(CustomRenderer, self).get_customizations()

        for k, v in swagger_settings.iteritems():
            data[k] = v
        return data


schema_view = get_schema_view(title="Prueba", renderer_classes=[CustomRenderer, SwaggerUIRenderer])





urlpatterns += [url(r'^docs/',
                schema_view)]


