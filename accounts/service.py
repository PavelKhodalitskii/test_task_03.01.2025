from django.contrib.auth.models import User, Group

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