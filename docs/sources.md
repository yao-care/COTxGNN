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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Colombia: qué cubren los datos locales

Datos locales: [INVIMA: Código Único de Medicamentos (CUM)](https://www.datos.gov.co/resource/i7cb-raxc.json). Los datos locales son los registros del Código Único de Medicamentos (CUM) del INVIMA publicados en datos.gov.co. Los registros en estado «Temporalmente no comercializado – Vigente» se cuentan aparte, no como vigentes comercializados.

| Concepto | Valor |
|---|---|
| Medicamentos presentes en los datos locales | {{ site.data.local_facts.licence.drugs_with_data }} |
| …con al menos un registro vigentes | {{ site.data.local_facts.licence.drugs_with_current }} |
| …con registros pero ninguno vigentes | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicamentos ausentes de los datos locales | {{ site.data.local_facts.licence.drugs_without_data }} |
| Registros locales (registros sanitarios del INVIMA (CUM)) | {{ site.data.local_facts.licence.items_total }} |
| …de ellos vigentes | {{ site.data.local_facts.licence.items_current }} |

{% if site.data.local_facts.no_current.size > 0 %}Medicamentos con registros sanitarios del INVIMA (CUM) en estos datos pero ninguno vigentes: {% for r in site.data.local_facts.no_current %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% if site.data.local_facts.no_current_more > 0 %}, y {{ site.data.local_facts.no_current_more }} más{% endif %}{% endif %}

{% if site.data.local_facts.recent_licence_reviews.size > 0 %}Últimas correcciones de datos regulatorios locales: {% for r in site.data.local_facts.recent_licence_reviews %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Panorama de las fuentes

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fuente</th><th>Se usa para</th></tr>
</thead>
<tbody>
<tr><td>Datos de registro sanitario</td><td><a href="https://www.invima.gov.co/">INVIMA</a></td><td>Medicamentos de Colombia con sus principios activos y el estado de cada registro sanitario (CUM)</td></tr>
<tr><td>Modelo de predicción</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Predicción de asociaciones entre medicamentos y enfermedades</td></tr>
<tr><td>Ensayos clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Clasificación de la evidencia (NCT)</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Clasificación de la evidencia (PMID)</td></tr>
<tr><td>Información de medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mapeo de principios activos y datos de blancos terapéuticos</td></tr>
<tr><td>Interacciones</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Datos de interacciones entre medicamentos</td></tr>
</tbody>
</table>

---

## Datos locales de este sitio

Los medicamentos de Colombia y el estado de su registro sanitario provienen del Código Único de
Medicamentos (CUM) del INVIMA, publicado como datos abiertos en datos.gov.co. El INVIMA divide el CUM en
cuatro conjuntos de datos según el estado del registro.

| Ítem | Detalle |
|------|---------|
| Conjunto de datos | CUM del INVIMA: vigentes (`i7cb-raxc`), en trámite de renovación (`vgr4-gemg`), otros estados (`spzp-dfuc`) y vencidos (`vwwf-4ftk`) |
| Publicador | INVIMA, portal de datos abiertos datos.gov.co |
| Descarga | <https://www.datos.gov.co/resource/i7cb-raxc.json> (los otros tres conjuntos usan la misma dirección con su identificador) |
| Identificador de producto | Número de expediente |
| Actualización | Descarga automática semanal (cada lunes); cada expediente toma el estado del INVIMA (Vigente, En trámite de renovación, Vencido, Cancelado…); un expediente que no aparece en los datos nuevos conserva su estado anterior |

---

## Licencias

Cada fuente tiene su propia licencia; por favor revísela antes de citar:

- **TxGNN**: uso académico; cite a Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: datos públicos de los NIH de Estados Unidos
- **DrugBank**: uso no comercial sujeto a sus términos de licencia
- **INVIMA**: sujeto a los términos de datos abiertos de la autoridad regulatoria de Colombia

---

## Frecuencia de actualización

| Datos | Frecuencia |
|------|-----------|
| CUM del INVIMA (datos.gov.co) | Semanal (cada lunes) |
| Evidencia de ensayos / literatura | Recolectada nuevamente de forma periódica |
| Datos de interacciones | Revisados trimestralmente |

---

## Citación académica

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

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
