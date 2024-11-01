from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserRegistrationForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.core.cache import cache
from django.shortcuts import render


class RegisterView(CreateView):
    model = User
    form_class = CustomUserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # email is being used as username
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправление на страницу входа после выхода



@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную страницу после сохранения
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def create_profile(request):
    # Если профиль уже существует, перенаправить пользователя на редактирование
    if hasattr(request.user, 'profile'):
        return redirect('edit_profile')  # Или куда вам нужно
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  # Перенаправление после создания профиля
    else:
        form = ProfileForm()

    return render(request, 'users/create_profile.html', {'form': form})


@login_required
def profile_view(request):
    # Получаем URL аватара из кеша, если он уже сохранен
    profile_image_url = cache.get(f"profile_image_{request.user.id}")

    profile = request.user.profile
    
    # Если URL аватара отсутствует в кеше, получаем его из профиля пользователя
    if not profile_image_url:
        profile = request.user.profile
        profile_image_url = profile.avatar.url if profile.avatar else None
        # Сохраняем URL аватара в кеше на 15 минут
        cache.set(f"profile_image_{request.user.id}", profile_image_url, timeout=60 * 15)
    
    # Передаем URL аватара в шаблон
    return render(request, 'users/profile.html', {
        'profile_image': profile_image_url,  # URL аватара
        'profile': profile  # Передаем объект профиля для отображения данных
    })