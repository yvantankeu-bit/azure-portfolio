# CLAUDE.md — Azure Portfolio

## Vue d'ensemble
Portfolio Azure de Yvan Tankeu — projets pratiques pour AZ-104/AZ-305.
GitHub : `yvantankeu-bit/azure-portfolio`
CV/Portfolio Vercel : repo séparé `yvantankeu-bit/yvan-tankeu-portfolio` (dossier `cv/`)

## Structure des projets

| Projet | Dossier | Statut | Notes |
|--------|---------|--------|-------|
| 1 — WordPress VM | projet-1-wordpress-vm | ✅ Terminé | Ubuntu 22.04, LAMP, NSG |
| 2 — Blob Storage + CDN | projet-2-blob-cdn | ✅ Terminé | Azure Front Door Standard |
| 3 — Hub-and-Spoke | projet-3-hub-spoke | ✅ Terminé | Azure Firewall, UDR, VNet Peering |
| 4 — Identity & Auth | projet-4-identity-auth | ✅ Terminé | Entra Connect, B2B, Managed Identity, Key Vault, Google OpenID Connect |
| 5 — Governance | projet-5-governance | ✅ Terminé | Management Groups FinDataCorp, 4 Azure Policies, tags |
| 6 — Load Balancer | projet-6-load-balancer | ✅ Terminé | Load Balancer Standard + 2 VMs Apache |
| 7 — Monitoring | projet-7-monitoring | ⏳ À faire | |
| 8 — Terraform | projet-8-terraform | ✅ Terminé | IaC, Data Lake Gen2, VM Ubuntu |
| 9 — CI/CD DevOps | projet-9-cicd-devops | ✅ Terminé | Azure DevOps, Flask, App Service |
| 10 — Architecture 3-tiers | projet-10-architecture-3tiers | ⏳ À faire | |

## Subscription Azure
- Subscription ID : `c2b9dd31-4d70-4c54-b2ba-99eed3035241`
- Git user : `yvantankeu-bit`

## Conventions des projets
Chaque projet contient :
- `docs/documentation.md` — architecture, ressources créées, commandes clés, description CV
- `screenshots/` — preuves visuelles numérotées
- `scripts/` — scripts Azure CLI (si applicable)

## Structure documentation.md
1. Objectif
2. Architecture (ASCII ou Mermaid)
3. Ressources créées (tableau)
4. Preuves visuelles (screenshots numérotés)
5. Compétences démontrées
6. Commandes clés (Azure CLI bash)
7. Description pour CV

## Repo CV
- Chemin local : `cv/` (exclu du .gitignore de ce repo)
- Remote : `https://github.com/yvantankeu-bit/yvan-tankeu-portfolio.git`
- Déployé sur Vercel — se met à jour automatiquement au push

## Projet 5 — Note
- Les policies Azure ont été assignées sur `mg-findatacorp`
- La subscription a été déplacée sous `mg-development`
- Screenshot de policy violation (Deny) à prendre quand propagation complète (~30 min)
- Scénario FinDataCorp orienté offre Desjardins (Administrateur Plateforme de Données Azure)

## Projet 6 — En cours
- Resource Group : `rg-loadbalancer-projet6` (eastus)
- Architecture : Load Balancer Standard + 2 VMs Ubuntu Apache
- En cours de déploiement
