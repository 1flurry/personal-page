from django.contrib import admin
from .models import UserProfile, Experience, Education, Skill, Interest, Project


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'number', 'email', 'sample_intro']


admin.site.register(UserProfile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Project)
