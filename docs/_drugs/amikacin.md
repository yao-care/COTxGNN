---
layout: default
title: Amikacin
parent: Solo Predicción del Modelo (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
monitor_inn: "amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "meningococcemia"]
last_modified_at: 2026-10-28
description: "Amikacin: nueva indicación predicha, fiebre paratifoidea (paratyphoid fever) (nivel de evidencia L5). Indicación original: AMIKACINA"
---

# Amikacin
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

## Amikacina: antibiótico aminoglucósido → fiebre paratifoidea (paratyphoid fever)
{: .text-alpha }

## Resumen en Una Frase

Amikacina es un antibiótico aminoglucósido de amplio espectro contra bacterias Gram negativas, disponible en Colombia como solución inyectable.
El modelo TxGNN predice que podría ser útil para **fiebre paratifoidea (paratyphoid fever)**, pero no hay ensayos clínicos y solo 8 publicaciones, casi todas epidemiológicas o de antibiogramas, sin evidencia directa de eficacia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AMIKACINA |
| Nueva Indicación Predicha | fiebre paratifoidea (paratyphoid fever) |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por su clase, amikacina inhibe la síntesis de proteínas bacterianas y tiene actividad amplia contra bacilos Gram negativos. *Salmonella paratyphi*, causante de la fiebre paratifoidea, es un bacilo Gram negativo, así que una actividad in vitro es biológicamente plausible.

Sin embargo, el vínculo clínico es débil. *Salmonella* vive dentro de los macrófagos y los aminoglucósidos penetran mal en las células, por lo que no son fiables en la fiebre entérica. Los tratamientos preferidos son las fluoroquinolonas, la azitromicina y las cefalosporinas de tercera generación.

La literatura recuperada es sobre todo de epidemiología y sensibilidad antibiótica. Solo un reporte de caso describe el uso de amikacina en una infección por *S. paratyphi* B, y lo hace dentro de un esquema combinado. El puntaje del modelo es una predicción computacional, no una demostración de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Reporte de caso | Pediatric Hematology and Oncology | Niño de 9 años con leucemia linfoblástica aguda y colecistitis acalculosa por *S. paratyphi* B, tratado con éxito con cefepima, amikacina y factor estimulante de colonias de granulocitos. |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Cohorte | Mikrobiyoloji Bülteni | Tratamiento y antibiogramas de 48 pacientes pediátricos con infección por paratifoidea B resistente al tratamiento clásico (ampicilina, cloranfenicol, cotrimoxazol). |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Cohorte | The New Microbiologica | Ocurrencia de *S. typhi* y *S. paratyphi* en casos de diarrea en Jordania entre 1988 y 2000. |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Revisión | Medical Journal, Armed Forces India | Sensibilidad de *S. typhi* y *S. paratyphi* A en 45 casos de fiebre entérica en el norte de la India; reaparición de la sensibilidad al cloranfenicol. |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohorte | Journal of the Indian Medical Association | Estudio clínico y microbiológico de 145 niños con fiebre entérica y sus patrones de sensibilidad antibiótica. |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Cohorte | Indian Journal of Pathology & Microbiology | 280 cepas de *S. typhi* en Ludhiana; las cepas multirresistentes siguieron siendo sensibles a aminoglucósidos y ciprofloxacino. |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cohorte | JNMA (Nepal) | Frecuencia de aislamientos en hemocultivos y sus antibiogramas en un hospital docente. |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Cohorte | Pakistan Journal of Biological Sciences | Aislamiento e identificación de *S. paratyphi* en pacientes con fiebre entérica en Quetta. |

## Información de Mercado en Colombia

Según los registros sanitarios locales, el estado de mercado de amikacina en Colombia es **Comercializado**. El producto está registrado como solución inyectable (concentración 500 mg/2 ml). Los registros disponibles pueden estar incompletos. La tabla detallada de registros sanitarios la añade el programa a partir de los datos de licencia.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 212 interacciones potenciales. Las más relevantes son:
  - **Mayores**: sulfato de magnesio y manitol.
  - **Moderadas**: otros aminoglucósidos (kanamicina, neomicina), anfotericina B (varias formulaciones), ácido acetilsalicílico, mesalazina, balsalazida, olsalazina, exenatida e inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos, la literatura es principalmente epidemiológica o de antibiogramas, y solo un reporte de caso menciona amikacina dentro de un esquema combinado. Además, la mala penetración intracelular de los aminoglucósidos y la existencia de alternativas eficaces (fluoroquinolonas, azitromicina, cefalosporinas de tercera generación) hacen poco favorable la relación riesgo-beneficio.

**Para avanzar se necesita:**
- Evidencia clínica directa de eficacia de amikacina en fiebre paratifoidea (estudios comparativos frente a los tratamientos de referencia).
- Datos de actividad intracelular y farmacocinética en tejidos relevantes.
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) para el análisis de seguridad.
- Análisis del perfil de riesgo (nefrotoxicidad y ototoxicidad) y de las interacciones antes de cualquier consideración clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

