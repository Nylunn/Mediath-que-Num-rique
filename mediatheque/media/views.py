from django.shortcuts import render
from .models import Livre, Dvd, Cd, Jeudeplateau

from .forms import Creationdvd, Updatedvd, Creationlivre, Updatelivre, Creationcd, Updatecd, Ajoutplateau


#déclaration
def listelivres(request):
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    livres = Livre.objects.all()
    creation_plateaux  = Jeudeplateau.objects.all()
    return render(request, 'lists.html',{'livres':livres,'creationPlateau': creation_plateaux,'cd':cds,'dvd':dvds})

#fonction ajout livre
def ajoutlivre(request):
    if request.method == 'POST':
        creationlivre = Creationlivre(request.POST)
        if creationlivre.is_valid():
            livre = Livre()
            livre.name = creationlivre.cleaned_data['name']
            livre.auteur = creationlivre.cleaned_data['auteur']
            livre.disponible = creationlivre.cleaned_data['disponible']
            livre.save()
            livres = Livre.objects.all()
            return render(request, 'lists.html',
                          {'livres': livres})
    else:
        creationlivre = Creationlivre()
        return render(request,
                      'ajoutlivre.html',
                      {'creationLivre': creationlivre}
                      )

#Fonction MAJ Livre
def updatelivre(request, id):
    if request.method == 'POST':
        livre = Livre.objects.get(pk=id)
        update_livre = Updatelivre(request.POST)
        if update_livre.is_valid():
            livre.name = update_livre.cleaned_data['name']
            livre.auteur = update_livre.cleaned_data['auteur']
            livre.save()
        livres = Livre.objects.all()
        return render(request, 'lists.html',
                      {'livres': livres})
    else:
        updateLivre = Updatelivre()
        return render(request,
                      'updatelivre.html',
                      {'updatelivre': updateLivre}
                      )

#Fonction Delete livre
def deletelivre(request, id):
    livre = Livre.objects.get(pk=id)
    livre.delete()
    livres = Livre.objects.all()
    return render(request, 'lists.html',
                  {'livres': livres})


#DVD

#Ajouts de la fonction création Dvd

def ajoutDvd(request):
    if request.method == 'POST':
        creationdvd = Creationdvd(request.POST)
        if creationdvd.is_valid():
            dvd = Dvd()
            dvd.name = creationdvd.cleaned_data['name']
            dvd.realisateur = creationdvd.cleaned_data['realisateur']
            dvd.disponible = creationdvd.cleaned_data['disponible']
            dvd.save()
            dvdst = Dvd.objects.all()
            return render(request, 'lists.html',
                          {'dvd': dvdst})
    else:
        creationdvd = Creationdvd()
        return render(request,
                      'dvd/ajoutdvd.html',
                      {'creationDvd': creationdvd}
                      )


#Fonction MAJ Dvd
def updatedvd(request, id):
    if request.method == 'POST':
        dvd = Dvd.objects.get(pk=id)
        update_dvd = Updatedvd(request.POST)
        if update_dvd.is_valid():
            dvd.name = update_dvd.cleaned_data['name']
            dvd.realisateur = update_dvd.cleaned_data['realisateur']
            dvd.save()
        dvds = Dvd.objects.all()
        return render(request, 'lists.html',
                      {'dvd': dvds})
    else:
        updateDvd = Updatedvd()
        return render(request,
                      'dvd/updatedvd.html',
                      {'updateDvd': updateDvd}
                      )

# fonction delete Dvd
def deletedvd(request, id):
    dvd = Dvd.objects.get(pk=id)
    dvd.delete()
    dvds = Dvd.objects.all()
    return render(request, 'lists.html',
                      {'dvd': dvds})


#CD

#Ajouts de la fonction création CD

def ajoutCd(request):
    if request.method == 'POST':
        creationcd = Creationcd(request.POST)
        if creationcd.is_valid():
            cd = Cd()
            cd.name = creationcd.cleaned_data['name']
            cd.artiste = creationcd.cleaned_data['artiste']
            cd.disponible = creationcd.cleaned_data['disponible']
            cd.save()
            cds = Cd.objects.all()
            return render(request, 'lists.html',
                          {'cd': cds})
    else:
        creationcd = Creationcd()
        return render(request,
                      'cd/ajoutcd.html',
                      {'creationCd': creationcd}
                      )


#Fonction MAJ Dvd
def updatecd(request, id):
    if request.method == 'POST':
        cd = Cd.objects.get(pk=id)
        update_cd = Updatecd(request.POST)
        if update_cd.is_valid():
            cd.name = update_cd.cleaned_data['name']
            cd.artiste = update_cd.cleaned_data['artiste']
            cd.save()
        cds = Cd.objects.all()
        return render(request, 'lists.html',
                      {'cd': cds})
    else:
        updateCd = Updatecd()
        return render(request,
                      'cd/updatedvd.html',
                      {'updateCd': updateCd}
                      )

# fonction delete Dvd
def deletecd(request, id):
    cd = Cd.objects.get(pk=id)
    cd.delete()
    cds = Cd.objects.all()
    return render(request, 'lists.html',
                      {'cd': cds})



#PLATEAUX

def ajoutPlateau(request):
    if request.method == 'POST':
        # Utilisation correcte du formulaire Ajoutplateau
        formulaire_plateau = Ajoutplateau(request.POST)
        if formulaire_plateau.is_valid():
            # Création d'une instance de Jeudeplateau
            nouveau_plateau = Jeudeplateau(
                name=formulaire_plateau.cleaned_data['name'],
                createur=formulaire_plateau.cleaned_data['createur']
            )
            nouveau_plateau.save()
            # Récupération de tous les plateaux pour les afficher
            creation_plateaux = Jeudeplateau.objects.all()
            # Afficher les plateaux dans le même template
            return render(request, 'lists.html', {'creationPlateau': creation_plateaux})
    else:
        formulaire_plateau = Ajoutplateau()

    # On affiche le formulaire sur la page d'ajout
    return render(request, 'plateau/ajoutplateau.html', {'creationPlateau': formulaire_plateau})




#Fonction MAJ Livre
def updatelivre(request, id):
    if request.method == 'POST':
        livre = Livre.objects.get(pk=id)
        update_livre = Updatelivre(request.POST)
        if update_livre.is_valid():
            livre.name = update_livre.cleaned_data['name']
            livre.auteur = update_livre.cleaned_data['auteur']
            livre.save()
        livres = Livre.objects.all()
        return render(request, 'lists.html',
                      {'livres': livres})
    else:
        updateLivre = Updatelivre()
        return render(request,
                      'updatelivre.html',
                      {'updatelivre': updateLivre}
                      )

#Fonction Delete livre
def deletelivre(request, id):
    livre = Livre.objects.get(pk=id)
    livre.delete()
    livres = Livre.objects.all()
    return render(request, 'lists.html',
                  {'livres': livres})


