**Déployer une Application Web Azure en .NET avec Accès au Key Vault via Identité Managée**
=======================================================================================

**Introduction**

J'ai un Key Vault dans Azure qui contient mes mots de passe et autres secrets. Je souhaite les lister dans mon application web Azure développée en C# avec .NET. Ce tutoriel vous guidera à travers les étapes pour déployer votre application web sur Azure App Service, configurer une identité managée pour accéder en toute sécurité à votre Key Vault, et afficher les secrets dans votre application web.

   ![image](https://github.com/user-attachments/assets/005294fb-092f-43ee-af09-58741797d7a5)
   
**Scénario**

Vous avez une application web en .NET que vous souhaitez déployer sur Azure App Service. Votre application doit accéder à des secrets stockés dans Azure Key Vault, comme des mots de passe ou des clés API, pour les afficher ou les utiliser. Pour garantir la sécurité, vous utiliserez une identité managée, ce qui évite de stocker des informations d'identification sensibles dans votre code.

**Prérequis**

  - Créer et déployer une application web sur Azure App Service : Vous devez avoir une application web déjà déployée sur Azure. Si ce n’est pas le cas, suivez les [instructions](https://learn.microsoft.com/fr-fr/azure/key-vault/general/tutorial-net-create-vault-azure-web-app?tabs=azure-cli#create-a-net-core-app) pour créer et déployer une application web sur Azure App Service.

  - Créer une ressource Azure Key Vault et le provisionner de mots de passes : Configurez un Key Vault dans Azure pour stocker vos secrets de manière sécurisée.

**Configurer l’application web pour se connecter au coffre de clés**

1 - Créer une identité managée dans azure pour votre application web


  - Dans le portail Azure, accédez à votre application web.

  - Allez dans Settings > Identity > System Assigned.
  
  - Activez l'option en basculant de "Off" à "On" et cliquez sur Save pour enregistrer les modifications.

 ![donneruneidentitealawebapp1](https://github.com/user-attachments/assets/0ea2280e-960b-4e09-9d57-96e3cb9fb955)

  - Confirmez l'activation de l'identité managée.

 ![donneruneidentitealawebapp2](https://github.com/user-attachments/assets/ed957bab-5681-4e78-83c1-5ba343072663)

  - Vous verrez l'ID de l'objet de l'identité managée, un principal de service créé dans votre locataire.
  
  ![donneruneidentitealawebapp3](https://github.com/user-attachments/assets/7feec3ec-d8a6-4f3b-b876-71ec3523502f)


2 - Attribuer les autorisations nécessaires à l'identité managée a votre application web

  Pour permettre à votre application web d'accéder aux secrets dans Azure Key Vault, vous devez lui accorder les autorisations nécessaires via le contrôle d'accès en fonction du rôle (RBAC).

  - Dans la ressource de votre application web, allez dans Access Control (IAM).  

   ![role1](https://github.com/user-attachments/assets/238b548c-588a-4fc9-8299-106f801e8d8e)

 - Cliquez sur Add role assignment.
 
   ![role2](https://github.com/user-attachments/assets/daa54502-f887-46fd-8415-bc935e2026c3)

  - Dans la liste des rôles, sélectionnez Key Vault Secrets User et cliquez sur Next.

  ![15](https://github.com/user-attachments/assets/a86c0fa5-9a58-435b-93de-d05620fe8c6c)

   - Cliquez sur Managed identity et sélectionnez Select Members.

  ![16](https://github.com/user-attachments/assets/0402581f-ad7c-4d26-b236-4d7a9dfabda3)

  - Choisissez votre abonnement de l'application web dans Select Members

  ![7](https://github.com/user-attachments/assets/ab76d28e-11e9-496f-ac31-d99924043487)

  - Sélectionnez l'identité managée que vous avez créée et cliquez sur Select.

  ![8](https://github.com/user-attachments/assets/94c44528-f452-4fc1-b920-4031b3929875)

  - Cliquez sur Select pour confirmer la sélection de l'application web comme membre.
  
  ![9](https://github.com/user-attachments/assets/0d394662-de95-4779-b0d9-f7917857181a)


3 - Créer des secrets dans Azure Key Vault

  Pour acceder a nos secrets, il va falloir que ceux-ci existent, alors nous devons creer nos secrets.

  - Accédez à votre Key Vault depuis le portail Azure.

  - Dans la section Objects > Secrets, vous verrez la liste des secrets existants.

  ![keyvault1](https://github.com/user-attachments/assets/70b41271-6ee5-41cd-92ab-10b873577643)

  - Pour ajouter un nouveau secret, cliquez sur Generate/Import.

  ![keyvault2](https://github.com/user-attachments/assets/772c6ad0-201f-4260-a736-39605bff50aa)

  - Dans la fenêtre de création, entrez le nom et la valeur de votre secret, puis cliquez sur Create.

  ![keyvault3](https://github.com/user-attachments/assets/28fb5876-4266-47aa-8af0-a284e4c15121)


4 - Acceder aux secrets via notre application web

Voici le code pour accéder aux secrets depuis votre application web :

    using Azure;
    using Azure.Identity;
    using Azure.Security.KeyVault.Secrets;
    using Azure.Core;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.Extensions.DependencyInjection;
    
    var builder = WebApplication.CreateBuilder(args);
    var app = builder.Build();
    
    // Configuration des options du client
    SecretClientOptions options = new SecretClientOptions()
    {
        Retry =
        {
            Delay = TimeSpan.FromSeconds(2),
            MaxDelay = TimeSpan.FromSeconds(16),
            MaxRetries = 5,
            Mode = RetryMode.Exponential
        }
    };
    
    // Créez un client pour accéder au Key Vault
    var client = new SecretClient(new Uri("https://<your-unique-key-vault-name>.vault.azure.net/"), new DefaultAzureCredential(), options);
    
    // Route pour récupérer et afficher tous les secrets
    app.MapGet("/", async () =>
    {
        var secretValues = new List<string>();
    
        // Récupérez les propriétés de tous les secrets
        await foreach (var secretProperties in client.GetPropertiesOfSecretsAsync())
        {
            try
            {
                // Récupérez chaque secret par son nom
                KeyVaultSecret secret = await client.GetSecretAsync(secretProperties.Name);
                secretValues.Add($"{secretProperties.Name}: {secret.Value}");
            }
            catch (RequestFailedException ex)
            {
                // Gestion des erreurs éventuelles lors de la récupération d'un secret
                secretValues.Add($"Erreur pour {secretProperties.Name}: {ex.Message}");
            }
        }
    
        // Retournez les secrets comme une chaîne formatée
        return string.Join("\n", secretValues);
    });
    
    app.Run();


**Résultat**
--------

Après avoir déployé et configuré votre application, vous devriez voir les secrets affichés sur votre page web.

![keyvault4](https://github.com/user-attachments/assets/5ed145cc-0723-4095-84f5-2a67b73f72d4)
![image](https://github.com/user-attachments/assets/6af8b667-1609-4848-83b4-c4c89c1a3bc2)


### Réseaux 
--------------
- [Discord](https://discord.com/users/yvantankeu)
- [LinkedIn](https://www.linkedin.com/in/yvan-tankeu-ab029a129/)
