# До рефакторингу
def check_role(user):
    if user.role == 'admin':
        return 'Access granted: Admin privileges'
    elif user.role == 'editor':
        return 'Access granted: Editor privileges'
    elif user.role == 'viewer':
        return 'Access granted: Viewer privileges'
    else:
        return 'Access denied'
    

# після рефакторингу
    def check_role(user):
    role_access = {
        'admin': 'Access granted: Admin privileges',
        'editor': 'Access granted: Editor privileges',
        'viewer': 'Access granted: Viewer privileges'
    }
    return role_access.get(user.role, 'Access denied')


#Приклад 
class User:
    def __init__(self, role):
        self.role = role

user1 = User('admin')

print(check_user_role(user1))  # Виведе: Access granted: Admin privileges

