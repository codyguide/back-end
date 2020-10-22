# Generated by Django 3.1 on 2020-10-18 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('img_path', models.FileField(max_length=200, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='member.person')),
            ],
            options={
                'db_table': 'gallery',
                'ordering': ['-created'],
            },
        ),
    ]