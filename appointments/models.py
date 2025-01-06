from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    clase = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.clase} - {self.dia} {self.hora}"

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.cliente} para {self.horario}"
