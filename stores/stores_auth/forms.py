from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from stores.common.mixins.bootstrap_form_mixins import BootstrapFormControlMixin

UserModel = get_user_model()


class SignUpForm(BootstrapFormControlMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class SignInForm(BootstrapFormControlMixin, forms.Form):
    user = None
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        if not self.user:
            raise ValidationError('No user with such credentials!')

    def save(self):
        return self.user
