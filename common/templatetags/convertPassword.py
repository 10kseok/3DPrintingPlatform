from django import template

register = template.Library()

@register.filter
def convertPassword(value):
    """
    패스워드를 글자길이와 무관하게 '********'형태로 변경시켜준다.
    """
    value = "********"
    return value