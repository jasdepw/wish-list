# built-in
from datetime import datetime

# django
from django.db import models
from django.utils import timezone

# models
from users.models import User


class Category(models.Model):
    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리 모음'

    name = models.CharField(verbose_name='카테고리 이름', max_length=200)
    is_active = models.BooleanField(verbose_name='활성화 유무', default=True)
    created_at = models.DateTimeField(verbose_name='생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정 시간', auto_now=True)

    def __str__(self):
        return f'{self.id}:{self.name}'


class Item(models.Model):
    class Meta:
        verbose_name = '아이템'
        verbose_name_plural = '아이템 모음'

    category = models.ForeignKey(
        Category,
        default=None,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(verbose_name='아이템 이름', max_length=200)
    url = models.CharField(verbose_name='제품 URL', max_length=2000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지')
    is_active = models.BooleanField(verbose_name='활성화 유무', default=True)
    is_public = models.BooleanField(verbose_name='공개 유무', default=False)
    created_at = models.DateTimeField(verbose_name='생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정 시간', auto_now=True)

    def __str__(self):
        return f'{self.id}:{self.name}'
