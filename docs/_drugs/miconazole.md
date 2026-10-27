---
layout: default
title: Miconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 441
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-14
description: "Miconazole: nueva indicación predicha, Acné (nivel de evidencia L3). Indicación original: Metronidazol"
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
---

# Miconazole
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

## Miconazol: De Metronidazol/Miconazol a Acné
{: .text-alpha }

## Resumen en Una Frase

Miconazol es un antifúngico imidazólico; en Colombia su único registro sanitario en los datos compilados corresponde a un óvulo vaginal (GYNOTRAN® OVULO) cuya indicación aparece como metronidazol.
El modelo TxGNN predice que podría ser efectivo para **acné**, con **0 ensayos clínicos** y **4 publicaciones** que actualmente respaldan esta dirección de forma preliminar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Metronidazol (texto tal como figura en el registro; corresponde a una combinación con miconazol) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según el conocimiento general, miconazol es un antifúngico imidazólico que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-demetilasa) y bloquea la síntesis de ergosterol. Esta explicación proviene de conocimiento general del fármaco y no de los datos suministrados.

Para el acné se plantean tres vías plausibles: (1) actividad in vitro de los azoles frente a *Cutibacterium (Propionibacterium) acnes* (PMID 20045949); (2) actividad frente a *Malassezia*, causante de la foliculitis por Pityrosporum, una afección que imita al acné (PMID 8593718); y (3) efectos antiinflamatorios y antibacterianos descritos sobre la piel (PMID 18627330).

El puntaje alto de TxGNN (0.995) es coherente con estos vínculos, pero es una predicción computacional y no constituye evidencia clínica. Cabe destacar que parte de la evidencia se refiere a una afección que simula el acné, no al acné vulgar propiamente dicho.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisión | Expert Opin Pharmacother | Revisión de los efectos múltiples del miconazol en enfermedades de la piel; el nitrato de miconazol es un antifúngico imidazólico de uso consolidado |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudio clínico (split-face, pequeña escala) | Skin Res Technol | Evaluación clínica y bioinstrumental en acné inflamatorio leve catamenial; aporta datos humanos de pequeña escala |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Estudio clínico (diagnóstico y terapéutico) | Clin Exp Dermatol | 62 pacientes con foliculitis por Pityrosporum, frecuentemente confundida con acné vulgar; no es acné verdadero |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Estudio in vitro | Biol Pharm Bull | Actividad in vitro de antifúngicos azólicos frente a *P. acnes* aislado de pacientes con acné vulgar |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19985092 (cancelado) | GYNOTRAN® OVULO | Óvulo | Metronidazol |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto)**: enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas / farmacología de dianas**: se identificaron 3 registros de interacción con dianas humanas (TRPM2, TRPV5 y CYP8B1). Sin nivel de gravedad asignado. Los datos indican que miconazol se une a CYP8B1 y lo inhibe.

No se dispone de advertencias del prospecto; consultar el prospecto para información adicional de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una revisión, un estudio clínico pequeño, un estudio in vitro y un estudio sobre una afección que simula el acné, sin ensayos clínicos registrados. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente una brecha de datos bloqueante para el tamizaje de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Aclarar la situación regulatoria actual (registro cancelado) y la disponibilidad de formulaciones tópicas
- Generar evidencia clínica específica en acné vulgar (idealmente ensayos aleatorizados)
- Evaluar la compatibilidad de vías de administración, dado que el producto registrado es un óvulo vaginal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

