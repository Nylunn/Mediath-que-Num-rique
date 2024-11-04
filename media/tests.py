from django.test import TestCase
from mediatheque.media.models import *

# Pour utiliser les test faites ./manage.py test "name"

#Plateau
class PlateauTestCase(TestCase):
    def setUp(self):
        Jeudeplateau.objects.create(name="Testunitaire", createur="Django"),

    def test_jeudeplateau_creation(self):
        echo="jeu de plateau créer"
        testunitaire = Jeudeplateau.objectfs.name(name="testunitaire",createur="Django")


#Livre

class LivreTestCase(TestCase):
    def setUp(self):
        Livre.objects.create(auteur="TestAuthor"),
    def test_livre_creation(self):
        echo="Livre créer"
        testunitaire = Livre.objectfs.name(name="TestAuthor")
#Media

class MediaTestCase(TestCase):
    def setUp(self):
        Media.objects.create(name="TestName", createur = "Django", date_emprunt=29/10/2025,Emprunteur="DjangoEmprunt"),

    def test_media_creation(self):
        echo="media créer"
        testunitaire = Media.objectfs.name(name="TestName", createur = "Django", date_emprunt=29/10/2025,Emprunteur="DjangoEmprunt")
#Media
#CD

class CDTestCase(TestCase):
    def setUp(self):
        Cd.objects.create(artiste="TestArtiste"),


        def test_cd_creation(self):
            echo = "CD créer"
            testunitaire = Cd.objectfs.name(artiste="TestArtiste")
    # Media
#Dvd

class DvdTestCase(TestCase):
    def setUp(self):
        Dvd.objects.create(realisateur="TestRealisator"),

        def test_livre_creation(self):
            echo = "Dvd créer"
            testunitaire = Dvd.objectfs.name(realisateur="TestRealisator")
    # Media

#Emprunteur

class EmprunteurTestCase(TestCase):
    def setUp(self):
        Emprunteur.objects.create(name="TestEmprunteur", bloque=True),

        def test_Emprunteur_creation(self):
            echo = "Emprunteur créer"
            testunitaire = Emprunteur.objectfs.name(name="TestEmprunteur",bloque=True)
    # Media