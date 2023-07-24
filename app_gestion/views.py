from django.shortcuts import render
from .models import Article

# Create your views here.
# creation de la fonction
def indexGestionView(request,templates_name="blog/pages/index.html"):
    #context permet a envoyer les codes python vers le html
    # declaration de notre  ou dictionnaire
    context ={}
    bonjour = "bonjour tout le monde ici c'est django"
    #affectation de la clef et valeur dans notre context
    #           clef    valeur
    #on etulise la clef pour aceder au valeur
    # instance articles
    a1 = Article("java","java description")
    a2 = Article("python","python description")
    a3 = Article("django","django description")
    a4 = Article("c++","c++ description")
    a5 = Article("poo","poo description")
    a6 = Article("lunix","lunix description")
    a7 = Article("html","html description")
    a8 = Article("artificiel","artificiel description")
    list_article = [a1, a2, a3, a4, a5,a6,a7,a8]
    for art in list_article:
        print(art.title)
    print(a1.title)
    context['name'] =bonjour
    context['article'] = list_article




    return render(request,templates_name,context)


def aboutView(request,templates_name="blog/pages/about.html"):
    #context permet a envoyer les codes python vers le html
    # declaration de notre  ou dictionnaire
    context ={}
    bonjour = "bonjour tout le monde ici c'est django"
    #affectation de la clef et valeur dans notre context
    #           clef    valeur
    #on etulise la clef pour aceder au valeur
    context['name'] =bonjour

    return render(request,templates_name,context)