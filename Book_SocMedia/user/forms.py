from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=20, required=True, help_text='Necessary')
    family_name = forms.CharField(max_length=30, required=True, help_text='Necessary')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(required=True, help_text = 'Necessary')
    bio = forms.CharField(max_length = 500, required = False, help_text = 'Optional')
    location = forms.CharField(max_length=30, required=False)
    phone_number = forms.IntegerField(max_value = 9999999999, required=False)
    class Meta:
        model = User
        fields = ('username', 'name', 'family_name', 'email', 'password1', 'password2', 'bio', 'phone_number',
                  'birth_date', 'location')
