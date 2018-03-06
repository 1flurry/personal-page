from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import UserProfile, Experience, Education, Skill, Interest, AwardAndCertification
from .forms import LoginForm


class HomePageView(View):
    def get(self, request, login_user):
        user_info = UserProfile.objects.get(username=login_user)
        user_id = UserProfile.objects.get(username=login_user).id
        experience_info = Experience.objects.filter(user_id=user_id)
        education_info = Education.objects.filter(user_id=user_id)
        skill_info = Skill.objects.filter(user_id=user_id)
        interest_info = Interest.objects.filter(user_id=user_id)
        award_and_certification_info = AwardAndCertification.objects.filter(user_id=user_id)
        context = {
            'user_info': user_info,
            'experience_info': experience_info,
            'education_info': education_info,
            'skill_info': skill_info,
            'interest_info': interest_info,
            'award_and_certification_info': award_and_certification_info,
        }
        return render(request, 'homepage.html', context=context)


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage', username)
            else:
                render(request, 'login.html')
        else:
            render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')