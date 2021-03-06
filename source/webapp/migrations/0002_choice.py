# Generated by Django 2.2 on 2021-04-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls_choice', to='webapp.Poll', verbose_name='Опрос')),
            ],
        ),
    ]
