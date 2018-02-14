from django.shortcuts import render
from .models import User, Experience, Education, Skill, Interest, AwardAndCertification


def homepage(request, user):
    user_info = User.objects.get(user=user)
    user_id = User.objects.get(user="luo").id
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
    return render(request, 'index.html', context=context)
