# Generated by Django 5.0.7 on 2024-07-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanpage', '0020_video_video_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsArticle',
        ),
        migrations.DeleteModel(
            name='RelatedLinks',
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
