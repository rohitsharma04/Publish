#Filter to get type of field in the template
from django import template
register = template.Library()

@register.filter('type')
def type(ob):
    return 'password' if ob.__class__.__name__=='PasswordInput' else 'text'
