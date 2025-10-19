from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart_view, name="cart_view"),
    path("add/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.checkout_view, name="checkout"),
]
