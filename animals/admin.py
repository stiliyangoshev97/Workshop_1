from django.contrib import admin

from animals.models import Animal, OtherPhotos, Comment

# Register your models here.


admin.site.register(Animal)
admin.site.register(OtherPhotos)
admin.site.register(Comment)