---
layout: default
title: Methotrexate
parent: Solo Predicción del Modelo (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Metotrexato: De una Indicación No Detallada en INVIMA a Blastoma Pulmonar

## Resumen en Una Frase

El metotrexato es un antimetabolito antifolato que se usa en oncología (leucemia linfoblástica aguda, linfomas, cáncer de mama, pulmón y cabeza y cuello) y en enfermedades autoinmunes como la psoriasis grave y la artritis reumatoide. Los registros sanitarios colombianos del pack no detallan la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **blastoma pulmonar**, un tumor pulmonar raro. Por ahora hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | "METROTEXATE" (el registro solo repite el nombre del principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Blastoma pulmonar (pulmonary blastoma) |
| Puntaje de Predicción TxGNN | 99.45% (posición 4655 en el ranking global del modelo) |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el pack de evidencia. Según la información farmacológica disponible, el metotrexato inhibe la enzima dihidrofolato reductasa (DHFR) y entra a las células mediante el transportador de folato reducido 1 (SLC19A1). Al bloquear la DHFR se frena la síntesis de nucleótidos, por lo que afecta sobre todo a las células que se dividen rápido, como las tumorales.

Mecanísticamente, esa actividad antifolato podría ser aplicable a un tumor pulmonar de crecimiento rápido como el blastoma pulmonar. Sin embargo, el vínculo se apoya solo en farmacología general. No se recuperó ningún ensayo ni publicación que evalúe el metotrexato en esta enfermedad, y la relación con la indicación original no ha sido evaluada.

Por eso la predicción debe leerse como una hipótesis generada por el modelo, no como una señal clínica confirmada. El puntaje alto de TxGNN indica cercanía en el grafo de conocimiento, no eficacia demostrada.

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
| 19927154 | METOTREXATO 2.5 MG (ASOFARMA S.A.I. Y C.) | Tableta | METROTEXATE (sin texto de indicación detallado) |

Nota: los 5 registros listados en el pack son idénticos y corresponden al mismo número sanitario. El total reportado es de 20 registros. Además de la tableta oral, el pack indica que existe una forma de solución inyectable.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase antifolato; inhibidor de DHFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. Por la clase de fármaco, la mielosupresión es un riesgo conocido, pero el pack no trae datos de toxicidad |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto (depende de la dosis y la vía) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones se completó, pero devolvió 3 registros que corresponden a **dianas farmacológicas** del metotrexato y no a interacciones con otros medicamentos: transportador de folato reducido 1 (SLC19A1), dihidrofolato reductasa (DHFR) y proteína HMGB1. No hay datos de interacciones con otros fármacos.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para blastoma pulmonar es solo del modelo (L5), sin ensayos ni literatura que la respalden, y el mecanismo se basa en farmacología general. No hay base para avanzar en esta indicación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones, que hoy es un vacío bloqueante para el tamizaje de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Aclarar la indicación aprobada real en los registros colombianos, porque el texto actual solo repite el nombre del fármaco.
- Buscar casos, series o literatura específica de blastoma pulmonar.
- Evaluar por separado otras predicciones del mismo pack que tienen más respaldo:
  - Rabdomiosarcoma (L3): un ensayo de fase II con metotrexato en dosis altas en niños con enfermedad de alto riesgo (PMID 9329466).
  - Linfoma de Hodgkin (L3): uso histórico del régimen VBM. Debe ponderarse con el riesgo de trastornos linfoproliferativos asociados al metotrexato.
  - Linfoma pulmonar primario (L4): evidencia indirecta, principalmente de linfoma del sistema nervioso central.

*Este informe es solo de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

