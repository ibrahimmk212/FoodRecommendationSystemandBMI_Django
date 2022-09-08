from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import Account


class ExpertRegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'phone',
                  'password1',
                  'password2',

                  )


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Incorrect email or password, try again.")
