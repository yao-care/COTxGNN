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

### Datos locales de este sitio

| Ítem | Detalle |
|------|---------|
| Conjunto de datos | CUM del INVIMA: vigentes (`i7cb-raxc`), en trámite de renovación (`vgr4-gemg`), otros estados (`spzp-dfuc`) y vencidos (`vwwf-4ftk`) |
| Publicador | INVIMA, portal de datos abiertos datos.gov.co |
| Descarga | <https://www.datos.gov.co/resource/i7cb-raxc.json> (los otros tres conjuntos usan la misma dirección con su identificador) |
| Identificador de producto | Número de expediente |
| Actualización | Descarga automática semanal (cada lunes); cada expediente toma el estado del INVIMA (Vigente, En trámite de renovación, Vencido, Cancelado…); un expediente que no aparece en los datos nuevos conserva su estado anterior |

Detalles: [Fuentes de Datos]({{ '/sources/' | relative_url }}).

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

### Medicamentos con mayor nivel de evidencia en este sitio

| Medicamento | Nivel de evidencia |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Fludarabine](/drugs/fludarabine/) | L1 |
| [Polidocanol](/drugs/polidocanol/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Propofol](/drugs/propofol/) | L1 |

### Medicamentos que solo cubre este sitio entre los 30 sitios TxGNN

| Medicamento | Nivel de evidencia |
|---|---|
| [Thimerosal](/drugs/thimerosal/) | L5 |

<!-- local-home:end -->

## Acerca del Desarrollador

Esta plataforma es desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.
