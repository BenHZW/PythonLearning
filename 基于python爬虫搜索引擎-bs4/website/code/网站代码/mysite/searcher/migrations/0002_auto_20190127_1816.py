# Generated by Django 2.1.5 on 2019-01-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('artid', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('pubtime', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('detailcontent', models.TextField()),
                ('arttype', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tid', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('stitle', models.CharField(max_length=255)),
                ('wr', models.CharField(max_length=255)),
                ('tit', models.CharField(max_length=255)),
                ('des', models.TextField()),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
                'db_table': 'suject',
            },
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
