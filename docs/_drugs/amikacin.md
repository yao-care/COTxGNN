---
layout: default
title: Amikacin
parent: Evidencia Moderada (L3-L4)
nav_order: 47
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Amikacin: nueva indicación predicha, Fiebre paratifoidea (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto de indicación solo repite \"A…"
monitor_inn: "amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "meningococcemia"]
---

# Amikacin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Amikacina: De Indicación No Especificada a Fiebre Paratifoidea

## Resumen en Una Frase

Amikacina es un antibiótico aminoglucósido, registrado en Colombia como solución inyectable (500 mg/2 mL); el registro sanitario disponible no detalla una indicación específica más allá del nombre del producto.
El modelo TxGNN predice que podría ser efectivo para **fiebre paratifoidea**, pero no existen ensayos clínicos y solo hay **8 publicaciones** de carácter indirecto (epidemiología, antibiogramas y reportes de casos).
La evidencia directa de eficacia es prácticamente inexistente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo repite "AMIKACINA") |
| Nueva Indicación Predicha | Fiebre paratifoidea |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, amikacina es un aminoglucósido con amplia actividad contra bacterias Gram-negativas, que actúa inhibiendo la síntesis de proteínas bacterianas. Por ello, es biológicamente plausible que tenga actividad contra *Salmonella* Paratyphi, una bacteria Gram-negativa.

Sin embargo, existe una limitación importante: *Salmonella* Paratyphi reside en el interior de los macrófagos, y los aminoglucósidos penetran mal en las células. Por eso, la actividad in vitro difícilmente se traduce en eficacia clínica en la fiebre entérica. Los tratamientos preferidos son las fluoroquinolonas, la azitromicina y las cefalosporinas de tercera generación.

La literatura recuperada es principalmente epidemiológica y de sensibilidad antibiótica. Incluye un informe de 1989 sobre antibióticos para infecciones por paratyphi B resistentes al tratamiento clásico y un caso pediátrico de colecistitis acalculosa por *S.* Paratyphi B tratado con cefepima, amikacina y factor estimulante de colonias. No hay evidencia directa de eficacia de amikacina como tratamiento de la fiebre paratifoidea.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Cohorte | Mikrobiyoloji Bülteni | Tratamiento y antibiograma de 48 pacientes con infección por *S.* Paratyphi B resistente al tratamiento clásico (ampicilina, cloranfenicol, cotrimoxazol) |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Reporte de caso | Pediatric Hematology and Oncology | Niño de 9 años con leucemia linfoblástica aguda y colecistitis acalculosa por *S.* Paratyphi B, tratado con éxito con cefepima, amikacina y G-CSF |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Cohorte | Indian J Pathol Microbiol | 280 cepas de *S.* Typhi; las cepas multirresistentes siguieron siendo sensibles a aminoglucósidos y ciprofloxacino |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Revisión | Med J Armed Forces India | Reaparición de sensibilidad al cloranfenicol en fiebre entérica (*S.* Typhi y Paratyphi A) |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohorte | J Indian Med Assoc | Estudio prospectivo de 145 niños con fiebre entérica y patrón de sensibilidad antibiótica |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Cohorte | New Microbiologica | Ocurrencia de *S.* Typhi y Paratyphi en Jordania (1988–2000) |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Cohorte | Pak J Biol Sci | Aislamiento e identificación de *S.* Paratyphi en pacientes de Quetta |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cohorte | JNMA | Frecuencia de aislamientos en hemocultivos y antibiograma en un hospital docente |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19908236 (cancelado) | AMIKACINA 500 MG/2ML | Solución inyectable | AMIKACINA |

El único registro sanitario (fabricante: VITALIS S.A.C.I.) figura como cancelado; no hay registros vigentes.

---

## Consideraciones de Seguridad

Los datos de advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para esa información.

- **Contraindicaciones según el grafo de conocimiento (no provienen del texto del prospecto)**: enfermedad renal, piouréter, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, vértigo de origen central, miastenia gravis (incluida la de inicio en adultos), enfermedades de la unión neuromuscular, trastornos parkinsonianos y enfermedad de Parkinson.
- **Interacciones farmacológicas**: se identificaron 212 interacciones en total. Las de nivel **mayor** son:
  - Sulfato de magnesio
  - Manitol
- Entre las de nivel **moderado** figuran anfotericina B (y sus formulaciones), kanamicina, neomicina, ácido acetilsalicílico, exenatida, mesalazina, balsalazida, olsalazina y los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol).
- Como aminoglucósido, el perfil de nefrotoxicidad y ototoxicidad exige especial cautela; las interacciones con otros fármacos nefrotóxicos son particularmente relevantes.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura es indirecta (epidemiología, antibiogramas y reportes de caso). Además, la baja penetración intracelular de los aminoglucósidos y la existencia de alternativas de primera línea (fluoroquinolonas, azitromicina, ceftriaxona) restan sustento a la predicción. Adicionalmente, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones), un vacío de datos que bloquea el análisis de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Evidencia clínica directa de eficacia de amikacina en fiebre paratifoidea (ensayos o estudios comparativos con tratamientos estándar)
- Evaluar la situación regulatoria (registro cancelado) y la viabilidad de comercialización en Colombia
- Valorar si el uso tendría algún nicho (p. ej., cepas multirresistentes) frente a las alternativas existentes

**Nota sobre otras predicciones:** las demás indicaciones predichas (esclerodermia difusa, queratoconjuntivitis epitelial punteada, fiebre tifoidea, epiglotitis, salmonelosis, analbuminemia congénita, hiperamilasemia, síndrome de hiperviscosidad policlonal y meningococemia) también quedan en **Hold**. Las de nivel L4 (fiebre tifoidea, salmonelosis y meningococemia) solo cuentan con evidencia indirecta o in vitro, y el resto son únicamente predicciones del modelo (L5), sin vínculo mecanístico plausible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

