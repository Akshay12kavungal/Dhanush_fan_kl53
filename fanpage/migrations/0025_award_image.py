# Generated by Django 5.0.7 on 2024-07-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanpage', '0024_remove_award_description_award_category_award_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='image',
            field=models.ImageField(blank=True, upload_to='Awards/'),
        ),
    ]