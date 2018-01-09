
from django.shortcuts import redirect


def ajax_required(func):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return redirect('dashboard:index')
        return func(request,*args,**kwargs)
    return wrap