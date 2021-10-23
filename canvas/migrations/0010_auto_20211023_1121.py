# Generated by Django 3.0.14 on 2021-10-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0009_auto_20210702_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvascourseregistration',
            name='is_blocked',
        ),
        migrations.RemoveField(
            model_name='canvascourseregistration',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='canvascourseregistration',
            name='status',
            field=models.CharField(choices=[('UNREGISTERED', 'UNREGISTERED'), ('PENDING_VERIFICATION', 'PENDING_VERIFICATION'), ('VERIFIED', 'VERIFIED'), ('BLOCKED', 'BLOCKED')], default='UNREGISTERED', max_length=100),
        ),
    ]
