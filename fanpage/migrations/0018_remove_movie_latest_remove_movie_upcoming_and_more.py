# Generated by Django 5.0.7 on 2024-07-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanpage', '0017_delete_movielist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='latest',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='upcoming',
        ),
        migrations.AddField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('released', 'Released'), ('upcoming', 'Upcoming')], default='released', max_length=10),
        ),
    ]
