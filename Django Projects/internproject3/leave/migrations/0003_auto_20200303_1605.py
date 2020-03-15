# Generated by Django 2.2 on 2020-03-03 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_ceo_hr_projectmanager_teamlead_teammember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr',
            name='CEO',
        ),
        migrations.RemoveField(
            model_name='projectmanager',
            name='HR',
        ),
        migrations.RemoveField(
            model_name='teamlead',
            name='ProjectManager',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='TeamLead',
        ),
        migrations.DeleteModel(
            name='CEO',
        ),
        migrations.DeleteModel(
            name='HR',
        ),
        migrations.DeleteModel(
            name='ProjectManager',
        ),
        migrations.DeleteModel(
            name='TeamLead',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]
