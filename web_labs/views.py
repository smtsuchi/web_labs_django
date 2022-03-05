from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web_labs.serializers import CourseSerializer, SectionSerializer, LessonSerializer, RegistrationSerializer, User_LessonSerializer

# models
from .models import Course, Section, Lesson, Account, User_Lesson
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["GET"])
def index(request):
    return Response({'hello': 'there'})

@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getCourse(request, course_url):
    course = Course.objects.get(url_path=course_url)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
@api_view(['GET'])
def getSections(request, course_id):
    sections = Section.objects.filter(course=course_id)
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getSection(request, section_id):
    section = Section.objects.get(section=section_id)
    serializer = SectionSerializer(section)
    return Response(serializer.data)
@api_view(['GET'])
def getLessons(request, section_id):
    lessons = Lesson.objects.filter(section=section_id)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getLessonsFromSectionURL(request, section_url):
    section = Section.objects.get(url_path=section_url)
    lessons = Lesson.objects.filter(section=section.id)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getLesson(request, lesson_url):
    lesson = Lesson.objects.get(url_path=lesson_url)
    serializer = LessonSerializer(lesson)
    return Response(serializer.data)


@api_view(["POST"])
def registerUser(request):
    serializer = RegistrationSerializer(data = request.data)
    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.get(user=account).key
        data = {
            'response': "Successfully registered a new user.",
            'email': account.email,
            'username': account.username,
            'token': token,
        }
    else:
        data = serializer.errors
    return Response(data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCompletedLessons(request):
    user = request.user
    completed_lessons = User_Lesson.objects.filter(user = user).all()
    completed_set = [l.lesson.id for l in completed_lessons]
    return  Response(completed_set)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def markLessonComplete(request):
    user = request.user
    lesson = Lesson.objects.get(id=request.data['id'])
    if User_Lesson.objects.filter(user=user).filter(lesson=lesson).first():
        return Response({'message':'Lesson already marked complete'})
    user_lesson = User_Lesson(user=user, lesson=lesson, complete=True, )
    serializer = User_LessonSerializer(user_lesson, data={"user":user.id, "lesson":lesson.id, "completed":True, "code":''},many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return  Response(serializer.errors)
















    # IDE Dependencies
from django.http import JsonResponse
import json
import subprocess
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .makeRunCode import makeRunCode

@csrf_exempt
def compile(request):
    if request.method == "POST":
        # language = request.POST.get("language")
        if request.POST:
            code = request.POST.get("code")
            assertions = json.loads(request.POST.get("assertions"))
        elif request.body:
            code = json.loads(request.body.decode('utf-8')).get('code')
            assertions = json.loads(request.body.decode('utf-8')).get('assertions')
            # assertions = json.loads(request.body.decode('utf-8')).get('assertions')

        new_code = makeRunCode(code, assertions)

        #write file
        from random import randrange
        substr = str(randrange(16**7))
        filePath = str(settings.STATIC_ROOT)+'/test.py'
        # filePath = str(settings.BASE_DIR)+'\\web_labs\\'+'test'+'.py'
        print(filePath)
        try:
            f= open(filePath,'w')
            f.write(new_code)
            f.close()
                    
            x = subprocess.check_output(f"python {str(settings.STATIC_ROOT)}/test.py", shell=True) 
        except Exception as err:
            print('error: ', err)
        # x = subprocess.check_output(f"python {str(settings.BASE_DIR)}\\web_labs\\test.py") 
        y=x.decode("utf-8")
        print("y",y)
        total=y.split('\n\\#\\#\\#\\#\\#\n')
        print(total)
        total[-1]=total[-1][:-2]
        if len(total) == 1:
            result = ''
            logs = [total[0].split('\n')[-1]]
            assertionsCompleted = {i:False for i in range(len(assertions))}
        else:
            group1 = total[0].split('\r\n')[1:]
            result = group1[-1]
            logs = group1[:-1]
            
            assertionGroup = total[-1]
            eachAssertion = assertionGroup.split('\n')
            assertionsCompleted = {i:(True if eachAssertion[i]=="True" else False) for i in range(len(eachAssertion))}
            if len(assertionsCompleted) != len(assertions):
                for i in range(len(assertions)):
                    assertionsCompleted[i] = assertionsCompleted.get(i, False)       
            print(assertionGroup) 
        
    return JsonResponse({"result":result,"logs":logs,"assertions":assertionsCompleted}, safe=False)