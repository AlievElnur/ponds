from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=2)
    phone = forms.CharField(max_length=70, min_length=4, help_text='Укажите в формате: +7 000 000-00-00')

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

