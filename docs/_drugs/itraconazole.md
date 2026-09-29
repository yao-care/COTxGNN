---
layout: default
title: Itraconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 233
evidence_level: L4
indication_count: 1
---

# Itraconazole
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

# Itraconazol: De Antifúngico (indicación original no detallada en el registro) a Neumocistosis

## Resumen en Una Frase

Itraconazol es un antifúngico azólico comercializado en Colombia como solución oral. Los registros locales no detallan su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero **no hay ensayos clínicos** y las **20 publicaciones** halladas no demuestran eficacia directa contra *Pneumocystis*.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto de los registros solo dice «ITRACONAZOL») |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 3 (2 números de registro únicos en el listado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Itraconazol pertenece a la clase de los azoles antifúngicos, que inhiben la enzima CYP51 (lanosterol 14-alfa-desmetilasa) y bloquean la síntesis de ergosterol de la membrana fúngica.

**La predicción tiene poco respaldo biológico.** *Pneumocystis jirovecii* tiene poco o ningún ergosterol en su membrana celular, por lo que el mecanismo azólico no debería ser activo contra él. El tratamiento y la profilaxis estándar son trimetoprima-sulfametoxazol, con atovacuona, pentamidina y dapsona como alternativas.

La literatura vincula itraconazol con la neumocistosis sobre todo por infecciones fúngicas que aparecen junto a ella o que se previenen a la vez. Son ejemplos la histoplasmosis, la talaromicosis y las infecciones invasivas por hongos filamentosos y levaduras, en pacientes con VIH, trasplantados o neutropénicos. Es probable que esa co-ocurrencia explique el puntaje alto del modelo de grafos. La similitud con la indicación original no pudo evaluarse porque no hay datos de indicación ni de MOA.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna publicación evalúa itraconazol como tratamiento de la neumocistosis. Los estudios describen coinfecciones o profilaxis de infecciones fúngicas en general.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | ECA | HIV Medicine | Ensayo fase III doble ciego con placebo de itraconazol en cápsulas para prevenir infecciones fúngicas profundas en pacientes con VIH. El resumen disponible no reporta resultados ni evalúa neumocistosis. |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte | Transplantation Proceedings | Experiencia de un centro con infecciones fúngicas invasivas tras trasplante renal. |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Terapia y profilaxis de infecciones sistémicas por protozoos, incluido *P. carinii*. |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revisión | Clinical Infectious Diseases | Profilaxis antimicrobiana en neutropenia febril. Trimetoprima-sulfametoxazol previene eficazmente la neumonía por *P. carinii*. |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revisión | BMJ Clinical Evidence | Profilaxis primaria y secundaria de infecciones oportunistas en VIH. |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revisión | Seminars in Respiratory Infections | Infecciones tras trasplante de pulmón y su prevención. |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revisión | Current Clinical Topics in Infectious Diseases | Profilaxis y tratamiento de infecciones en receptores de trasplante de médula ósea. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clinical Pharmacokinetics | Penetración de antifúngicos y otros antiinfecciosos en el líquido de revestimiento epitelial pulmonar. |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Reporte de caso | Frontiers in Immunology | Coinfección por *Talaromyces marneffei* y *P. jirovecii* en un niño con mutación de STAT1. |
| [40949034](https://pubmed.ncbi.nlm.nih.gov/40949034/) | 2025 | Reporte de caso | Germs | Coinfección pulmonar por *P. jirovecii* e *Histoplasma capsulatum* en un paciente inmunocomprometido sin VIH. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20122550 | ITRACONAZOL 10 MG/ML (Clínicos y Hospitalarios de Colombia S.A.S.) | Solución oral | No detallada (solo indica «ITRACONAZOL») |
| 20095994 | FUNGITRAL® 1G/100 ML (Salusphara Labs S.A.S) | Solución oral | No detallada (solo indica «ITRACONAZOL») |

El registro 20095994 aparece duplicado en los datos de origen.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es alto (99.34%), pero no hay ensayos clínicos ni estudios que muestren eficacia de itraconazol contra *Pneumocystis*. Además, la ausencia de ergosterol en el organismo hace improbable el mecanismo azólico. Ya existen tratamientos estándar eficaces.

**Para avanzar se necesita:**
- Descargar y revisar los prospectos de INVIMA (advertencias y contraindicaciones) para completar el tamizaje de seguridad.
- Obtener el mecanismo de acción y las indicaciones originales desde DrugBank.
- Buscar estudios preclínicos o clínicos que evalúen directamente itraconazol frente a *Pneumocystis*. Sin ellos, el candidato permanece en L4.
- Aclarar si el vínculo del modelo proviene solo de la co-ocurrencia con otras micosis, en cuyo caso probablemente sea un artefacto del grafo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

