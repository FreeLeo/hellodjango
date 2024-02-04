from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.models import Subject, SubjectMapper, Teacher
from polls.serializers import SubjectSerializer, TeacherSerializer
from django.shortcuts import render


@api_view(('GET', ))
def api_show_subjects(request: HttpRequest):
    queryset = Subject.objects.all()
    serializer = SubjectSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(('GET', ))
def show_subjects_json(request):
    queryset = Subject.objects.all()
    subjects = []
    for subject in queryset:
        subjects.append(SubjectMapper(subject).as_dict())
    # return JsonResponse(subjects, safe=False, json_dumps_params={'ensure_ascii': False})
    return Response(subjects)


@api_view(('GET',))
def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        subject = Subject.objects.only('name').filter(no=sno).first()
        teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
        subjectSerializer = SubjectSerializer(subject, many=False)
        teacherSerializer = TeacherSerializer(teachers, many=True)
        return Response({'subject': subjectSerializer.data, 'teachers': teacherSerializer.data})
    except (TypeError, ValueError, Subject.DoesNotExist) as e:
        print(e)
        return Response(status=404)
