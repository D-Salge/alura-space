from django.db import models
from datetime import datetime

# Fotografia Model
class Fotografia(models.Model):
  
  opcoes_tag = [
    ("Nebulosa", "Nebulosa"),
    ("Estrela", "Estrela"),
    ("Galáxia", "Galáxia"),
    ("Planeta", "Planeta"),
    ("Satélite", "Satélite"),
  ]
  
  nome = models.CharField(max_length=100, null=False, blank=False)
  legenda = models.CharField(max_length=150, null=False, blank=False)
  descricao = models.TextField(null=False, blank=False)
  tag = models.CharField(max_length=100, choices=opcoes_tag, default="")
  foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
  publicada = models.BooleanField(default=False)
  data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

  def __str__(self):
    return self.nome