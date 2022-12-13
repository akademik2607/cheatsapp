# Generated by Django 4.1.4 on 2022-12-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheats', '0002_alter_cheat_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheat',
            name='status',
            field=models.CharField(choices=[('draft', 'черновик'), ('published', 'опубликовано'), ('edited', 'редактируется')], max_length=12, verbose_name='статус'),
        ),
    ]
