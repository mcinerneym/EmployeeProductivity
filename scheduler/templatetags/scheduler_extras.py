from django import template
from datetime import datetime, date

register = template.Library()

@register.filter
def subtractTimes(value, arg):
    return datetime.combine(date.today(), value) - datetime.combine(date.today(), arg)