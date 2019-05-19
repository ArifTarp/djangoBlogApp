from django.contrib import admin
from article.models import Article,Comment # .models --> şuanki dosyanın models bölümü demek
# Register your models here.

#admin.site.register(Article) özelleştirilmemiş 
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): # Özelleştirmek için class yazdık
    list_display = ["title","author","createdDate"]
    list_display_links = ["title","author","createdDate"]
    list_filter = ["createdDate"]
    search_fields = ["title"]
    class Meta: # Article Modeline Göre Özelleştirme İşlemi Yapmak İçin
        model = Article

admin.site.register(Comment)
