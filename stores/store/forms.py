from django import forms

from stores.common.mixins.bootstrap_form_mixins import BootstrapFormControlMixin
from stores.store.models import Store


class CreateStoreForm(BootstrapFormControlMixin, forms.ModelForm):
    class Meta:
        model = Store
        exclude = ('owner',)


class EditStoreForm(CreateStoreForm):
    pass