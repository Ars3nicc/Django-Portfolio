# Generated by Django 4.2.4 on 2023-08-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolStacks',
            fields=[
                ('stackid', models.AutoField(primary_key=True, serialize=False)),
                ('teck_stacks', models.CharField(max_length=50, verbose_name='Tech Stacks')),
                ('design_stacks', models.CharField(max_length=50, verbose_name='Design Stacks')),
                ('documentation_stacks', models.CharField(max_length=50, verbose_name='Documentation Stacks')),
            ],
        ),
    ]
