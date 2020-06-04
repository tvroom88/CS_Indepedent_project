# make sure this is at the top if it isn't already
from django import forms
from .models import NewMenu

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )


class RegisterNewMenuForm(forms.ModelForm):

    class Meta:
        model = NewMenu
        fields = ('Menu', 'image', 'price', 'Info')