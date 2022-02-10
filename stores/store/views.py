from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from stores.profiles.models import Profile
from stores.store.forms import CreateStoreForm, EditStoreForm
from stores.store.models import Store


class IndexListView(ListView):
    model = Store
    template_name = 'index.html'
    context_object_name = 'stores'


class StoreCreateView(CreateView):
    model = Store
    form_class = CreateStoreForm
    template_name = 'create_store.html'
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        store = form.save(commit=False)
        store.owner = self.request.user
        store.save()
        form.save_m2m()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class StoreUpdateView(UpdateView):
    model = Store
    template_name = 'update_store.html'
    form_class = EditStoreForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store_pk'] = self.object.id
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
