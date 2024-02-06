from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.models import Subject, SubjectMapper, Teacher
from polls.pagination import CustomizedPagination
from polls.serializers import SubjectSerializer, TeacherSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet


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
        teachers = Teacher.objects.filter(
            subject=subject).defer('subject').order_by('no')
        subjectSerializer = SubjectSerializer(subject, many=False)
        teacherSerializer = TeacherSerializer(teachers, many=True)
        return Response({'subject': subjectSerializer.data, 'teachers': teacherSerializer.data})
    except (TypeError, ValueError, Subject.DoesNotExist) as e:
        print(e)
        return Response(status=404)


# class SubjectView(ListAPIView):
#     subjects = Subject.objects.all()
#     serializer_class = SubjectSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # 指定如何分页
    pagination_class = CustomizedPagination
    
    def get_queryset(self):
        sno = self.request.GET.get('sno', None)
        queryset = super().get_queryset()

        if sno:
            # 如果传递了 sno 参数，就按照 sno 进行过滤
            queryset = queryset.filter(no=sno)

        return queryset
