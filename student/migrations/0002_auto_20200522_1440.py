# Generated by Django 2.2.8 on 2020-05-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['name'], 'verbose_name_plural': 'Khu vực'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'verbose_name_plural': 'Sách'},
        ),
        migrations.AlterModelOptions(
            name='cambridgelevel',
            options={'ordering': ['name'], 'verbose_name_plural': 'Cambridge Level'},
        ),
        migrations.AlterModelOptions(
            name='classes',
            options={'ordering': ['name'], 'verbose_name_plural': 'Lớp'},
        ),
        migrations.AlterModelOptions(
            name='fee',
            options={'ordering': ['-payment_date'], 'verbose_name_plural': 'Học phí'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name'], 'verbose_name_plural': 'Học sinh'},
        ),
        migrations.AlterModelOptions(
            name='systemlevel',
            options={'ordering': ['name'], 'verbose_name_plural': 'Trình độ'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['name'], 'verbose_name_plural': 'Giáo viên'},
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birtdate',
            field=models.DateField(blank=True, null=True, verbose_name='Ngày sinh'),
        ),
        migrations.AlterField(
            model_name='student',
            name='joined_date',
            field=models.DateField(auto_now_add=True, verbose_name='Ngày vào học'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Tên học sinh'),
        ),
        migrations.AlterField(
            model_name='student',
            name='note',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Chú thích'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number_1',
            field=models.CharField(max_length=12, verbose_name='Số điện thoại'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number_2',
            field=models.CharField(blank=True, default='', max_length=12, null=True, verbose_name='Số điện thoại 2'),
        ),
    ]
