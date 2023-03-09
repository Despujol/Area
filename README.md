# PROJET AREA  

Le but du projet est de faire une application web et une application mobile afin d'automatiser des tâches en fonction de ce qu'on appelle une area.  
Une area est composé d'un trigger, d'une action et d'une réaction.  
  
Pour mieux comprendre :  
- une action est un événement qui va se produire. Par exemple, si l'utilisateur reçois un mail c'est une action.  
- une réaction est un événement qui est produit en réponse à une action. Par exemple, si l'utilisateur reçois un mail, il va faire une publication facebook.  
- un trigger est l'algorithme qui va nous permettre de savoir sur une action s'est réalisée.  

# Languages  

Ce projet a était développé avec les technologies suivantes:  

- API -> Django.
- Base de donnée -> MySql.
- L'application Web -> React/Javascript.
- Application Mobile -> Flutter.  

# API  

"getactions/" :  
  -> Prends en paramètre l'email d'un utilisateur  
  -> Obtenir toutes les actions qu'un utilisateur peut activer  
  -> Renvoi une liste avec les actions  
  
"getreactions/" :  
  -> Prends en paramètre l'email d'un utilisateur  
  -> Obtenir toutes les réactions qu'un utilisateur peut activer  
  -> Renvoi une liste avec les réactions  
  
"getuseractreact/" :  
  -> Prends en paramètre l'email d'un utilisateur  
  -> Obtenir toutes les area qu'un utilisateur a créé  
  -> Renvoi une liste avec les actions  
  
"login/" :  
  -> Prends en paramètre l'email et le mot de passe d'un utilisateur  
  -> Connecte un utilisateur à l'application  
  -> Renvoi un dictionnaire avec l'email, le prénom et le token django de l'utilisateur  
  
"google/" :  
  -> Prends en paramètre l'email, le mot de passe, le nom, le prénom et le google_access_token d'un utilisateur  
  -> Connecte un utilisateur au service google  
  -> Renvoi un dictionnaire avec l'email, le prénom et le token django de l'utilisateur  
  
"microsoft/" :  
  -> Prends en paramètre l'email, le mot de passe, le nom, le prénom et le microsoft_access_token d'un utilisateur  
  -> Connecte un utilisateur au service microsoft  
  -> Renvoi un dictionnaire avec l'email, le prénom et le token django de l'utilisateur  
  
"github/" :  
  -> Prends en paramètre l'email, le mot de passe, le nom, le prénom et le github_access_token d'un utilisateur  
  -> Connecte un utilisateur au service github  
  -> Renvoi un dictionnaire avec l'email, le prénom et le token django de l'utilisateur  
  
"facebook/" :  
  -> Prends en paramètre l'email, le mot de passe, le nom, le prénom et le facebook_access_token d'un utilisateur  
  -> Connecte un utilisateur au service facebook  
  -> Renvoi un dictionnaire avec l'email, le prénom et le token django de l'utilisateur  
  
"checkservices/" :  
  -> Prends en paramètre l'email d'un utilisateur  
  -> Vérifie à quels services l'utilisateur est connecté  
  -> Renvoi un dictionnaire avec le nom des services liés à un booléen  
  
"about.json/" :  
  -> Prends rien en paramètre    
  -> Fourni une liste des area disponibles  
  -> Renvoi un dictionnaire avec les area disponibles  
  
"createarea/" :  
  -> Prends en paramètre l'email d'un utilisateur, les informations d'une action et les information d'une réaction  
  -> Créer une area  
  -> Renvoi un dictionnaire avec l'email de l'utilisateur, le titre de l'action et de la réaction  
  

# Services  

Les différentes actions/réactions :  
* Facebook.  
`* Si l'utilisateur fait une publication`.  
`* Si l'utilisateur aime une page`.  
* Github.  
`* Si l'utilisateur fait un commit`.  
`* Quand l'utilisateur crée une issue`.  
* Météo.  
`* Alerte quand il pleut`.  
`* Alerte quand il y a de l'orage`.  
* Nasa.  
`* Quand la Nasa publie une photo`.  
* Google.  
`* Quand l'utilisateur rajoute un fichier dans son drive`.  
`* Quand l'utilisateur reçois un gmail`.  
`* Quand l'utilisateur envoie un gmail`.  
`* Quand l'utilisateur enregistre un fichier dans le drive`.  
* Microsoft.  
`* Envoyer un mail avec outlook`.  
`* Quand l'utilisateur crée un event`

# Installation  

Pour installer le projet, suivez les étapes suivantes :

Clonez ce dépôt de code source : git clone git@github.com:EpitechPromo2025/B-DEV-500-BDX-5-2-area-jaykumar.parvedy.git
Lancez l'application avec la commande suivante : docker-compose up  

# Fonctionnement  

- L'utilisateur se connecte à l'application.  
- L'utilisateur se connecte aux services de son choix parmis ceux implémentés.  
- Les données de connexion de l'utilisateur sont enregistrés dans la base de données.  
- L'utilisateur va choisir de lier une action à une réaction parmis celles disponibles dans les services auxquels il s'est connecté.  
- Le trigger va vérifier si l'action est réalisé puis exécuter la réaction associée.  

# Configuration  

Le fichier de configuration se trouve dans config/settings.py. Vous pouvez y modifier les variables suivantes :

DATABASES: pour configurer la base de données.  
        "NAME": <name>,  
        "USER": <user>,  
        "PASSWORD": <password>,
        
        
# Utilisation
Pour utiliser l'application, après avoir lancer docker-compose up --build ouvrez votre navigateur web et rendez-vous à l'adresse suivante :   __http://localhost:8081__  

## __Fait par__ :  
        - Hector Despujol  
        - Enzo Gouband  
        - Lili Bourgeois  
        - Benjamin Bourdeau  
        - Jaykumar Parvedy
message