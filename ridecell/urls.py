"""ridecell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

api_info = openapi.Info(title="RideCell API", default_version='v1', )

schema_view = get_schema_view(api_info, public=True, permission_classes=(AllowAny,), )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('api/', include('user_auth.urls')),
    path('api/', include('slots.urls')),
]


urlpatterns += [

    # path('swagger(<format>.json|.yaml)', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None),
        name='schema-swagger-ui')
]

urlpatterns += [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]