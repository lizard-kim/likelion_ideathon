# Generated by Django 3.0.5 on 2020-05-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200529_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/profile'),
        ),
    ]
