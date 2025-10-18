from django.shortcuts import render, redirect, get_object_or_404
from apps.products.models import Product
from .models import Order, OrderItem

def cart_view(request):
    order_id = request.session.get("order_id")
    order = Order.objects.filter(id=order_id, is_paid=False).first()
    return render(request, "orders/cart.html", {"order": order})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_id = request.session.get("order_id")
    order, created = Order.objects.get_or_create(
        id=order_id, defaults={"buyer": request.user}
    )
    OrderItem.objects.create(order=order, product=product, quantity=1)
    request.session["order_id"] = order.id
    return redirect("cart_view")

def checkout_view(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        order.is_paid = True
        order.save()
        del request.session["order_id"]
        return redirect("payment_success")
    return render(request, "orders/checkout.html", {"order": order})
