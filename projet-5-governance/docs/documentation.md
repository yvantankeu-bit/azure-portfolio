# Projet 5 — Gouvernance Azure (Azure Policy & Cost Management)

## Objectif
Implémenter une stratégie de gouvernance cloud complète pour **FinDataCorp**, une plateforme de données analytiques fictive : hiérarchie organisationnelle via Management Groups, contrôle des coûts, conformité des ressources et résidence des données au Canada via Azure Policy.

## Architecture de gouvernance

```
Tenant Root Group
└── mg-findatacorp (FinDataCorp)
    ├── mg-production      → pipelines data live
    ├── mg-development     → data scientists / dev
    └── mg-analytics       → BI & reporting
```

## Ressources créées

| Ressource | Nom | Détails |
|-----------|-----|---------|
| Management Group | mg-findatacorp | Racine FinDataCorp |
| Management Group | mg-production | Sous-groupe Production |
| Management Group | mg-development | Sous-groupe Development |
| Management Group | mg-analytics | Sous-groupe Analytics |
| Policy Assignment | vm-sizes-findatacorp | VMs Series B uniquement |
| Policy Assignment | require-tag-environment | Tag `environment` obligatoire |
| Policy Assignment | require-tag-costcenter | Tag `cost-center` obligatoire |
| Policy Assignment | allowed-locations-canada | Région Canada uniquement |
| Resource Group | rg-analytics-projet5 | canadacentral — tags appliqués |

## Politiques déployées

| Policy | Scope | Effet |
|--------|-------|-------|
| Allowed VM sizes (Series B) | mg-findatacorp | Deny — VMs hors Series B bloquées |
| Require tag: environment | mg-findatacorp | Deny — ressources sans tag bloquées |
| Require tag: cost-center | mg-findatacorp | Deny — ressources sans tag bloquées |
| Allowed locations: Canada | mg-findatacorp | Deny — déploiements hors Canada bloqués |

## Preuves visuelles

### 1. Hiérarchie Management Groups
![Hiérarchie complète](../screenshots/01%20—%20Vue%20hiérarchie%20complète.png)
> Tenant Root Group → mg-findatacorp avec ses 3 sous-groupes Production, Development et Analytics.

---

### 2. Détail mg-findatacorp
![Sous-groupes](../screenshots/Screenshot%2002%20avec%20les%203%20sous-groupes%20visibles.png)
> Les 3 sous-groupes visibles sous mg-findatacorp — héritage des policies du haut vers le bas.

---

### 3. Policies assignées
![Policies](../screenshots/Screenshot%2003%20%20vue%20des%204%20policies.png)
> Les 4 policies déployées au niveau mg-findatacorp — applicables à toutes les subscriptions enfants.

---

### 4. Détail policy — VM sizes
![VM sizes policy](../screenshots/Screenshot%2004%20VM%20sizes.png)
> Policy "Allowed VM sizes" — restreint les déploiements aux VMs Series B uniquement (Standard_B1s à Standard_B4ms).

---

### 5. Resource Group avec tags
![Resource Group tags](../screenshots/Screenshot%2005%20rg-analytics-projet5.png)
> Resource Group `rg-analytics-projet5` créé en canadacentral avec les tags requis.

---

### 6. Tags appliqués
![Tags](../screenshots/6%203%20tags.png)
> Les 3 tags obligatoires appliqués : `environment=development`, `cost-center=analytics`, `project=findatacorp`.

---

## Compétences démontrées

- Azure Management Groups — hiérarchie organisationnelle
- Azure Policy — déploiement et assignation au niveau Management Group
- Héritage des policies (Management Group → Subscription → Resource Group)
- RBAC au niveau Management Group
- Resource tagging — suivi des coûts par équipe/projet
- Azure Cost Management — analyse des coûts par tag
- Résidence des données (data residency) — Canada uniquement

## Commandes clés

```bash
# Créer la hiérarchie Management Groups
az account management-group create --name mg-findatacorp --display-name "FinDataCorp"
az account management-group create --name mg-production --display-name "Production" --parent mg-findatacorp
az account management-group create --name mg-development --display-name "Development" --parent mg-findatacorp
az account management-group create --name mg-analytics --display-name "Analytics" --parent mg-findatacorp

# Déplacer la subscription sous mg-development
az account management-group subscription add --name mg-development --subscription <SUBSCRIPTION_ID>

# Déployer les policies (depuis bash)
az policy assignment create \
  --name "vm-sizes-findatacorp" \
  --display-name "FinDataCorp - Allowed VM sizes (Series B)" \
  --policy "cccc23c7-8427-4f53-ad12-b6a63eb452b3" \
  --scope "/providers/Microsoft.Management/managementGroups/mg-findatacorp" \
  --params '{"listOfAllowedSKUs": {"value": ["Standard_B1s","Standard_B1ms","Standard_B2s","Standard_B2ms","Standard_B4ms"]}}'

az policy assignment create \
  --name "require-tag-environment" \
  --display-name "FinDataCorp - Require tag: environment" \
  --policy "871b6d14-10aa-478d-b590-94f262ecfa99" \
  --scope "/providers/Microsoft.Management/managementGroups/mg-findatacorp" \
  --params '{"tagName": {"value": "environment"}}'

az policy assignment create \
  --name "require-tag-costcenter" \
  --display-name "FinDataCorp - Require tag: cost-center" \
  --policy "871b6d14-10aa-478d-b590-94f262ecfa99" \
  --scope "/providers/Microsoft.Management/managementGroups/mg-findatacorp" \
  --params '{"tagName": {"value": "cost-center"}}'

az policy assignment create \
  --name "allowed-locations-canada" \
  --display-name "FinDataCorp - Canada data residency" \
  --policy "e56962a6-4747-49cd-b67b-bf8b01975c4c" \
  --scope "/providers/Microsoft.Management/managementGroups/mg-findatacorp" \
  --params '{"listOfAllowedLocations": {"value": ["canadacentral","canadaeast"]}}'

# Créer un Resource Group avec tags
az group create \
  --name rg-analytics-projet5 \
  --location canadacentral \
  --tags environment=development cost-center=analytics project=findatacorp

# Supprimer les ressources
az group delete --name rg-analytics-projet5 --yes
az account management-group subscription remove --name mg-development --subscription <SUBSCRIPTION_ID>
az account management-group delete --name mg-analytics
az account management-group delete --name mg-production
az account management-group delete --name mg-development
az account management-group delete --name mg-findatacorp
```

## Description pour CV

> Implémenté une stratégie de gouvernance cloud enterprise pour une plateforme de données analytiques (FinDataCorp) : hiérarchie Management Groups (Production/Development/Analytics), 4 Azure Policies déployées au niveau Management Group (restriction VMs Series B, tags obligatoires environment et cost-center, résidence des données Canada uniquement). Validation du blocage des déploiements non conformes.

**Compétences :** Azure Policy · Management Groups · RBAC · Resource Tags · Cost Management · Data Residency
