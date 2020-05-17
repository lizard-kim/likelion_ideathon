<<<<<<< HEAD
# Generated by Django 3.0.6 on 2020-05-16 10:44
=======
# Generated by Django 3.0.5 on 2020-05-13 17:31
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
<<<<<<< HEAD
import signIn.models
=======
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('auth', '0011_update_proxy_permissions'),
=======
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
<<<<<<< HEAD
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
=======
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('user_school', models.CharField(blank=True, max_length=20, null=True)),
                ('user_about', models.TextField(blank=True, max_length=100, null=True)),
                ('user_contact', models.TextField(blank=True, max_length=200, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
<<<<<<< HEAD
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
=======
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab
            ],
            options={
                'abstract': False,
            },
<<<<<<< HEAD
            managers=[
                ('objects', signIn.models.MyUserManager()),
            ],
=======
>>>>>>> 425981045af651f982f323c7d9a00500584a81ab
        ),
        migrations.CreateModel(
            name='Idea_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='idea.Idea')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]