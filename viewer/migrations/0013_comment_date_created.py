# Generated by Django 3.2.5 on 2022-12-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0012_glbmodels_ipr_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]