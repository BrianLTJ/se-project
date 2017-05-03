'''

Decorators for project

'''

from django.http import JsonResponse



'''
Response JSONs
'''
method_not_allowed = {"result": "error", "message": "Invalid request"}


'''
# Filter request via method
Usage:
@accept_methods(['GET','post'])
Pass accepted methods.
'''
def accept_methods(accepted_methods):
    def decorator(func):
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
                return JsonResponse(method_not_allowed)

        return wrapper

    return decorator




