# Generated by Django 3.2.10 on 2022-06-20 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appawwards', '0004_auto_20220620_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='country',
        ),
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sitename',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Welcome Me!', max_length=800),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prof_pic',
            field=models.ImageField(upload_to='profiles/images'),
        ),
    ]