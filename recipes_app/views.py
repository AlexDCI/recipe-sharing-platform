from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile


@login_required
def home(request):
    context = {}
    try:
        context['profile'] = request.user.profile
    except Profile.DoesNotExist:
        context['profile'] = None  # Если у пользователя нет профиля
    return render(request, 'recipes_app/home.html', context)