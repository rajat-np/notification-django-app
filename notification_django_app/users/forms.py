from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

from notifications.models import Notification as NotificationModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class NotificationCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create'))

    class Meta:
        model = NotificationModel
        fields = ('actor_content_type', 'actor_object_id', 'recipient', 'verb', 'level', )
        labels = {
            'recipient': 'Recipient User',
            'verb': 'Message',
            'actor_content_type': 'Notification Creator',
            'actor_object_id': 'Notification Creator ID'
        }
