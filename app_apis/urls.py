from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

app_name = 'app_apis'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque/', include('estoque.urls')),
    path('api-auth/', include('rest_framework.urls',namespace="rest_framework")),
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]