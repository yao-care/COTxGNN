---
layout: default
title: Metronidazole
parent: Solo Predicción del Modelo (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Metronidazole: nueva indicación predicha, Neumocistosis (nivel de evidencia L5). Indicación original: Metronidazol / combinaciones de imidazol derivados"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Metronidazol: De Metronidazol (derivados imidazólicos) a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

Metronidazol es un antimicrobiano derivado del imidazol, con registros sanitarios en Colombia para metronidazol solo y en combinaciones de imidazoles.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero no hay ensayos clínicos y la literatura disponible (10 publicaciones) es solo descriptiva (revisiones y reportes de caso), sin evidencia directa de eficacia.

<!-- review:begin co-lic-20261105-metronidazole-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Metronidazol es un antimicrobiano derivado del imidazol, con registros sanitarios en Colombia para metronidazol solo y en combinaciones de imidazoles (hoy todos cancelados)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-metronidazole-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Metronidazol / combinaciones de imidazol derivados |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

<!-- review:begin co-lic-20261112-metronidazole-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "3 registros vigentes" Corregido: el número de registros sanitarios escrito en el texto no coincidía con los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23); el texto ya no indica una cifra fija. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-metronidazole-1 -->

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metronidazole (traducción no oficial): «El metronidazol, un nitroimidazol, ejerce efectos antibacterianos en un entorno anaerobio contra la mayoría de los anaerobios obligados. Una vez que el metronidazol ingresa en el microorganismo por difusión pasiva y se activa en el citoplasma de las bacterias anaerobias sensibles, se reduce; este proceso incluye donantes intracelulares de transporte de electrones, como la ferredoxina, y la transferencia de un electrón al grupo nitro del metronidazol, lo que conduce a la formación de un radical libre nitroso de vida corta.» Texto original en inglés: "Metronidazole, a nitroimidazole, exerts antibacterial effects in an anaerobic environment against most obligate anaerobes. Once metronidazole enters the organism by passive diffusion and activated in the cytoplasm of susceptible anaerobic bacteria, it is reduced; this process includes intra-cellular electron transport donors such as ferredoxin and transfer of an electron to the nitro group of the metronidazole leading to formation of a short-lived nitroso free radical." ([DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255), versión del 2026-11-02; consultado el 2026-11-19). Según el conocimiento farmacológico general, metronidazol es un nitroimidazol activo contra bacterias anaerobias y protozoos (Trichomonas, Giardia, Entamoeba), mediante la activación reductora de su grupo nitro.

La relación con la nueva indicación es débil. *Pneumocystis jirovecii* es un hongo que carece de la vía de activación dependiente de nitrorreductasa, por lo que **no existe una justificación mecanística establecida**. El puntaje alto de TxGNN probablemente refleja la cercanía en la red del conocimiento con fármacos antiparasitarios, y no una actividad real. El tratamiento estándar es trimetoprima-sulfametoxazol.

En conjunto, esta predicción debe considerarse una señal del modelo sin respaldo biológico claro. Entre las demás candidatas, la **poliposis en capuchón (cap polyposis)** (puntaje TxGNN 0.9973, nivel L4) tiene la plausibilidad mecanística más sólida según los datos compilados, y podría merecer una evaluación aparte.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revisión | Mayo Clin Proc | Panorama de agentes antiparasitarios, resistencia y toxicidad; no demuestra eficacia de metronidazol en neumocistosis |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisión | Am Fam Physician | Metronidazol es de elección en amebiasis y tricomoniasis; para neumonía por Pneumocystis se indica trimetoprima-sulfametoxazol |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revisión | Clin Pharmacokinet | Justificación farmacocinética de la terapia antiprotozoaria en huéspedes normales e inmunocomprometidos |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisión | Clin Pharm | Terapias para infecciones oportunistas del SIDA; la neumonía por P. carinii es la más frecuente |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revisión | Top Antivir Med | Infecciones oportunistas relacionadas con VIH siguen siendo relevantes en 2015 |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Reporte de caso | Am Rev Respir Dis | Neumonía por P. carinii y citomegalovirus en adulto previamente sano, antes tratado con metronidazol y tetraciclina por diarrea |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Reporte de caso | Kansenshogaku Zasshi | Dos pacientes con SIDA; metronidazol se usó para amebiasis, no para neumocistosis |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revisión | Rev Infect Dis | Crítica de ensayos de profilaxis antimicrobiana |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Reporte de caso | J Formos Med Assoc | Perforación de colon en paciente con SIDA por citomegalovirus y colitis amebiana |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Reporte de caso | J Med Case Rep | Absceso cerebeloso por *Streptococcus intermedius* como primera manifestación de sarcoidosis |

Ninguna publicación muestra que metronidazol sea eficaz contra la neumocistosis; la relación es contextual (pacientes con SIDA u otras infecciones tratadas con metronidazol).

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 1980496 | METRONIDAZOL 500 MG TABLETAS | TABLETA | METRONIDAZOL | Vigente |
| 1983837 | METRONIDAZOL 500 MG OVULOS | OVULO | METRONIDAZOL | Vigente |
| 19908154 | GYNOFLOR® CREMA VAGINAL | CREMA VAGINAL | COMBINACIONES DE IMIDAZOL DERIVADOS | Vigente |
| 19924454 | FLAGYL® ÓVULOS VAGINALES | OVULO | NISTATINA COMBINACIONES | Vigente |
| 19934637 | METARSAL N CAPSULAS | CAPSULA DURA | COMBINACIONES DE IMIDAZOL DERIVADOS | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): insuficiencia hepática, enfermedad hepática, enfermedad renal, epilepsia, enfermedades hematológicas (neutropenia, leucopenia, agranulocitosis), trastornos de la coagulación, neuropatía periférica y enfermedades del sistema nervioso periférico, enfermedades cerebrales, enfermedades del nervio óptico y vías visuales, insuficiencia cardíaca congestiva, diabetes mellitus y cetoacidosis diabética, gota, enfermedad de la vesícula biliar, dermatitis, meningitis no infecciosa, piouréter y abuso o dependencia de sustancias.
- **Interacciones farmacológicas** (100 interacciones registradas; se muestran las más relevantes):
  - **Mayor:** etanol (riesgo de reacción tipo disulfiram).
  - **Moderadas:** paclitaxel, adalimumab, trastuzumab emtansina, etinilestradiol, estradiol, butalbital, amiodarona, celecoxib, amobarbital, loperamida.
  - **Menores:** abiraterona, tramadol, famotidina, salbutamol, alfuzosina, amisulprida, amitriptilina, anagrelida, propofol.

No se dispuso de advertencias ni contraindicaciones del prospecto de INVIMA; se recomienda consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos, la literatura es solo descriptiva y no muestra eficacia, y el mecanismo de acción del metronidazol no es plausible frente a *Pneumocystis* (hongo sin la vía de activación nitrorreductasa). Existe un tratamiento estándar eficaz (trimetoprima-sulfametoxazol). Además, el medicamento está comercializado en Colombia y cuenta con registros vigentes.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y estudios preclínicos que justifiquen actividad contra *Pneumocystis*
- Estudios in vitro o en modelos animales de eficacia
- Prospecto de INVIMA con advertencias y contraindicaciones (brecha de datos bloqueante para el tamizaje de seguridad)
- Considerar priorizar otras indicaciones con mejor respaldo, como la poliposis en capuchón (L4) y otras candidatas de enfermedad inflamatoria intestinal o úlceras vulvares

<!-- review:begin co-lic-20261031-metronidazole-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria (registros cancelados) antes de cualquier desarrollo local / Considerar priorizar otras indicaciones con mejor respaldo, como la poliposis en capuchón (L4) y otras candidatas de enfermedad inflamatoria intestinal o úlceras vulvares" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-metronidazole-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registros cancelados) antes de cualquier desarrollo local" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "(hoy todos cancelados)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-24 | Número de registros sanitarios corregido (sin cifra fija; ver Resumen rápido) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

