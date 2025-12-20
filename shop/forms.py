from django import forms
from .models import UserProfile,Product
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'profile_image']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

