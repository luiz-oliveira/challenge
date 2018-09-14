from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from oauth2_provider import views as oauth2_views

app_name = "SERVER API"

# OAuth2 provider Endpoints
oauth2_endpoints = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token")
]

if settings.DEBUG:
    # OAuth2 Application Management Endpoints
    oauth2_endpoints += [
        path('applications', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<int:pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<int:pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<int:pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update")
    ]

    # OAuth2 Token Management Endpoints
    oauth2_endpoints += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<int:pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete")
    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth Endpoints
    path('api/v1/auth/', include((oauth2_endpoints, app_name), namespace="oauth2_provider")),
    # Auth Endpoints
    path('api/v1/customers/', include(('apps.customers.urls', app_name), namespace="customers"))
]
