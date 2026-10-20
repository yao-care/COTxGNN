---
layout: default
title: Vismodegib
parent: Solo Predicción del Modelo (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vismodegib: nueva indicación predicha, Meduloblastoma con nodularidad extensa (nivel de evidencia L5). Indicación original: Registro INVIMA solo consigna \"Vismodegib\" como indicación (sin texto…"
monitor_inn: "VISMODEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "prostate cancer/brain cancer susceptibility", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "benign neoplasm of sweat gland"]
---

# Vismodegib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Vismodegib: De Carcinoma Basocelular Avanzado a Meduloblastoma con Nodularidad Extensa

## Resumen en Una Frase

Vismodegib es un inhibidor de la vía Hedgehog (bloquea la proteína Smoothened, SMO), conocido por su uso en el carcinoma basocelular avanzado. El modelo TxGNN predice que podría ser efectivo para **meduloblastoma con nodularidad extensa**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; la predicción es solo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Registro INVIMA solo consigna "Vismodegib" como indicación (sin texto descriptivo). La indicación conocida del fármaco es el carcinoma basocelular localmente avanzado o metastásico |
| Nueva Indicación Predicha | Meduloblastoma con nodularidad extensa |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
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
| 20048393 (cancelado) | ERIVEDGE® | Cápsula dura | Vismodegib |

El fabricante registrado es F. Hoffmann-La Roche Ltda. (Basilea, Suiza). No hay registros vigentes en Colombia.

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
La predicción para meduloblastoma con nodularidad extensa tiene un puntaje alto en TxGNN y un mecanismo plausible, pero no cuenta con ningún ensayo clínico ni publicación (nivel L5). A esto se suman el riesgo en población pediátrica y que el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Revisión de la literatura sobre inhibidores de SMO en meduloblastoma del subgrupo SHH, incluida la variante nodular/desmoplásica, y sus resultados clínicos.
- Evaluación específica del riesgo de cierre prematuro de las placas de crecimiento en población pediátrica.
- Obtener y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones.
- Confirmar la situación regulatoria y de disponibilidad en Colombia, dado que el registro está cancelado.
- Datos detallados de mecanismo de acción desde DrugBank.

**Nota adicional:** entre las demás predicciones de TxGNN para este fármaco, el cáncer de piel (carcinoma basocelular) corresponde a su uso ya establecido y cuenta con ensayos y literatura. El xeroderma pigmentoso (nivel L4) tiene solo reportes de caso, que muestran viabilidad pero no eficacia ni seguridad a escala; su beneficio sería indirecto, al tratar los carcinomas basocelulares asociados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

