NetFloux
Projet realisé par Kahina RAHMANI et Marina BOTNARI

Pour le projet de ce module "Architecture et micro services", nous avons choisi de réaliser un site web "NETFLOUX".
Pour ce faire, nous avons installé Docker sur notre machine virtuelle, et nous avons choisi de le concevoir avec Python en utilisant ses bibliothèques
spécialisées dans le Web et les API (Flask).

Dès qu'on lance le site avec "localhost:5000", on se trouve sur la page d'accueil, puis on clique sur sign up, et on se connecte avec le username et mot de
passe (test@yahoo.com et mdp : test).
Si les identifiants sont bons (existent dans la base de données myBase) on est redirigé vers la page catalog sinon un message s'affiche nous indiquant que 
nos identifiants ne sont pas bons.
Sur la page catalog, on peut revenir sur la page d'accueil en cliquant sur "home", et on peut accéder à la liste des films favoris en cliquant
sur "my list". Ce dernier nous redirige vers la page myList qui affiche la liste des films favoris de l'utilisateur actuel.


L'architecture de notre projet se base sur plusieurs microservices qui se communiquent :
	
	1) Front : s'occupe du front de notre site
	2) Authentification : pour le login d'un utilisateur, ce service a une base de données (celle des Users)
	3) Catalog : c'est le microservice qui récupère et renvoie les films existants dans la base de donnés (celle des Films)
	4) Mylist : c'est le microservice qui gère la list des films favoris des utilisateurs
		Les deux microservices "catalog et mylist" se partagent la base de données "baseCatalog"
	5) db : microservice pour la base de données des utilisateurs (appelée myBase)
	6) db-Catalog : c'est le microservice pour la base de données baseCatalog
	

Tous ces services sont gérés par le fichier docker-compose.yml(les ports à exposer pour chaque service, link, ...)
	
		
Concernant les bases de données, comme mentionné en haut, nous avons 2 :
	myBase : contient une seule table "users" qui liste les utilisateurs (id, username, mdp )
	baseCatalog :contient 3 tables : 
		movies : les films (id, title, duration, image, description, idType)
		typeMovie : liste les catégories des films (action, tv show ...)
		mylist : contient la liste des films favoris pour chaque utilisateur (id, idUser,username, idMovie)
		
		
Organisation des dossiers : 

authentication:
   ---Dockerfile
   ---requirements.txt
   ---user.py
catalog:
   ---catalog.py
   ---Dockerfile
   ---requirements.txt
mylist:
   ---Dockerfile
   ---mylist.py
   ---requirements.txt
db:
   ---init.sql
db-Catalog:
   ---init.sql
front:
   ---static
      ---images
      ---styles
         ---catalog-style.css
         ---index-style.css
         ---login-style.css
         ---myList-style.css
   ---templates
      ---catalog.html
      ---index.html
      ---login.html
      ---myList.html
   ---Dockerfile
   ---front.py
   ---requirements.txt
docker-compose.yml
README


Ps : On aurait aimé ajouter un bouton "Add" sur chaque film du catalogue afin qu'un utilisateur puisse ajouter des films à sa liste
     On aurait également voulu ajouté le logout et le register qui ne sont pas fonctionnels actuellement
     Malheureusement on n'avait pas eu assez de temps pour affiner notre projet tel qu'on l'a imaginé au début, (la période entreprise est aussi chargé)


	