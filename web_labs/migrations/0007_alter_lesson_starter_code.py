# Generated by Django 3.2.8 on 2022-02-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_labs', '0006_lesson_assertions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='starter_code',
            field=models.TextField(blank=True),
        ),
    ]
