# Generated by Django 5.0.6 on 2024-07-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanpage', '0007_alter_newsarticle_read_more_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_lists/')),
            ],
        ),
    ]
