# Generated by Django 3.2.6 on 2021-08-06 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='카테고리 이름')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 유무')),
                ('created_at', models.DateTimeField(verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(verbose_name='수정 시간')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='아이템 이름')),
                ('url', models.CharField(max_length=2000, verbose_name='제품 URL')),
                ('image', models.ImageField(upload_to='', verbose_name='이미지')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 유무')),
                ('is_public', models.BooleanField(default=False, verbose_name='공개 유무')),
                ('created_at', models.DateTimeField(verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(verbose_name='수정 시간')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='items.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
