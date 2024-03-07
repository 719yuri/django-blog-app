from django.db import models


class Post(models.Model):
  title = models.CharField('タイトル', max_length = 200)
  content = models.TextField('本文')
  create_at = models.DateTimeField('作成日', auto_now_add=True)
  update_at = models.DateTimeField('更新日', auto_now=True)
  is_published = models.BooleanField('公開設定',default=False)

  def __str__(self):
    return self.title

  #'タイトル'とかっているのかな？どう表示されるのかな　→日本語設定にする、という行為らしい。
  #公開設定のカラム何を使うのか不明 →ブーリアンで合ってた
  #https://qiita.com/kotayanagi/items/3cfadae951c407ac044a#booleanfield
  #↑これのコードわかりやすいなんか。もう少し作り込むためにはこうして「記事」「カテゴリー」ごとに作るものなのかな、
  #def...とかも使うんだよねきっと？関数なのはわかるけど何をしてくれるものどういう時に使うものなのか確認しないと。
  #↑使った。記事のタイトルを管理画面で表示させてくれるらしい。ホォーん・・？
