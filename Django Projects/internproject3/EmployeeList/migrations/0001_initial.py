# Generated by Django 2.2 on 2020-03-03 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('MobileNo', models.IntegerField()),
                ('Address', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('MobileNo', models.IntegerField()),
                ('Address', models.CharField(max_length=500)),
                ('CEO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hrs', to='EmployeeList.CEO')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('MobileNo', models.IntegerField()),
                ('Address', models.CharField(max_length=500)),
                ('HR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_managers', to='EmployeeList.HR')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='TeamLead',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('MobileNo', models.IntegerField()),
                ('Address', models.CharField(max_length=500)),
                ('ProjectManager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_leads', to='EmployeeList.ProjectManager')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=40)),
                ('MobileNo', models.IntegerField()),
                ('Address', models.CharField(max_length=500)),
                ('TeamLead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='EmployeeList.TeamLead')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]
