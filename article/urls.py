from django.contrib import admin
from django.urls import path
from article import views

app_name = "article"

# Bu Uygulamada Çalışacak URL Adresleri
urlpatterns = [
    path('controlPanel/', views.controlPanel , name = "controlPanel"),
    path('addarticle/', views.addarticle , name = "addarticle"),
    path('article/<int:id>', views.detail , name = "detail"),
    path('update/<int:id>', views.updateArticle , name = "updateArticle"),
    path('delete/<int:id>', views.deleteArticle , name = "deleteArticle"),
    path('', views.articles , name = "articles"),
    path('comment/<int:id>', views.comment , name = "comment"),
]