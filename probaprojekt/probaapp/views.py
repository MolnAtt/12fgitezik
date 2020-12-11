from django.shortcuts import render

from .models import User, Tetel, Kapcsolat
# Create your views here.

def home_view(request, *args, **kwargs):

	"""

	Ezt hoztuk össze a shellben, ezt csináljuk meg most nagyban:

		list(Tetel.objects.all()) 				# ez itt a tételek listája
		szurtkapcsolatok = Kapcsolat.objects.filter(tetelid = tetel)
		valasztotanulo = szurtkapcsolatok[0].userid

	"""

	if request.method=="POST":
		szurtlista = list(User.objects.filter(nev = request.POST['felhasznalo'], jelszo = request.POST['jelszo']))
		if  len(szurtlista)>0 : # sikeres a bejelentkezés
			Kapcsolat.objects.create(userid = szurtlista[0], tetelid = Tetel.objects.get(id=request.POST['valasztotttetel']))
		else:
			print("rossz felhasználónév-jelszó páros!")



	tablazat = []
	tanulonev = ""

	for tetel in list(Tetel.objects.all()):
		szurtkapcsolatok = Kapcsolat.objects.filter(tetelid = tetel)
		if len(szurtkapcsolatok) == 0:
			tanulonev = "nincs"
		else:
			tanulonev = szurtkapcsolatok[0].userid.nev
		tablazat.append([tanulonev, tetel.nev, tetel.id])

	# a kontextus legyen két oszlopos mátrix! a második elem a tétel, az első elem, hogy ki választotta a tételt.

	kontextus = {"tablazat": tablazat}

	return render(request, "probahtml.html", kontextus)
