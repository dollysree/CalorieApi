# Generated by Django 2.0.3 on 2018-03-30 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('calories', models.IntegerField()),
            ],
            options={
                'ordering': ('item',),
            },
        ),
        migrations.CreateModel(
            name='UserCalorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('calories', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('owner', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estimate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
