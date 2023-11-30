from django.db import models

# class Category(models.Model):
#     title=models.CharField(
#         verbose_name='カテゴリ',
#         max_length=20
#     )

class CommentPost(models.Model):
    comment=models.TextField(
            verbose_name='コメント',
            max_length= 1000,
        )
    def __str__(self):
        return self.comment