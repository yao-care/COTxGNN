---
layout: default
title: Miconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 441
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
description: "Miconazole: nueva indicación predicha, acné (acne (disease)) (nivel de evidencia L4). Indicación original: METRONIDAZOL"
---

# Miconazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Miconazole: acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Miconazol es un antifúngico de la clase de los imidazoles, con registro sanitario vigente en Colombia.
El modelo TxGNN predice que podría ser útil para **acné (acne (disease))**,
pero la evidencia es limitada: **0 ensayos clínicos** y **4 publicaciones** (una revisión, un estudio clínico pequeño, un estudio in vitro y un estudio sobre una afección que imita el acné), sin un estudio clínico directo en acné. Nivel de evidencia: **L4**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METRONIDAZOL; MICONAZOL |
| Nueva Indicación Predicha | acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, el miconazol inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa), bloqueando la síntesis de ergosterol. Esta descripción proviene de conocimiento general y no de los datos suministrados.

En el acné se plantean varios vínculos posibles: (1) actividad in vitro de los azoles contra *Cutibacterium (Propionibacterium) acnes* (PMID 20045949); (2) actividad contra *Malassezia*, causante de la foliculitis por *Malassezia*, una afección que imita el acné (PMID 8593718); y (3) efectos antibacterianos y antiinflamatorios descritos en la piel (PMID 18627330). Un estudio dividido en hemicara en acné inflamatorio leve catamenial (PMID 15536660) aporta datos humanos a pequeña escala.

El puntaje de 0,9954 es coherente con estos vínculos, pero es una predicción computacional y no constituye evidencia clínica. Ningún estudio citado evalúa de forma directa y concluyente el miconazol en acné; por ello el nivel de evidencia se mantiene en L4, apoyado principalmente en la revisión sobre sus efectos cutáneos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisión | Expert Opin Pharmacother | Revisión de los efectos multifacéticos del miconazol en trastornos de la piel; antifúngico imidazólico de uso consolidado |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudio clínico (hemicara, pequeña escala) | Skin Res Technol | Evaluación clínica y bioinstrumental en acné inflamatorio leve catamenial |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Estudio clínico | Clin Exp Dermatol | Foliculitis por *Pityrosporum* (*Malassezia*) en Arabia Saudita, a menudo confundida con acné vulgar; diagnóstico y ensayos terapéuticos |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biol Pharm Bull | Actividad in vitro de azoles antifúngicos contra *P. acnes* aislado de pacientes con acné vulgar |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19985092 | GYNOTRAN® OVULO | Óvulo | Metronidazol |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones farmacológicas (farmacología de dianas):** se registraron 3 interacciones con dianas humanas: TRPM2, TRPV5 y CYP8B1 (el miconazol se une e inhibe CYP8B1). No se dispone de niveles de gravedad.
- **Advertencia adicional:** en los datos compilados figuran relaciones con enfermedad hepática y enfermedad de la vesícula biliar como posibles contraindicaciones; conviene tener precaución en pacientes con estas condiciones.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9954), pero la evidencia llega solo a L4: una revisión de los efectos del miconazol en la piel, datos in vitro y un estudio pequeño, sin ensayos clínicos directos en acné.

**Para avanzar se necesita:**
- Ensayos clínicos controlados de miconazol en acné
- Datos detallados del mecanismo de acción
- Información de seguridad del prospecto de INVIMA (advertencias y contraindicaciones)
- Evaluación de la viabilidad de la vía de administración para uso en acné

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria actual (registro cancelado) y la disponibilidad de formulaciones tópicas" | Ya no aparece tras regenerar el informe (2026-11-12: el informe se regeneró en noviembre de 2026 y ya no contiene esta afirmación; antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

