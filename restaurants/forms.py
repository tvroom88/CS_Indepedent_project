from django import forms
from restaurants.models import Menu, Restaurant
from account.models import Account
from django.contrib.auth.models import User

# class Restaurant(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     restaurant_name = models.CharField(max_length=50, null=False, blank=False)
#     phone = PhoneNumberField()


class RegisterRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        # fields = ('owner','restaurant_name', 'phone')
        fields = ('restaurant_name', 'phone')

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('Menu', 'price', 'Info')

    # def __init__(self, user, *args, **kwargs):
    #     super(MenuForm, self).__init__(*args, **kwargs)
    #     self.fields['restaurant'].queryset = Restaurant.objects.filter(restaurant = user)

class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('Menu', 'price', 'Info')

    def save(self, commit=True):
        menu = self.instance
        menu.Menu = self.cleaned_data['Menu']
        menu.price = self.cleaned_data['price']
        menu.Info = self.cleaned_data['Info']

        if commit:
            menu.save()
        return menu

