from django import forms

from core.models import MailTest


class MailForms(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'placeholder': "Email",'class': 'form-control'}))

    class Meta:
        model = MailTest
        fields = '__all__'
