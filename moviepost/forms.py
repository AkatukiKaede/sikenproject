from django.forms import ModelForm
from .models import MoviePost

class MoviePostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = MoviePost
        fields = ['user','category','title','image1','movie','gaiyou']