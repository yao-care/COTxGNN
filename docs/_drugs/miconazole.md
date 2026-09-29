---
layout: default
title: Miconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 282
evidence_level: L4
indication_count: 1
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Miconazol: De Infecciones Fúngicas Cutáneas a Acné

## Resumen en Una Frase

Miconazol es un antifúngico imidazólico, usado originalmente contra infecciones fúngicas de la piel como tiña y candidiasis cutánea.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero el respaldo real es débil: **1 ensayo clínico** (suspendido y de relevancia baja) y **4 publicaciones**, entre ellas un estudio in vitro, una revisión y estudios clínicos indirectos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones fúngicas cutáneas (tiña pedis, tiña cruris, tiña corporis, candidiasis cutánea, pitiriasis versicolor). El campo de indicación de INVIMA solo lista principios activos (Metronidazol, Miconazol), no una indicación en texto. |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, miconazol es un antifúngico imidazólico que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa) y bloquea así la síntesis de ergosterol. También se han descrito efectos antibacterianos contra bacterias Gram-positivas y efectos antiinflamatorios.

Estos dos efectos son vínculos plausibles con el acné. Por un lado, hay actividad in vitro de los azoles contra *Cutibacterium (Propionibacterium) acnes*, la bacteria asociada al acné vulgar. Por otro, *Malassezia* participa en la inflamación folicular.

El puntaje de 0.995 es una predicción computacional y no cuenta como evidencia clínica. Tampoco se ha demostrado que miconazol sea útil en acné vulgar propiamente dicho, a diferencia de la foliculitis por *Malassezia*. Esta última suele confundirse con acné y es la que sí responde a antifúngicos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la combinación de beclometasona, gentamicina y un azol (probablemente clotrimazol, no miconazol) en dermatosis contaminada con lesiones bilaterales simétricas. No tiene resultados publicados. No se puede aislar el aporte de miconazol ni confirmar que se trate de acné vulgar. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisión | Expert Opin Pharmacother | Revisa los efectos múltiples de miconazol en trastornos de la piel. |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudio clínico (split-face) | Skin Res Technol | Evaluación clínica e instrumental del acné inflamatorio leve catamenial. El resumen disponible no detalla el papel de miconazol. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Estudio clínico | Clin Exp Dermatol | En 62 pacientes con foliculitis por *Pityrosporum*, una condición frecuentemente confundida con acné vulgar, se evaluaron el diagnóstico y ensayos terapéuticos. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biol Pharm Bull | Determina la actividad in vitro de antifúngicos azoles contra *P. acnes* aislado de pacientes con acné vulgar. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19985092 | GYNOTRAN® OVULO (Exeltis S.A.S) | Óvulo | Metronidazol; Miconazol (el campo solo indica principios activos) |

Los cinco registros de la muestra corresponden al mismo registro sanitario, por lo que se muestra una sola fila. Además, la única forma farmacéutica disponible es un óvulo (vaginal), que no sirve para tratar acné.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas / Dianas Farmacológicas**: la consulta se completó con 3 registros. Son datos de farmacología (dianas moleculares) y no interacciones clínicas con otros medicamentos, y no tienen nivel de severidad asignado.
  - TRPM2
  - TRPV5
  - CYP8B1 (miconazol se une a la enzima humana CYP8B1 y la inhibe)

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: solo hay estudios in vitro, una revisión y estudios indirectos, y el único ensayo clínico está suspendido y no aísla el efecto de miconazol. El puntaje alto del modelo no basta por sí solo. Además, falta la revisión de seguridad por la ausencia del prospecto de INVIMA.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy bloquea el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Confirmar si existe en Colombia una formulación tópica de miconazol; la única presentación registrada es un óvulo vaginal.
- Buscar o diseñar ensayos controlados en acné vulgar que distingan entre acné y foliculitis por *Malassezia*.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

