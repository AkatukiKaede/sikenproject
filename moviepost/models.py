from django.db import models

from account.models import CustomUser


class Category(models.Model):
    title=models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )
    
    def __str__(self):
        return self.title

class MoviePost(models.Model):
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    
    title=models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    
    gaiyou=models.TextField(
        verbose_name='概要欄',
        max_length=100000
    )
    
    image1=models.ImageField(
        verbose_name='サムネイル',
        upload_to='photos'
    )
    
    movie=models.FileField(
        verbose_name='動画',
        upload_to='photos'       
    )
    
    posted_at=models.DateField(
        verbose_name='投稿日時',
        auto_now_add=True,

    )
    def __str__(self):
        return self.title    