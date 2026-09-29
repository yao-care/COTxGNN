---
layout: default
title: Metronidazole
parent: Solo Predicción del Modelo (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazol: De Indicación Original No Detallada en el Registro (Nitroimidazol Antimicrobiano) a Neumocistosis

## Resumen en Una Frase

Metronidazol es un antimicrobiano de la familia de los nitroimidazoles, comercializado en Colombia en tabletas y formas vaginales. El registro sanitario no detalla su indicación clínica original: solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero **no hay ningún ensayo clínico relevante** y la literatura recuperada (10 publicaciones revisadas) no muestra eficacia de metronidazol contra *Pneumocystis*. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METRONIDAZOL (el registro no especifica una indicación clínica) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, metronidazol es un nitroimidazol activo contra bacterias anaerobias y protozoos, pero no contra hongos.

Aquí la predicción **no resulta razonable** desde el punto de vista mecanístico. *Pneumocystis* es un hongo y metronidazol no tiene actividad antifúngica. El tratamiento estándar de la neumocistosis es trimetoprima-sulfametoxazol (TMP-SMX), y una de las revisiones recuperadas (1980) ya lo señala así.

El puntaje alto de TxGNN probablemente es un artefacto del grafo de conocimiento, causado por vecinos compartidos como "antiinfeccioso" o "infección oportunista". Los casos clínicos recuperados mencionan metronidazol solo como tratamiento de una infección concurrente (por ejemplo, amebiasis), no como tratamiento de la neumocistosis.

## Evidencia de Ensayos Clínicos

Se recuperaron 25 ensayos, y **ninguno evalúa metronidazol ni *Pneumocystis***. La clasificación de relevancia otorga grado C a los 10 primeros y deja el resto pendiente. Se muestran los 10 clasificados:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03451630](https://clinicaltrials.gov/study/NCT03451630) | No aplica | Completado | 1400 | Modelos integrados de atención para adultos con necesidades complejas; sin relación con el fármaco |
| [NCT02362750](https://clinicaltrials.gov/study/NCT02362750) | No aplica | Completado | 991 | Modelos de atención a sobrevivientes de cáncer; no relacionado |
| [NCT04576715](https://clinicaltrials.gov/study/NCT04576715) | No aplica | Completado | 101 | Manejo del traumatismo craneal leve pediátrico; no relacionado |
| [NCT06638099](https://clinicaltrials.gov/study/NCT06638099) | No aplica | Completado | 195 | Uso de monitores continuos de glucosa en diabetes tipo 2; no relacionado |
| [NCT04198974](https://clinicaltrials.gov/study/NCT04198974) | No aplica | Activo, sin reclutar | 12500 | Prevención del consumo de sustancias en adolescentes; no relacionado |
| [NCT02208947](https://clinicaltrials.gov/study/NCT02208947) | Fase 3 | Terminado | 77 | Incentivos para planificación anticipada de cuidados; aunque figura como Fase 3, no es un ensayo farmacológico |
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | No aplica | Completado | 65 | Herramienta de supervivencia en cáncer de cabeza y cuello; no relacionado |
| [NCT06597123](https://clinicaltrials.gov/study/NCT06597123) | No aplica | No reclutando aún | 150 | Entrenamiento en entrevista motivacional con IA; no relacionado |
| [NCT03542084](https://clinicaltrials.gov/study/NCT03542084) | No aplica | Completado | 305 | Interconsultas de endocrinología para control glucémico; no relacionado |
| [NCT04463914](https://clinicaltrials.gov/study/NCT04463914) | No aplica | Completado | 649 | Aplicación móvil de activación conductual para depresión; no relacionado |

## Evidencia de Literatura

Se priorizan las revisiones sobre los reportes de caso. Ninguna publicación demuestra eficacia de metronidazol en neumocistosis.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revisión | Mayo Clin Proc | Panorama de los antiparasitarios y sus problemas (resistencia, toxicidad, disponibilidad) |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisión | Am Fam Physician | Metronidazol para amebiasis y tricomoniasis; TMP-SMX como fármaco de elección para neumonía por *Pneumocystis* |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revisión | Clin Pharmacokinet | Justificación farmacocinética de las terapias antiprotozoarias |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisión | Clin Pharm | Complicaciones infecciosas del SIDA; la neumonía por *P. carinii* es la más frecuente |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revisión | Top Antivir Med | Las infecciones oportunistas asociadas al VIH siguen siendo relevantes; sin datos de metronidazol |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revisión | Rev Infect Dis | Crítica de los ensayos de profilaxis antimicrobiana; tema general, no específico |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Reporte de caso | Am Rev Respir Dis | Neumonía por *P. carinii* y citomegalovirus en un adulto previamente tratado con metronidazol por diarrea; el fármaco no se usó como tratamiento |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Reporte de caso | Kansenshogaku Zasshi | Metronidazol resolvió una disentería amebiana; la neumonía por *P. carinii* apareció después, sin relación de tratamiento |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Reporte de caso | J Formos Med Assoc | Perforación de colon en un paciente con SIDA por citomegalovirus y amebiasis; sin neumocistosis |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Reporte de caso | J Med Case Rep | Absceso cerebeloso por *S. intermedius* como primera manifestación de sarcoidosis; tangencial |

## Información de Mercado en Colombia

El paquete de evidencia lista 5 filas, pero corresponden a solo 2 registros únicos (de un total de 20 registros sanitarios).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20174992 | SOLMETRIN® 500 MG TABLETAS (ANGLOPHARMA S.A.) | Tableta | METRONIDAZOL |
| 20162295 | METRONIDAZOL 10% + CLOTRIMAZOL 2% (MEMPHIS PRODUCTS S.A.) | Crema vaginal | COMBINACIONES DE IMIDAZOL DERIVADOS |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene nivel de evidencia L5: no hay ensayos relevantes ni literatura que respalde eficacia. Además, no existe un vínculo mecanístico plausible, porque metronidazol no tiene actividad antifúngica y la terapia estándar (TMP-SMX) ya está bien establecida.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA, hoy sin datos.
- Solo si hubiera hipótesis mecanística nueva, estudios preclínicos in vitro contra *Pneumocystis*. En caso contrario, no continuar con esta indicación.
- Redirigir el esfuerzo a otras predicciones del mismo fármaco con más respaldo: **úlcera de vulva** (nivel L3, serie retrospectiva de 22 pacientes con enfermedad de Crohn vulvar más casos de amebiasis genital) y **pólipos con capuchón (*cap polyposis*)** (nivel L4, reportes de caso).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

