# Generated by Django 2.2 on 2019-12-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sregno', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('smarks', models.IntegerField()),
            ],
        ),
    ]
