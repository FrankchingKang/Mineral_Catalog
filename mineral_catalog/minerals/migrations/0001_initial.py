# Generated by Django 2.2.4 on 2019-09-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minerals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_filename', models.CharField(default='', max_length=255)),
                ('image_caption', models.TextField(default='')),
                ('category', models.CharField(default='', max_length=255)),
                ('formula', models.CharField(default='', max_length=255)),
                ('strunz_classification', models.CharField(default='', max_length=255)),
                ('crystal_system', models.CharField(default='', max_length=255)),
                ('unit_cell', models.CharField(default='', max_length=255)),
                ('color', models.CharField(default='', max_length=255)),
                ('crystal_symmetry', models.CharField(default='', max_length=255)),
                ('cleavage', models.CharField(default='', max_length=255)),
                ('mohs_scale_hardness', models.CharField(default='', max_length=255)),
                ('luster', models.CharField(default='', max_length=255)),
                ('streak', models.CharField(default='', max_length=255)),
                ('diaphaneity', models.CharField(default='', max_length=255)),
                ('optical_properties', models.CharField(default='', max_length=255)),
                ('group', models.CharField(default='', max_length=255)),
                ('refractive_index', models.CharField(default='', max_length=255)),
                ('crystal_habit', models.CharField(default='', max_length=255)),
                ('specific_gravity', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
