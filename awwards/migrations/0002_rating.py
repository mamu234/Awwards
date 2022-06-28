# Generated by Django 4.0.5 on 2022-06-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
