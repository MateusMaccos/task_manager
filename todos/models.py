from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    STATUS_CHOICES = [
        ("Pendente", "Pendente"),
        ("Concluido", "Concluido"),
    ]
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)
    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=STATUS_CHOICES,
        default="Pendente",
    )
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.status = "Concluido"
            self.save()
