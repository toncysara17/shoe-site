from django import forms
from django.contrib.auth.forms import UserCreationForm
from shoeapp.models import User,Brand,Product


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "mobile", "usertype"]


        widgets={"usertype":forms.HiddenInput(attrs={"value":"customer"}),
            "first_name": forms.TextInput(attrs={"class": "form-control","placeholder":"First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mobile Number"}),
            "gender": forms.TextInput(attrs={"class": "form-control", "placeholder": "Gender"}),
        }

class UserSigninForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Password'}))

class BrandModelForm(forms.Form):
    class Meta:
        model = Brand
        fields = ["id","name","details","image"]

class ProductCreateForm(forms.Form):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "id":forms.TextInput(attrs={"class":"form-control p-2"}),
            "name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "details": forms.Textarea(attrs={"class": "form-control p-2"}),

        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        if price<500:
            msg="invalid price"
            self.add_error("price",msg)
