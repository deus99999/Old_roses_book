from django.contrib import admin
from .models import Text


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Text, PostAdmin)

