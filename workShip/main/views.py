from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from vacancies.models import Vacancy

from .forms import *
from .utils import DataMixin
from .models import *


def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'main/index.html', {'vacancies': vacancies})


def register_company(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        profile_form = RegisterCompanyProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()

            print(profile_form.cleaned_data)

            profile = CompanyProfile.objects.create(
                user=new_user,
                company_name=profile_form.cleaned_data['company_name'],
                phone_number=profile_form.cleaned_data['phone_number'],
                logo=profile_form.cleaned_data['logo'],
                address=profile_form.cleaned_data['address'],
                about=profile_form.cleaned_data['about'],
                contact_patronymic=profile_form.cleaned_data['contact_patronymic']
                )


            return redirect('login')
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:

        user_form = RegisterUserForm
        profile_form = RegisterCompanyProfileForm

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'main/register_company.html', context=context)


def register_seaman(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        profile_form = RegisterSeamanProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()

            profile = Profile.objects.create(
                user=new_user,
                patronymic=profile_form.cleaned_data['patronymic'],
                birthdate=profile_form.cleaned_data['birthdate'],
                phone_number=profile_form.cleaned_data['phone_number'],
                photo=profile_form.cleaned_data['photo'])
            return redirect('login')
    else:

        user_form = RegisterUserForm
        profile_form = RegisterSeamanProfileForm

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'main/register_seaman.html', context=context)


def edit_company(request):
    profile = CompanyProfile.objects.get(user=request.user.id)

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = RegisterCompanyProfileForm(request.POST, request.FILES, instance=profile)

        print(user_form.errors)
        print(profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('personal_account_home')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = RegisterCompanyProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'main/edit_company.html', context=context)


def edit_seaman(request):
    profile = Profile.objects.get(user=request.user.id)

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = RegisterSeamanProfileForm(request.POST, request.FILES, instance=profile)

        print(user_form.errors)
        print(profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('personal_account_home')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = RegisterSeamanProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'main/edit_seaman.html', context=context)


def register(request):
    return render(request, 'main/register.html')


def in_develop(request):
    return render(request, 'main/in_develop.html')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register_company.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')