![Static Badge](static/badges/Build-with-Python-3.7.2.svg)

<div id="top"></div>

## Menu   

1. **[Info general](#informations-générales)**   
2. **[Liste pré-requis](#liste)**   
3. **[Création environnement virutel](#creation-environnement)**   
4. **[Activation environnement virutel](#activation-environnement)**   
5. **[installation librairies](#installation)**   
6. **[Exécution de l'application](#execution)**   
7. **[Développement](#developpement)**   
8. **[Auteur et contact](#auteur)**   


<div id="informations-générales"></div>

### Projet script ETL   

Script permettant d'extraire les données d'un site web et d'ecrire les données sur plusieurs fichiers csv.   
Les tests d'extraction sont faits sur le site: http://books.toscrape.com/   

>_**Note :** Testé sous Windows 7 - Python 3.7.2_   

-------------------------------------------------------------------------------------------------------------------

<div id="liste"></div>

### Liste pré-requis   

Programme élaborés avec les technologies suivantes :   

- **Python** ``v3.7.2`` choisissez la version adaptée à votre ordinateur et système ➔ [Téléchargement Python](https://www.python.org/downloads/)   
- **VSCode** ``v1.85.2`` ➔ [Documentation et téléchargement de VSCode](https://code.visualstudio.com/) 
- **Cmder** ``v1.3.19.1181`` : remplace le cmd par défaut de Windows (optionnel)   
- **Windows 7** professionnel SP1   
  &nbsp;   

- Les scripts **Python** s'exécutent depuis un terminal.   
- Pour ouvrir un terminal sur **Windows**, pressez la touche ```windows + r``` et entrez ```cmd```.   
- Sur **Mac**, pressez la touche ```command + espace``` et entrez ```terminal```.   
- Sur **Linux**, vous pouvez ouviri un terminal en pressant les touches ```Ctrl + Alt + T```.   

>_**Note :** Interpréteur **Python**, version 3.6 ou supérieure     

-------------------------------------------------------------------------------------------------------------------

<div id="creation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Création environnement virtuel   

- Installer une version de **Python** compatible pour votre ordinateur.   
- Une fois installer ouvrer le **cmd (terminal)** placer vous dans le dossier princiaple **(dossier racine)**.   

Taper dans votre terminal la commande :   

```bash
$ python -m venv env
```   

>_**Note :** Un répertoire appelé **env** doit être créé._   

-------------------------------------------------------------------------------------------------------------------

<div id="activation-environnement"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Activation environnement virtuel   

- Placez-vous avec le terminal dans le dossier princiaple **(dossier racine)**.   
- Pour activer l'environnement virtuel créé.   

>_**Note :** Pour activer l'environnement virtuel créé, il vous suffit de taper dans votre terminal :_   

Taper dans votre terminal la commande :

```bash
$ env\Scripts\activate.bat
```
- Ce qui ajoutera à chaque ligne de commande de votre terminal ``(env)``   
- Pour désactiver l'environnement virtuel.   

>_**Note :** Pour désactiver l'environnement virtuel, il suffit de taper dans votre terminal :_   

Taper dans votre terminal la commande :

```bash
$ deactivate   
```

-------------------------------------------------------------------------------------------------------------------

<div id="installation"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Installation librairies   

- Placez-vous dans le dossier ou se trouve le fichier ``requirements.txt`` avec le terminal l'environnement virtuel doit être activé.   
- Pour faire fonctionner le script, il vous faudra installer les librairies requises à l'aide du fichiers ``requirements.txt`` mis à disposition.   

Taper dans votre terminal la commande :   

```bash
$ pip install -r requirements.txt
```
-------------------------------------------------------------------------------------------------------------------

<div id="execution"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Exécution de l'application   

Pour exécuter le script placez vous dans le dossier avec le terminal ou se trouve le script avec l'environnement virtuel activé.   

Taper dans votre terminal la commande :   

```bash
$ python projet_script_ETL_V1.2.0.py
```

- Le programme se lance et va lister les données à extraire et ensuite les écriras sur des fichiers ``csv``.   

>_**Note :** Vous pouvez mettre pause en appuyant sur ``ctrl + s`` et contrôler les informations en cours d'extraction qui défile dans votre terminal._   

- Le programme est paramétré pour extraire les 50 catégories du site, vous pouvez changer se paramètre et saisir seulement les catégories souhaitées.   
  
>_**Note :** Il y a 50 catégories la liste est régler sur ``[3:53]``_   


##### Vous pouvez la modifier en changeant les paramétres sur les 2 fonctions suivantes :   

- ``projet_script_ETL_V1.2.0.py`` ➔ ([projet_script_ETL_V1.2.0.py](projet_script_ETL_V1.2.0.py))   


```python
def fonction_main_extract_all_categories(url):
Ligne 29   
Ligne 44 
```   

```python
def write_file_import_csv(data):
Ligne 393
```   

**Exemple :** si vous souhaitez seulement la première catégorie mettre ``[3:4]``   
**Exemple :** si vous souhaitez seulement la deuxième et la troisième catégorie mettre ``[4:6]``   

-------------------------------------------------------------------------------------------------------------------

<div id="developpement"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Développement   

**Actuellement en cours de développement :**   

- Une fonction pour télécharger les images.   
- Une fonction permettant de voir le temps d'exécution du programme.   

-------------------------------------------------------------------------------------------------------------------

<div id="auteur"></div>
<a href="#top" style="float: right;">Retour en haut ↑</a>

### Auteur et contact   

Pour toute information suplémentaire, vous pouvez me contacter.   
**Bubhux :** bubhuxpaindepice@gmail.com   
