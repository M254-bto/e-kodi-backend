from django.urls import path, include
from .views import tenants, tenant_by_id, create_tenant, update_tenant, delete_tenant, tenant_by_appartment

urlpatterns = [
    path('', tenants, name='tenants'),
    path('auth/', include('rest_auth.urls')),
    path('new/', create_tenant, name='create_tenant'),
    path('<int:tenant_id>/', tenant_by_id, name='tenant_by_id'),
    path('<int:tenant_id>/update/', update_tenant, name='update_tenant'),
    path('<int:tenant_id>/delete/', delete_tenant, name='delete_tenant'),
    path('app/<int:appartment_id>/', tenant_by_appartment, name='tenant_by_appartment'),
    # path('rent/<int:tenant_id>/', mpesa_payment, name='mpesa_payment'),

]

