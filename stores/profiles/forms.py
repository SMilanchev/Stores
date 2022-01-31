from django import forms

from stores.common.mixins.bootstrap_form_mixins import BootstrapFormControlMixin
from stores.profiles.models import Profile


class EditProfileFrom(BootstrapFormControlMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
