from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse # get_object.... elemanı o idli varsa obje döndürür yoksa 404 sayfası döndürür|||reverse fonk. ise redirect işlemlerinde dinamik url kullanmak için gerekli
from article.forms import ArticleForm
from django.contrib import messages
from article.models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse("Ana Sayfa") VEYA
    return render(request,"index.html",context={"number":7})

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def controlPanel(request):
    articles = Article.objects.filter(author = request.user) # oturumu açılan hesabın veri tabanında kayıtlı bütün articlelarını aldık
    content={"articles":articles}
    return render(request,"controlPanel.html",content)

@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None) # form oluşturma
    context = {"form":form}

    if form.is_valid(): # formda sıkıntı çıkmadıysa
        # formumuz model formdan oluştuğu için direk save yapabiliriz
        article = form.save(commit=False)# save işlemini biz gerçekleştircez diye belirttik
        """
        article objesi oluşturur
        bizim bu arada userı vermemiz gerek çünkü article'ları böyle kaydediyor
        article.save() yapar otomatik
        """
        article.author = request.user
        # created date ise otomatik oluşacak
        article.save()
        messages.success(request,"Makale Başarıyla Eklendi...")
        return redirect("index")

    return render(request,"addarticle.html",context) # formu sayfaya gönderdik daha doğrusu formu sayfada kullandık

@login_required(login_url="user:login")
def detail(request,id): # dinamik urldeki idyi aldık
    article = get_object_or_404(Article,id = id) # hangi modelden istiyorsak yazıyoruz

    comments = article.comments.all() # Veritabanındaki Comment tablosundan bu article olan varsa hepsini aldık
    content = {"article":article,"comments":comments}
    return render(request,"detail.html",content)

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id) # güncellenecek makale veri tabanında varsa obje yoksa 404 sayfası döncek
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article) # article obje ise instance ile form doldurulacak, obje değilse sayfa olarak gitcek. Sayfa olarak giderse isvalid kısma girmeyecek

    # post kısmı
    if form.is_valid(): # post yaparken hiç bir sıkıntı yoksa
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi...")
        return redirect("article:controlPanel") # article uygulamasının altında controlPanel name'e gitcek
    
    # veritabanında güncellenmek istenen makale yoksa ve get request ise buraya gircek
    content = {"form":form}
    return render(request,"updateArticle.html",content)
    # Bu fonk. şöyle çalışcak; get request geldiğinde makale var mı yok mu kontrolü yapılcak. Makale varsa objeye yoksa 404 sayfasına sahip olacak article değişkeni
    # makale varsa form doldurulup (get old. için) content olarak html sayfasına gönderilecek
    # makale yoksa 404 sayfası gösterilcek. article değişkeni if kısmına girmeyecek çünkü form boş
    # post request olursa makale varsa objeye yoksa 404 sayfasına sahip olacak article değişkeni
    # makale varsa form doldurulup post request old için if kısmına gircek
    # makale yoksa if kısmına girmeyecek

@login_required(login_url="user:login")
def deleteArticle(request,id):
    kontrol = get_object_or_404(Article,id = id)
    kontrol.delete()
    messages.success(request,"Makale Silindi...")
    return redirect("article:controlPanel") 

def articles(request):
    
    keyword = request.GET.get("keyword")
    # Arama işlemi olmadığında GET request yapılıyor. Ara butonuna basılırsa da GET request olur.
    # Ara butonuna basılırsa GET request olup keyword değer alır
    # Ara butonuna basılmadan GET request olursa keyword boş değer alır

    if keyword: # Ara butonuna basarsa(GET request) keyword değer alır
        articles = Article.objects.filter(title__contains=keyword) # ara butonu ile gönderilen veriyi veri tabanında varsa aldık
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all() # veritabanından bütün makaleleri aldık
    return render(request,"articles.html",{"articles":articles})

def comment(request,id):
    article = get_object_or_404(Article,id=id) # dinamik url sayesinde yorum eklenen article'ın idsini alıp kontrol ediyoruz

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        
        newComment = Comment(article=article,comment_author=comment_author,comment_content=comment_content)
        
        newComment.save() # Veritabanında Comment tablosuna verileri ekliyoruz

    #return redirect("/articles/article/"+str(id))
    return redirect(reverse("article:detail",kwargs={"id":id})) 
    

    