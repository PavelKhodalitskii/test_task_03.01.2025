from django import template


register = template.Library()

@register.filter
def root_comments(queryset):
    '''
    Используйте этот фильтр, что бы получить "корневые" комментарии. 
    '''
    return queryset.filter(parent=None)