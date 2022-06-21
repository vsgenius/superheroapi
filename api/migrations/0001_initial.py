# Generated by Django 4.0.5 on 2022-06-20 23:05

import api.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('company', models.CharField(blank=True, max_length=40, verbose_name='Компания')),
                ('position', models.CharField(blank=True, max_length=40, verbose_name='Должность')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('type', models.CharField(choices=[('online-university', 'Онлайн Университет'), ('user', 'Пользователь'), ('university', 'Университет'), ('school', 'Школа'), ('admin', 'администратор')], default='buyer', max_length=20, verbose_name='Тип пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Список пользователей',
                'ordering': ('email',),
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=350, null=True)),
                ('base', models.CharField(max_length=350, null=True)),
                ('hero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Powerstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intelligence', models.PositiveIntegerField()),
                ('strength', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
                ('durability', models.PositiveIntegerField()),
                ('power', models.PositiveIntegerField()),
                ('combat', models.PositiveIntegerField()),
                ('hero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xs', models.URLField()),
                ('sm', models.URLField()),
                ('md', models.URLField()),
                ('lg', models.URLField()),
                ('hero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupAffiliation', models.TextField(null=True)),
                ('relatives', models.TextField(null=True)),
                ('hero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmEmailToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='When was this token generated')),
                ('key', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Key')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_tokens', to=settings.AUTH_USER_MODEL, verbose_name='The User which is associated to this password reset token')),
            ],
            options={
                'verbose_name': 'Токен подтверждения Email',
                'verbose_name_plural': 'Токены подтверждения Email',
            },
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=300, null=True)),
                ('alterEgos', models.CharField(max_length=300, null=True)),
                ('aliases', models.CharField(max_length=300, null=True)),
                ('placeOfBirth', models.CharField(max_length=300, null=True)),
                ('firstAppearance', models.CharField(max_length=300, null=True)),
                ('publisher', models.CharField(max_length=300, null=True)),
                ('alignment', models.CharField(max_length=150, null=True)),
                ('hero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50, null=True)),
                ('race', models.CharField(max_length=50, null=True)),
                ('height', models.CharField(max_length=50, null=True)),
                ('weight', models.CharField(max_length=50, null=True)),
                ('hero_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hero')),
            ],
        ),
    ]