from django.db import models

# Create your models here.

class User(models.Model):
	nev = models.CharField(max_length=100)
	jelszo = models.CharField(max_length=100)
	def __str__(self):
		return self.nev + "(" + str(self.id) +")"

class Tetel(models.Model):
	nev = models.CharField(max_length=100)
	megj = models.CharField(max_length=255)
	def __str__(self):
		return self.nev # + "(" + self.megj +")"

class Kapcsolat(models.Model):
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
	tetelid = models.ForeignKey(Tetel, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.userid.nev} ({self.userid.id}) --> {self.tetelid.nev}"

		