# Generated by Django 3.2.8 on 2022-03-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_labs', '0009_alter_user_lesson_date_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_lesson',
            name='code',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
