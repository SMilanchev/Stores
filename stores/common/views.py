from django.shortcuts import render, redirect

from stores.common.forms import ProductCreateForm, CategoryCreateForm


def index(request):
    return render(request, 'index.html')


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