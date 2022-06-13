# Generated by Django 3.2.10 on 2022-03-31 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20220328_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
