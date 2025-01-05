from django.contrib.auth.models import User, Group

class UserController:
    @staticmethod
    def set_group(user: User, group_name: str) -> None:
        '''
        Используйте эту функцию, что бы установить пользователю группу
        '''
        group = Group.objects.get(name=group_name)
        user.groups.add(group.id)
        user.save()