---
layout: default
title: Amoxicilina
parent: Solo Predicción del Modelo (L5)
nav_order: 53
evidence_level: L5
indication_count: 8
drugbank_id: DB01060
monitor_inn: "Amoxicillin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-24
description: "Amoxicilina: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5)."
---

# Amoxicilina
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

## Amoxicilina: Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Amoxicilina es un antibiótico betalactámico que inhibe la síntesis de la pared celular bacteriana.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AMOXICILINA Y BETA-LACTAMASA INHIBIDOR; AMOXICILINA |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 18 de 19) |
| Número de Registros Sanitarios | 19 (vigentes: 18) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amoxicilina (traducción no oficial): «La amoxicilina es un fármaco antibacteriano. […] La amoxicilina es similar a la penicilina en su acción bactericida contra las bacterias sensibles durante la fase de multiplicación activa. Actúa mediante la inhibición de la biosíntesis de la pared celular, lo que provoca la muerte de las bacterias.» Texto original en inglés: "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), versión del 2026-11-13; consultado el 2026-11-19). Por conocimiento general, la amoxicilina es un betalactámico que impide la formación de la pared celular de las bacterias sensibles.

El síndrome de hiperviscosidad policlonal se debe a un aumento de inmunoglobulinas policlonales en sangre. No se identifica un mecanismo plausible por el cual un antibiótico que actúa sobre la pared bacteriana pueda corregir ese aumento de viscosidad.

El puntaje alto (0.9963) refleja una cercanía en la red de relaciones del modelo, probablemente a través de comorbilidades infecciosas, y no un efecto terapéutico demostrado. Por ello, esta predicción debe tratarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay registros sanitarios vigentes; se listan los principales (hasta 5):

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20004922 | KOACT 312.5 POLVO PARA RECONSTITUIR A SUSPENSIÓN ORAL | POLVO PARA RECONSTITUIR A SUSPENSION ORAL | AMOXICILINA Y BETA-LACTAMASA INHIBIDOR | Vigente |
| 20032447 | IPICLAV® 1 G | TABLETA RECUBIERTA | AMOXICILINA Y BETA-LACTAMASA INHIBIDOR | Vigente |
| 20079039 | ATAK CLAV® | POLVO PARA RECONSTITUIR A SUSPENSION ORAL | AMOXICILINA Y BETA-LACTAMASA INHIBIDOR | Vigente |
| 20083462 | SOLOMOXY | CAPSULA DURA | AMOXICILINA | Vigente |
| 20109747 | AMOXICLIN ® DUO | TABLETA RECUBIERTA | AMOXICILINA Y BETA-LACTAMASA INHIBIDOR | Vigente |

Se muestran 5 de 19 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que estudie esta enfermedad con amoxicilina, y no hay un mecanismo biológico plausible. La predicción se basa solo en el modelo computacional (nivel L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto
- Evidencia preclínica o clínica que vincule directamente la amoxicilina con el síndrome de hiperviscosidad policlonal
- Replantear si esta predicción merece una pregunta de investigación, dada la ausencia de un mecanismo plausible

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

