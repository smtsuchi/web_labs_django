# Generated by Django 3.2.8 on 2022-02-27 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_labs', '0007_alter_lesson_starter_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='test_case',
            field=models.TextField(blank=True),
        ),
    ]
