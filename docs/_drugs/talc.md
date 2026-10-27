---
layout: default
title: Talc
parent: Evidencia Moderada (L3-L4)
nav_order: 603
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Talc: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L4). Indicación original: CLINDAMICINA"
monitor_inn: "talc"
predicted_indications: ["thrombotic disease", "exostosis", "rheumatoid arthritis", "bronchitis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "vein disease", "fibromyalgia", "myositis fibrosa"]
---

# Talc
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Talco: De Clindamicina (registro sanitario) a Enfermedad Trombótica
{: .text-alpha }

## Resumen en Una Frase

El registro sanitario colombiano asociado a este candidato corresponde a un producto de clindamicina en cápsulas (cuyo registro está cancelado), aunque el principio activo identificado en los datos es el talco. El modelo TxGNN predice que podría ser efectivo para la **enfermedad trombótica**, pero **no hay ensayos clínicos** y las 11 publicaciones recuperadas describen al talco como causa de daño trombótico y embólico, no como tratamiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLINDAMICINA (texto del registro; no describe una indicación clínica específica) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del talco en los datos compilados para este informe. Además, el único registro sanitario local corresponde a clindamicina, un antibiótico, y no guarda relación evidente con el talco ni con la enfermedad trombótica.

La literatura recuperada indica que el talco **causa** enfermedad trombótica y embólica, no que la trate. El talco inyectado por vía intravenosa (por ejemplo, en tabletas trituradas usadas por personas que consumen drogas) produce granulomatosis pulmonar, hipertensión pulmonar angiotrombótica y microembolización retiniana y cerebral. La dirección del efecto es dañina.

El alto puntaje del modelo probablemente es un artefacto de proximidad en la red de conocimiento: el talco se asocia con patología vascular y pleural, pero esa asociación no implica beneficio terapéutico. Por ello, el reposicionamiento no está respaldado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Revisión | Current Opinion in Oncology | Complicaciones intratorácicas del cáncer; el síndrome de vena cava superior por trombosis aumenta con los catéteres venosos |
| [41646593](https://pubmed.ncbi.nlm.nih.gov/41646593/) | 2026 | Reporte de caso | Cureus | Neumotórax recurrente tras neumonectomía manejado con soporte ECMO |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Reporte de caso | Archives of Neurology | Síndrome medular medial con infartos y granulomatosis sistémica por talco en una consumidora de drogas |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Reporte de caso | Texas Heart Institute Journal | Síndrome de Trousseau con neoplasia oculta de colon y síndrome de Lynch |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Observacional | International Ophthalmology | Zona avascular foveal ampliada en oclusión de rama venosa; se menciona la retinopatía por talco |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Reporte de caso | Arch Pathol Lab Med | Embolia pulmonar y granulomatosis por celulosa inyectada; la lesión vascular principal es la trombosis |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Serie de casos | J Can Assoc Radiol | Granulomatosis por talco e hipertensión pulmonar angiotrombótica en adictos |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Reporte de caso | Am J Med Sci | Microembolización retiniana y cerebral por talco |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Serie de casos | Rev Clin Esp | Granulomatosis pulmonar angiotrombótica en usuarios de drogas intravenosas; el talco provoca fenómenos trombóticos |
| [8010794](https://pubmed.ncbi.nlm.nih.gov/8010794/) | 1994 | Serie de casos | Ann Thorac Surg | Cirugía toracoscópica para quilotórax (tangencial a la indicación) |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20270123 | CLINDAMICINA 300 MG CÁPSULA | Cápsula dura | CLINDAMICINA | Cancelado |

## Consideraciones de Seguridad

- **Daño documentado en la literatura**: el talco por vía intravenosa se asocia con granulomatosis pulmonar, hipertensión pulmonar angiotrombótica y microembolización retiniana y cerebral. Los hallazgos respiratorios por inhalación (bronquitis, estenosis de vía aérea) también son relevantes para otras indicaciones predichas.

Para advertencias, contraindicaciones e interacciones del producto registrado, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura disponible muestra que el talco es causa de eventos trombóticos y embólicos, por lo que el puntaje de 99.85% parece un artefacto del modelo. Las demás indicaciones predichas (exostosis, artritis reumatoide, bronquitis, deficiencias de factores de coagulación, enfermedad venosa, fibromialgia, miositis fibrosa) tampoco cuentan con evidencia terapéutica; en bronquitis y enfermedad venosa la evidencia apunta a daño.

**Para avanzar se necesita:**
- Aclarar la inconsistencia entre el principio activo (talco) y el registro sanitario asociado (clindamicina).
- Datos del mecanismo de acción desde DrugBank.
- Prospecto del INVIMA con advertencias y contraindicaciones.
- Evidencia clínica o preclínica que demuestre un efecto terapéutico, no dañino, en la indicación propuesta; de lo contrario, descartar el candidato.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

