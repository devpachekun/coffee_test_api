# Generated by Django 5.0.6 on 2024-06-29 01:39

import api.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id_coffee', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image64', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('correo', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('rol', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', api.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id_transaccion', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_transaccion', models.CharField(max_length=200)),
                ('tipo_gasto', models.CharField(max_length=200)),
                ('sub_categoria', models.CharField(max_length=200)),
                ('monto', models.IntegerField()),
                ('fecha_transaccion', models.DateField()),
                ('nota', models.CharField(max_length=200)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
