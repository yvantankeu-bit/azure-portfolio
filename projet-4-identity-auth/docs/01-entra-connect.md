Migration et Synchronisation des Identités On-Premises avec Azure AD Connect
============================================================================

Je possède des utilisateurs et des groupes d'utilisateurs dans mon Active Directory Domain Services (AD DS) sous Windows Server 2022, et je souhaite les migrer vers Azure. Vous pouvez voir ces utilisateurs et groupes dans l'image ci-dessous.

![16](https://github.com/user-attachments/assets/8c1ebde5-9787-49ba-b2ce-c41ba3b60b73)

Pour effectuer cette migration, les prérequis suivants sont nécessaires :

- Utilisateur dans Entra ID :

    - Créez ou identifiez un utilisateur dans Entra ID (anciennement Azure AD) sur Azure.
    - Assurez-vous que cet utilisateur dispose du rôle de Global Administrator.
    - Activer TLS 1.2 sur votre server Onpremise si c'est pas fait

- Téléchargement de l'application :

    - Téléchargez et installez l'application Azure AD Connect sur votre serveur Windows depuis le lien suivant : [Azure AD Connect Download.](https://www.microsoft.com/en-ie/download/details.aspx?id=47594&msockid=293044c43edd6b7d3589572a3fe66a0a)

- Exécution de l'application :

    - Après avoir téléchargé Azure AD Connect, exécutez l'application sur votre serveur Windows.
    - Vous verrez apparaître un guide de configuration qui vous guidera à travers les différentes étapes pour configurer la synchronisation entre votre AD DS et Entra ID.

      ![1](https://github.com/user-attachments/assets/271e419c-ff39-4d20-9304-ab58048ace7b)

  On va utiliser la configuration rapide pour ce tuto, alors cliquez sur configuration rapide en vers qui nous emmenera a la  prochaine étape

- Connexion à Azure
  
    Entrez le nom d'utilisateur et le mot de passe de l'utilisateur de votre Microsoft Entra ID dans Azure AD Connect et cliquez sur Suivant.

  ![2](https://github.com/user-attachments/assets/f437bd3a-076d-48d6-a417-01976aecebc9)

  Le nom d'utilisateur requis peut être trouvé sous Issuer Assigned ID.
  ![3](https://github.com/user-attachments/assets/8f22fa13-89c9-4e3f-b1a3-fd90d8098d68)
  
  Ensuite, entrez ces mêmes informations dans la fenêtre de connexion ci-après pour vous connecter à votre compte Azure.

  ![4](https://github.com/user-attachments/assets/48fc49ab-920b-4d9d-afa5-eb06eca76174)

    Configuration du site de confiance  :
  
  Une fenêtre d'internet explorer s'ouvrira a cause d'un probleme de javascript, cliquer sur ajouter pour ajouter le site comme un site de confiance

  ![5](https://github.com/user-attachments/assets/cf2fcb2b-767a-4f31-b89f-7b320e0b7b09)
    
  ![6](https://github.com/user-attachments/assets/5c993cce-88d7-47ea-9157-86d7b9ec783c)

  Approuvez la connexion avec votre appareil secondaire si cela est configuré, afin qu'Azure AD Connect puisse se connecter à votre compte Azure.

  ![7](https://github.com/user-attachments/assets/65bc24c7-e39a-4865-b310-3e823eec6e41)

  Attention Problèmes de sécurité supplémentaires :
  
  ![8](https://github.com/user-attachments/assets/e2f40b4f-ccc7-401f-b3bf-d9bafcdf5d0b)
  
  L'utilisateur administrateur que vous avez ajouté pourrait être bloqué en raison des paramètres de sécurité supplémentaires d'Azure, qui nécessitent une authentification supplémentaire,     
      comme une vérification multifacteur (MFA).
      
  Si vous utilisez un compte gratuit, vous devrez disposer d'un Microsoft Entra tenant fonctionnel avec des licences Microsoft Entra ID P1 ou des licences d'essai.

  Si vous ne disposez pas de ces licences, vous pouvez contourner ce problème en désactivant les "security defaults" :

  Allez dans l'application Microsoft Entra ID (MEID) -> Properties -> Manage security defaults.
        Réglez Enable security defaults sur No.
     
  <img width="897" alt="9" src="https://github.com/user-attachments/assets/a14908f9-66c4-48c2-a491-a844361edded">

   Rôle d'administrateur global : Ce rôle est requis pour contourner le blocage d'Azure. Assurez-vous que l'utilisateur ajouté est configuré comme Global Administrator dans Azure.

    Note Importante : Dans un environnement de production, il n'est pas recommandé de désactiver les paramètres de sécurité par défaut. Ces paramètres sont importants pour garantir une sécurité 
    optimale. L'utilisation du rôle d'administrateur global pour contourner des blocages peut exposer votre environnement à des risques de sécurité.

  
- Connexion à AD DS

    L'étape suivante consiste à vous connecter à Active Directory Domain Services (AD DS) en utilisant les identifiants de votre compte administrateur Windows Server. Une fois connecté, cliquez sur Suivant.

    ![10](https://github.com/user-attachments/assets/dfb00f64-e185-45e0-b569-32e9318f779a)

- Configuration de la connexion a Microsoft Entra ID

    Dans cette étape, vous allez configurer Azure AD Connect pour établir une connexion avec Azure Active Directory (Azure AD). Cette configuration inclut la correspondance des UPN (User 
    Principal Names) entre votre Active Directory on-premises et Azure AD.

    Cependant, dans votre cas, la correspondance des UPN n'est pas nécessaire. Vous pouvez donc sélectionner l'option "Sans faire correspondance" pour avancer sans configurer cette         
    correspondance. Cela vous permettra de poursuivre la configuration sans avoir à aligner les UPN entre les deux environnements.

    ![11](https://github.com/user-attachments/assets/47f00dc7-048a-423e-9c4b-62df12e9da47)
    ![11-2](https://github.com/user-attachments/assets/9f2fdafd-3720-4fb2-b5ee-5a8cc469bc31)
    ![11-1](https://github.com/user-attachments/assets/71ea33e3-f294-40c0-b7c5-7127cb002f73)

- On y est prêt

    ![12](https://github.com/user-attachments/assets/3d15c46b-8416-4798-b8c3-9200e7a27a6c)

    Cliquez sur Installer pour lancer le processus d'installation d'Azure AD Connect.

    Problème avec TLS 1.2 : Si une erreur liée à TLS 1.2 survient pendant l'installation, vérifiez les paramètres de votre registre.

  ![13](https://github.com/user-attachments/assets/08bcc78c-5d14-4e27-ab75-e0788a7e0e08)
  
    Activation de TLS 1.2 : Assurez-vous que TLS 1.2 est activé, sinon la synchronisation ne pourra pas être effectuée. Pour activer TLS 1.2, suivez les instructions fournies dans le lien 
    suivant :
    
  https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-tls-enforcement

- Configuration terminée :

Tout est prêt ! La configuration d'Azure AD Connect est maintenant terminée. Vous avez établi la connexion entre votre Active Directory on-premises et Azure AD, et vous avez configuré la synchronisation des identités. Vous pouvez maintenant vérifier que la synchronisation fonctionne correctement et surveiller les mises à jour dans le portail Azure.

![14](https://github.com/user-attachments/assets/82959490-c333-4d5b-9a42-5b94219fd619)

- Comparaison des identités on-premises avec les utilisateurs Azure :

Identités On-Premises :

  ![16](https://github.com/user-attachments/assets/807aee93-85a9-490a-86e1-2d29ff4dd49b)
  

Apres la  configuration et migration des utilisateurs et groupes d'utilisateurs depuis votre Active Directory Domain Services (AD DS) sur Windows Server 2022.

Utilisateurs Azure :

Voici une vue des utilisateurs synchronisés et visibles dans votre Azure Active Directory (Azure AD) après la configuration et la synchronisation effectuées.

  ![15](https://github.com/user-attachments/assets/3b4b0a4d-9a19-4ad6-8a57-5c3958cfc5d3)


### Réseaux 
--------------
- [Discord](https://discord.com/users/yvantankeu)
- [LinkedIn](https://www.linkedin.com/in/yvan-tankeu-ab029a129/)

