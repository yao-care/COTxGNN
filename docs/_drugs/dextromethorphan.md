---
layout: default
title: Dextromethorphan
parent: Solo Predicción del Modelo (L5)
nav_order: 215
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Dextromethorphan: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L5). Indicación original: Tos (supresores y expectorantes)"
monitor_inn: "Dextromethorphan"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Dextrometorfano: De Tos (Supresores y Expectorantes) a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

Dextrometorfano es un antitusígeno de acción central, registrado en Colombia para el tratamiento de la tos (supresores y expectorantes).
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tos (supresores y expectorantes) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 15) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para dextromethorphan hydrobromide, bupropion hydrochloride (combinación que contiene Dextromethorphan) (traducción no oficial): «Dextrometorfano es un antagonista no competitivo del receptor NMDA (un receptor ionotrópico de glutamato) y un agonista del receptor sigma-1. El mecanismo de dextrometorfano en el tratamiento del TDM y de la agitación asociada a la demencia debida a la enfermedad de Alzheimer no está claro.» Texto original en inglés: "Dextromethorphan is an uncompetitive antagonist of the NMDA receptor (an ionotropic glutamate receptor) and a sigma-1 receptor agonist. The mechanism of dextromethorphan in the treatment of MDD and agitation associated with dementia due to Alzheimer’s disease is unclear." ([DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79), versión del 2026-08-17; consultado el 2026-11-19). Según la información conocida, el dextrometorfano actúa de forma central como antitusígeno (antagonista del receptor NMDA y agonista del receptor sigma-1). Los datos farmacológicos compilados muestran afinidad por el receptor sigma-1 (SIGMAR1), por la subunidad GluN2C del receptor NMDA y por el receptor del gusto amargo TAS2R1.

La relación entre la indicación original (tos) y la nueva (enfermedad de la cavidad nasal) es de cercanía anatómica y sintomática dentro de las vías respiratorias superiores. Sin embargo, el mecanismo del fármaco no tiene un vínculo establecido con la patología nasal.

La puntuación alta proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Por ello, el mecanismo no puede considerarse verificado para esta indicación.

Otras predicciones del modelo, todas de nivel L5 y sin ensayos ni literatura, son:

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Laringofaringitis aguda | 0.9998 | Solapamiento sintomático plausible (alivio de la tos), pero es manejo sintomático de la indicación original, no un reposicionamiento real |
| Difteria faucial | 0.9936 | Infección mediada por toxina; el fármaco no tiene mecanismo antibacteriano ni antitoxina |
| Cefalea autonómica trigeminal | 0.9932 | Racional especulativo basado en antagonismo NMDA y sensibilización central |
| Trastorno degenerativo del disco cervical | 0.9930 | Vínculo débil e indirecto; podría influir en el dolor, no en la degeneración |
| Urticaria alérgica | 0.9925 | Mediada por histamina y mastocitos; el fármaco puede liberar histamina, lo que sugiere que no habría beneficio |

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20116677 | NOGLUPEC® JARABE | Jarabe | TOS SUPRESORES Y EXPECTORANTES |

## Consideraciones de Seguridad

- **Enfermedades con contraindicación o precaución según el grafo de conocimiento** (derivadas de relaciones fármaco-enfermedad del grafo PrimeKG, no del texto del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia hepática y enfermedad hepática, epilepsia, enfermedad pulmonar obstructiva crónica, bronquitis, úlcera gástrica y péptica, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, trombocitopenia, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, enfermedad inflamatoria intestinal, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, trastornos hipotensivos, entre otras.
- **Interacciones farmacológicas**: los datos disponibles corresponden a interacciones con dianas farmacológicas (GluN2C, TAS2R1 y SIGMAR1), no a interacciones con otros medicamentos.

Para las advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones carecen de ensayos clínicos y de literatura, y el nivel de evidencia es L5. Además, el vínculo mecanístico con la enfermedad de la cavidad nasal no está respaldado.

<!-- review:begin co-lic-20261105-dextromethorphan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el vínculo mecanístico con la enfermedad de la cavidad nasal no está respaldado, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dextromethorphan-1 -->

**Para avanzar se necesita:**
- Búsqueda dirigida de literatura y ensayos clínicos sobre dextrometorfano en patología nasal
- Datos detallados del mecanismo de acción (MOA) y análisis del vínculo mecanístico
- Advertencias y contraindicaciones del prospecto aprobado
- Evaluación de compatibilidad de vía de administración y de la situación regulatoria vigente en Colombia
- Revisión de las contraindicaciones del grafo de conocimiento (p. ej., QT largo, hipertensión, epilepsia) antes de cualquier evaluación clínica

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

