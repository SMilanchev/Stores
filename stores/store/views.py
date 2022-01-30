from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from stores.store.forms import CreateStoreForm, EditStoreForm
from stores.store.models import Store


def index(request):
    store = Store.objects.first()
    is_owner = request.user == store.owner
    context = {
        'store': store,
        'is_owner': is_owner,
    }
    return render(request, 'index.html', context)


@login_required
def create_store(request):
    if request.method == 'POST':
        form = CreateStoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = CreateStoreForm()

    context = {
        'form': form,
    }

    return render(request, 'create_store.html', context)


@login_required
def update_store(request, pk):
    store = Store.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditStoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditStoreForm(instance=store)

    context = {
        'form': form,
        'store_pk': store.id,
    }

    return render(request, 'update_store.html', context)
