# Generated by Django 4.2 on 2023-07-24 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '5. Block',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='city')),
            ],
            options={
                'verbose_name_plural': '2. City',
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='locality')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.city')),
            ],
            options={
                'verbose_name_plural': '3. Locality',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='state')),
            ],
            options={
                'verbose_name_plural': '1. State',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='project')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.locality')),
            ],
            options={
                'verbose_name_plural': '4. Project',
            },
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_no', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('price_sq_ft', models.CharField(max_length=100)),
                ('total_price', models.CharField(max_length=100)),
                ('dimension', models.CharField(max_length=100)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.block')),
            ],
            options={
                'verbose_name_plural': '6. Plat',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.state'),
        ),
        migrations.AddField(
            model_name='block',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]
