---
layout: default
title: Posaconazole
parent: Solo Predicción del Modelo (L5)
nav_order: 524
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
description: "Posaconazole: nueva indicación predicha, Neumocistosis (nivel de evidencia L5). Indicación original: No especificada en detalle"
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
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

## Posaconazol: De Posaconazol (indicación no detallada en el registro) a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

Posaconazol es un antifúngico triazólico, registrado en Colombia en tabletas de liberación retardada, cuyo texto de indicación en el registro sanitario solo indica el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero la evidencia real es muy limitada: **1 ensayo clínico** (que evalúa otro fármaco, rezafungina) y **5 publicaciones** de carácter general (guías, revisiones y un estudio de cohorte), ninguna de las cuales demuestra eficacia de posaconazol en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en detalle (el registro solo indica "Posaconazol"); clase antifúngica triazólica |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Posaconazole (traducción no oficial): «El posaconazol es un antifúngico azólico. […] El posaconazol bloquea la síntesis de ergosterol, un componente clave de la membrana celular fúngica, mediante la inhibición de la enzima lanosterol 14α-desmetilasa dependiente del citocromo P-450, responsable de la conversión del lanosterol en ergosterol en la membrana celular fúngica. Esto da lugar a una acumulación de precursores de esteroles metilados y a una depleción de ergosterol en la membrana celular, lo que debilita la estructura y la función de la membrana celular fúngica.» Texto original en inglés: "Posaconazole is an azole antifungal agent. […] Posaconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84), versión del 2026-02-13; consultado el 2026-11-19). Según el conocimiento farmacológico general, posaconazol es un antifúngico triazólico que inhibe la lanosterol 14-alfa-desmetilasa (CYP51), bloqueando la síntesis de ergosterol en la membrana fúngica.

Sin embargo, la plausibilidad mecanística para neumocistosis es débil. *Pneumocystis jirovecii* carece de ergosterol en su membrana y utiliza colesterol y otros esteroles, por lo que el mecanismo de los azoles no tiene una diana clara en este organismo. El puntaje tan alto de TxGNN (0.9977) probablemente refleja la cercanía en la red de conocimiento con otros antifúngicos y enfermedades fúngicas invasivas, más que una verdadera afinidad mecanística.

Como referencia, el tratamiento de primera línea de la neumocistosis es trimetoprima-sulfametoxazol. Las equinocandinas (por ejemplo, rezafungina) se han investigado como posible complemento porque inhiben la beta-1,3-glucano sintasa de la forma quística de *Pneumocystis*; este mecanismo es distinto al de posaconazol.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fase 3 | Completado | 602 | Rezafungina intravenosa frente al régimen antimicrobiano estándar para prevenir enfermedades fúngicas invasivas en adultos sometidos a trasplante alogénico de sangre y médula ósea (estudio ReSPECT). No evalúa posaconazol para neumocistosis; relevancia baja. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guía/Revisión | The Lancet. Infectious Diseases | Recomendaciones de la Sociedad Británica de Micología Médica (actualización 2025) para el diagnóstico de enfermedades fúngicas graves; no aborda eficacia de posaconazol en neumocistosis |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guía/Revisión | Zhonghua Jie He He Hu Xi Za Zhi | Guía china 2025 para el diagnóstico y manejo de enfermedades fúngicas pulmonares invasivas |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revisión | Swiss Medical Weekly | Panorama de candidiasis invasiva, aspergilosis, criptococosis y neumonía por *Pneumocystis*; menciona que la profilaxis con posaconazol (activo frente a mohos) redujo infecciones fúngicas invasivas en pacientes hemato-oncológicos de alto riesgo |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clinical Pharmacokinetics | Penetración de antiinfecciosos (incluidos antifúngicos) en el líquido de revestimiento epitelial pulmonar |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohorte | Transplant Infectious Disease | Complicaciones infecciosas en la enfermedad injerto contra huésped aguda tras trasplante hepático |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20064520 | NOXAFIL ® TABLETAS RECUBIERTAS DE LIBERACIÓN RETARDADA | TABLETA DE LIBERACION RETARDADA | POSACONAZOL | Vigente |
| 20195133 | POSACONAZOL 100 MG TABLETAS GASTRORRESISTENTES | TABLETA DE LIBERACION RETARDADA | POSACONAZOL | Vigente |
| 20263473 | POZASANA® 100 MG TABLETA DE LIBERACIÓN RETARDADA | TABLETA DE LIBERACION RETARDADA | POSACONAZOL | Vigente |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 269 interacciones en total. Entre las de nivel **mayor** figuran loperamida, triamcinolona y budesonida. Entre las de nivel **moderado** figuran famotidina, ranitidina, rabeprazol, omeprazol, cimetidina, hidrocortisona, dexametasona, betametasona, aprepitant, claritromicina, bisacodilo, ácido picosulfúrico, polietilenglicol 3350 con electrolitos y saxagliptina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta, pero no hay estudios que evalúen posaconazol en neumocistosis y el mecanismo azólico carece de una diana clara en *Pneumocystis*.

<!-- review:begin co-lic-20261105-posaconazole-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción de TxGNN es muy alta, pero no hay estudios que evalúen posaconazol en neumocistosis y el mecanismo azólico carece de una diana clara en *Pneumocystis*. Además, el fármaco no tiene registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-posaconazole-2 -->

**Para avanzar se necesita:**
- Datos de mecanismo de acción verificados en fuentes primarias (por ejemplo, DrugBank)
- Estudios preclínicos o clínicos que evalúen directamente posaconazol frente a *Pneumocystis*, comparado con trimetoprima-sulfametoxazol
- Prospecto del INVIMA con advertencias y contraindicaciones para completar el tamizaje de seguridad
- Análisis de compatibilidad de vías de administración y similitud con la indicación original

<!-- review:begin co-lic-20261031-posaconazole-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria (registros cancelados) y la indicación aprobada originalmente / Análisis de compatibilidad de vías de administración y similitud con la indicación original" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-posaconazole-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registros cancelados) y la indicación aprobada originalmente" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el fármaco no tiene registros sanitarios vigentes en Colombia" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

