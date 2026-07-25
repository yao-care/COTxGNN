---
layout: default
title: Solo Predicción del Modelo (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidatos L5 en COTxGNN: solo predicción del modelo, aún sin evidencia clínica ni de literatura."
---

# Solo Predicción del Modelo (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos con solo predicción del modelo y aún sin evidencia en humanos
</p>

---

## Criterios

| Nivel | Definición | Significado clínico |
|-------|------------|------------------|
| **L5** | Solo predicción del modelo | Etapa de hipótesis; aún sin evidencia en humanos |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }} medicamentos)

| Medicamento | Indicaciones | Enlace |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver informe]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe es únicamente para referencia de investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste su medicación por cuenta propia. Toda decisión de reposicionamiento de medicamentos requiere validación clínica completa y revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
