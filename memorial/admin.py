from django.contrib import admin
from .models import Profile, Person, Memory, Picture, Soundtrack
# Register your models here.

admin.site.register(Profile)
admin.site.register(Person)
admin.site.register(Memory)
admin.site.register(Picture)
admin.site.register(Soundtrack)
