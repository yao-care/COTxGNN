---
layout: default
title: Alectinib
parent: Solo Predicción del Modelo (L5)
nav_order: 34
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Alectinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: ALECTINIB"
monitor_inn: "ALECTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Alectinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Alectinib: De Alectinib (indicación no detallada en el registro) a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Alectinib es un inhibidor de la quinasa del linfoma anaplásico (ALK), conocido por su uso en el cáncer de pulmón de células no pequeñas ALK positivo; el registro sanitario colombiano solo menciona "ALECTINIB" como indicación.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ALECTINIB (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, alectinib es un inhibidor selectivo de ALK, utilizado en el cáncer de pulmón de células no pequeñas con reordenamiento de ALK, donde ensayos de Fase 3 han demostrado su eficacia.

Para la fibromatosis gingival no se ha establecido ningún mecanismo relacionado con ALK. La puntuación elevada de TxGNN proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; tampoco está respaldada por ensayos ni literatura. La similitud con la indicación original no ha sido evaluada.

**Conclusión:** la predicción es hipotética y no tiene sustento mecanístico ni clínico en este momento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20157000 | ALECENSA | Cápsula dura | ALECTINIB |

Fabricante: F. Hoffmann-La Roche Ltd., Basilea, Suiza.

<!-- review:begin co-lic-20261105-alectinib-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Hoffmann-La Roche Ltd., Basilea, Suiza. No hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-alectinib-1 -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. La literatura describe casos de anemia hemolítica asociada a alectinib. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, perfil lipídico (se han descrito casos de hipertrigliceridemia con pancreatitis), peso y monitoreo cardíaco según criterio clínico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron **92 interacciones** registradas. Entre las más relevantes:
  - **Mayor:** ácido aminolevulínico.
  - **Moderadas:** dolasetrón, naltrexona, edrofonio, fisostigmina, mefloquina, quinina, metoxaleno, acebutolol, ambenonio, asparaginasa (*Erwinia chrysanthemi* y *E. coli*), atazanavir, atenolol, bedaquilina, betaxolol y bisoprolol, entre otras.
- **Señales de seguridad en la literatura (reportes de casos):** pancreatitis por hipertrigliceridemia, anemia hemolítica, síndrome DRESS, eritema multiforme, aumento de peso significativo y síndrome de lisis tumoral (con otro inhibidor de ALK).

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fibromatosis gingival se basa solo en el modelo, sin ensayos, literatura ni vínculo mecanístico con la inhibición de ALK (Nivel L5).

<!-- review:begin co-lic-20261105-alectinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para fibromatosis gingival se basa solo en el modelo, sin ensayos, literatura ni vínculo mecanístico con la inhibición de ALK (Nivel L5). Además, el producto no tiene registro vigente en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-alectinib-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y una hipótesis biológica que relacione ALK con la fibromatosis gingival
- Estudios preclínicos que sustenten la hipótesis
- Prospecto de INVIMA con advertencias y contraindicaciones, y confirmación de la situación regulatoria actual
- Evaluación de la viabilidad de la vía de administración y la relación riesgo-beneficio en una enfermedad benigna

---

### Nota sobre otras predicciones

El mayor respaldo aparece en "neoplasia benigna de pulmón" (puesto 5; L1, con ensayos de Fase 3 ALEX, J-ALEX y ALINA). Sin embargo, esa evidencia corresponde al cáncer de pulmón de células no pequeñas ALK positivo, que es la indicación ya establecida del fármaco. Por tanto, no constituye reposicionamiento ni respalda tumores benignos. Entre las demás predicciones, "tumor de células germinales de pulmón" (puesto 7) solo cuenta con un ensayo de Fase 2 terminado con 1 participante y reportes de casos de tumores neuroendocrinos con fusión ALK, lo que sugiere una línea de investigación basada en biomarcadores, aún sin evidencia de eficacia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "No hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el producto no tiene registro vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

