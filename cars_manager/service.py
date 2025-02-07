from accounts.service import UserController
from .models import Comment, Car

# Тут я расположил классы, призванные инкапсулировать логику, связанную с моделями
# В этот раз, логики вышло не очень много, но обычно пригождается

class CarController:
    pass

class CommentsController:
    @staticmethod
    def get_comment(**kwargs) -> Comment:
        comments = Comment.objects.filter(**kwargs)
        if comments.exists():
            return comments.first()
        return None


    @staticmethod
    def create_comment(content: str, author_id: int, car: Car, reply_to: Comment) -> Comment:
        '''
        Используйте эту функцию, что бы создать комментарий
        '''

        author = UserController.get_user_by_pk(pk=author_id)     

        if not car or not author:
            return None
        
        new_comment = Comment(content=content, author=author, car=car, parent=reply_to)
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