from django.template import Library

from stores.profiles.models import Profile

register = Library()


@register.inclusion_tag('tags/profile_complete.html', takes_context=True)
def profile_complete_notification(context):
    user_id = context.request.user.id
    profile = Profile.objects.get(pk=user_id)

    if profile.first_name and profile.last_name and profile.age and profile.image:
        profile.is_complete = True
    else:
        profile.is_complete = False

    return {'is_complete': profile.is_complete}
