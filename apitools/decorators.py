'''

Decorators for project

'''
import functools
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.models import Group, User, Permission, ContentType

'''
Response JSONs
'''
response_method_not_allowed = JsonResponse({"result": "error", "message": "Invalid request"})
response_permission_not_allowed = JsonResponse({"result": "error", "message": "Permission Denied"})
response_permission_not_allowed_redirect = '/'
login_url = '/login'
# response_permission_not_allowed = HttpResponseForbidden
'''
# Filter request via method
Usage:
@accept_methods(['GET','post'])
Pass accepted methods.
'''
def accept_methods(accepted_methods):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            allowed = False
            req_method = args[0].method.upper()
            for i in accepted_methods:
                if i.upper() == req_method:
                    allowed = True
                    break

            if allowed:
                return func(*args,**kw)
            else:
                return response_method_not_allowed

        return wrapper

    return decorator


'''
# Permission Control
Usage:
@have_perms(['appname.codename','appname.codename2'])
Pass accepted methods.
Reject unauthorized request with JSON responses.
Check items:
Superuser pass
User logged in
User is_active is true
User is_anonymous is false
User has the permission
'''
def have_perms(perms):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            allowed = False
            try:
                user = args[0].user
                allowed = user.has_perms(perms) & user.is_authenticated()
                # Let superuser pass
                if user.is_superuser:
                    allowed = True
            except:
                return HttpResponseRedirect(login_url)

            if allowed:
                return func(*args,**kw)
            else:
                if args[0].is_ajax():
                    return response_permission_not_allowed
                else:
                    return HttpResponseRedirect(response_permission_not_allowed_redirect)

        return wrapper

    return decorator

