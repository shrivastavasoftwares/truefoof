# Generated by Django 2.2.5 on 2021-02-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0003_remove_school_school_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='School_which_user',
            new_name='school_which_user',
        ),
        migrations.AddField(
            model_name='school',
            name='school_address',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
