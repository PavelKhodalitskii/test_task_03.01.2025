from django.contrib.auth.models import User, Group, Permission


class UserController:
    @staticmethod
    def get_user_by_pk(pk):
        '''
        Используйте эту функцию, что бы получить пользователя по первичному ключу
        '''
        user = User.objects.get(pk=pk)
        return user

    @staticmethod
    def set_group(user: User, group_name: str) -> None:
        '''
        Используйте эту функцию, что бы установить пользователю группу
        '''
        group = Group.objects.get(name=group_name)
        user.groups.add(group.id)
        user.save()

    @staticmethod
    def create_default_perm_group() -> Group:
        group = Group.objects.filter(name='default_user')
        if not group.exists():
            group = Group.objects.create(name='default_user')

            comments_permissions = Permission.objects.filter(codename__endswith='comment')
            car_permissions = Permission.objects.filter(codename__endswith='car')

            for comment_perm in comments_permissions:
                group.permissions.add(comment_perm.id)

            for car_perm in car_permissions:
                group.permissions.add(car_perm.id)

            group.save()
            return group
        
        return group.first()

    @staticmethod
    def register_user(username: str, password: str, first_name: str, last_name: str) -> User:
        '''
        Используйте этот метод, что-бы зарегстрировать пользователя в системе
        '''
        user = User.objects.filter(username=username)

        if not user.exists():
            user = User.objects.create(username=username,
                                    first_name=first_name,
                                    last_name=last_name)
            user.set_password(password)
            user.save()        
            UserController.set_group(user, 'default_user')        
            return user
        
        return user.first()