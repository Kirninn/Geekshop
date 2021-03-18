from django.shortcuts import render

def index(request):
    return render(request, 'adminapp/index.html')

def admin_users(request):
    return render(request, 'adminapp/admin-users-read.html')

def admin_users_create(request):
    return render(request, 'adminapp/admin_users_create.html')

def admin_users_update(request):
    return render(request, 'adminapp/admin_users_update_delete.html')

def admin_users_delete(request):
    pass
