from django.contrib import admin
from .models import PostModel,Comment,Contact
# Register your models here.

admin.site.register(PostModel)


admin.site.register(Comment)

admin.site.register(Contact)