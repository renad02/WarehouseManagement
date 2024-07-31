from django.urls import path, include
from .views import change_password, register_user, user_login, user_logout, ProductsViewSet, CustomersViewSet, SuppliersViewSet, OrderViewSet, InvoiceViewSet, ReportViewSet, WarehouseViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductsViewSet, basename='products')
router.register('customers', CustomersViewSet, basename='customers')
router.register('suppliers', SuppliersViewSet, basename='suppliers')
router.register('orders', OrderViewSet, basename='orders')
router.register('invoices', InvoiceViewSet, basename='invoices')
router.register('reports', ReportViewSet, basename='reports')
router.register('warehouses', WarehouseViewSet, basename='warehouses')


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('', include(router.urls)),
]
