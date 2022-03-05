from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

# Create your models here.
class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_pro = models.BooleanField(default=False)
    about = models.TextField()
    night_mode = models.BooleanField(default=False)
    github = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=60)
    website = models.CharField(max_length=60)
    is_public = models.BooleanField(default=True)
    image = models.ImageField()
    last_lesson_url = models.CharField(max_length=100)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.username}'
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

class Course(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    url_path = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    def __str__(self):
        return f'{self.title}'

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url_path = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    def __str__(self):
        return f'{self.title}'

class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url_path = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    question = models.TextField()
    instructions = models.TextField(max_length=600)
    test_case = models.TextField(blank=True)
    assertions = models.TextField(blank=True)
    hints = models.TextField(blank=True)
    checker = models.TextField(max_length=600, blank=True)
    starter_code = models.TextField(blank=True)
    def __str__(self):
        return f'{self.title}'


class User_Lesson(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    code = models.CharField(max_length=1000, blank=True)
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username}|{self.lesson.id}'