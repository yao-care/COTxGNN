---
layout: default
title: Evidencia Alta (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Candidatos L1-L2 de reposicionamiento de medicamentos en COTxGNN, respaldados por ensayos clínicos o revisiones sistemáticas."
---

# Evidencia Alta (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos que pueden priorizarse para evaluación clínica
</p>

---

## Criterios

| Nivel | Definición | Significado clínico |
|-------|------------|------------------|
| **L1** | Múltiples ECA de fase 3 / revisiones sistemáticas | Respaldo sólido; puede considerarse el uso clínico |
| **L2** | Un solo ECA o múltiples ensayos de fase 2 | Respaldo moderado; se pueden diseñar ensayos de validación |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe es únicamente para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste su medicación por cuenta propia. Toda decisión de reposicionamiento de medicamentos requiere validación clínica completa y revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
