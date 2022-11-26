from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def char_DashFormatting(value):
    """
    String을 전화번호 형태로 변환, 
    핸드폰 - 8자리, 집전화 - 7자리
    """
    PHONE, TEL = 11, 10
    if len(value) == PHONE:
        return f"{value[:3]}-{value[3:7]}-{value[7:]}"
    elif len(value) == TEL:
        return f"{value[:3]}-{value[3:6]}-{value[6:]}"