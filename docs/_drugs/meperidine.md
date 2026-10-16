---
layout: default
title: Meperidine
parent: Solo Predicción del Modelo (L5)
nav_order: 427
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Meperidine: nueva indicación predicha, Síndrome de Tourette (nivel de evidencia L5). Indicación original: Petidina"
monitor_inn: "meperidine"
predicted_indications: ["Tourette syndrome", "trichotillomania"]
---

# Meperidine
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

# Meperidina: De Petidina (analgésico opioide) a Síndrome de Tourette

## Resumen en Una Frase

La meperidina (petidina) es un analgésico opioide cuyo único registro sanitario en Colombia está cancelado. El modelo TxGNN predice que podría ser efectivo para el **síndrome de Tourette**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Petidina (según el registro INVIMA; no se detalla una indicación clínica) |
| Nueva Indicación Predicha | Síndrome de Tourette |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la meperidina es un agonista sintético del receptor opioide mu, con cierta inhibición de la recaptación de serotonina y una actividad anticolinérgica débil.

Sin embargo, los datos disponibles **no respaldan un vínculo mecanístico** con la supresión de tics. El síndrome de Tourette se asocia a una disregulación de los circuitos cortico-estriato-tálamo-corticales y a hiperactividad dopaminérgica, y no se ha establecido una justificación para usar un agonista opioide en este contexto.

El puntaje alto de TxGNN (0.9946) es una predicción computacional que no está sustentada por evidencia clínica ni bibliográfica. Debe interpretarse como una hipótesis para generar investigación, no como una indicación de eficacia.

**Otra predicción del modelo:** la tricotilomanía (puntaje 99.39%, nivel L5, Hold). Aquí el vínculo es incluso contraintuitivo, porque para esa condición se han explorado antagonistas opioides (como la naltrexona) y no agonistas.

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
| 20008613 (cancelado) | MEPERIDINA CLORHIDRATO 100 MG/2 ML | Solución inyectable | PETIDINA |

El titular es el Fondo Nacional de Estupefacientes (Ministerio de Salud y Protección Social). No hay registros vigentes, lo que limita la disponibilidad práctica del fármaco.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** insuficiencia y enfermedad hepática, epilepsia, enfermedad pulmonar obstructiva crónica, insuficiencia respiratoria, apnea del sueño, hipotiroidismo/mixedema, enfermedad de Addison, glaucoma de ángulo cerrado, hiperplasia prostática benigna, úlcera péptica, enfermedad de la vesícula biliar, hipotensión, anemia falciforme, tromboflebitis, hiperbilirrubinemia (incluido el síndrome de Gilbert), abuso/dependencia de sustancias, y trastornos de los ganglios basales (distonía focal de la mano, blefaroespasmo).
- **Interacciones farmacológicas:** se registran 181 interacciones. Entre las de nivel **mayor** destacan alvimopán, bupropión, morfina, lorcaserina, dolasetrón y palonosetrón. Entre las de nivel moderado se incluyen hiosciamina, loperamida, atropina, glicopirronio, cimetidina, naloxona, fentermina y dronabinol, entre otras.
- **Riesgos adicionales señalados en el análisis:** síndrome serotoninérgico (con IMAO y otros agentes serotoninérgicos), el metabolito neurotóxico normeperidina (riesgo de convulsiones) y potencial de dependencia a opioides.

Consultar el prospecto para la información completa de advertencias y contraindicaciones, ya que no se dispone del texto del prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, sin vínculo mecanístico plausible, con un perfil de seguridad desfavorable (dependencia, normeperidina, interacciones numerosas) y sin registro sanitario vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y un análisis que justifique un vínculo con el síndrome de Tourette.
- Revisión sistemática de la literatura y de registros de ensayos clínicos para esta indicación.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Evaluar alternativas con mejor perfil de seguridad y disponibilidad, dado el estado cancelado del registro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

