from django import forms

from stores.common.mixins.bootstrap_form_mixins import BootstrapFormControlMixin
from stores.common.models import Category, Product


class CategoryCreateForm(BootstrapFormControlMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        cleaned_name = cleaned_name.lower()
        return cleaned_name


class CategoryUpdateForm(CategoryCreateForm):
    pass


class ProductCreateForm(BootstrapFormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateForm(BootstrapFormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('category_type',)
