from django import template

#create customer filter
register=template.Library()

def cut(value,arg):
    """
    this cuts out all values of "arg"from the string
    """
    return value.replace(arg,'')

#register this
register.filter('cut',cut)
#'cut'is the callable string, while the second cut is the defined function
