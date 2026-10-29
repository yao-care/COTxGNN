---
layout: default
title: Predicciones de Reposicionamiento de Medicamentos
nav_order: 1
description: "Predicciones de reposicionamiento de medicamentos impulsadas por IA para Colombia. Análisis basado en evidencia de medicamentos aprobados para posibles nuevas indicaciones terapéuticas."
permalink: /
---

# Predicciones de Reposicionamiento de Medicamentos — Colombia

Este proyecto utiliza el modelo TxGNN (aprendizaje profundo) para predecir posibles nuevos usos terapéuticos para medicamentos aprobados en Colombia.

**Descargo de Responsabilidad**: Este contenido es solo para fines de investigación y no constituye consejo médico. Todas las predicciones de reposicionamiento de medicamentos requieren validación clínica antes de su aplicación.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Colombia: qué cubre este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en los datos de registro de [INVIMA](https://www.invima.gov.co/) (Colombia).

Informes por nivel de evidencia: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Medicamentos con mayor nivel de evidencia en este sitio

| Medicamento | Nivel de evidencia |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Fludarabine](/drugs/fludarabine/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Polidocanol](/drugs/polidocanol/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Triptorelin](/drugs/triptorelin/) | L1 |
| [Candesartan](/drugs/candesartan/) | L1 |

### Medicamentos que solo cubre este sitio entre los 30 sitios TxGNN

| Medicamento | Nivel de evidencia |
|---|---|
| [Thimerosal](/drugs/thimerosal/) | L5 |

<!-- local-home:end -->

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care, número de registro
mercantil 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

COTxGNN es el sitio de Colombia de la línea de productos "TxGNN Drug Repurposing" de la compañía.
El mismo sistema está desplegado en 30 países y regiones, cada uno con el nombre `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, etc.) en `{cc}txgnn.yao.care`.
Descripción del producto: <https://www.yao.care/medical/txgnn/>.

El modelo TxGNN fue desarrollado por el Zitnik Lab de Harvard Medical School y publicado en
*Nature Medicine*. Esta plataforma es el sistema de producción que 藥提醒科技有限公司 construyó sobre ese
modelo, y abarca la integración de datos nacionales de registro sanitario, la predicción por aprendizaje profundo que excluye los usos ya registrados en el grafo de conocimiento, la clasificación de evidencia de PubMed /
ClinicalTrials y la integración con historias clínicas electrónicas mediante SMART on FHIR.
