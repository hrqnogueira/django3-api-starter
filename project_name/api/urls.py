from django.conf.urls import url
from django.urls import include, path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from {{ project_name }}.api.v1 import router

urlpatterns = [
    url(r'^v1/', include(router.router.urls)),
    url(r'api-auth/', include('rest_framework.urls')),

    # Authentication endpoints
    path(r'token-auth/', obtain_jwt_token),
    path(r'token-refresh/', refresh_jwt_token),
]
