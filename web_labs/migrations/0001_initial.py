# Generated by Django 3.2.8 on 2021-10-19 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_pro', models.BooleanField(default=False)),
                ('about', models.TextField()),
                ('night_mode', models.BooleanField(default=False)),
                ('github', models.CharField(max_length=30)),
                ('linkedin', models.CharField(max_length=60)),
                ('website', models.CharField(max_length=60)),
                ('is_public', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='')),
                ('last_lesson_url', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('url_path', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=600)),
                ('question', models.TextField(max_length=600)),
                ('instructions', models.TextField(max_length=600)),
                ('test_case', models.TextField(max_length=600)),
                ('starter_code', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='User_Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=1000)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_labs.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=600)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_labs.course')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_labs.section'),
        ),
    ]
