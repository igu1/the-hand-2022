from django.forms import ModelForm
from .models import ClientMessages


class ClientMessageForm(ModelForm):
    class Meta:
        model = ClientMessages
        fields = ['name', 'email', 'phone_number' , 'message']