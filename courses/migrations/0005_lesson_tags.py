# Generated by Django 4.0.3 on 2022-04-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]
