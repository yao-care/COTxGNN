---
layout: default
title: Rivastigmine
parent: Evidencia Moderada (L3-L4)
nav_order: 569
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Rivastigmine: nueva indicación predicha, Glaucoma (nivel de evidencia L4). Indicación original: RIVASTIGMINA"
---

# Rivastigmine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Rivastigmina: De Rivastigmina (indicación sin detallar) a Glaucoma

## Resumen en Una Frase

Rivastigmina es un inhibidor de colinesterasas que figura en dos registros sanitarios de INVIMA (parches transdérmicos), cuyo texto de indicación solo indica "RIVASTIGMINA"; en la literatura se utiliza en la enfermedad de Alzheimer.
El modelo TxGNN predice que podría ser efectivo para **glaucoma**,
con **0 ensayos clínicos** y **3 publicaciones** (una de ellas un estudio preclínico en conejos) que respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RIVASTIGMINA (el registro no detalla la indicación; según la farmacología, se usa en enfermedad de Alzheimer) |
| Nueva Indicación Predicha | Glaucoma |
| Puntaje de Predicción TxGNN | 99.27% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelados (sin producto vigente) |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información farmacológica compilada, la rivastigmina inhibe la acetilcolinesterasa (ACHE) y la butirilcolinesterasa (BCHE), lo que aumenta los niveles de acetilcolina. Su uso conocido es la enfermedad de Alzheimer, y también se ha explorado en deterioro cognitivo vascular y en disfunción de la marcha en enfermedad de Parkinson (ensayo de Fase 2).

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20242182 | DURIVAST® 9.5MG/24H (cancelado) | Transdérmicos | RIVASTIGMINA |
| 20242522 | DURIVAST® 4.6MG/24H (cancelado) | Sistema transdérmico de liberación prolongada (parche) | RIVASTIGMINA |

Ambos registros pertenecen a BIOTOSCANA FARMA S.A. y están cancelados; no hay productos vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la rivastigmina con contraindicación en: epilepsia, enfermedad de los ganglios basales, distonía focal de la mano, blefaroespasmo, enfermedad pulmonar obstructiva crónica (incluida la de inicio temprano severo), asma (intrínseco y alérgico), enfermedad diarreica, paro cardíaco súbito, enfermedad de conducción cardíaca, anorexia nerviosa, úlcera péptica activa, obstrucción de vías urinarias, síndrome del seno enfermo (incluida la forma familiar), trastornos parkinsonianos/enfermedad de Parkinson y bloqueo auriculoventricular.
- **Interacciones farmacológicas:** la consulta devolvió 2 registros, ambos de interacción farmacológica con dianas (no con otros fármacos): acetilcolinesterasa (ACHE) y butirilcolinesterasa (BCHE), que corresponden a su mecanismo de acción.
- **Seguridad ocular:** los agentes colinérgicos pueden causar miosis, espasmo de acomodación y, raramente, riesgo de cierre angular; habría que evaluarlo antes de cualquier uso oftálmico.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo preclínica e indirecta (nivel L4), sin ensayos en humanos para glaucoma. Además, no hay producto vigente en Colombia y faltan datos de seguridad del prospecto. El puntaje de TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos bloqueante para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos adicionales y, de ser favorables, ensayos en humanos sobre reducción de la PIO.
- Evaluar la seguridad ocular (miosis, espasmo de acomodación, riesgo de cierre angular) y la viabilidad de una formulación oftálmica, ya que los productos registrados son transdérmicos.
- Definir la vía de acceso regulatorio, dado que los dos registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

