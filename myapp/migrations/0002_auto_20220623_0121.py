# Generated by Django 3.2.10 on 2022-06-22 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=800)),
                ('image', models.FileField(upload_to='posts/')),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('Technology', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='prof_pic',
            field=models.ImageField(blank=True, default='profile/a.jpg', upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Welcome Me!', max_length=800),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]