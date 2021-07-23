from django.contrib import admin
from django.urls import path, include
from .views import home_page
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view  # new

API_TITLE = 'Blog Api'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'

schema_view = get_swagger_view(title='BLOG API')


urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),  # new
    path('api/v1/rest-auth/', include('rest_auth.urls')),  # new
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),  # new
    # path('schemas/', schema_view),
    path('swagger-docs/', schema_view),
]
