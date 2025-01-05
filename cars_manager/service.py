from accounts.service import UserController
from .models import Comments, Car

class CarController:
    @staticmethod
    def get_car(**kwargs) -> Car:
        cars = Car.objects.filter(**kwargs)
        if cars.exists():
            return cars.first()
        return None

class CommentsController:
    @staticmethod
    def get_comment(**kwargs) -> Comments:
        comments = Comments.objects.filter(**kwargs)
        if comments.exists():
            return comments.first()
        return None


    @staticmethod
    def create_comment(content: str, author_id: int, car: Car, reply_to: Comments) -> Comments:
        '''
        Используйте эту функцию, что бы создать комментарий
        '''

        author = UserController.get_user_by_pk(pk=author_id)     

        if not car or not author:
            return None
        
        new_comment = Comments(content=content, author=author, car=car, parent=reply_to)
        new_comment.save()

        return new_comment
    
    @staticmethod
    def delete_comment(comment_id: int):
        '''
        Используйте эту функцию, что-удалить комментарий.
        '''
        comment = CommentsController.get_comment(id=comment_id)
        if comment:
            comment.delete()