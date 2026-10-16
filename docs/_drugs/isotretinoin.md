---
layout: default
title: Isotretinoin
parent: Solo Predicción del Modelo (L5)
nav_order: 359
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isotretinoin: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: ISOTETRINOINA"
---

# Isotretinoin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Isotretinoína: De Isotretinoína (indicación no detallada en el registro) a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Isotretinoína es un retinoide que figura en registros sanitarios de Colombia, aunque el texto de indicación del registro solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ISOTETRINOINA (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.01% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Isotretinoína es un retinoide que actúa a través de los receptores del ácido retinoico, los cuales regulan la diferenciación celular. Esta información proviene del conocimiento general sobre la clase y no de los datos suministrados.

De forma hipotética, la modulación retinoide podría influir en la biología renal y vascular (por ejemplo, remodelado vascular, expresión de renina o lesión glomerular y de podocitos, con hallazgos preclínicos reportados). Ninguno de estos vínculos está respaldado por evidencia incluida en este informe.

También conviene señalar que la segunda predicción del modelo, **hipertensión renovascular maligna**, tiene exactamente el mismo puntaje (99.01%). Esto sugiere que ambas provienen de una misma ruta de inferencia en el grafo de conocimiento (probablemente a través de un nodo relacionado con la enfermedad renal hipertensiva) y no de evidencia independiente. No se ha determinado la similitud entre la indicación original y la nueva, ni la compatibilidad de vías de administración.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002702 | DERMALONA 20 MG CÁPSULA BLANDA | Cápsula blanda | ISOTETRINOINA |
| 19993476 | HYNDRIAX 20 MG CÁPSULAS | Cápsula blanda | ISOTETRINOINA |
| 19970684 | ISOTRETINOINA 20 MG | Cápsula blanda | ISOTETRINOINA |

Los tres registros corresponden a productos de un solo principio activo y todos figuran como cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto de prospecto): trastornos de ansiedad, trastornos neuróticos y distímicos, trastornos psicóticos y mentales (incluyendo esquizoafectivo y esquizofreniforme), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, pancreatitis, angioedema (adquirido, hereditario y otras formas), enfermedad inflamatoria intestinal, osteoporosis (incluida la posmenopáusica), lupus eritematoso sistémico, diabetes mellitus y cetoacidosis diabética, deficiencia de potasio, neutropenia, agranulocitosis, trastornos hipotensivos y piuria ureteral. Es especialmente relevante la **enfermedad renal**, dada la población objetivo de la nueva indicación.
- **Interacciones farmacológicas**: se identificaron 98 interacciones en total. Las de nivel **mayor** incluyen:
  - Doxiciclina, minociclina y tetraciclina
  - Vitamina A

  Entre las de nivel moderado figuran corticosteroides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triamcinolona), warfarina, dicumarol, etanol, naltrexona, nitisinona, fostamatinib, ivacaftor, lumacaftor y abametapir.
- **Otras consideraciones** (conocimiento general de la clase, no de los datos compilados): isotretinoína es fuertemente teratogénica y puede elevar los lípidos y afectar la presión arterial, lo que genera preocupación en esta población.

Consultar el prospecto para advertencias y contraindicaciones oficiales, ya que no se dispone de ellas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el perfil de seguridad (teratogenicidad, contraindicación renal en el grafo, 98 interacciones) y la ausencia de registros vigentes en Colombia desaconsejan avanzar a corto plazo.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank y analizar el vínculo mecanístico con la enfermedad renal hipertensiva.
- Descargar y analizar el prospecto del INVIMA para obtener advertencias y contraindicaciones oficiales (brecha de seguridad bloqueante).
- Realizar una revisión sistemática de la literatura y de registros de ensayos clínicos sobre retinoides en enfermedad renal o hipertensión maligna.
- Evaluar estudios preclínicos que respalden el vínculo mecanístico.
- Determinar la similitud con la indicación original y la compatibilidad de vías de administración.
- Aclarar la situación regulatoria: no hay registros vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

