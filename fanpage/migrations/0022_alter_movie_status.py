# Generated by Django 5.0.7 on 2024-07-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanpage', '0021_delete_newsarticle_delete_relatedlinks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('released', 'Released Movie'), ('upcoming', 'Upcoming Movie')], default='released', max_length=10),
        ),
    ]
