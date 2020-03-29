# Generated by Django 3.0.2 on 2020-03-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='category_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
