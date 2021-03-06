# Generated by Django 3.0.3 on 2020-05-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
                ('date_of_pub', models.DateField()),
                ('department', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='storage/')),
            ],
        ),
    ]
