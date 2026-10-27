---
layout: default
title: Metronidazole
parent: Solo Predicción del Modelo (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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

Metronidazol es un antimicrobiano derivado del imidazol, con registros sanitarios en Colombia para metronidazol solo y en combinaciones de imidazoles (hoy todos cancelados).
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero no hay ensayos clínicos y la literatura disponible (10 publicaciones) es solo descriptiva (revisiones y reportes de caso), sin evidencia directa de eficacia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Metronidazol / combinaciones de imidazol derivados |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, metronidazol es un nitroimidazol activo contra bacterias anaerobias y protozoos (Trichomonas, Giardia, Entamoeba), mediante la activación reductora de su grupo nitro.

La relación con la nueva indicación es débil. *Pneumocystis jirovecii* es un hongo que carece de la vía de activación dependiente de nitrorreductasa, por lo que **no existe una justificación mecanística establecida**. El puntaje alto de TxGNN probablemente refleja la cercanía en la red del conocimiento con fármacos antiparasitarios, y no una actividad real. El tratamiento estándar es trimetoprima-sulfametoxazol.

En conjunto, esta predicción debe considerarse una señal del modelo sin respaldo biológico claro. Entre las demás candidatas, la **poliposis en capuchón (cap polyposis)** (puntaje TxGNN 99.73%, nivel L4) tiene la plausibilidad mecanística más sólida según los datos compilados, y podría merecer una evaluación aparte.

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20174992 | SOLMETRIN® 500 MG TABLETAS | Tableta | Metronidazol | Cancelado |
| 20162295 | Metronidazol 10% + Clotrimazol 2% | Crema vaginal | Combinaciones de imidazol derivados | Cancelado |
| 20052649 | GYNECLOR | Óvulo | Combinaciones de imidazol derivados | Cancelado |

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
No existen ensayos clínicos, la literatura es solo descriptiva y no muestra eficacia, y el mecanismo de acción del metronidazol no es plausible frente a *Pneumocystis* (hongo sin la vía de activación nitrorreductasa). Existe un tratamiento estándar eficaz (trimetoprima-sulfametoxazol). Además, todos los registros en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y estudios preclínicos que justifiquen actividad contra *Pneumocystis*
- Estudios in vitro o en modelos animales de eficacia
- Prospecto de INVIMA con advertencias y contraindicaciones (brecha de datos bloqueante para el tamizaje de seguridad)
- Aclarar la situación regulatoria (registros cancelados) antes de cualquier desarrollo local
- Considerar priorizar otras indicaciones con mejor respaldo, como la poliposis en capuchón (L4) y otras candidatas de enfermedad inflamatoria intestinal o úlceras vulvares
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

