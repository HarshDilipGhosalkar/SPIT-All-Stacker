# Generated by Django 3.1 on 2023-02-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0004_contentrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentdetails',
            name='adult_type',
            field=models.TextField(blank=True, null=True),
        ),
    ]
