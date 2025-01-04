from django.contrib.auth.models import User

class UserController:
    @staticmethod
    def get_user_by_pk(pk):
        '''
        Используйте эту функцию, что бы получить пользователя по первичному ключу
        '''
        user = User.objects.get(pk=pk)
        return user