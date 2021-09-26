import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class EditUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class RegisterSeamanProfileForm(forms.ModelForm):
    patronymic = forms.CharField(label='Отчество (если имеется)', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}))
    phone_number = forms.CharField(label='Номер телефона', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}))
    birthdate = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    photo = forms.ImageField(label='Фото', required=False, widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = ('patronymic', 'phone_number', 'company_name', 'birthdate', 'photo')


class RegisterCompanyProfileForm(forms.ModelForm):
    company_name = forms.CharField(label='Название компании', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}))
    logo = forms.ImageField(label='Логотип', widget=forms.FileInput())
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}))
    about = forms.CharField(label='О компании', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    contact_patronymic = forms.CharField(label='Отчество (если имеется)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}))
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}))

    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'logo', 'address', 'about', 'contact_patronymic', 'phone_number')



class RegisterProfileForm(forms.ModelForm):
    patronymic = forms.CharField(label='Отчество (если имеется)', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}))
    phone_number = forms.CharField(label='Номер телефона', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}))
    is_company = forms.BooleanField(label='Это компания', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    company_name = forms.CharField(label='Название компании', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}))
    birthdate = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    photo = forms.ImageField(label='Фото', required=False, widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = ('patronymic', 'phone_number', 'company_name', 'birthdate', 'photo')




class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')
