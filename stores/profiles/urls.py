from django.urls import path
from stores.profiles.views import details_profile, edit_profile

urlpatterns = [
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
]

from stores.profiles import signals