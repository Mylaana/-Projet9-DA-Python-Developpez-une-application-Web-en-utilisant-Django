# Projet9-DA-Python-Developpez-une-application-Web-en-utilisant-Django

Ce README explique comment installer et configurer l'application Django LIT Review.

## Table des matières
**Prérequis**  
**Installation**  
**Exécution**  
**Utilisation**  
**Tests**  

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

Python : Vous pouvez le télécharger sur python.org.  
pip : Le gestionnaire de paquets Python.

## Installation
**Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :**
```
git clone https://github.com/Mylaana/Projet9-DA-Python-Developpez-une-application-Web-en-utilisant-Django.git
```
**Accédez au répertoire du projet :**
```
cd repertoire-du-projet
```

**Créez un environnement virtuel pour isoler les dépendances du projet :**
```
python -m venv venv
```

**Activez l'environnement virtuel :**

Sur macOS et Linux :
```
source venv/bin/activate
```
  
Sur Windows (PowerShell) :
```
.\venv\Scripts\Activate.ps1
```
  
**Installez les dépendances du projet :**
```
pip install -r requirements.txt
```

## Exécution
Appliquez les migrations de base de données :
```
python manage.py migrate
```
Créez un superutilisateur Django (administrateur) :
```
python manage.py createsuperuser
```
Lancez le serveur de développement Django :
```
python manage.py runserver
```

## Utilisation
L'application est maintenant accessible à l'adresse http://localhost:8000/.  
Vous pouvez également vous connecter à l'interface d'administration http://localhost:8000/admin avec le superutilisateur que vous avez créé et explorer les fonctionnalités de l'application.

## Tests
A des fins de test, deux users sont créés dans la base :
- un superuser ID: admin-oc Password:password-oc
- un user ID: user1 Password:secret123A$
