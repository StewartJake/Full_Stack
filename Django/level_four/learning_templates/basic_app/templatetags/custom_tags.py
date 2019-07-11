from django import template

register = template.Library()

@register.filter(name='cut')
def cut(val, arg):
    """
    Fn: cuts all instances of "arg" from "val"
    Arg: val and arg should be strings
    Ret: a string
    """
    return val.replace(arg,'')


# w/o decorator
#register.filter('cut',cut)
