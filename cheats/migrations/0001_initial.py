# Generated by Django 4.1.4 on 2022-12-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='логотип')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Cheat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('body', models.TextField(verbose_name='текст')),
                ('status', models.CharField(choices=[('draft', 'черновик'), ('published', 'опубликовано'), ('edited', 'редактируется')], max_length=12)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='время редактирования')),
            ],
        ),
    ]
