from django import forms

from apps.galeria.models import Fotografia

class LoginForms(forms.Form):
  nome_login = forms.CharField(
    label="Nome de Login",
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex.: João Silva"
      }
    )
  )

  senha = forms.CharField(
    label="Senha",
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    )
  )
  
class CadastroForms(forms.Form):
  nome_cadastro = forms.CharField(
    label="Nome de Cadastro",
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex.: João Silva"
      }
    )
  )
  email = forms.EmailField(
    label="Email",
    required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex.: joaosilva@xpto.com"
      }
    )
  )
  senha1 = forms.CharField(
    label="Senha",
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    )
  )
  senha2 = forms.CharField(
    label="Confirmação de Senha",
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha mais uma vez"
      }
    )
  )
  
  def clean_nome_cadastro(self):
    nome = self.cleaned_data.get("nome_cadastro")
    if nome:
      nome = nome.strip()
      if " " in nome:
        raise forms.ValidationError("Não é possível cadastrar usuários com espaços")
      else:
        return nome
      
  def clean_senha2(self):
    senha1 = self.cleaned_data.get("senha1")
    senha2 = self.cleaned_data.get("senha2")
    if senha1 and senha2:
      if senha1 != senha2:
        raise forms.ValidationError("Senhas não correspondem")
      return senha2
    
class FotografiaForms(forms.ModelForm):
  class Meta:
    model = Fotografia
    exclude = ['publicada',]
    labels = {
      'descricao': 'Descrição',
      'data_fotografia': 'Data',
      'usuario': 'Usuário',
    }
    
    widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }