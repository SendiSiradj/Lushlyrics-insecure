from django.shortcuts import redirect
from django.conf import settings

def login_excluded():
    def decorator(view_method):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated :
                return redirect('default')
            return view_method(request, *args, **kwargs)
        return wrapper_func
    return decorator


