---
layout: default
title: Acyclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Acyclovir: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Aciclovir"
monitor_inn: "ACYCLOVIR"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
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

## Aciclovir: De Aciclovir (uso antiviral) a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

Aciclovir es un antiviral análogo de la guanosina, registrado en Colombia bajo la indicación "aciclovir" (el texto de indicación del registro no detalla la enfermedad).
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, pero la evidencia directa es nula: **0 ensayos clínicos** y **2 publicaciones** poco pertinentes (series de casos sobre otras causas de queratoconjuntivitis).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Aciclovir (el registro sanitario no especifica la enfermedad) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Acyclovir (traducción no oficial): «El aciclovir es un análogo sintético de nucleósido de purina con actividad inhibitoria in vitro e in vivo contra los virus del herpes simple tipo 1 (VHS-1) y tipo 2 (VHS-2) y el virus de la varicela-zóster (VVZ). La actividad inhibitoria del aciclovir es altamente selectiva debido a su afinidad por la enzima timidina cinasa (TK) codificada por el VHS y el VVZ.» Texto original en inglés: "Acyclovir is a synthetic purine nucleoside analogue with in vitro and in vivo inhibitory activity against herpes simplex virus types 1 (HSV-1), 2 (HSV-2), and varicella-zoster virus (VZV). The inhibitory activity of acyclovir is highly selective due to its affinity for the enzyme thymidine kinase (TK) encoded by HSV and VZV." ([DailyMed: acyclovir prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=499c6a98-0614-4ded-8526-909942bae8a4), versión del 2026-06-26; consultado el 2026-11-19). Según la información conocida, aciclovir es un análogo de la guanosina que inhibe la ADN polimerasa de los herpesvirus, y su eficacia en infecciones herpéticas está bien establecida.

La queratitis epitelial punteada puede tener causa herpética o adenoviral, lo que explicaría en parte la predicción. Sin embargo, la literatura recuperada trata de queratoconjuntivitis por microsporidios y de lipidosis corneal en pacientes con SIDA, y aciclovir no tiene actividad contra esos agentes. El vínculo mecanístico es débil y el puntaje alto del modelo no está respaldado por la evidencia.

Cabe destacar que, entre las demás predicciones, la candidata con mejor respaldo es **verruga común** (nivel L2, con un ECA de Fase 2/3 y su publicación correspondiente). Se menciona como referencia, pues el informe se centra en la predicción de mayor puntaje.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Serie de casos | Indian J Pathol Microbiol | Características de la queratoconjuntivitis microsporidial en una cohorte del este de la India; no involucra aciclovir ni herpesvirus |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Reporte/serie de casos | Am J Ophthalmol | Lipidosis corneal inducida por fármacos en dos pacientes con SIDA; sin relación con la eficacia de aciclovir |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 219368 | VIREX® UNGÜENTO (vigente) | Ungüento tópico | ACICLOVIR |
| 53077 | ACYCLOVIR TABLETAS (vigente) | Tableta recubierta | ACICLOVIR |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia aciclovir con enfermedades como hipertensión, enfermedad renal y función renal alterada, síndrome hemolítico urémico, púrpura trombocitopénica, diabetes y cetoacidosis diabética, hiperglucemia, insuficiencia suprarrenal (enfermedad de Addison), obesidad, accidente cerebrovascular, infarto de miocardio, enfermedad vascular periférica, hemoglobinopatías, telangiectasia y atrofia cutánea. Son señales del grafo y requieren verificación con el prospecto.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Las de nivel moderado incluyen balsalazida, mesalazina, olsalazina, sulfasalazina y trospio. Otras (nivel desconocido) incluyen anfotericina B, metformina, morfina, omeprazol, pantoprazol, doxiciclina y epinefrina.

No se dispone de las advertencias y contraindicaciones del prospecto de INVIMA, por lo que se recomienda consultarlo.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0.9967), pero no existen ensayos clínicos y la literatura recuperada es indirecta y no respalda la eficacia. El mecanismo es débil para las causas más probables (microsporidios, adenovirus).

<!-- review:begin co-lic-20261105-acyclovir-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El mecanismo es débil para las causas más probables (microsporidios, adenovirus), y ambos registros sanitarios en Colombia están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-acyclovir-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad.
- Estudios que distingan la etiología herpética de la no herpética en la queratoconjuntivitis epitelial punteada.
- Evaluar la candidata con mayor respaldo (verruga común, aciclovir intralesional) como línea alternativa, incluyendo su compatibilidad de vía de administración, pues los registros colombianos previos eran tópicos y orales, no intralesionales.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y ambos registros sanitarios en Colombia están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: acyclovir prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=499c6a98-0614-4ded-8526-909942bae8a4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

