# Generated by Django 2.0.5 on 2018-08-22 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_readed_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
        migrations.AddField(
            model_name='readnum',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
        ),
    ]