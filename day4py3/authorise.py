authorized_users = ["ankur", "khushi", "admin"]

def authorize(username):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if username in authorized_users:
                print(f" Access granted to: {username}")
                return func(*args, **kwargs)
            else:
                print(f" Access denied for: {username}. Not authorized!")
        return wrapper
    return decorator


@authorize("khushi")
def view_dashboard():
    print(" Viewing Dashboard...")


@authorize("guest")
def delete_user():
    print("User Deleted Successfully!")


view_dashboard()
delete_user()
