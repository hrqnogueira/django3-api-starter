from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('{{ project_name }}.api.urls', '{{ project_name }}.api'), namespace='api')),
    path('core/', include(('{{ project_name }}.core.urls', 'core'), namespace='core')),

    url(r'api-docs/', include_docs_urls(title='API {{ project_name }}', public=True)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, url(r'^__debug__/', include(debug_toolbar.urls)))
