from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from account.forms import ExpertRegistrationForm, UserAuthenticationForm


def home(request):
    return render(request, 'home.html')


def admin_dashboard(request):
    return render(request, 'admindashboard.html')


def expert_registration_view(request):
    context = {}
    if request.POST:
        form = ExpertRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('home')
        else:
            context['expert_registration_form'] = form
    else:
        form = ExpertRegistrationForm()
        context['expert_registration_form'] = form
    return render(request, 'expert-registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def my_page_view(request):
    context = {}
    return render(request, "my-expert-page.html", context)


def my_profile_view(request):
    context = {}
    return render(request, "myprofile.html", context)


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('home')
        else:
            context['login_form'] = form
    else:
        form = UserAuthenticationForm()
        context['login_form'] = form
    return render(request, 'login.html', context)


