---
layout: default
title: Rivastigmine
parent: Solo Predicción del Modelo (L5)
nav_order: 569
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Rivastigmine: nueva indicación predicha, Glaucoma (nivel de evidencia L5). Indicación original: RIVASTIGMINA"
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
---

# Rivastigmine
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

## Rivastigmina: De Rivastigmina (indicación sin detallar) a Glaucoma
{: .text-alpha }

## Resumen en Una Frase

Rivastigmina es un inhibidor de colinesterasas que figura en registros sanitarios de INVIMA (parches transdérmicos), cuyo texto de indicación solo indica "RIVASTIGMINA"; en la literatura se utiliza en la enfermedad de Alzheimer.
El modelo TxGNN predice que podría ser efectivo para **glaucoma**,
con **0 ensayos clínicos** y **3 publicaciones** (una de ellas un estudio preclínico en conejos) que respaldan esta dirección de forma indirecta.

<!-- review:begin co-lic-20261112-rivastigmine-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "figura en dos registros sanitarios de INVIMA (parches transdérmicos)" Corregido: el número de registros sanitarios escrito en el texto no coincidía con los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23); todos corresponden a sistemas transdérmicos; el texto ya no indica una cifra fija. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-rivastigmine-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RIVASTIGMINA (el registro no detalla la indicación; según la farmacología, se usa en enfermedad de Alzheimer) |
| Nueva Indicación Predicha | Glaucoma |
| Puntaje de Predicción TxGNN | 0.9927 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 11) |
| Número de Registros Sanitarios | 11 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Rivastigmine (traducción no oficial): «Aunque se desconoce el mecanismo de acción exacto de la rivastigmina, se cree que ejerce su efecto terapéutico potenciando la función colinérgica. Esto se logra aumentando la concentración de acetilcolina mediante la inhibición reversible de su hidrólisis por la colinesterasa.» Texto original en inglés: "Although the precise mechanism of action of rivastigmine is unknown, it is thought to exert its therapeutic effect by enhancing cholinergic function. This is accomplished by increasing the concentration of acetylcholine through reversible inhibition of its hydrolysis by cholinesterase." ([DailyMed: rivastigmine tartrate prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52781229-ee82-43f9-a113-4419a611978d), versión del 2025-11-11; consultado el 2026-11-19). Según la información farmacológica compilada, la rivastigmina inhibe la acetilcolinesterasa (ACHE) y la butirilcolinesterasa (BCHE), lo que aumenta los niveles de acetilcolina. Su uso conocido es la enfermedad de Alzheimer, y también se ha explorado en deterioro cognitivo vascular y en disfunción de la marcha en enfermedad de Parkinson (ensayo de Fase 2).

En el ojo, más acetilcolina sobre los receptores muscarínicos puede contraer el músculo ciliar y aumentar el drenaje por la malla trabecular, lo que reduciría la presión intraocular (PIO), principal factor de riesgo modificable del glaucoma. Un estudio en conejos con rivastigmina tópica reportó descenso de la PIO, y una revisión de 2024 respalda el papel de los agentes colinérgicos en la reducción de la PIO.

Esta evidencia es indirecta y preclínica. No hay ensayos en humanos con glaucoma, y el puntaje alto de TxGNN es una predicción computacional, no una validación clínica. Además, la similitud con la indicación original (Alzheimer) es de tipo mecanístico (inhibición colinesterásica), no de enfermedad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclínico (conejos) | J Ocul Pharmacol Ther | La rivastigmina tópica, inhibidor selectivo de acetilcolinesterasa, redujo la presión intraocular en conejos normotensos |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revisión / computacional | Front Mol Biosci | Analiza los agentes colinérgicos en la reducción de la PIO; los agonistas M3 aprobados tienen limitaciones por efectos adversos colinérgicos sistémicos |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revisión | Expert Opin Ther Pat | Revisión de patentes sobre inhibidores y reactivadores de AChE; la inhibición leve tiene relevancia terapéutica en Alzheimer, miastenia gravis y glaucoma |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19985874 | EXELON PARCHES 9 MG | TRANSDERMICOS | RIVASTIGMINA | Vigente |
| 19985986 | EXELON®PARCHES 27 MG | TRANSDERMICOS | RIVASTIGMINA | Vigente |
| 19985987 | EXELON PARCHES 18 MG | TRANSDERMICOS | RIVASTIGMINA | Vigente |
| 20242182 | DURIVAST® 9.5MG/24H | TRANSDERMICOS | RIVASTIGMINA | Vigente |
| 20242522 | DURIVAST® 4.6MG/24H | SISTEMA TRANSDÉRMICO DE LIBERACIÓN PROLONGADA (PARCHE) | RIVASTIGMINA | Vigente |

Se muestran 5 de 11 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la rivastigmina con contraindicación en: epilepsia, enfermedad de los ganglios basales, distonía focal de la mano, blefaroespasmo, enfermedad pulmonar obstructiva crónica (incluida la de inicio temprano severo), asma (intrínseco y alérgico), enfermedad diarreica, paro cardíaco súbito, enfermedad de conducción cardíaca, anorexia nerviosa, úlcera péptica activa, obstrucción de vías urinarias, síndrome del seno enfermo (incluida la forma familiar), trastornos parkinsonianos/enfermedad de Parkinson y bloqueo auriculoventricular.
- **Interacciones farmacológicas:** la consulta devolvió 2 registros, ambos de interacción farmacológica con dianas (no con otros fármacos): acetilcolinesterasa (ACHE) y butirilcolinesterasa (BCHE), que corresponden a su mecanismo de acción.
- **Seguridad ocular:** los agentes colinérgicos pueden causar miosis, espasmo de acomodación y, raramente, riesgo de cierre angular; habría que evaluarlo antes de cualquier uso oftálmico.

<!-- review:begin co-lic-20261105-rivastigmine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros pertenecen a BIOTOSCANA FARMA S.A. y están cancelados; no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-rivastigmine-1 -->

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo preclínica e indirecta (nivel L4), sin ensayos en humanos para glaucoma. Además, faltan datos de seguridad del prospecto. El puntaje de TxGNN por sí solo no basta para avanzar.

<!-- review:begin co-lic-20261105-rivastigmine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay producto vigente en Colombia y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-rivastigmine-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos bloqueante para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos adicionales y, de ser favorables, ensayos en humanos sobre reducción de la PIO.
- Evaluar la seguridad ocular (miosis, espasmo de acomodación, riesgo de cierre angular) y la viabilidad de una formulación oftálmica, ya que los productos registrados son transdérmicos.
- Definir la vía de acceso regulatorio.

<!-- review:begin co-lic-20261105-rivastigmine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Definir la vía de acceso regulatorio, dado que los dos registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-rivastigmine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambos registros pertenecen a BIOTOSCANA FARMA S.A. y están cancelados; no hay productos vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "no hay producto vigente en Colombia y" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los dos registros están cancelados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-24 | Número de registros sanitarios corregido (sin cifra fija; ver Resumen rápido) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: rivastigmine tartrate prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52781229-ee82-43f9-a113-4419a611978d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

