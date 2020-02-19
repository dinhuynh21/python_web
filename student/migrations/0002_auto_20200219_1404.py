# Generated by Django 2.2.8 on 2020-02-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='course_date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fee',
            name='level',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fee',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classer', to='student.Class'),
        ),
    ]