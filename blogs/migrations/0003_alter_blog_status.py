# Generated by Django 5.1.5 on 2025-02-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_categorias_options_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.TextField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=20),
        ),
    ]
