from django import template

register = template.Library()

@register.filter(name='cut') #decoraters
def cut(value,arg):
    """
    this cut out all values
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
