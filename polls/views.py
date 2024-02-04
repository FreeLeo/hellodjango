from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from polls.captcha import Captcha
from polls.models import Subject, SubjectMapper, Teacher, User
from polls.utils import gen_md5_digest, gen_random_code
from django.db.models import Avg

# Create your views here.


def show_teacher_charts(request):
    return render(request, 'teachers_data.html')


def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_subjects_vue(request):
    return render(request, 'subjects_vue.html')


def show_subjects_json(request):
    queryset = Subject.objects.all()
    subjects = []
    for subject in queryset:
        subjects.append(SubjectMapper(subject).as_dict())
    return JsonResponse(subjects, safe=False, json_dumps_params={'ensure_ascii': False})


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))  # 啥意思
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(
                subject=subject).order_by('no')
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    try:
        tno = int(request.GET.get('tno'))
        teacher = Teacher.objects.get(no=tno)
        if request.path.startswith('/praise/'):
            teacher.good_count += 1
            count = teacher.good_count
        else:
            teacher.bad_count += 1
            count = teacher.bad_count
        teacher.save()
        data = {'code': 20000, 'mesg': '投票成功', 'count': count}
    except (ValueError, Teacher.DoesNotExist):
        data = {'code': 20001, 'mesg': '投票失败'}
    return JsonResponse(data)


# wangdachui和hellokitty密码分别是1qaz2wsx和Abc123!!
def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(
                username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {'hint': hint})


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')


def get_captcha(request: HttpRequest) -> HttpResponse:
    captcha_text = gen_random_code()
    print(f"captcha_text: {captcha_text}")
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def get_teachers_data(request):
    # queryset = Teacher.objects.all()
    # names = [teacher.name for teacher in queryset]
    # good_counts = [teacher.good_count for teacher in queryset]
    # bad_counts = [teacher.bad_count for teacher in queryset]

    # queryset = Teacher.objects.values('subject').annotate(
    #     good=Avg('good_count'), bad=Avg('bad_count'))
    queryset = Teacher.objects.values('subject__intro').annotate(
        good=Avg('good_count'), bad=Avg('bad_count'))
    print(queryset)
    names = [data['subject__intro'] for data in queryset]
    print(names)
    good_counts = [data['good'] for data in queryset]
    bad_counts = [data['bad'] for data in queryset]
    return JsonResponse({'names': names, 'good': good_counts, 'bad': bad_counts})
