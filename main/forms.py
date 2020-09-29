from django.core.exceptions import ValidationError
from django.forms import ModelForm

from main.models import MainUser


class UserForm(ModelForm):
    class Meta:
        model = MainUser
        fields = '__all__'

    def clean_pin(self):
        pin = self.cleaned_data['pin']
        if not pin.isnumeric():
            raise ValidationError('Введите корректные данные')
        return pin
