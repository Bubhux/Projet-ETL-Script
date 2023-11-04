![Static Badge](static/badges/build-with-python.svg)

<div id="top"></div>

## Menu 
1. **[Info general](#informations-générales)**   
2. **[Liste pré-requis](#liste)**   
3. **[Création environnement virutel](#creation-environnement)**   
4. **[Activation environnement virutel](#activation-environnement)**   
5. **[installation librairies](#installation)**   
6. **[Exécution de l'application](#execution)**   
7. **[Développement](#developpement)**   
8. **[Auteurs et contact](#auteur)**   


<div id="informations-générales"></div>

## Projet script ETL 
Script permettant d'extraire les données d'un site web et d'ecrire les données sur plusieurs fichiers csv.   
Les tests d'extraction sont faits sur le site: http://books.toscrape.com/   

-------------------------------------------------------------------------------------------------------------------

<div id="liste"></div>

### Liste pré-requis 
- Script construit avec les logiciels suivants:   
- Python v3.7.2   
- Sublime Text 3.2.2 build 3211   
- Cmder v1.3.19.1181 : remplace le cmd par défaut de - Windows (optionnel)   
- Windows 7 professionnel SP1   

-------------------------------------------------------------------------------------------------------------------

<div id="creation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Création environnement virtuel
- Installer une version de Python compatible pour votre ordinateur.   
- Une fois installer ouvrer le cmd (terminal) placer vous dans le dossier princiaple (dossier racine).   

**Taper dans votre terminal la commande :**

```bash
$ python -m venv env
```
Un répertoire appelé ``env`` doit être créé   

-------------------------------------------------------------------------------------------------------------------

<div id="activation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Activation environnement virtuel
- Placez-vous avec le terminal dans le dossier princiaple (dossier racine).   
- Pour activer l'environnement virtuel créé.   

**Taper dans votre terminal la commande :**

```bash
$ env\Scripts\activate.bat
```
- Ce qui ajoutera à chaque ligne de commande de votre terminal ``(env)``   
- Pour désactiver l'environnement virtuel.   

**Taper dans votre terminal la commande :**

```bash
$ deactivate   
```
-------------------------------------------------------------------------------------------------------------------

<div id="installation"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Installation librairies
- Placez-vous dans le dossier ou se trouve le fichier requirements.txt avec le terminal l'environnement virtuel doit être activé.   
- Pour faire fonctionner le script, il vous faudra installer les librairies requises à l'aide du fichiers ``requirements.txt`` mis à disposition.   

**Taper dans votre terminal la commande :**

```bash
$ pip install -r requirements.txt
```
-------------------------------------------------------------------------------------------------------------------

<div id="execution"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Exécution de l'application
Pour exécuter le script placez vous dans le dossier avec le terminal ou se trouve le script avec l'environnement virtuel activé.   

**Taper dans votre terminal la commande :**

```bash
$ python projet_script_ETL_V1.2.0.py
```

- Le programme se lance et va lister les données à extraire et ensuite les ecriras sur des fichiers csv.   

    Vous pouvez mettre pause en appuyant sur ``ctrl+s`` et contrôler les informations en cours d'extraction qui défile dans votre terminal.   

- Le programme est paramétré pour extraire les 50 catégories du site, vous pouvez changer se paramètre et saisir seulement les catégories souhaitées.   
  
*Note : Il y a 50 catégories la liste est régler sur ``[3:53]``*   

Vous pouvez la modifier en changeant les paramétres sur les 2 fonctions suivantes :   

```python
def fonction_main_extract_all_categories(url):
Ligne 28   
Ligne 43 
``` 


```python
def write_file_import_csv(data):
Ligne 392
```   

**Exemple :** si vous souhaitez seulement la première catégorie mettre ``[3:4]``   
**Exemple :** si vous souhaitez seulement la deuxième et la troisième catégorie mettre ``[4:6]``

-------------------------------------------------------------------------------------------------------------------

<div id="developpement"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Développement
Actuellement en cours de développement :   
Une fonction pour télécharger les images.   
Une fonction permettant de voir le temps d'exécution du programme.   

-------------------------------------------------------------------------------------------------------------------

<div id="auteur"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Auteurs et contact 
Pour toute information suplémentaire, vous pouvez me contacter.   
**Bubhux:** bubhuxpaindepice@gmail.com   
