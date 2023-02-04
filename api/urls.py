from .views import *
from .views_api import *
from django.urls import path, re_path

# swagger

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='homePage'),

    path('api/v1/docs/download/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/v1/cutLink/', CutLinkAPIView.as_view(), name='cutLink'),
    path('api/v1/link/<str:key>/', GetLinkAPIView.as_view(), name='link_statistics'),
    path('api/v1/allStatistics/', GetAllStatisticsAPIView.as_view(), name='allStatistics'),

    path('<str:key>/statistics/', LinkStatisticsPageTemplateView.as_view(), name='link_statistics'),
    path('<str:key>/', ForwardingPageTemplateView.as_view(), name='forwarding'),
]
