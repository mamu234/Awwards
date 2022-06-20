# Generated by Django 4.0.5 on 2022-06-18 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appawwards', '0002_tag_alter_post_options_remove_post_technology_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]