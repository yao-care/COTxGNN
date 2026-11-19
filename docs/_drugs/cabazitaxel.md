---
layout: default
title: Cabazitaxel
parent: Solo Predicción del Modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
monitor_inn: "CABAZITAXEL"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin d disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "HIV infectious disease", "hyperthyroidism", "neuroblastoma", "rheumatoid arthritis"]
last_modified_at: 2026-11-06
description: "Cabazitaxel: nueva indicación predicha, Carcinoma de mama femenino (female breast carcinoma) (nivel de evidencia L5). Indicación original: CABAZITAXEL"
---

# Cabazitaxel
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

## Cabazitaxel: taxano antimitótico → carcinoma de mama femenino (female breast carcinoma)
{: .text-alpha }

## Resumen en Una Frase

Cabazitaxel es un taxano semisintético que estabiliza los microtúbulos e inhibe la división celular, usado como quimioterapia antineoplásica.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino (female breast carcinoma)**,
con **0 ensayos clínicos registrados** y **20 publicaciones**, en su mayoría preclínicas y de revisión, además de un estudio de fase II (GENEVIEVE) en mama.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CABAZITAXEL |
| Nueva Indicación Predicha | Carcinoma de mama femenino (female breast carcinoma) |
| Puntaje de Predicción TxGNN | 0,9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 7) |
| Número de Registros Sanitarios | 7 (vigentes: 7) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cabazitaxel (traducción no oficial): «El cabazitaxel es un inhibidor de los microtúbulos. El cabazitaxel se une a la tubulina y promueve su ensamblaje en microtúbulos, a la vez que inhibe su desensamblaje. Esto conduce a la estabilización de los microtúbulos, lo que da lugar a la inhibición de las funciones celulares mitóticas y de interfase.» Texto original en inglés: "Cabazitaxel is a microtubule inhibitor. Cabazitaxel binds to tubulin and promotes its assembly into microtubules while simultaneously inhibiting disassembly. This leads to the stabilization of microtubules, which results in the inhibition of mitotic and interphase cellular functions." ([DailyMed: Jevtana (cabazitaxel) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de3d9c26-572b-4ea4-9b2d-dd58a2b3e8fa), versión del 2025-10-07; consultado el 2026-11-19). Según la información conocida, cabazitaxel es un taxano semisintético que estabiliza los microtúbulos y bloquea la mitosis. Tiene baja afinidad por la glicoproteína P, lo que puede ayudar a superar la resistencia a paclitaxel y docetaxel.

El cáncer de mama es un tumor sensible a los taxanos, por lo que el mecanismo es biológicamente plausible. Los estudios preclínicos incluidos usan nanoformulaciones (liposferas, vehículos lipídicos nanoestructurados, nanopartículas, micelas) en líneas celulares y xenoinjertos de mama, incluido el cáncer de mama triple negativo.

El estudio de fase II GENEVIEVE comparó cabazitaxel con paclitaxel semanal como tratamiento neoadyuvante en cáncer de mama operable triple negativo o luminal B/HER2 negativo, y su seguimiento a largo plazo se publicó en 2024. Este es el único estudio clínico que aborda directamente la enfermedad predicha. Un estudio de fase I/II en cáncer de mama metastásico (cabazitaxel con capecitabina) también aporta datos clínicos. Los datos compilados no incluyen resultados completos de eficacia de estos estudios, por lo que no se puede asignar un nivel superior a L2 y la certeza de su beneficio sigue sin confirmarse.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en los datos compilados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Fase II aleatorizado (GENEVIEVE) | Eur J Cancer | Cabazitaxel vs paclitaxel semanal neoadyuvante en cáncer de mama HER2 negativo; comparación de la tasa de respuesta patológica completa |
| [38663168](https://pubmed.ncbi.nlm.nih.gov/38663168/) | 2024 | Fase II aleatorizado (seguimiento) | ESMO Open | Resultados a largo plazo de GENEVIEVE en cáncer de mama triple negativo y luminal B/HER2 negativo |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Fase I/II | Eur J Cancer | Cabazitaxel con capecitabina en cáncer de mama metastásico tras antraciclinas y taxanos: dosis máxima tolerada, seguridad y actividad |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclínico | J Immunother Cancer | El efecto de cabazitaxel sobre macrófagos mejora la inmunoterapia dirigida a CD47 en cáncer de mama triple negativo |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclínico | J Control Release | Nanopartículas con cabazitaxel lograron remisión completa en 6 de 8 tumores en un xenoinjerto de mama derivado de paciente |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Revisión/preclínico | Mol Cancer Ther | Mecanismos de resistencia a cabazitaxel; menor resistencia cruzada que paclitaxel y docetaxel en variantes de células MCF-7 |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclínico | Int J Nanomedicine | Eficacia preclínica de variantes de nanopartículas de cianoacrilato con cabazitaxel |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | Preclínico | Acta Pharmacol Sin | Micelas poliméricas con cabazitaxel contra la metástasis de cáncer de mama |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclínico | Chem Phys Lipids | Liposferas con cabazitaxel y timoquinona como combinación sinérgica |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclínico | Colloids Surf B | Vehículos lipídicos nanoestructurados con cabazitaxel frente a líneas celulares de mama |

## Información de Mercado en Colombia

Se registran 5 registros sanitarios (la lista puede ser parcial).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 20176284 | XITACAB® 60MG/1.5ML (40MG/ML) | Solución inyectable |
| 20205910 | Cabazitaxel 60 mg/1.5 mL solución inyectable | Solución inyectable |
| 20039453 | JEVTANA® 60 mg/1.5 mL solución concentrada para infusión | Solución concentrada para infusión |
| 20104913 | CABAZRED 60 mg/1.5 mL | Solución concentrada para infusión |
| 20207930 | CABAXITAL® | Solución concentrada para infusión |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (taxano, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Alto (la neutropenia es el efecto adverso más frecuente en los taxanos; también se describe neuropatía) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, bilirrubina |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones. Entre las de mayor gravedad figuran deferiprona y lexidronam de samario (153Sm) (Mayor). Entre las moderadas están aprepitant, claritromicina, clotrimazol, metronidazol, miconazol, rosuvastatina, simvastatina, ticagrelor, cobicistat y deferasirox. Varias reflejan la vía metabólica CYP3A4.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un estudio de fase II en cáncer de mama (GENEVIEVE) con seguimiento a largo plazo, además de un estudio de fase I/II y abundante evidencia preclínica. No hay ensayos de fase 3 ni ensayos registrados en los datos compilados, y el perfil de mielosupresión exige precaución.

**Para avanzar se necesita:**
- Revisar los resultados completos de eficacia y seguridad de GENEVIEVE y de los estudios de fase I/II
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de los registros sanitarios
- Un plan de monitoreo hematológico y de manejo de interacciones (especialmente inhibidores e inductores de CYP3A4)
- Ensayos de fase 3 o evidencia comparativa frente a los estándares actuales en cáncer de mama

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Jevtana (cabazitaxel) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de3d9c26-572b-4ea4-9b2d-dd58a2b3e8fa) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

