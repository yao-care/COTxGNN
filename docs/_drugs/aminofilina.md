---
layout: default
title: Aminofilina
parent: Solo Predicción del Modelo (L5)
nav_order: 48
evidence_level: L5
indication_count: 9
drugbank_id: DB01223
monitor_inn: "Aminophylline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
last_modified_at: 2026-11-24
description: "Aminofilina: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: AMINOFILINA"
---

# Aminofilina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Aminofilina: Trastorno de migraña (migraine disorder)
{: .text-alpha }

## Resumen en Una Frase

Aminofilina es una metilxantina (antagonista de los receptores de adenosina e inhibidor de la fosfodiesterasa) con registro sanitario vigente en Colombia en forma de solución inyectable.
El modelo TxGNN predice que podría ser útil para el **trastorno de migraña (migraine disorder)**, pero actualmente no hay ensayos clínicos registrados y solo se dispone de **4 publicaciones** (una revisión narrativa de 2023, dos reportes de caso y una revisión antigua de 1964).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AMINOFILINA |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Aminofilina (traducción no oficial): «La teofilina tiene dos acciones distintas en las vías respiratorias de los pacientes con obstrucción reversible: la relajación del músculo liso (es decir, broncodilatación) y la supresión de la respuesta de las vías respiratorias a los estímulos (es decir, efectos profilácticos no broncodilatadores).» Texto original en inglés: "Theophylline has two distinct actions in the airways of patients with reversible obstruction; smooth muscle relaxation (i.e., bronchodilation) and suppression of the response of the airways to stimuli (i.e., nonbronchodilator prophylactic effects)." ([DailyMed: aminophylline prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52bbc6cd-4baf-7859-e063-6394a90ac87d), versión del 2026-05-26; consultado el 2026-11-19). Según la información conocida, la aminofilina es una metilxantina que bloquea los receptores de adenosina e inhibe la fosfodiesterasa.

La señalización de adenosina participa en la activación trigeminovascular y en la vasodilatación cerebral, por lo que antagonizarla es mecanísticamente plausible en cefalea y migraña. Una revisión de 2023 (PMID 38059379) plantea que la migraña podría estar asociada a un metabolismo energético cerebral alterado con niveles elevados de adenosina, y que la aminofilina podría aliviar el dolor, en especial la cefalea pospunción dural. Un reporte de caso describe además un episodio de migraña hemipléjica desencadenado por regadenosón, un agonista de adenosina, lo que respalda el mecanismo de forma indirecta.

Aun así, el respaldo es de tipo narrativo y de casos individuales. No hay ensayos clínicos controlados que evalúen la aminofilina en migraña.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Revisión | Pain management | La migraña podría estar impulsada por un metabolismo energético cerebral alterado con adenosina elevada; la aminofilina, antagonista de adenosina, podría dar alivio en dolor, sobre todo en cefalea pospunción dural |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Reporte de caso | Journal of Nuclear Cardiology | Episodio de migraña hemipléjica desencadenado por regadenosón (agonista de adenosina A2A) |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Reporte de caso | Canadian Journal of Cardiology | Paciente con síndrome X por efecto excesivo de adenosina ("migraña miocárdica") |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Revisión | Aggiornamenti Clinicoterapeutici | Revisión antigua sobre cefaleas de origen médico, sin resumen disponible |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19924459 | AMINOFILINA 250 MG / 10 ML SOLUCION INYECTABLE | SOLUCION INYECTABLE | AMINOFILINA | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado evalúa directamente la aminofilina como tratamiento de la migraña en ensayos clínicos; la evidencia se limita a una revisión narrativa y reportes de caso, por lo que el nivel de evidencia es L5 y la predicción sigue siendo una pregunta de investigación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde fuentes farmacológicas
- Advertencias y contraindicaciones del prospecto aprobado por INVIMA
- Estudios clínicos controlados (por ejemplo, fase 2) en migraña o cefalea
- Evaluación de la vía de administración (solución inyectable) frente a las necesidades de la migraña
- Revisión de seguridad, incluidos riesgos cardiovasculares y de interacción con otros fármacos

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: aminophylline prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52bbc6cd-4baf-7859-e063-6394a90ac87d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

