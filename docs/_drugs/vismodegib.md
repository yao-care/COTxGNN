---
layout: default
title: Vismodegib
parent: Solo Predicción del Modelo (L5)
nav_order: 662
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
description: "Vismodegib: nueva indicación predicha, Meduloblastoma con nodularidad extensa (nivel de evidencia L5). Indicación original: Registro INVIMA solo consigna \"Vismodegib\" como indicación (sin texto…"
monitor_inn: "VISMODEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "benign neoplasm of sweat gland"]
---

# Vismodegib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Vismodegib: De Carcinoma Basocelular Avanzado a Meduloblastoma con Nodularidad Extensa
{: .text-alpha }

## Resumen en Una Frase

Vismodegib es un inhibidor de la vía Hedgehog (bloquea la proteína Smoothened, SMO), conocido por su uso en el carcinoma basocelular avanzado. El modelo TxGNN predice que podría ser efectivo para **meduloblastoma con nodularidad extensa**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; la predicción es solo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Registro INVIMA solo consigna "Vismodegib" como indicación (sin texto descriptivo). La indicación conocida del fármaco es el carcinoma basocelular localmente avanzado o metastásico |
| Nueva Indicación Predicha | Meduloblastoma con nodularidad extensa |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Vismodegib inhibe la proteína Smoothened (SMO) de la vía de señalización Hedgehog. En el carcinoma basocelular, las mutaciones en PTCH1 o SMO activan esta vía de forma aberrante, y vismodegib la bloquea directamente. No se dispone de datos detallados de mecanismo de acción en la ficha del fármaco, pero esta descripción procede del análisis mecanístico de los datos compilados.

El meduloblastoma del subgrupo SHH, que incluye la variante desmoplásica/nodular, también depende de la señalización Hedgehog. Por eso el mecanismo es biológicamente plausible: el mismo blanco molecular que explica el efecto en el carcinoma basocelular podría ser relevante en este tumor.

Sin embargo, la plausibilidad mecanística no equivale a evidencia clínica. Para esta entidad no hay ensayos ni literatura en los datos compilados. Además, el meduloblastoma ocurre sobre todo en población pediátrica, y vismodegib se asocia con cierre prematuro de las placas de crecimiento, lo que es una preocupación de seguridad importante.

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
| 20048393 | ERIVEDGE® | Cápsula dura | Vismodegib |

El fabricante registrado es F. Hoffmann-La Roche Ltda. (Basilea, Suiza).

<!-- review:begin co-lic-20261105-vismodegib-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "(Basilea, Suiza). No hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-vismodegib-1 -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de la vía Hedgehog / SMO) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Es un fármaco con riesgo de toxicidad embriofetal (teratogénico); consultar el prospecto y seguir las normas institucionales de manejo de antineoplásicos orales |

---

## Consideraciones de Seguridad

- **Advertencias principales** (según el análisis de los datos compilados): toxicidad embriofetal (teratogenicidad), espasmos musculares, alopecia, disgeusia y pérdida de peso. En población pediátrica, riesgo de cierre prematuro de las placas de crecimiento.
- **Interacciones farmacológicas**: se registran 56 interacciones. Entre las listadas, la de mayor nivel es la de **claritromicina (moderada)**. El resto son de nivel menor e incluyen antiácidos (hidróxido de aluminio, carbonato de calcio, hidróxido de magnesio, bicarbonato de sodio), antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina) e inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, pantoprazol, rabeprazol, dexlansoprazol).

Para contraindicaciones y advertencias oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para meduloblastoma con nodularidad extensa tiene un puntaje alto en TxGNN y un mecanismo plausible, pero no cuenta con ningún ensayo clínico ni publicación (nivel L5). A esto se suman el riesgo en población pediátrica.

<!-- review:begin co-lic-20261105-vismodegib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "A esto se suman el riesgo en población pediátrica y que el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-vismodegib-2 -->

**Para avanzar se necesita:**
- Revisión de la literatura sobre inhibidores de SMO en meduloblastoma del subgrupo SHH, incluida la variante nodular/desmoplásica, y sus resultados clínicos.
- Evaluación específica del riesgo de cierre prematuro de las placas de crecimiento en población pediátrica.
- Obtener y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones.
- Confirmar la situación regulatoria y de disponibilidad en Colombia.
- Datos detallados de mecanismo de acción desde DrugBank.

<!-- review:begin co-lic-20261105-vismodegib-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Confirmar la situación regulatoria y de disponibilidad en Colombia, dado que el registro está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-vismodegib-3 -->

**Nota adicional:** entre las demás predicciones de TxGNN para este fármaco, el cáncer de piel (carcinoma basocelular) corresponde a su uso ya establecido y cuenta con ensayos y literatura. El xeroderma pigmentoso (nivel L4) tiene solo reportes de caso, que muestran viabilidad pero no eficacia ni seguridad a escala; su beneficio sería indirecto, al tratar los carcinomas basocelulares asociados.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "No hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y que el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

