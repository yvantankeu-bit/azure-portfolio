Sécuriser la Collaboration B2B avec des Partenaires Externes via Microsoft Entra External ID
============================================================================================

### Introduction

La collaboration avec des partenaires commerciaux et des invités externes est essentielle pour de nombreuses entreprises, mais cela peut souvent poser des défis en matière de gestion des accès et de sécurité des données. Avec Microsoft Entra External ID, vous pouvez faciliter cette collaboration en permettant à votre personnel de partager en toute sécurité des applications et services avec des partenaires externes, même s'ils n'utilisent pas de Microsoft Entra ID ou d'autres services informatiques. Ce guide vous montrera comment mettre en place et gérer efficacement la collaboration B2B dans votre locataire Microsoft Entra, tout en gardant un contrôle total sur vos données d'entreprise.

   ![b2b-collaboration-overview](https://github.com/user-attachments/assets/aa4842c5-6c54-41bd-bf1d-5d2e25588be6)


### Scénario

Imaginez que vous êtes le responsable IT d'une entreprise de conseil en stratégie, StratWise Consulting, qui collabore régulièrement avec diverses entreprises partenaires pour fournir des services à des clients communs. L'un de vos partenaires, Lima tech Solutions, doit accéder à certains outils internes de StratWise pour collaborer sur un projet client important. Cependant, Lima tech n'utilise pas Microsoft Entra ID et dispose de son propre système de gestion des identités.

Votre objectif est de permettre aux employés de Lima tech de collaborer efficacement avec votre équipe tout en maintenant un contrôle strict sur les données de votre entreprise. Grâce à Microsoft Entra External ID, vous pouvez inviter les utilisateurs de Lima tech en tant qu'invités dans votre locataire, leur accorder les autorisations nécessaires pour accéder aux ressources spécifiques, et surveiller leurs activités pour assurer la conformité et la sécurité.

### Prérequis

   Pour mettre en place la collaboration B2B avec des invités externes via Microsoft Entra External ID, voici les prérequis nécessaires :

   1 - **Un locataire Microsoft Entra ID :** Votre organisation doit disposer d'un locataire Microsoft Entra ID (anciennement Azure Active Directory) pour gérer les identités et les accès.

   2 - **Accès administrateur global ou administrateur d'utilisateur invité :** Vous devez avoir les autorisations appropriées pour configurer et gérer les paramètres de collaboration B2B dans votre locataire.

   3 - **Partenaires ou invités externes :** Identifiez les partenaires ou invités externes qui doivent accéder à vos ressources. Ils peuvent être issus d'autres organisations qui n'utilisent pas Microsoft Entra ID.

   4 - **Applications et ressources à partager :** Déterminez quelles applications, services ou ressources de votre entreprise seront partagés avec les invités externes.
   

### Collaboration entre StarWise Consulting et Lima Tech Solutions

  1 -   Créer un utilisateur externe avec Microsoft Entra ID (MEI)
  
 Nous allons utiliser Microsoft Entra ID (abrégé en "MEI") pour créer un utilisateur externe et envoyer le lien d'intégration au développeur .NET de Lima Tech via le portail Azure.

  - Dans le portail Azure, ouvrez MEI, cliquez sur `Add`, sélectionnez `User`, sélectionnez `Invite external user`:

    ![1](https://github.com/user-attachments/assets/b99f3c60-b068-48a7-a887-7518813b8a4f)

  - Une nouvelle fenetre va s'ouvrir. Dans l'onglet "Basics", remplissez les champs pour  corresponde cela à l'utlisateur que vous souhaitez inviter :
    
    ![2](https://github.com/user-attachments/assets/88858c49-b2dd-4980-b74b-cfe94a860cda)
    
  - Dans l'onglet `Properties`, remplissez les champs de manière similaire et laissez l'onglet `Assignments` vide :
    <p float="left">
      <img src="https://github.com/user-attachments/assets/a49ff595-e473-4615-b372-ceacc12c8108" width="45%" />
      <img src="https://github.com/user-attachments/assets/218ef904-206f-4324-99ce-20a2a7947537" width="45%" />
    </p>

  - Dans l'onglet `Review + invite`, vous verrez un récapitulatif des informations remplies dans les onglets précédents. Validez les informations et créez l'utilisateur en lui envoyant le lien pour l'inviter dans notre tenant de StratWise en cliquant sur `invite` :

    ![2-3](https://github.com/user-attachments/assets/a031c2c5-c805-48cb-a36f-652b8577291b)

Microsoft se chargera d'envoyer le lien d'invitation au courriel insere dans les champs pendant le creation de l'utlisateur. 

**2 - Accéder à l'utilisateur créé**

  L'utilisateur a été créé et l'invitation lui a été envoyée. Vous pouvez maintenant retourner dans votre liste d'utilisateurs pour accéder à l'utilisateur que vous avez créé. Suivez ces étapes :
  
  - Accédez à `Manage` puis à `Users`.
  - Vous verrez la liste des utilisateurs. Faites défiler la liste pour trouver l'utilisateur que vous avez créé, ou utilisez le bouton de recherche pour trouver l'utilisateur en utilisant un mot-clé le caractérisant:
  
    ![3-1-2](https://github.com/user-attachments/assets/34956727-5383-4ff8-ad76-c9482df9f2e5)

  Vous verrez un récapitulatif sur l'utilisateur et son statut, avec les informations suivantes :

   - **Account Status** : `Enabled` (Cela confirme que l'utilisateur est créé et actif.)
   - **B2B Invitation** : En attente de validation par le client.
   - **B2B Collaboration** : L'utilisateur est actuellement un utilisateur externe.

     ![3-1-1](https://github.com/user-attachments/assets/ab8a4ea8-fb5b-4be1-a26b-c46d49cde95d)

**4 - Accepter l'invitation par l'utilisateur externe**

  L'utilisateur externe a reçu un courriel d'invitation ressemblant à ceci (exemple en russe, car un courriel éphémère a été utilisé) :
  
  ![image](https://github.com/user-attachments/assets/d172ba1b-600a-4fe3-b0e4-eed86b01d1fe)

  Pour accepter l'invitation :

  - Cliquez sur `Accept Invitation` pour valider l'invitation:

    ![image](https://github.com/user-attachments/assets/dbc53249-8c84-4ce1-bb84-ac6922d35d00)
    
  - Une fenêtre s'ouvrira et Microsoft demandera une authentification. Notez que vous n'aurez pas besoin de mot de passe immédiatement, car le mot de passe n'a pas encore été défini.
Vous pourrez définir un nouveau mot de passe après avoir complété l'invitation.

    ![3-2](https://github.com/user-attachments/assets/5e82f4f3-8c29-426c-bed2-5e54850c4f00)

  Pour procéder :
  - Cliquez sur `Email code to xxx@xxx`, l'adresse à laquelle vous avez reçu le courriel d'invitation.
  - Vous recevrez un code par courriel. Entrez ce code pour vous connecter et finaliser l'ajout au tenant et cliquez sur `Sign in`:

    ![3-3](https://github.com/user-attachments/assets/ed763be2-13c7-4d07-bd2d-a14009c98010)

 - Ici depend de vous
   
   ![3-4](https://github.com/user-attachments/assets/d504f2a6-eb16-4675-bf60-3dfb86cf2724)

- Cliquez sur `Accept`
  
  ![3-5](https://github.com/user-attachments/assets/0f398d61-7967-48a7-99e5-b7bc40bbdfc4)

- Selectionnez votre compte pour la connexion
  
  ![3-6](https://github.com/user-attachments/assets/cd4fd57e-fc8c-40c1-8790-9f4a09e25109)

Une fois l'invitation acceptée, une fenêtre sur [https://myapplications.microsoft.com/](https://myapplications.microsoft.com/) s'affichera, confirmant que votre compte a été validé.

  ![image](https://github.com/user-attachments/assets/b738b98f-5760-45fd-adb8-dd0b2d83176e)

**5 - Accéder à l'utilisateur créé et valider**

Dans le portail Azure, vous pouvez accéder à l'utilisateur de nouveau pour vérifier son statut. Vous devriez voir les informations suivantes :

  - **Account Status** : `Enabled` (Cela confirme que l'utilisateur est créé et actif.)
  - **B2B Invitation** : `Accepted` (Cela indique que l'utilisateur a accepté l'invitation et validé son compte.)
  - **B2B Collaboration** : L'utilisateur est actuellement un utilisateur externe.

    ![3-8](https://github.com/user-attachments/assets/d651c7a0-cac4-4ed7-abd1-0f96a0e9c43d)

### Résultat
--------

Voici un exemple de ce à quoi cela pourrait ressembler dans le portail Azure :

  ![3-7](https://github.com/user-attachments/assets/8ddc4d87-d74e-49a5-899c-18fa1f1a71cf)

Cet utilisateur nouvellement invité pourra également accéder aux ressources de manière granulaire si des droits RBAC (Contrôle d'accès basé sur les rôles) lui sont attribués, ou il pourra obtenir les droits nécessaires au sein du tenant.

     
### Réseaux 
--------------
- [Discord](https://discord.com/users/yvantankeu)
- [LinkedIn](https://www.linkedin.com/in/yvan-tankeu-ab029a129/)
 











    




  
