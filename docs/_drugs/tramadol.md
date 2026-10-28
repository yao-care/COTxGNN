---
layout: default
title: Tramadol
parent: Solo Predicción del Modelo (L5)
nav_order: 634
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Tramadol: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Tramadol"
monitor_inn: "TRAMADOL"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
---

# Tramadol
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

## Tramadol: De Analgésico Opioide a Displasia acromesomélica, tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Tramadol es un analgésico opioide, registrado en Colombia solo o combinado con diclofenaco y en una asociación con paracetamol, para el tratamiento del dolor.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tramadol (registros de tramadol solo, tramadol + diclofenaco y asociación con paracetamol) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tramadol es un analgésico que actúa como agonista de receptores opioides mu e inhibidor de la recaptación de monoaminas (serotonina y noradrenalina), y su utilidad en el dolor está establecida.

La displasia acromesomélica tipo Hunter-Thompson es una enfermedad esquelética rara causada por mutaciones con pérdida de función en CDMP1/GDF5. Tramadol no actúa sobre la vía de señalización GDF5/BMP, por lo que **no se identifica un vínculo mecanístico creíble** entre el fármaco y la enfermedad.

El puntaje alto de TxGNN refleja una predicción del modelo TxGNN (aprendizaje profundo), probablemente por vecinos de red compartidos relacionados con el dolor o el sistema esquelético. Sin ensayos ni literatura, esta predicción no tiene respaldo clínico. En el mejor de los casos, tramadol podría ofrecer alivio sintomático del dolor, no modificación de la enfermedad.

Otras predicciones del modelo (por ejemplo, braquiolmia, pseudoacondroplasia, artritis idiopática juvenil y espondiloartropatía) tampoco muestran vínculos mecanísticos directos; en el mejor de los casos, solo una justificación sintomática indirecta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal. (Para otra indicación predicha, la artritis idiopática juvenil, se recuperó una revisión sobre ketoprofeno pediátrico, que no aporta evidencia directa sobre tramadol.)

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20080775 | TRAMASINDOL® 100 MG/ML SOLUCIÓN ORAL | Solución oral | Tramadol (vigente) |
| 20154923 | DICLOFENACO SÓDICO / TRAMADOL HCL 25 MG/25 MG | Tableta recubierta | Tramadol y diclofenaco (vigente) |
| 19948799 | FASTFEN JARABE | Jarabe | Paracetamol, combinaciones excluyendo sicolépticos (vigente) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión, insuficiencia hepática, enfermedad hepática y cirrosis, epilepsia, trastornos de ansiedad, abuso de sustancias y dependencia, síndrome de abstinencia (incluido el alcohólico), insuficiencia respiratoria, intoxicación por paracetamol, síndrome serotoninérgico, hipertensión intracraneal y pseudotumor cerebral, diabetes y cetoacidosis diabética, hiperlipidemia, enfermedad de la vesícula biliar, síndrome de Wernicke-Korsakoff, e infecciones del sistema nervioso central.
- **Interacciones farmacológicas:** se identificaron 100 interacciones; entre las de nivel **mayor** figuran alvimopán, bupropión, cisaprida, dexfenfluramina, dietilpropión, dolasetrón, dronabinol, efedrina y fenfluramina. Entre las de nivel moderado figuran atropina, bisacodilo, cimetidina, claritromicina, famotidina y eliglustat.
- **Consideración pediátrica:** el uso de opioides en niños conlleva riesgos, como la variabilidad de CYP2D6 y la depresión respiratoria.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, ya que no se dispone de ellas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico creíble entre tramadol y la displasia acromesomélica tipo Hunter-Thompson. Además, el fármaco no tiene registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia preclínica que conecte tramadol con la vía GDF5/BMP (hoy no existe).
- Obtener el prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Aclarar la situación regulatoria, ya que los 3 registros están cancelados.
- Considerar otras indicaciones predichas con posible beneficio sintomático (por ejemplo, dolor en artritis idiopática juvenil o espondiloartropatía), con evaluación de seguridad específica, sobre todo en población pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

