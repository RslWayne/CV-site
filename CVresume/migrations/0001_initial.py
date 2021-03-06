# Generated by Django 3.2 on 2021-04-09 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'M'), ('W', 'W')], max_length=50)),
                ('bio', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B2'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=20)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVresume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('position', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=20)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVresume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('school_name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('spec', models.CharField(max_length=20)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CVresume.resume')),
            ],
        ),
    ]
