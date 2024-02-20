"""
URL configuration for testproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from main import views


admin.site.site_header = "Age Giess"

schema_view = get_schema_view(
    openapi.Info(
        title="Age Guess API",
        default_version="v1",
        description="API",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)


urlpatterns = [    
    # Swagger Docs url
    path("", schema_view.with_ui("swagger"), name="schema-swagger-ui"),
    # Redoc Docs url
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('admin/', admin.site.urls),
    path('api/human-age/', views.HumanAgeView.as_view(), name='human_age_view'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

