from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),
    path('payments/', include('apps.payments.urls')),
        # added API endpoints
    path('api/', include('apps.products.urls_api')),
    path('api/', include('apps.orders.urls_api')),
    path('api/', include('apps.payments.urls_api')),
    path('api/auth/', include('apps.accounts.urls_api')),  # JWT & auth endpoints
]
