# Generated by Django 3.0.5 on 2020-05-29 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0004_auto_20200530_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea_comments',
            name='idea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='idea.Idea'),
        ),
    ]