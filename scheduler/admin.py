from django.contrib import admin

from .models import Employee, Shift, Break, Note, Position

# Register your models here.
admin.site.register(Employee)
admin.site.register(Shift)
admin.site.register(Break)
admin.site.register(Note)
admin.site.register(Position)