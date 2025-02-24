from django.urls import path
from .views import home, about, contact, ProductListCreateView, ProductRetrieveUpdateDeleteView, delete_product

urlpatterns = [
    # Template-based views
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # REST API views
    path('api/products/', ProductListCreateView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),

    # Delete product view
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
]
