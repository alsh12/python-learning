user = {"username":"ashish","access_level":"guest"}

def get_password():
    return "password"


def make_func_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"{user['username']} doesn't have proper permission."

    return secure_function

get_password = make_func_secure(get_password)

print(get_password())



