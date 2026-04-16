Configurez votre application web pour utiliser une connexion Google.
====================================================================

### Introduction

Cette rubrique vous guide à travers la configuration d'Azure App Service ou Azure Functions pour utiliser Google comme fournisseur d'authentification. En intégrant l'authentification via Google, vous permettez aux utilisateurs de se connecter à votre application en utilisant leurs comptes Google, offrant ainsi une expérience fluide et sécurisée.

  ![architecture](https://github.com/user-attachments/assets/4df205eb-dd7c-4651-9b2f-669ae12d3727)


### Scénario

Imaginons que vous êtes le développeur principal d'une plateforme d'éducation en ligne appelée "EduLearn", qui permet aux étudiants de suivre des cours et de compléter des évaluations. Pour simplifier le processus de connexion des utilisateurs, vous décidez d'intégrer l'authentification via Google, car une grande majorité de vos utilisateurs possèdent déjà des comptes Google.

En configurant Azure App Service pour utiliser Google comme fournisseur d'authentification, vous facilitez l'accès à votre plateforme tout en garantissant la sécurité des données de vos utilisateurs. Les étudiants pourront désormais se connecter en quelques clics, en utilisant leurs identifiants Google, ce qui améliore l'expérience utilisateur et encourage une plus grande participation sur la plateforme.

### Prérequis

   Pour mettre en place cette authentification voici les prérequis nécessaires :
   
   1 - **Un compte google :** Disposer d'un compte Google avec une adresse électronique vérifiée.
   
   2 - **Une web app (Azure App Service) :**

### Enregistrez votre application web auprès de Google

  1 - Pour commencer, accédez au tableau de bord Google Cloud Console et enregistrez votre application en suivant ce lien : [Google Cloud Console](https://console.cloud.google.com/apis/dashboard?project=intrepid-stock-288303).
  
   ![image](https://github.com/user-attachments/assets/f9e429ed-cbfc-432a-b881-dbedd50d7ff7)
  
  2 - Créez les identifiants pour votre webapp. Dans la console de Google, cliquez sur `Identifiants`, puis sélectionnez `CRÉER DES IDENTIFIANTS` et choisir `ID client OAuth`

   <p float="left">
    <img src="https://github.com/user-attachments/assets/9f271af5-e01a-4fb8-99f9-6d853789c6b0" width="45%" />
    <img src="https://github.com/user-attachments/assets/14ac1d1a-934c-4d33-99f5-bbb64d7bb667" width="45%" />
   </p>

  3 - Dans la fenêtre suivante, dans "Type d'application", choisissez "Application Web" et donnez un nom à votre application.
  
  4 - Cliquez sur `AJOUTER UN URI` dans "Origines JavaScript autorisées" et "URI de redirection autorisés", puis terminez en cliquant sur le bouton `CRÉER`.

   ![image](https://github.com/user-attachments/assets/1913f3f9-59f5-4c76-b504-4e542aae3cae)

  Les URI que vous devez insérer doivent avoir ce format :

   ![image](https://github.com/user-attachments/assets/5168b551-8c60-43a5-8df9-d296f838b1f6)

  Au final, vous obtiendrez cette fenêtre, car en enregistrant l'application, Google Console générera un ID client et un secret client que vous utiliserez dans Azure pour accéder à l'API de Google pour l'authentification. Il n’est pas nécessaire d’apporter des modifications au code. Utilisez simplement les informations suivantes :

   ![4](https://github.com/user-attachments/assets/aa6a86ec-8dbd-441e-9689-9eb3047aab17)

### Ajouter les informations Google à votre application

1. Connectez-vous au [Portail Azure](https://portal.azure.com) et accédez à votre application.

2. Sélectionnez  `Authentification` dans le menu de gauche, puis cliquez sur `Ajouter un fournisseur d’identité/Add provider` : 

   ![1](https://github.com/user-attachments/assets/4161a8a8-909c-4bd9-9a1d-6b131839ca8d)


3. Sélectionnez **Google** dans le menu déroulant des fournisseurs d’identité. Collez les valeurs de l'ID d'application et du secret d'application que vous avez obtenues précédemment.

     ![2](https://github.com/user-attachments/assets/c0fae2ad-2aed-4b4d-b5ae-d51ab3ff3248)

4. Inserer votre client ID et client secret genere par google console et cliquez sur `Add`

     ![3](https://github.com/user-attachments/assets/4690a962-c816-4271-852d-044295a1ea49)

   Pour avoir le provider google dans la liste
   
   ![5](https://github.com/user-attachments/assets/8f63be81-e69f-4a22-99f8-b7a03c18547b)

### Test d'authentification

On va acceder a la webapp et on aura ceci en images

![12](https://github.com/user-attachments/assets/04c023cf-2da9-42de-b97a-19f393da3b49)
![13](https://github.com/user-attachments/assets/0cdf49b9-1cb8-40af-b6be-6f031162f1c7)
![14](https://github.com/user-attachments/assets/1b671438-02f3-400e-bf22-c3f752c49d0d)
![15](https://github.com/user-attachments/assets/66a80b10-dfc7-406c-a0fc-0fb1727d6319)


### Réseaux 
--------------
- [Discord](https://discord.com/users/yvantankeu)
- [LinkedIn](https://www.linkedin.com/in/yvan-tankeu-ab029a129/)
 

    

     



