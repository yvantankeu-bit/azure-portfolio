# Projet 4 — Gestion des Identités & Authentification

## Objectif
Concevoir et déployer une solution d'identité hybride complète dans Azure : synchronisation on-premises via Entra Connect, collaboration externe B2B, accès sécurisé aux secrets via Managed Identity + Key Vault, et authentification Google sur une application web.

## Architecture

```
On-Premises (VM Windows Server 2022)
        │
        │  Microsoft Entra Connect (sync)
        ▼
Microsoft Entra ID (Tenant)
        ├── Utilisateurs synchronisés (on-premises → cloud)
        │
        ├── Utilisateurs invités B2B (Lima Tech Solutions)
        │       └── Conditional Access (restrictions d'accès)
        │
        └── App Service (Web App .NET)
                ├── Managed Identity (System Assigned)
                │       └── RBAC → Key Vault Secrets User
                ├── Google Identity Provider (OpenID Connect)
                └── Azure Key Vault
                        └── Secrets (mots de passe, clés API)
```

## Ressources créées

| Ressource | Nom | Détails |
|-----------|-----|---------|
| Resource Group | rg-identity-projet4 | eastus |
| VM Windows Server | vm-adconnect | Windows Server 2022, Standard_B2s — AD DS + Entra Connect |
| App Service Plan | asp-identity-projet4 | Linux, Free F1 |
| App Service (Web App) | app-identity-projet4 | .NET — démo Managed Identity |
| Key Vault | kv-identity-p4 | secrets stockés, accès via RBAC |
| Managed Identity | System Assigned | attachée à l'App Service |
| Role Assignment | Key Vault Secrets User | Managed Identity → Key Vault |
| B2B Guest User | dev@limatech.com | utilisateur externe invité |
| Google Identity Provider | OpenID Connect | configuré sur l'App Service |

## Partie 1 — Synchronisation Hybride (Entra Connect)

### 1. VM Windows Server avec AD DS
![VM Windows Server + AD DS](../screenshots/01_adds_users_onprem.jpg)
> Utilisateurs et groupes créés dans Active Directory Domain Services sur Windows Server 2022.

---

### 2. Installation et configuration d'Entra Connect
![Entra Connect — Configuration rapide](../screenshots/02_entraconnect_setup.jpg)
> Installation d'Azure AD Connect sur la VM on-premises, connexion au tenant Entra ID via un compte Global Administrator.

---

### 3. Synchronisation réussie
![Utilisateurs synchronisés dans Entra ID](../screenshots/03_users_synced_entraid.jpg)
> Utilisateurs on-premises visibles dans Microsoft Entra ID après la synchronisation.

---

## Partie 2 — Collaboration B2B

### 4. Invitation d'un utilisateur externe
![Invitation B2B](../screenshots/04_b2b_invite.jpg)
> Invitation d'un développeur de Lima Tech Solutions en tant qu'utilisateur guest dans le tenant StratWise Consulting.

---

### 5. Invitation acceptée
![B2B Accepted](../screenshots/05_b2b_accepted.jpg)
> Statut B2B Invitation : Accepted. L'utilisateur externe accède aux ressources partagées.

---

## Partie 3 — Managed Identity + Key Vault

### 6. Managed Identity activée sur l'App Service
![Managed Identity](../screenshots/06_managed_identity.jpg)
> System Assigned Identity activée sur l'App Service — un Principal de service est créé automatiquement dans Entra ID.

---

### 7. Role Assignment — Key Vault Secrets User
![RBAC Key Vault](../screenshots/07_keyvault_rbac.jpg)
> Rôle Key Vault Secrets User assigné à la Managed Identity de l'App Service via IAM.

---

### 8. Secrets dans Key Vault
![Key Vault Secrets](../screenshots/08_keyvault_secrets.jpg)
> Secrets stockés dans le Key Vault, accessibles par l'application sans credentials hardcodés.

---

### 9. Application web affichant les secrets via Managed Identity
![Web App Secrets Result](../screenshots/09_webapp_secrets_result.jpg)
> L'application .NET récupère et affiche les secrets du Key Vault grâce à DefaultAzureCredential — aucun mot de passe dans le code.

---

## Partie 4 — Google comme fournisseur d'identité

### 10. Configuration Google OAuth dans Azure
![Google Identity Provider](../screenshots/10_google_idp_configured.jpg)
> Google configuré comme fournisseur d'identité sur l'App Service (ID client + secret OAuth depuis Google Cloud Console).

---

### 11. Authentification via compte Google
![Google Auth Test](../screenshots/11_google_auth_test.jpg)
> Connexion réussie à l'application web via un compte Google — fédération OpenID Connect opérationnelle.

---

## Compétences démontrées

- Microsoft Entra ID (Azure AD)
- Entra Connect — synchronisation hybride on-premises
- Azure AD B2B — collaboration externe
- Managed Identity (System Assigned)
- Azure Key Vault — stockage et accès aux secrets
- RBAC — Key Vault Secrets User
- Google Identity Provider (OpenID Connect)
- Azure App Service

## Commandes clés

```bash
# Créer le Resource Group
az group create \
  --name rg-identity-projet4 \
  --location eastus

# Créer la VM Windows Server (AD DS + Entra Connect)
az vm create \
  --resource-group rg-identity-projet4 \
  --name vm-adconnect \
  --image Win2022Datacenter \
  --size Standard_B2s \
  --admin-username azureuser \
  --admin-password <mot-de-passe>

# Créer le Key Vault
az keyvault create \
  --name kv-identity-p4 \
  --resource-group rg-identity-projet4 \
  --location eastus \
  --enable-rbac-authorization true

# Créer un secret dans le Key Vault
az keyvault secret set \
  --vault-name kv-identity-p4 \
  --name "db-password" \
  --value "MonMotDePasse123"

# Créer l'App Service Plan
az appservice plan create \
  --name asp-identity-projet4 \
  --resource-group rg-identity-projet4 \
  --sku F1 \
  --is-linux

# Créer la Web App (.NET)
az webapp create \
  --name app-identity-projet4 \
  --resource-group rg-identity-projet4 \
  --plan asp-identity-projet4 \
  --runtime "DOTNETCORE:8.0"

# Activer la Managed Identity (System Assigned)
az webapp identity assign \
  --name app-identity-projet4 \
  --resource-group rg-identity-projet4

# Récupérer le Principal ID de la Managed Identity
PRINCIPAL_ID=$(az webapp identity show \
  --name app-identity-projet4 \
  --resource-group rg-identity-projet4 \
  --query principalId -o tsv)

# Assigner le rôle Key Vault Secrets User à la Managed Identity
az role assignment create \
  --role "Key Vault Secrets User" \
  --assignee $PRINCIPAL_ID \
  --scope $(az keyvault show --name kv-identity-p4 --query id -o tsv)

# Inviter un utilisateur externe B2B
az ad invitation create \
  --invited-user-email-address "dev@limatech.com" \
  --invite-redirect-url "https://myapplications.microsoft.com" \
  --invited-user-display-name "Dev Lima Tech"

# Éteindre la VM (économiser les coûts)
az vm deallocate \
  --resource-group rg-identity-projet4 \
  --name vm-adconnect

# Supprimer toutes les ressources
az group delete --name rg-identity-projet4 --yes
```

## Description pour CV

> Déployé une solution d'identité hybride complète : synchronisation on-premises via Microsoft Entra Connect (VM Windows Server 2022 + AD DS), collaboration B2B avec invitation d'utilisateurs externes, accès sécurisé aux secrets Key Vault via Managed Identity sans credentials dans le code (RBAC Key Vault Secrets User), et configuration de Google comme fournisseur d'identité externe (OpenID Connect) sur une App Service .NET.

**Compétences :** Entra Connect · B2B · Managed Identity · Key Vault · RBAC · Google Identity Provider · App Service
