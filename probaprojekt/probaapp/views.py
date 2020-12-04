from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	kontextus = {
	"w": 'Ez itt a változó értéke',
	"lista": [1,3,5,7,9],
	}
	return render(request, "probahtml.html", kontextus)
