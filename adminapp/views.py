from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm
from admin.contrid.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url = '/')
def index(request):
    return render(request, 'adminapp/index.html')

@user_passes_test(lambda u: u.is_superuser, login_url = '/')
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url = '/')
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url = '/')
def admin_users_update(request, user_id):
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance = request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance = user)
    context = {'form': form, 'user': user,}
    return render(request, 'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url = '/')
def admin_users_delete(request, user_id):
    user = User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
