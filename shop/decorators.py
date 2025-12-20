from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # redirect if not logged in
        if not request.user.is_staff:  # or use is_superuser if you prefer
            messages.error(request, "You do not have permission to access this page.")
            return redirect('profile_page')  # or some other page
        return view_func(request, *args, **kwargs)
    return wrapper
