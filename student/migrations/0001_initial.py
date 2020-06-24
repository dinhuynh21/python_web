# Generated by Django 2.2.8 on 2020-04-10 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fee', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CambridgeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fee', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('room', models.CharField(max_length=20)),
                ('shift', models.CharField(default=1, max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('note', models.TextField(blank=True, default='', max_length=200)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='student.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birtdate', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('phone_number_1', models.CharField(max_length=12)),
                ('phone_number_2', models.CharField(blank=True, default='', max_length=12, null=True)),
                ('identity_number', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('is_learning', models.BooleanField(default=True)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('note', models.TextField(blank=True, max_length=200, null=True)),
                ('learning_area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='learning_area', to='student.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_male', models.BooleanField(default=False)),
                ('birthdate', models.DateField()),
                ('address', models.TextField(blank=True, default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('identity_number', models.CharField(default='', max_length=10)),
                ('note', models.TextField(blank=True, default='', max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='area', to='student.Area')),
            ],
        ),
        migrations.CreateModel(
            name='SystemLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fee', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, default='', max_length=200)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.Area')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='student.Book')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.Area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=50)),
                ('course_date', models.CharField(blank=True, max_length=50)),
                ('fee', models.IntegerField(default=0)),
                ('receipt_number', models.IntegerField()),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('note', models.TextField(blank=True, default='', max_length=100)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classer', to='student.Classes')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='student.SystemLevel'),
        ),
        migrations.AddField(
            model_name='classes',
            name='members',
            field=models.ManyToManyField(through='student.StudentInClass', to='student.Student'),
        ),
        migrations.AddField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='student.Teacher'),
        ),
    ]
