# Generated by Django 3.2.16 on 2022-10-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_rename_board_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
