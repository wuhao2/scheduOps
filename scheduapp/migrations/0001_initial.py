# Generated by Django 2.0.1 on 2019-09-23 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_results', '0004_auto_20190516_0412'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResultModels',
            fields=[
                ('taskresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_celery_results.TaskResult')),
                ('nick_name', models.CharField(max_length=20, verbose_name='别名')),
            ],
            bases=('django_celery_results.taskresult',),
        ),
    ]