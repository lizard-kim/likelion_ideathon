<<<<<<< HEAD
# Generated by Django 3.0.6 on 2020-05-16 10:44
=======
# Generated by Django 3.0.5 on 2020-05-13 17:31
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_title', models.CharField(blank=True, max_length=20, null=True)),
                ('idea_subtitle', models.TextField(blank=True, max_length=100, null=True)),
                ('idea_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('idea_description', models.TextField(blank=True, max_length=500, null=True)),
                ('idea_hashtag', models.TextField(blank=True, max_length=100, null=True)),
                ('idea_likecount', models.IntegerField(blank=True, null=True)),
                ('idea_create_data', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Idea_AddComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('create_data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Idea_image_storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.Idea')),
            ],
        ),
        migrations.CreateModel(
            name='Idea_Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('create_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('idea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='idea.Idea')),
            ],
        ),
    ]