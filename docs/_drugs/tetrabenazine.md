---
layout: default
title: Tetrabenazine
parent: Solo Predicción del Modelo (L5)
nav_order: 620
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Tetrabenazine: nueva indicación predicha, Enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística (nivel de evidencia L5). Indicación original: Tetrabenazina"
monitor_inn: "Tetrabenazine"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
---

# Tetrabenazine
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

## Tetrabenazina: De Tetrabenazina (indicación registrada sin detalle) a Enfermedad Renal Poliquística tipo 3 con o sin Enfermedad Hepática Poliquística
{: .text-alpha }

## Resumen en Una Frase

Tetrabenazina es un inhibidor del transportador vesicular de monoaminas (VMAT), usado principalmente para tratar trastornos hipercinéticos como la corea de la enfermedad de Huntington, el síndrome de Tourette y la discinesia tardía.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tetrabenazina (el registro sanitario no detalla la indicación; el uso clínico conocido es el de trastornos hipercinéticos) |
| Nueva Indicación Predicha | Enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, la tetrabenazina es un inhibidor reversible de VMAT2 que agota las monoaminas presinápticas (dopamina, serotonina, noradrenalina). Los datos de farmacología también registran su unión a VMAT1 (SLC18A1) y VMAT2 (SLC18A2).

**Honestamente, no se identifica un vínculo mecanístico plausible.** La enfermedad renal poliquística y la enfermedad hepática poliquística se asocian con genes ciliares y del retículo endoplásmico (por ejemplo, GANAB), sin relación conocida con el transporte de monoaminas. El puntaje alto (0.9990) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no está respaldado por ensayos ni literatura. La similitud con la indicación original (trastornos del movimiento) no ha sido evaluada.

Las otras predicciones del modelo (displasia renal-hepática-pancreática, síndrome de Joubert con defecto renal, nefritis intersticial cariomegálica, porfiria aguda intermitente, entre otras) presentan el mismo patrón: puntajes altos, sin evidencia clínica y sin conexión mecanística conocida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20034891 | TETMODIS | Tableta | Tetrabenazina |
| 20203198 | TETRABEX® | Tableta recubierta | Tetrabenazina |

Ningún registro se encuentra vigente actualmente.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): enfermedad de Parkinson y trastornos parkinsonianos, síndrome de QT largo (incluida la forma familiar) y torsades de pointes, hipotensión ortostática e hipotensión, atrofia multisistémica, síndrome de taquicardia postural ortostática, trastornos de ansiedad, trastorno neurótico, trastorno distímico, enfermedad hepática, enfermedad de la vesícula biliar, acatisia inducida por fármacos, discinesia tardía y discinesia linguo-facio-bucal, e hiperprolactinemia (incluidas formas familiar, adquirida y por tumor hipofisario productor de prolactina).
- **Interacciones farmacológicas**: no se identificaron interacciones fármaco-fármaco con nivel de gravedad; solo se registró la actividad sobre los transportadores VMAT1 y VMAT2.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.
- Para la porfiria aguda intermitente, el metabolismo hepático de la tetrabenazina (CYP2D6) y su seguridad en esa condición no están caracterizados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en un puntaje del modelo, sin ensayos clínicos, sin literatura y sin vínculo mecanístico plausible. Además, el perfil de seguridad incluye numerosas condiciones de riesgo, incluidas hepáticas.

<!-- review:begin co-lic-20261105-tetrabenazine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los dos registros sanitarios en Colombia están cancelados y el perfil de seguridad incluye numerosas condiciones de riesgo, incluidas hepáticas." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-tetrabenazine-2 -->

**Para avanzar se necesita:**
- Obtener datos del mecanismo de acción y evaluar si existe alguna hipótesis biológica que conecte VMAT2 con la patogenia de la enfermedad renal poliquística.
- Estudios preclínicos que respalden la hipótesis.
- Obtener y revisar el prospecto oficial (advertencias y contraindicaciones) del INVIMA.
- Revisión de seguridad hepática y cardiaca (QT) antes de considerar cualquier uso en poblaciones con enfermedad renal o hepática.

<!-- review:begin co-lic-20261031-tetrabenazine-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria (registros cancelados) y la disponibilidad real del producto en Colombia. / Revisión de seguridad hepática y cardiaca (QT) antes de considerar cualquier uso en poblaciones con enfermedad renal o hepática." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-tetrabenazine-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registros cancelados) y la disponibilidad real del producto en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "los dos registros sanitarios en Colombia están cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

