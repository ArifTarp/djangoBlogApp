from django.shortcuts import render,redirect
from user import forms
from django.contrib.auth.models import User # username ile passwordü kullanarak kullanıcı oluşturmam lazım
from django.contrib.auth import login,authenticate,logout      # kullanıcıyı login ettirmek için
# Create your views here.
from django.contrib import messages # mesajlar için ekledik

def Register(request):
    """if request.method=="POST":
        form = forms.RegisterForm(request.POST) # Doldurulmuş formu aldık
        if form.is_valid():     # forms classındaki clean metodu sadece ve sadece burada çağrılıyor...
            # clean metodu sıkıntı olmassa değer return ediyor
            username = form.cleaned_data.get("username") # clean metodunda return ettiğimiz values sözlük yapısındaki anahtar isimlerini alıyoruz
            password = form.cleaned_data.get("password")
            
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)

            return redirect("index") # djangoBlog uygulamasında urls.py'deki name tagı ile eşleşen urle gitcek
        else:
            # clean methodundan raise ile hata atarsa boş form olarak tekrar göstercez sayfayı
            context = {"form":form}
            return render(request,"register.html",context)

    else:
        form = forms.RegisterForm()
        context = {"form":form} # Sözlük olarak göndermek gerektiği için
        return render(request,"register.html",context)"""
    
    # 2.YÖNTEM
    form = forms.RegisterForm(request.POST or None) # Parametre; GET request ise None, POST request ise request.POST olarak kalacak
    
    if form.is_valid(): # POST request olursa çalışacak burası
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)
        
        messages.success(request,"Başarıyla Kayıt Oldunuz...")

        return redirect("index")
    
    # Hem GET, Hemde POST Olup Clean Metodu Hata Fırlatırsa Bura Çalışacak
    context = {"form":form}
    return render(request,"register.html",context)
     
def Login(request):
    form = forms.LoginForm(request.POST or None)

    context = {"form":form}

    if form.is_valid(): # istek POST ise login formun default clean metodu çağrılacak
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password) # bilgiler doğru değilse none döner
        if user:
            login(request,user)
            messages.success(request,"Giriş Yapıldı...")
            return redirect("index")
        else:
            messages.success(request,"Yanlış Kullanıcı Adı Veya Parola...")
            return render(request,"login.html",context)

    return render(request,"login.html",context)

def Logout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("index")

