---
layout: default
title: Methotrexate
parent: Solo Predicción del Modelo (L5)
nav_order: 435
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Methotrexate: nueva indicación predicha, Pulmonary blastoma (nivel de evidencia L5). Indicación original: METROTEXATE"
---

# Methotrexate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Methotrexate: Pulmonary blastoma
{: .text-alpha }

## Resumen en Una Frase

El metotrexato es un antifolato.
El modelo TxGNN predice que podría ser efectivo para **blastoma pulmonar**, pero para esta predicción principal **no hay ensayos clínicos ni publicaciones** que la respalden.
Entre las demás predicciones, las que cuentan con más soporte son el **rabdomiosarcoma** y el **linfoma de Hodgkin**, descritas más abajo.

<!-- review:begin co-lic-20261105-methotrexate-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El metotrexato es un antifolato que en Colombia tuvo registros sanitarios (hoy cancelados), sin que el texto de indicación aprobada detalle un uso específico más allá del nombre del producto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-methotrexate-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METROTEXATE |
| Nueva Indicación Predicha | Pulmonary blastoma |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 9 de 12) |
| Número de Registros Sanitarios | 12 (vigentes: 9) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el metotrexato es un antifolato que inhibe la enzima dihidrofolato reductasa (DHFR) y, a través del transportador de folato reducido 1 (SLC19A1), afecta la síntesis de ADN en células de proliferación rápida. Se usa en leucemia linfoblástica aguda, linfomas, cáncer de mama, pulmón y de cabeza y cuello, así como en psoriasis y artritis reumatoide.

La relación con el blastoma pulmonar es solo especulativa: es un tumor proliferativo de tipo blastomatoso en el que un antifolato podría actuar, pero no existen ensayos ni literatura que lo respalden. La puntuación alta del modelo (0.9945) es únicamente una predicción computacional.

Como contexto, otras predicciones del modelo tienen respaldo indirecto más sólido. Para linfoma pulmonar primario, el metotrexato a dosis altas es parte de esquemas de linfoma (en especial linfoma primario del SNC). Para rabdomiosarcoma existe un ensayo de Fase 2 de metotrexato a dosis altas en niños y adolescentes. Para linfoma de Hodgkin existe el esquema histórico VBM (vinblastina, bleomicina, metotrexato).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para blastoma pulmonar.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para blastoma pulmonar.

<!-- review:begin co-lic-20261105-methotrexate-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "No hay registros vigentes actualmente." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-methotrexate-2 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19927154 | METOTREXATO 2.5 MG (ASOFARMA S.A.I. Y C.) | Tableta | METROTEXATE | Vigente |
| 20243244 | METREXATO® 50 MG/2 ML (BLAU FARMACÉUTICA COLOMBIA S.A.S.) | Solución inyectable | METROTEXATE | Temp. no comerc - Vigente |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, antagonista del folato) |
| Riesgo de Mielosupresión | Alto (las condiciones de leucopenia, trombocitopenia y anemia figuran entre las contraindicaciones del grafo de conocimiento) |
| Clasificación de Emetogenicidad | Baja a moderada a dosis bajas; moderada a alta a dosis altas |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, niveles séricos de metotrexato en esquemas de dosis altas, función pulmonar si hay síntomas respiratorios |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad renal, enfermedad de la vesícula biliar, úlcera gástrica y enfermedad ulcerosa péptica, trombocitopenia, leucopenia, anemia (incluida la macrocítica), enfermedad pulmonar intersticial, fibrosis pulmonar (incluida la posinflamatoria), colitis ulcerosa y enfermedad inflamatoria intestinal, estomatitis, abuso o dependencia de sustancias, piuria y enfermedades del sistema inmunitario.
- **Interacciones farmacológicas (blancos farmacológicos):** transportador de folato reducido 1 (SLC19A1), dihidrofolato reductasa (DHFR) y proteína HMGB1. No se dispone de interacciones con otros medicamentos.
- **Linfoproliferación asociada a metotrexato:** la literatura recopilada describe trastornos linfoproliferativos asociados a su uso, relevante sobre todo en el contexto de linfoma.

No se dispone de las advertencias y contraindicaciones del prospecto de INVIMA; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para blastoma pulmonar solo existe la predicción del modelo (L5), sin ensayos ni literatura.

<!-- review:begin co-lic-20261105-methotrexate-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Para blastoma pulmonar solo existe la predicción del modelo (L5), sin ensayos ni literatura, y además el producto no tiene registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-methotrexate-3 -->

**Para avanzar se necesita:**
- Revisar otras predicciones con mejor respaldo, en particular rabdomiosarcoma (L2, con un ensayo de Fase 2 publicado, 1997), linfoma de Hodgkin (L3) y linfoma pulmonar primario (L4), todas con evidencia indirecta o histórica.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), brecha de datos bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: los dos y el texto de indicación aprobada es poco informativo.
- Definir la compatibilidad de vías de administración, hoy pendiente.
- Realizar estudios preclínicos o series de casos específicos antes de considerar cualquier uso en blastoma pulmonar.

<!-- review:begin co-lic-20261105-methotrexate-4 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria: los dos registros están cancelados y el texto de indicación aprobada es poco informativo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 9); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-methotrexate-4 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "que en Colombia tuvo registros sanitarios (hoy cancelados), sin que el texto de indicación aprobada detalle un uso específico más allá del n" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "No hay registros vigentes actualmente" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y además el producto no tiene registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

