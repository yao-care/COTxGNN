---
layout: default
title: Guía del Usuario
nav_order: 92
permalink: /guide/
description: "Guía del usuario de COTxGNN: cómo consultar medicamentos, leer los niveles de evidencia e interpretar las recomendaciones."
---

# Guía del Usuario

<div class="key-takeaway">
Revise primero el nivel de evidencia, luego la recomendación y después lea la literatura de origen.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Colombia: datos de este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en los datos de registro de [INVIMA](https://www.invima.gov.co/) (Colombia).

Conjunto de datos: [INVIMA: Código Único de Medicamentos (CUM)](https://www.datos.gov.co/resource/i7cb-raxc.json); se descarga y se compara automáticamente cada semana (los lunes). Detalles: [Fuentes de Datos]({{ '/sources/' | relative_url }}).

Informes por nivel de evidencia:

| Nivel de evidencia | Informes | Proporción |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

10 pares medicamento–enfermedad predichos en este sitio no aparecen en ningún otro de los 30 sitios TxGNN.

<!-- site-data:end -->

## Cómo consultar un medicamento

<ol class="actionable-steps">
<li>Use el buscador en la parte superior de la página (los nombres de principios activos coinciden mejor que los nombres comerciales).</li>
<li>O explore el listado completo en <a href="{{ '/drugs/' | relative_url }}">Todos los Medicamentos</a>.</li>
<li>También puede explorar por nivel de evidencia: <a href="{{ '/evidence-high/' | relative_url }}">alta</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderada</a>, <a href="{{ '/evidence-low/' | relative_url }}">solo predicción del modelo</a>.</li>
</ol>

---

## Cómo leer un informe

<p class="key-answer" data-question="¿Qué significan los niveles de evidencia L1 a L5?">
Cada informe de medicamento lista las nuevas indicaciones predichas, y cada indicación tiene un
nivel de evidencia L1&ndash;L5. <strong>L1 significa que ya existen múltiples ensayos clínicos
aleatorizados de fase 3 que la respaldan; L5 significa solo predicción del modelo, sin evidencia
en humanos.</strong> Los criterios completos están en la página de
<a href="{{ '/methodology/' | relative_url }}">Metodología</a>.
</p>

| Si usted ve | Significa | Acción sugerida |
|-----------|----------|------------------|
| L1 / L2 | Existe evidencia de ensayos clínicos | Revise los registros NCT y PMID de origen |
| L3 / L4 | Evidencia observacional o preclínica | Tómelo como una pista de investigación |
| L5 | Solo predicción del modelo | Solo para generar hipótesis; no sirve de referencia clínica |

---

## Citación y trazabilidad

Cada pieza de evidencia de un informe tiene un identificador rastreable:

- **Número NCT**: enlaza al registro en ClinicalTrials.gov
- **PMID**: enlaza al registro en PubMed
- **DrugBank ID**: enlaza a los datos del medicamento y sus blancos terapéuticos

Por favor lea la literatura de origen para confirmar el contexto antes de citar cualquier conclusión de esta plataforma.

---

## Preguntas frecuentes

<p class="key-answer" data-question="¿Qué medicamentos con registro INVIMA ya tienen ensayos clínicos para una indicación nueva?">
En el listado de <a href="{{ '/drugs/' | relative_url }}">Todos los Medicamentos</a> puede filtrar por nivel de evidencia. Los medicamentos marcados como <a href="{{ '/evidence-high/' | relative_url }}">evidencia alta</a> o <a href="{{ '/evidence-medium/' | relative_url }}">moderada</a> (L1&ndash;L4) ya cuentan con ensayos clínicos u otra evidencia en humanos para la nueva indicación predicha; revise los registros NCT y PMID citados en cada informe para confirmar el estado del ensayo.
</p>

<p class="key-answer" data-question="¿Se pueden usar las predicciones en la práctica clínica?">
<strong>No.</strong> Las predicciones de esta plataforma son pistas de investigación, no consejo
clínico. Toda aplicación clínica de reposicionamiento de medicamentos debe pasar por una validación
completa mediante ensayos clínicos y por revisión regulatoria.
</p>

<p class="key-answer" data-question="¿Por qué no encuentro un medicamento en particular?">
Un principio activo debe poder mapearse al vocabulario de DrugBank para ser incluido en la predicción.
Los extractos de plantas, las vacunas, los excipientes y otros elementos no catalogados por DrugBank
no aparecen en esta plataforma.
</p>

---

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe es únicamente para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste su medicación por cuenta propia. Toda decisión de reposicionamiento de medicamentos requiere validación clínica completa y revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
