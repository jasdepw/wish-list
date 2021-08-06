# built-in
from datetime import datetime

# django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자 모음'

    email = models.CharField(
        verbose_name='이메일 주소',
        max_length=2000,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name='닉네임', max_length=200, default=None)
    is_active = models.BooleanField(verbose_name='활성화 유무', default=True)
    last_login_at = models.DateTimeField(verbose_name='최종 로그인 시간')
    created_at = models.DateTimeField(verbose_name='생성 시간', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정 시간', auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.id}:{self.email}'
