from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
# veritabanına eklerken hangi alanlarla eklenecek onu belirliyoruz modellerde bi nevi tablo oluşturuyoruz
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar") # ForeignKey ile de hazır tabloya(modele) atıfta bulunarak Djangonun hazır user tablosunu kullandık. Ve her yazar kullanıcı olarak eklenmiş olacak.
    # Yazarı Djangonun içindeki hazır user tablosundan oluşturmuş olduk
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    image = models.FileField(blank = True,null = True,verbose_name="Makaleye Resim Ekleyin") #burayı sonrada eklediğimiz için veri tabanını tekrardan biçimlendirmemiz gerek
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-createdDate']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments") # veritabanından eriştiğimizde article.comments dediğimizde comment tablosuna erişebiliyoruz
    comment_author = models.CharField(max_length=20,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_createdDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author
    
    class Meta:
        ordering = ['-comment_createdDate']
