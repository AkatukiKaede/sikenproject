from django.contrib import admin
# CustomUserをインポート
from .models import  CommentPost

class CommentPostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'comment')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'comment')

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(CommentPost,CommentPostAdmin)
