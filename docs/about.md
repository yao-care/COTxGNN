---
layout: default
title: Acerca de
nav_order: 90
permalink: /about/
description: "COTxGNN es una plataforma de predicción de reposicionamiento de medicamentos desarrollada por 藥提醒科技有限公司 (yao.care), construida sobre el modelo TxGNN de Harvard, que cubre los medicamentos aprobados por el INVIMA en Colombia."
---

# Acerca de

<div class="key-takeaway">
Aceleramos la validación de evidencia del reposicionamiento de medicamentos con IA: de la predicción a la evidencia de un vistazo.
</div>

---

## Antecedentes

<p class="key-answer" data-question="¿Qué es COTxGNN?">
<strong>COTxGNN</strong> es una plataforma de apoyo a la investigación en reposicionamiento de
medicamentos, construida sobre el modelo TxGNN publicado en <em>Nature Medicine</em> por el
Zitnik Lab de la Universidad de Harvard. Predice la ampliación de indicaciones de los medicamentos
aprobados por el INVIMA en Colombia. Además de los puntajes de predicción de la IA, la plataforma
integra evidencia clínica de ClinicalTrials.gov y PubMed para que los investigadores puedan
evaluar rápidamente qué tan creíble es cada predicción.
</p>

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

## ¿Qué es el reposicionamiento de medicamentos?

<p class="key-answer" data-question="¿Qué es el reposicionamiento de medicamentos?">
El <strong>reposicionamiento de medicamentos</strong> consiste en encontrar nuevos usos terapéuticos
para medicamentos ya existentes. Frente al desarrollo de un medicamento nuevo desde cero —de 10 a
15 años y entre USD 1.000&ndash;2.000 millones—, el reposicionamiento toma de 3 a 5 años y entre
USD 100&ndash;300 millones, y ya existen datos de seguridad en humanos, por lo que el riesgo de
fracaso es menor.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspecto</th><th>Desarrollo de un medicamento nuevo</th><th>Reposicionamiento de medicamentos</th></tr>
</thead>
<tbody>
<tr><td>Tiempo</td><td>10&ndash;15 años</td><td>3&ndash;5 años</td></tr>
<tr><td>Costo</td><td>USD 1.000&ndash;2.000 millones</td><td>USD 100&ndash;300 millones</td></tr>
<tr><td>Datos de seguridad</td><td>Deben generarse desde cero</td><td>Ya existen datos en humanos</td></tr>
<tr><td>Riesgo de fracaso</td><td>Muy alto (&gt;90%)</td><td>Menor</td></tr>
</tbody>
</table>

---

## ¿Qué es TxGNN?

<p class="key-answer" data-question="¿Qué es TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> es un modelo de aprendizaje
profundo desarrollado por el Zitnik Lab de Harvard Medical School y publicado en <em>Nature Medicine</em>.
Predice nuevas asociaciones entre medicamentos y enfermedades, y es el primer modelo fundacional para
reposicionamiento de medicamentos diseñado específicamente para el personal clínico.
</p>

<blockquote class="expert-quote">
"TxGNN integra un grafo de conocimiento de 17.080 entidades biomédicas y utiliza redes neuronales de
grafos para aprender relaciones complejas entre nodos, prediciendo la eficacia potencial de los
medicamentos frente a enfermedades raras."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Fuentes de datos

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fuente</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>Predicción con IA</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Modelo de predicción con grafo de conocimiento de Harvard</td></tr>
<tr><td>Ensayos clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Registro global de ensayos clínicos</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Base de datos de literatura biomédica</td></tr>
<tr><td>Información de medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Base de datos de medicamentos y blancos terapéuticos</td></tr>
<tr><td>Datos de registro sanitario</td><td><a href="https://www.invima.gov.co/">INVIMA</a></td><td>Datos de aprobación de medicamentos en Colombia</td></tr>
</tbody>
</table>

---

## Base académica

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Alcance

| Ítem | Valor |
|------|-------|
| Informes de medicamentos | {{ site.drugs.size }} |
| Autoridad regulatoria | INVIMA |
| Sitios desplegados | 30 países / regiones |

---

## Contacto

- **GitHub Issues**: <https://github.com/yao-care/COTxGNN/issues>
- **Desarrollador**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Descripción del producto**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe es únicamente para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste su medicación por cuenta propia. Toda decisión de reposicionamiento de medicamentos requiere validación clínica completa y revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
