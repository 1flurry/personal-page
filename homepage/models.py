from django.db import models


class User(models.Model):
    user = models.CharField(max_length=128, verbose_name='用户名')
    name = models.CharField(max_length=128, verbose_name='姓名')
    address = models.CharField(max_length=256, verbose_name='地址')
    number = models.CharField(max_length=128, verbose_name='联系方式')
    email = models.CharField(max_length=128, verbose_name='邮箱')
    sample_intro = models.TextField(verbose_name='简介')
    Facebook_account = models.CharField(max_length=128, blank=True, verbose_name='Facebook账号')
    Twitter_account = models.CharField(max_length=128, blank=True, verbose_name='Twitter账号')
    Ins_account = models.CharField(max_length=128, blank=True, verbose_name='Ins账号')
    Github_account = models.CharField(max_length=128, blank=True, verbose_name='GitHub账号')
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='姓名')
    company = models.CharField(max_length=128, verbose_name='公司名')
    position = models.CharField(max_length=128, verbose_name='职位')
    content = models.TextField(verbose_name='内容')
    start_data = models.DateField(verbose_name='起始时间')
    end_data = models.DateField(default='至今', verbose_name='结束时间')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = '工作经历'
        verbose_name_plural = '工作经历'


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='姓名')
    name = models.CharField(max_length=128, verbose_name='校名')
    ACADEMIC = (('高中', '高中', ), ('大专', '大专', ), ('本科', '本科', ), )
    academic = models.CharField(max_length=128, choices=ACADEMIC, verbose_name='学历')
    major = models.CharField(max_length=128, verbose_name='专业')
    start_data = models.DateField(verbose_name='起始时间')
    end_data = models.DateField(default='至今', verbose_name='结束时间')
    mark = models.CharField(max_length=128, blank=True, verbose_name='成绩')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '教育经历'
        verbose_name_plural = '教育经历'


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='姓名')
    skill = models.CharField(max_length=128, verbose_name='技能')
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = '工作技能'
        verbose_name_plural = '工作技能'


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='姓名')
    interest = models.TextField(verbose_name='兴趣爱好')

    class Meta:
        verbose_name = '兴趣爱好'
        verbose_name_plural = '兴趣爱好'


class AwardAndCertification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='姓名')
    award_or_certification = models.CharField(max_length=128, verbose_name='获奖情况及证书')

    class Meta:
        verbose_name = '获奖及证书'
        verbose_name_plural = '获奖及证书'



