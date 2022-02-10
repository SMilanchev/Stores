from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView, UpdateView

from stores.common.forms import ProductCreateForm, CategoryCreateForm, ProductUpdateForm, CategoryUpdateForm
from stores.common.models import Product, Category


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'common/create_product.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


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


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'common/create_category.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'common/list_category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_empty = not self.object.product_set.all().exists()
        context['category_empty'] = category_empty
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'common/update_category.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.object.id
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@login_required
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')