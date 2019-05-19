from django import forms
from article.models import Article

# burada yaptığımız şu
# var olan modeli(veritabanına modele göre kaydedilir) alıp tekrar kullandık çünkü makale oluşturulurken belli modele göre oluşturuluyor
# kullanırken istediğimiz alanları fields kısmında söyledik
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","image"]