---
layout: default
title: Guselkumab
parent: Solo Predicción del Modelo (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Guselkumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Guselkumab: De Indicación No Especificada en el Registro a Psoriasis

> Nota: predicted_indications[0] (osteoporosis inducida por fármacos) no cuenta con evidencia. Este informe se centra en la predicción de mayor rango con evidencia disponible, **psoriasis** (rango 3), que corresponde a una indicación ya establecida del fármaco. También se menciona la colitis ulcerosa (rango 6) como candidata con evidencia sólida.

## Resumen en Una Frase

Guselkumab es un anticuerpo monoclonal anti-IL-23 (subunidad p19) comercializado como TREMFYA®; el registro sanitario colombiano solo lista el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **psoriasis** (indicación ya establecida, por lo que funciona como validación del modelo) y para **colitis ulcerosa** (reposicionamiento real),
con **31 ensayos clínicos** y **20 publicaciones** para psoriasis, y **10 ensayos** y **20 publicaciones** para colitis ulcerosa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "GUSELKUMAB") |
| Nueva Indicación Predicha | Psoriasis (rango 3); colitis ulcerosa (rango 6) |
| Puntaje de Predicción TxGNN | 99.75% (psoriasis); 99.70% (colitis ulcerosa) |
| Nivel de Evidencia | L1 (ambas) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

Las otras 8 predicciones de mayor puntaje (osteoporosis inducida por fármacos, retinopatía diabética grave no proliferativa, retinopatía diabética, osteodistrofia renal, hipotricosis congénita con distrofia macular juvenil, trastorno de liberación plaquetaria, trombastenia de Glanzmann e hiperparatiroidismo secundario no renal) son solo predicciones del modelo (L5), sin ensayos ni literatura: **Hold**.

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción de forma oficial. Según la información conocida, guselkumab es un anticuerpo monoclonal humano que bloquea la subunidad p19 de la interleucina-23. El eje IL-23/Th17 es central en la patogénesis de la psoriasis, por lo que la predicción para esta enfermedad es coherente con su uso establecido.

Para la colitis ulcerosa, la vía IL-23 impulsa la inflamación de la mucosa intestinal en la enfermedad inflamatoria intestinal. El bloqueo selectivo de p19 es mecanísticamente plausible, y el programa QUASAR (Fase 2b/3) respalda la eficacia en colitis ulcerosa moderada a grave.

Para las demás predicciones (osteoporosis, retinopatía, trastornos plaquetarios, etc.) no existe un vínculo mecanístico demostrado con el bloqueo de IL-23.

## Evidencia de Ensayos Clínicos

**Psoriasis** (se listan los 10 más relevantes de 31 ensayos):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03090100](https://clinicaltrials.gov/study/NCT03090100) | Fase 3 | Completado | 1048 | Guselkumab vs secukinumab en psoriasis en placas moderada a grave |
| [NCT03573323](https://clinicaltrials.gov/study/NCT03573323) | Fase 4 | Completado | 1027 | Ixekizumab vs guselkumab en psoriasis en placas a 24 semanas |
| [NCT02207244](https://clinicaltrials.gov/study/NCT02207244) | Fase 3 | Completado | 992 | Eficacia y seguridad con retirada aleatorizada y retratamiento (VOYAGE 2) |
| [NCT02203032](https://clinicaltrials.gov/study/NCT02203032) | Fase 3 | Completado | 872 | Guselkumab en pacientes con respuesta inadecuada a ustekinumab |
| [NCT02207231](https://clinicaltrials.gov/study/NCT02207231) | Fase 3 | Completado | 837 | Eficacia y seguridad frente a placebo y comparador activo (VOYAGE 1) |
| [NCT06039189](https://clinicaltrials.gov/study/NCT06039189) | Fase 3 | Completado | 338 | Guselkumab vs placebo en psoriasis de superficie corporal baja con áreas especiales |
| [NCT04914429](https://clinicaltrials.gov/study/NCT04914429) | Fase 4 | Completado | 327 | Eficacia y seguridad en participantes chinos con psoriasis en placas |
| [NCT05272150](https://clinicaltrials.gov/study/NCT05272150) | Fase 3 | Completado | 211 | Guselkumab vs placebo en piel de color con psoriasis moderada a grave |
| [NCT02951533](https://clinicaltrials.gov/study/NCT02951533) | Fase 3 | Completado | 119 | Guselkumab vs ésteres de ácido fumárico en pacientes sin tratamiento sistémico |
| [NCT04882098](https://clinicaltrials.gov/study/NCT04882098) | Fase 3 | Activo, sin reclutar | 1054 | Guselkumab en artritis psoriásica activa: signos, síntomas y progresión radiográfica |

**Colitis ulcerosa** (se listan los 5 más relevantes de 10 ensayos):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Fase 2b/3 | Activo, sin reclutar | 1064 | QUASAR: eficacia y seguridad frente a placebo en colitis ulcerosa moderada a grave |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Fase 3 | Activo, sin reclutar | 418 | Inducción subcutánea frente a placebo |
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Fase 2b | Activo, sin reclutar | 577 | Terapia combinada guselkumab + golimumab |
| [NCT03662542](https://clinicaltrials.gov/study/NCT03662542) | Fase 2a | Completado | 214 | Prueba de concepto de la combinación guselkumab + golimumab |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Fase 3 | Activo, sin reclutar | 112 | Eficacia en población pediátrica con colitis ulcerosa |

## Evidencia de Literatura

**Psoriasis** (10 más relevantes de 20):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28057360](https://pubmed.ncbi.nlm.nih.gov/28057360/) | 2017 | ECA | J Am Acad Dermatol | VOYAGE 1: guselkumab frente a adalimumab en psoriasis moderada a grave |
| [28057361](https://pubmed.ncbi.nlm.nih.gov/28057361/) | 2017 | ECA | J Am Acad Dermatol | VOYAGE 2: retirada aleatorizada y retratamiento frente a adalimumab |
| [28635018](https://pubmed.ncbi.nlm.nih.gov/28635018/) | 2018 | ECA | Br J Dermatol | NAVIGATE: eficacia en pacientes con respuesta inadecuada a ustekinumab |
| [32880909](https://pubmed.ncbi.nlm.nih.gov/32880909/) | 2021 | ECA | Br J Dermatol | Ixekizumab vs guselkumab (IXORA-R), resultados a 24 semanas |
| [31583255](https://pubmed.ncbi.nlm.nih.gov/31583255/) | 2019 | Metaanálisis en red | J Immunol Res | Eficacia y seguridad de inhibidores de IL-17, IL-12/23 e IL-23 |
| [37436070](https://pubmed.ncbi.nlm.nih.gov/37436070/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Tratamientos sistémicos para psoriasis crónica en placas |
| [37906417](https://pubmed.ncbi.nlm.nih.gov/37906417/) | 2024 | Análisis integrado | Drug Saf | Seguridad a largo plazo en 11 estudios de Fase II/III en psoriasis y artritis psoriásica |
| [34105767](https://pubmed.ncbi.nlm.nih.gov/34105767/) | 2021 | Seguimiento de ECA | Br J Dermatol | Mantenimiento de la respuesta clínica a 5 años (VOYAGE 1 y 2) |
| [32427307](https://pubmed.ncbi.nlm.nih.gov/32427307/) | 2020 | Revisión | JAMA | Fisiopatología, presentación clínica y tratamiento de la psoriasis |
| [38796266](https://pubmed.ncbi.nlm.nih.gov/38796266/) | 2024 | Revisión | Dermatol Clin | Terapias biológicas para psoriasis |

**Colitis ulcerosa** (6 más relevantes de 20):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | ECA | Lancet | QUASAR: estudios de Fase 3 de inducción y mantenimiento con guselkumab |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | ECA | Gastroenterology | QUASAR Fase 2b: estudio de inducción |
| [41544637](https://pubmed.ncbi.nlm.nih.gov/41544637/) | 2026 | ECA | Lancet Gastroenterol Hepatol | ASTRO: inducción subcutánea de guselkumab |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Guía clínica | Gastroenterology | Guía AGA sobre manejo farmacológico de colitis ulcerosa moderada a grave |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Metaanálisis en red | Gastroenterology | Eficacia comparativa de terapias avanzadas (síntesis AGA 2024) |
| [37069321](https://pubmed.ncbi.nlm.nih.gov/37069321/) | 2023 | Revisión | Nat Rev Gastroenterol Hepatol | Inhibición de las vías IL-12 e IL-23 en enfermedad inflamatoria intestinal |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20123370 (cancelado) | TREMFYA® (JANSSEN CILAG S.A.) | Solución inyectable | GUSELKUMAB |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales mostradas:
  - **Mayor**: adalimumab.
  - **Moderada**: simvastatina, apixabán, warfarina, rivaroxabán, dicumarol, lidocaína, hidrocodona, teofilina, roflumilast, aminofilina, oxtrifilina, tacrolimus, fentanilo, nifedipino y toxoide tetánico.
  - **Menor**: sales de zinc (sulfato, acetato, gluconato, cloruro).

No se dispone de datos de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails** (psoriasis y colitis ulcerosa); **Hold** para las demás predicciones.

**Justificación:**
Existen múltiples ECA de Fase 3 completados en psoriasis (nivel L1), pero es una indicación ya establecida, por lo que no constituye un reposicionamiento real. La colitis ulcerosa, respaldada por el programa QUASAR, es la candidata de reposicionamiento más sólida. Las demás predicciones carecen de evidencia.

**Para avanzar se necesita:**
- Verificar el estado regulatorio vigente en Colombia, ya que el único registro figura como cancelado.
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Definir un plan de monitoreo de seguridad a largo plazo, con atención a la interacción mayor con adalimumab.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

