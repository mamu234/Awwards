# Generated by Django 4.0.5 on 2022-06-18 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('user_name', models.CharField(blank=True, max_length=30)),
                ('prof_pic', models.ImageField(blank=True, default='profile/a.jpg', upload_to='profiles/')),
                ('bio', models.CharField(default='Welcome Me!', max_length=800)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=50)),
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
    ]
