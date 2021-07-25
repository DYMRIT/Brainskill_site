from django.contrib import admin
from courses.models import Course, Type, BaseForArticle, Homework


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_course': ('name_course',)}


admin.site.register(Course, PostAdmin)
admin.site.register(Type)
admin.site.register(BaseForArticle)
admin.site.register(Homework)