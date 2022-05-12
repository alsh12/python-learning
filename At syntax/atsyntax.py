import functools

user = {"username":"ashish","access_level":"admin"}

def make_func_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args,**kwargs):
            if user["access_level"] == "admin":
                return func(*args,**kwargs)
            else:
                return f"{user['username']} doesn't have proper permission."

        return secure_function
    return decorator


@make_func_secure("admin")
def get_password(role):
    if role == "normaluser":
        return "password"
    elif role == "secureuser":
        return "secure"

@make_func_secure("guest")
def get_password(role):
    return "guestuser"

print(get_password("secureuser"))

