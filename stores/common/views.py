from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from stores.common.forms import ProductCreateForm, CategoryCreateForm, ProductUpdateForm, CategoryUpdateForm
from stores.common.models import Product, Category


def index(request):
    return render(request, 'index.html')


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'common/create_product.html', context)


@login_required
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductUpdateForm(instance=product)

    context = {
        'form': form,
        'product_id': product.id,
    }

    return render(request, 'common/update_product.html', context)


@login_required
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'common/create_category.html', context)


@login_required
def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryUpdateForm(instance=category)

    context = {
        'form': form,
        'category_id': category.id,
    }
    return render(request, 'common/update_category.html', context)


@login_required
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')