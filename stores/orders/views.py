from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from stores.common.models import Product
from stores.orders.models import Order, OrderProducts
from stores.profiles.models import Profile


@login_required
def add_to_order(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    category = product.category_type

    if not user.order_set.exists():
        order = Order(user=user)
        order.save()
    else:
        order = user.order_set.last()
        if order.is_send:
            order = Order(user=user)
            order.save()

    add_product_to_order = OrderProducts(
        product=product,
        order=order,
    )

    try:
        add_product_to_order.clean_product()
        add_product_to_order.save()
        return redirect('list category', product.category_type_id)
    except ValidationError as exc:
        return render(request, 'common/list_category.html', context={
            'category': category,
            'errors': exc.message,
        })


@login_required
def send_order(request):
    user = request.user

    order: Order = user.order_set.last()
    order.is_send = True
    order.save()

    return redirect('details profile')