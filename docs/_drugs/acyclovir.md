---
layout: default
title: Acyclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, aciclovir es un análogo de la guanosina que inhibe la ADN polimerasa de los herpesvirus, y su eficacia en infecciones herpéticas está bien establecida.

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
La predicción tiene un puntaje alto (0.9967), pero no existen ensayos clínicos y la literatura recuperada es indirecta y no respalda la eficacia. El mecanismo es débil para las causas más probables (microsporidios, adenovirus), y ambos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad.
- Estudios que distingan la etiología herpética de la no herpética en la queratoconjuntivitis epitelial punteada.
- Evaluar la candidata con mayor respaldo (verruga común, aciclovir intralesional) como línea alternativa, incluyendo su compatibilidad de vía de administración, pues los registros colombianos previos eran tópicos y orales, no intralesionales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

