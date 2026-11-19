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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Colombia: los datos de este sitio en cifras

Datos locales: [INVIMA: Código Único de Medicamentos (CUM)](https://www.datos.gov.co/resource/i7cb-raxc.json). Los datos locales son los registros del Código Único de Medicamentos (CUM) del INVIMA publicados en datos.gov.co. Los registros en estado «Temporalmente no comercializado – Vigente» se cuentan aparte, no como vigentes comercializados.

| Concepto | Valor |
|---|---|
| Medicamentos con informe publicado | {{ site.data.local_facts.drugs_total }} |
| Medicamentos presentes en los datos locales | {{ site.data.local_facts.licence.drugs_with_data }} |
| …con al menos un registro vigentes | {{ site.data.local_facts.licence.drugs_with_current }} |
| …con registros pero ninguno vigentes | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicamentos ausentes de los datos locales | {{ site.data.local_facts.licence.drugs_without_data }} |
| Registros locales (registros sanitarios del INVIMA (CUM)) | {{ site.data.local_facts.licence.items_total }} |
| …de ellos vigentes | {{ site.data.local_facts.licence.items_current }} |
| Entradas del registro de revisiones | {{ site.data.local_facts.reviews.records }} |
| Páginas con entradas de revisión | {{ site.data.local_facts.reviews.public_pages_with_records }} |
| Pares medicamento–enfermedad predichos que no figuran en ningún otro sitio TxGNN | {{ site.data.local_facts.cross.unique_pairs }} |

{% if site.data.local_facts.top_licensed.size > 0 %}Medicamentos con más registros sanitarios del INVIMA (CUM) vigentes: {% for r in site.data.local_facts.top_licensed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Últimas correcciones del registro de revisiones: {% for r in site.data.local_facts.recent_reviews limit: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Ejemplos de predicciones que ningún otro sitio TxGNN incluye para el mismo medicamento: [Thimerosal]({{ '/drugs/thimerosal/' | relative_url }}) → hypotrichosis simplex of the scalp.

<!-- local-facts:end -->

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

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Acerca del Desarrollador

Esta plataforma la desarrolla y opera **藥提醒科技有限公司** (yao.care, registro 83620786, Taichung, Taiwán) como uno de los 30 sitios por país y región de su línea de productos TxGNN ([presentación del producto](https://www.yao.care/medical/txgnn/)).

---

## El método en breve

Las predicciones provienen de TxGNN, un modelo de redes neuronales de grafos del Zitnik Lab de la Facultad de Medicina de Harvard (Huang et al., *Nature Medicine* 2024, [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)); cada indicación predicha se clasifica de L1 a L5 con ClinicalTrials.gov y PubMed. Modelo, niveles y reglas: [Metodología]({{ '/methodology/' | relative_url }}). Conjuntos de datos, descargas y licencias: [Fuentes de Datos]({{ '/sources/' | relative_url }}).
<!-- local-condensed:end -->

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
