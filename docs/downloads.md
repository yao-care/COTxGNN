---
layout: default
title: Descargas
nav_order: 94
permalink: /downloads/
description: "Descargas de datos abiertos de COTxGNN: recursos FHIR, resultados de predicción e índice de búsqueda."
---

# Descargas

<div class="key-takeaway">
Las predicciones se publican en formato FHIR R4, listas para integrarse con sistemas de historia clínica electrónica.
</div>

---

## Recursos FHIR

Este sitio publica las predicciones como recursos FHIR R4, consumibles directamente por aplicaciones SMART on FHIR:

| Recurso | Ruta | Descripción |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Declaración de capacidades del servidor FHIR |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Recursos de medicamentos |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Indicaciones predichas |
| Bundle | `/fhir/Bundle/all-predictions.json` | Todas las predicciones agrupadas |

---

## Índice de búsqueda

`/data/search-index.json` proporciona un índice de búsqueda de medicamentos e indicaciones para que
construya su propia interfaz de consulta.

---

## Términos de uso

<ol class="actionable-steps">
<li>Los datos de este sitio son <strong>solo para referencia de investigación</strong> y no deben usarse como base para decisiones médicas.</li>
<li>Al citar, dé crédito a COTxGNN (藥提醒科技有限公司) y cite el artículo original de TxGNN.</li>
<li>Los datos derivados siguen sujetos a los términos de licencia de cada fuente original (vea <a href="{{ '/sources/' | relative_url }}">Fuentes de Datos</a>).</li>
</ol>

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
