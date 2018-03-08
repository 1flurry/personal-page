from django.shortcuts import render
from django.views.generic import View
from .models import UserProfile, Experience, Education, Skill, Interest, Project


class HomePageView(View):
    def get(self, request):
        user_info = UserProfile.objects.get(username="pysteins")
        user_id = UserProfile.objects.get(username="pysteins").id
        experience_info = Experience.objects.filter(user_id=user_id)
        education_info = Education.objects.filter(user_id=user_id)
        skill_info = Skill.objects.filter(user_id=user_id)
        interest_info = Interest.objects.filter(user_id=user_id)
        project_info = Project.objects.filter(user_id=user_id)
        context = {
            'user_info': user_info,
            'experience_info': experience_info,
            'education_info': education_info,
            'skill_info': skill_info,
            'interest_info': interest_info,
            'project_info': project_info,
        }
        return render(request, 'homepage.html', context=context)
