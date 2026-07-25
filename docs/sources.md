---
layout: default
title: Fuentes de Datos
nav_order: 93
permalink: /sources/
description: "Fuentes de datos detrás de COTxGNN: datos de registro sanitario del INVIMA, TxGNN, ClinicalTrials.gov, PubMed y DrugBank."
---

# Fuentes de Datos

<div class="key-takeaway">
Cada conclusión se remonta a una fuente de datos pública: nada es una caja negra.
</div>

---

## Panorama de las fuentes

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fuente</th><th>Se usa para</th></tr>
</thead>
<tbody>
<tr><td>Datos de registro sanitario</td><td><a href="https://www.invima.gov.co/">INVIMA</a></td><td>Listado de medicamentos aprobados y sus principios activos en Colombia</td></tr>
<tr><td>Modelo de predicción</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Predicción de asociaciones entre medicamentos y enfermedades</td></tr>
<tr><td>Ensayos clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Clasificación de la evidencia (NCT)</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Clasificación de la evidencia (PMID)</td></tr>
<tr><td>Información de medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mapeo de principios activos y datos de blancos terapéuticos</td></tr>
<tr><td>Interacciones</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Datos de interacciones entre medicamentos</td></tr>
</tbody>
</table>

---

## Licencias

Cada fuente tiene su propia licencia; por favor revísela antes de citar:

- **TxGNN**: uso académico; cite a Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: datos públicos de los NIH de Estados Unidos
- **DrugBank**: uso no comercial sujeto a sus términos de licencia
- **INVIMA**: sujeto a los términos de datos abiertos de la autoridad regulatoria de Colombia

---

## Frecuencia de actualización

| Datos | Frecuencia |
|------|-----------|
| Datos de registro sanitario | Según la publicación de la autoridad regulatoria |
| Evidencia de ensayos / literatura | Recolectada nuevamente de forma periódica |
| Datos de interacciones | Revisados trimestralmente |

---

## Citación académica

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care, número de registro
mercantil 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

COTxGNN es el sitio de Colombia de la línea de productos "TxGNN Drug Repurposing" de la compañía.
El mismo sistema está desplegado en 30 países y regiones, cada uno con el nombre `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, etc.) en `{cc}txgnn.yao.care`.
Descripción del producto: <https://www.yao.care/medical/txgnn/>.

El modelo TxGNN fue desarrollado por el Zitnik Lab de Harvard Medical School y publicado en
*Nature Medicine*. Esta plataforma es el sistema de producción que 藥提醒科技有限公司 construyó sobre ese
modelo, y abarca la integración de datos nacionales de registro sanitario, la predicción dual con
grafo de conocimiento y aprendizaje profundo, la clasificación de evidencia de PubMed /
ClinicalTrials y la integración con historias clínicas electrónicas mediante SMART on FHIR.

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe es únicamente para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste su medicación por cuenta propia. Toda decisión de reposicionamiento de medicamentos requiere validación clínica completa y revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
