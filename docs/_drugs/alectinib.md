---
layout: default
title: Alectinib
parent: Solo Predicción del Modelo (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alectinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: ALECTINIB"
---

# Alectinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Alectinib: De Alectinib (indicación no detallada en el registro) a Fibromatosis Gingival

## Resumen en Una Frase

Alectinib es un inhibidor de la quinasa del linfoma anaplásico (ALK), conocido por su uso en el cáncer de pulmón de células no pequeñas ALK positivo; el registro sanitario colombiano solo menciona "ALECTINIB" como indicación.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ALECTINIB (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, alectinib es un inhibidor selectivo de ALK, utilizado en el cáncer de pulmón de células no pequeñas con reordenamiento de ALK, donde ensayos de Fase 3 han demostrado su eficacia.

Para la fibromatosis gingival no se ha establecido ningún mecanismo relacionado con ALK. La puntuación elevada de TxGNN proviene de relaciones en un grafo de conocimiento y no está respaldada por ensayos ni literatura. La similitud con la indicación original no ha sido evaluada.

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
| 20157000 (cancelado) | ALECENSA | Cápsula dura | ALECTINIB |

Fabricante: F. Hoffmann-La Roche Ltd., Basilea, Suiza. No hay registros vigentes en Colombia.

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
La predicción para fibromatosis gingival se basa solo en el modelo, sin ensayos, literatura ni vínculo mecanístico con la inhibición de ALK (Nivel L5). Además, el producto no tiene registro vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y una hipótesis biológica que relacione ALK con la fibromatosis gingival
- Estudios preclínicos que sustenten la hipótesis
- Prospecto de INVIMA con advertencias y contraindicaciones, y confirmación de la situación regulatoria actual
- Evaluación de la viabilidad de la vía de administración y la relación riesgo-beneficio en una enfermedad benigna

---

### Nota sobre otras predicciones

El mayor respaldo aparece en "neoplasia benigna de pulmón" (puesto 5; L1, con ensayos de Fase 3 ALEX, J-ALEX y ALINA). Sin embargo, esa evidencia corresponde al cáncer de pulmón de células no pequeñas ALK positivo, que es la indicación ya establecida del fármaco. Por tanto, no constituye reposicionamiento ni respalda tumores benignos. Entre las demás predicciones, "tumor de células germinales de pulmón" (puesto 7) solo cuenta con un ensayo de Fase 2 terminado con 1 participante y reportes de casos de tumores neuroendocrinos con fusión ALK, lo que sugiere una línea de investigación basada en biomarcadores, aún sin evidencia de eficacia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

