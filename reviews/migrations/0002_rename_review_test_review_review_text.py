# Generated by Django 4.2 on 2023-04-29 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_test',
            new_name='review_text',
        ),
    ]