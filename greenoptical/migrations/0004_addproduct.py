# Generated by Django 3.1.4 on 2020-12-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenoptical', '0003_auto_20210101_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_catogory', models.CharField(max_length=20)),
                ('pd_detail', models.TextField()),
                ('pd_img_1_220x245', models.ImageField(upload_to='pics')),
                ('pd_name1', models.CharField(max_length=20)),
                ('pd_img_2_220x245', models.ImageField(upload_to='pics')),
                ('pd_name2', models.CharField(max_length=20)),
                ('pd_img_3_220x245', models.ImageField(upload_to='pics')),
                ('pd_name3', models.CharField(max_length=20)),
            ],
        ),
    ]
