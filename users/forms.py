from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .models import Profile

class CustomUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)  # Добавляем имя
    last_name = forms.CharField(max_length=50, required=True)   # Добавляем фамилию
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]  # Сохраняем имя
        user.last_name = self.cleaned_data["last_name"]    # Сохраняем фамилию
        if commit:
            user.save()
        return user
    

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)  # Добавляем имя
    last_name = forms.CharField(max_length=50, required=True)   # Добавляем фамилию

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'location', 'birth_date', 'avatar']  # Поля профиля

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.first_name = self.cleaned_data["first_name"]  # Сохраняем имя
        profile.last_name = self.cleaned_data["last_name"]    # Сохраняем фамилию
        if commit:
            profile.save()
        return profile
