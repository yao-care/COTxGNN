---
layout: default
title: Flunarizine
parent: Solo Predicción del Modelo (L5)
nav_order: 293
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Flunarizine: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L5). Indicación original: No especificada"
---

# Flunarizine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Flunarizina: De Indicación No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Flunarizina es un bloqueador de los canales de calcio que cuenta con registros sanitarios históricos en Colombia, aunque el texto de indicación registrado solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con **14 ensayos clínicos** y **20 publicaciones** en los datos compilados para este informe.
Cabe aclarar que la profilaxis de la migraña ya es un uso establecido de la flunarizina en muchos países, por lo que esta predicción confirma una indicación conocida y no un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro sanitario solo indica "FLUNARIZINA") |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.12% |
| Nivel de Evidencia | L1 (según la clasificación de los datos; ver nota en la conclusión) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información farmacológica compilada, la flunarizina es un bloqueador de los canales de calcio del grupo de las difenilpiperazinas. También tiene actividad bloqueadora de canales de sodio, antihistamínica y antagonista del receptor de dopamina D2. Los datos de farmacología registran interacciones con el receptor D2 y con los canales de calcio tipo T (Cav3.1, Cav3.2 y Cav3.3).

Bloquear la entrada de calcio y estabilizar la excitabilidad neuronal se relaciona de forma plausible con la supresión de la depresión cortical propagada y con la activación trigeminovascular, procesos que subyacen a la fisiopatología de la migraña. Por eso el puntaje alto del modelo (99.12%) es coherente con el mecanismo.

La fuente farmacológica señala que la flunarizina está aprobada en un gran número de países, no está aprobada por la FDA y su uso principal es la profilaxis de la migraña. Por lo tanto, esta predicción confirma un uso ya conocido. El estado "solo cancelados" en Colombia refleja el registro local y no necesariamente la disponibilidad mundial del fármaco.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes para la indicación (la lista completa contiene 14).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Fase 4 | Completado | 62 | Flunarizina 10 mg/día frente a topiramato 50 mg/día en profilaxis de migraña crónica |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completado | 120 | Bloqueo del nervio occipital mayor vs. topiramato vs. flunarizina en migraña episódica |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Fase 4 | Aún sin reclutar | 460 | Ensayo pragmático que compara amitriptilina, flunarizina, topiramato y propranolol como prevención de primera línea |
| [NCT07655700](https://clinicaltrials.gov/study/NCT07655700) | Fase 4 | Aún sin reclutar | 177 | Propranolol, flunarizina y su combinación en profilaxis de migraña |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Desconocido | 84 | Flunarizina vs. amitriptilina en profilaxis de migraña |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Reclutando | 44 | Flunarizina vs. propranolol en migraña pediátrica (PedMIDAS) |
| [NCT07751497](https://clinicaltrials.gov/study/NCT07751497) | Fase 2 | Aún sin reclutar | 400 | Rimegepant vs. flunarizina en prevención de migraña vestibular (no inferioridad) |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Activo, sin reclutar | 60 | Radiofrecuencia pulsada transcutánea vs. bloqueadores de canales de calcio en migraña infantil |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Desconocido | 96 | Acupuntura en migraña sin aura; la flunarizina es probablemente el comparador |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Fase 1 | Aún sin reclutar | 60 | Aguja subcutánea de Fu vs. flunarizina en migraña sin aura |

Otros ensayos incluidos en los datos tienen relevancia indirecta: un estudio farmacocinético de interacción con topiramato (NCT00752466, Fase 1, 75 participantes), estudios de firmas cerebrales del dolor (NCT04702971 y NCT02747940), un estudio de electroacupuntura con 2 participantes (NCT02580968) y un estudio de ácido lipoico adicional en adolescentes (NCT04064814).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Revisión sistemática con modelo económico | Health Technology Assessment | Compara efectividad y costo-efectividad de fármacos preventivos en migraña crónica del adulto |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Metaanálisis en red | JAMA Network Open | Eficacia y seguridad de medicamentos preventivos en migraña pediátrica |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Guía de práctica clínica | Neurology | Recomendaciones de la AAN/AHS para prevención farmacológica de migraña pediátrica |
| [42673559](https://pubmed.ncbi.nlm.nih.gov/42673559/) | 2026 | Revisión sistemática | Neurology | Prevención farmacológica de la migraña en adultos (AAN/AHS) |
| [41572863](https://pubmed.ncbi.nlm.nih.gov/41572863/) | 2026 | Revisión | Dtsch Arztebl Int | Fármacos para la profilaxis de migraña |
| [36257618](https://pubmed.ncbi.nlm.nih.gov/36257618/) | 2022 | Consenso | Arq Neuropsiquiatr | Consenso brasileño sobre tratamiento profiláctico de la migraña episódica |
| [38307673](https://pubmed.ncbi.nlm.nih.gov/38307673/) | 2024 | Revisión | Handb Clin Neurol | Agentes orales no específicos para la prevención de la migraña |
| [39324692](https://pubmed.ncbi.nlm.nih.gov/39324692/) | 2024 | Revisión | Expert Rev Neurother | Opciones de tratamiento actuales y emergentes en migraña vestibular |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | Estudio clínico | Acta Neurol Scand | La combinación de flunarizina con neuroestimulación supraorbitaria transcutánea mejora la profilaxis frente a cada tratamiento por separado |
| [21049704](https://pubmed.ncbi.nlm.nih.gov/21049704/) | 2010 | Revisión | J Assoc Physicians India | Los betabloqueadores, la flunarizina, el topiramato, el valproato y la amitriptilina son fármacos de primera elección en profilaxis |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 43310 | Flunarizina 10 mg tabletas (Memphis Products S.A.) | Tableta | Flunarizina (cancelado) |
| 45084 | Flunarizina 5 mg (Tecnoquímicas S.A.) | Cápsula dura | Flunarizina (cancelado) |
| 20013222 | Flui-Dex 10 mg (Patmar S.A.) | Tableta | Flunarizina (cancelado) |
| 19999406 | Flunarizina 10 mg tabletas (Pentacoop S.A.) | Tableta | Flunarizina (cancelado) |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** se registraron 4 entradas de farmacología, correspondientes a interacciones con dianas y no con otros fármacos: receptor de dopamina D2 y canales de calcio Cav3.1, Cav3.2 y Cav3.3. Se recomienda revisar posibles interacciones con depresores del sistema nervioso central y con otros antimigrañosos.
- **Precauciones sugeridas en el análisis:** vigilar depresión, síntomas extrapiramidales o parkinsonismo, sedación y aumento de peso. Se debe tener cautela en adultos mayores y en pacientes con depresión o enfermedad de Parkinson.

No se dispone de advertencias ni contraindicaciones del prospecto aprobado; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La migraña es una indicación ya establecida de la flunarizina en muchos países, y el mecanismo (bloqueo de canales de calcio) es plausible. Sin embargo, la clasificación L1 de los datos debe interpretarse con cautela. Entre los ensayos listados solo hay unos pocos completados y de comparación directa, de fases 4 o no definidas, y ninguno es un ECA de Fase 3 completado. Además, en Colombia no hay registros vigentes y falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Confirmar los datos del mecanismo de acción en DrugBank.
- Aclarar la situación regulatoria: los 4 registros están cancelados, por lo que sería necesaria una nueva solicitud o reactivación.
- Revisar los resultados de los ensayos comparativos completados (NCT02639598, NCT03712917) y de los que están por iniciar.
- Definir un plan de monitoreo de depresión, síntomas extrapiramidales y sedación, en especial en adultos mayores y en pacientes con depresión o enfermedad de Parkinson.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

