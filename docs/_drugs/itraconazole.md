---
layout: default
title: Itraconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 361
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Itraconazole: nueva indicación predicha, Neumocistosis (nivel de evidencia L4). Indicación original: ITRACONAZOL"
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Itraconazol: De Indicación Original (ITRACONAZOL, sin detalle) a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

Itraconazol es un antifúngico azólico, registrado en Colombia bajo el nombre ITRACONAZOL en solución oral (los dos registros sanitarios están cancelados).
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, con un puntaje alto (99.34%), pero **sin ensayos clínicos** registrados y con **20 publicaciones** de apoyo indirecto, ninguna que demuestre eficacia contra *Pneumocystis*.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ITRACONAZOL (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, itraconazol inhibe la lanosterol 14-alfa-desmetilasa fúngica (CYP51), bloqueando la síntesis de ergosterol de la membrana celular. Su eficacia en infecciones fúngicas sistémicas está bien establecida, aunque el registro local no detalla la indicación aprobada.

La relación con la neumocistosis es **débil**. *Pneumocystis jirovecii* es taxonómicamente un hongo, pero su membrana contiene muy poco ergosterol y depende sobre todo de colesterol y esteroles relacionados. Esto limita la plausibilidad de un mecanismo azólico, y los azoles no están establecidos como eficaces contra *Pneumocystis*.

El puntaje alto del modelo (0.993) probablemente refleja la asociación de itraconazol con la clase antifúngica y su uso en los mismos contextos de infecciones oportunistas (VIH, trasplante, neutropenia), y no un mecanismo validado contra este patógeno. La predicción debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Las publicaciones son en su mayoría revisiones y series de casos sobre infecciones oportunistas. Ninguna evalúa itraconazol como tratamiento de la neumocistosis. Se listan las más relevantes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | ECA (fase III, doble ciego) | HIV Medicine | Itraconazol en cápsulas como profilaxis de infecciones fúngicas profundas en pacientes con VIH inmunodeficientes; no se evalúa específicamente *Pneumocystis* |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clin Pharmacokinet | Penetración de antifúngicos y otros antiinfecciosos en el líquido epitelial pulmonar |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revisión | BMJ Clin Evid | Profilaxis primaria y secundaria de infecciones oportunistas en VIH |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revisión | Clin Infect Dis | Profilaxis antimicrobiana en neutropenia febril; la prevención de neumonía por *Pneumocystis* se basa en trimetoprim-sulfametoxazol |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Terapia y profilaxis de infecciones sistémicas por protozoos, incluido *Pneumocystis carinii* |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revisión | Semin Respir Infect | Infecciones tras trasplante de pulmón |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revisión | Curr Clin Top Infect Dis | Profilaxis y tratamiento de infecciones en receptores de trasplante de médula ósea |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte | Transplant Proc | Infecciones fúngicas invasivas tras trasplante renal en un solo centro |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Reporte de caso | Front Immunol | Coinfección por *Talaromyces marneffei* y *P. jirovecii* en un niño con mutación de STAT1 |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Serie de casos | Medicine | Histoplasmosis diseminada en SIDA: hallazgos clínicos, diagnóstico y tratamiento |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20122550 | ITRACONAZOL 10 MG/ ML (cancelado) | Solución oral | ITRACONAZOL |
| 20095994 | FUNGITRAL® 1G/100 ML (cancelado) | Solución oral | ITRACONAZOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento de TxGNN (PrimeKG) asocia itraconazol con condiciones como síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia cardíaca congestiva, cardiomiopatía (incluida la hipertrófica), cardiopatía isquémica y enfermedad arterial coronaria, enfermedad hepática y lesión hepática inducida por fármacos, enfermedad renal y función renal alterada, EPOC, neuropatía periférica, trastornos visuales y pérdida de audición, entre otras.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; entre las muestras disponibles, las de nivel **mayor** son:
  - Loperamida
  - Triamcinolona
  - Budesonida

  Hay además interacciones moderadas (por ejemplo famotidina, ranitidina, omeprazol, rabeprazol, cimetidina, dexametasona, hidrocortisona, betametasona, aprepitant y alosetrón) y menores (por ejemplo metformina, pioglitazona y anfotericina B).

La información de advertencias y contraindicaciones del prospecto no está disponible; consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que respalden itraconazol contra la neumocistosis, y el fundamento mecanístico es débil porque *Pneumocystis* carece prácticamente de ergosterol. El puntaje alto del modelo parece reflejar una asociación de clase y de contexto clínico. Además, ambos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Estudios preclínicos o in vitro que demuestren actividad de itraconazol contra *Pneumocystis jirovecii*
- Datos del mecanismo de acción y comparación con la terapia estándar (trimetoprim-sulfametoxazol)
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) para el cribado de seguridad
- Evaluar el estado regulatorio local, ya que no hay registros vigentes
- Evaluar los riesgos cardiovasculares (QT largo) y las interacciones en la población objetivo (VIH, trasplante)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

