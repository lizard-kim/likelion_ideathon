from django import template

register = template.Library() 

@register.simple_tag 
def getvalue(d, k):
    return d.get(k)
