from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,widget=forms.PasswordInput,label="Parola")
    confirm = forms.CharField(max_length=20,widget=forms.PasswordInput,label="Parolayı Doğrula")
    
    def clean(self): # Form classından override ettik
        # form submit edilmeden önce aşağıda bu alanların değerlerini alıp işlemleri yapcak
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if (password and confirm) and (password != confirm): # password ve confirm alanı dolu olup birbirleriyle aynı değilse
            # django diyorki hata fırlat
            raise forms.ValidationError("Parolalar Aynı Değil")
        
        values = {"username":username,"password":password} # sözlük olarak atmamız gerek

        return values