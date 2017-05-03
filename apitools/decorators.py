'''

Decorators for project

'''
import functools
from django.http import JsonResponse
from django.contrib.auth.models import Group, User, Permission, ContentType

'''
Response JSONs
'''
response_method_not_allowed = JsonResponse({"result": "error", "message": "Invalid request"})
response_permission_not_allowed = JsonResponse({"result": "error", "message": "Permission Denied"})

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
            user = args[0].user
            allowed = user.has_perms(perms) & user.is_authenticated()
            if allowed:
                return func(*args,**kw)
            else:
                return response_permission_not_allowed

        return wrapper

    return decorator

