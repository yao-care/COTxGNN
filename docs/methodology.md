---
layout: default
title: Metodología
nav_order: 91
permalink: /methodology/
description: "Cómo COTxGNN genera y valida sus predicciones: predicción con el grafo de conocimiento TxGNN, recolección de evidencia, clasificación L1-L5 y recomendaciones de decisión."
---

# Metodología

<div class="key-takeaway">
De la predicción con IA a la clasificación de evidencia: cada candidato tiene una base rastreable para su calificación.
</div>

---

## Flujo general

<p class="key-answer" data-question="¿Cómo genera COTxGNN sus predicciones?">
La plataforma usa un flujo de cuatro etapas: el modelo de grafo de conocimiento TxGNN predice
posibles asociaciones entre medicamentos y enfermedades, luego se recolecta evidencia de forma
automática para cada par predicho, la evidencia se clasifica de L1 a L5 y, finalmente, se emite
una recomendación de decisión.
</p>

<ol class="actionable-steps">
<li><strong>Predicción TxGNN</strong>: relaciones entre medicamentos y enfermedades predichas con un grafo de conocimiento combinado con redes neuronales de grafos.</li>
<li><strong>Recolección de evidencia</strong>: para cada par predicho se reúne evidencia de ClinicalTrials.gov, PubMed, DrugBank e INVIMA.</li>
<li><strong>Clasificación de la evidencia</strong>: se clasifica de L1 a L5, donde L1 es la más sólida (múltiples ECA de fase 3) y L5 corresponde únicamente a predicción del modelo.</li>
<li><strong>Recomendación de decisión</strong>: Go, Proceed, Consider, Explore o Hold, según el nivel de evidencia.</li>
</ol>

---

## Criterios de clasificación de la evidencia

<table class="comparison-table">
<thead>
<tr><th>Nivel</th><th>Definición</th><th>Significado clínico</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Múltiples ECA de fase 3 / revisiones sistemáticas</td><td>Respaldo sólido; puede considerarse el uso clínico</td></tr>
<tr><td><strong>L2</strong></td><td>Un solo ECA o múltiples ensayos de fase 2</td><td>Respaldo moderado; se pueden diseñar ensayos de validación</td></tr>
<tr><td><strong>L3</strong></td><td>Estudios observacionales / series de casos grandes</td><td>Respaldo preliminar; requiere validación adicional</td></tr>
<tr><td><strong>L4</strong></td><td>Estudios preclínicos / mecanísticos</td><td>Respaldo teórico; lejos del uso clínico</td></tr>
<tr><td><strong>L5</strong></td><td>Solo predicción del modelo</td><td>Etapa de hipótesis; aún sin evidencia en humanos</td></tr>
</tbody>
</table>

---

## Predicción de doble motor

Dos métodos corren en paralelo y una etiqueta de confianza registra si coinciden entre sí:

| Método | Velocidad | Precisión | Descripción |
|--------|-------|-----------|-------------|
| Grafo de conocimiento (KG) | Rápida | Menor | Inferencia sobre las relaciones de DrugBank y la estructura del grafo |
| Aprendizaje profundo (DL) | Lenta | Mayor | Modelo de red neuronal de grafos TxGNN |

| Confianza | Origen | Significado |
|------------|--------|---------|
| very_high | KG + DL | Ambos métodos coinciden |
| high | Solo DL | Respaldo de aprendizaje profundo con puntaje alto |
| medium | Solo KG | Respaldo del grafo de conocimiento |

---

## Integración de datos regulatorios

Los datos de aprobación de medicamentos en Colombia provienen del INVIMA. Los nombres de los
principios activos se mapean al vocabulario de DrugBank; los principios activos que no se pueden
mapear —extractos de plantas, vacunas, excipientes y otros no catalogados por DrugBank— quedan
excluidos de la predicción.

---

## Limitaciones

<ol class="actionable-steps">
<li>Las predicciones son asociaciones estadísticas y <strong>no implican causalidad ni eficacia clínica</strong>.</li>
<li>Una calificación L5 significa que solo hay predicción del modelo, sin evidencia de respaldo en humanos.</li>
<li>La recolección de evidencia depende de bases de datos públicas; los estudios no publicados o no indexados no quedan capturados.</li>
<li>El mapeo de principios activos puede omitir elementos por diferencias en la nomenclatura.</li>
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
