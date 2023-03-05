from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2, 
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}) )
