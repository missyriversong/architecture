# Generated by Django 5.0.2 on 2024-02-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.CharField(default='', help_text='Enter language', max_length=10),
        ),
    ]
