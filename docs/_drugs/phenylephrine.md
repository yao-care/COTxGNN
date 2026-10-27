---
layout: default
title: Phenylephrine
parent: Evidencia Moderada (L3-L4)
nav_order: 513
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-14
description: "Phenylephrine: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L3). Indicación original: Paracetamol combinaciones excluyendo sicolépticos"
monitor_inn: "Phenylephrine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia"]
---

# Phenylephrine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **3** 
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

## Fenilefrina: De Combinaciones de Paracetamol/Fenilefrina a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

La fenilefrina se comercializó en Colombia como componente de combinaciones para síntomas de resfriado (paracetamol y fenilefrina), con registros hoy cancelados.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, con **0 ensayos clínicos** y **5 publicaciones** que actualmente respaldan esta dirección, todas de calidad limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol combinaciones excluyendo sicolépticos |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Sin embargo, los datos farmacológicos compilados muestran que la fenilefrina actúa sobre los receptores adrenérgicos alfa-1A, alfa-1B y alfa-1D. Es un agonista alfa-1 que produce vasoconstricción de la mucosa, y por eso se usa como descongestionante nasal.

La indicación original (combinaciones para síntomas de resfriado y gripe) ya incluye el alivio de la congestión nasal. Por ello, la enfermedad de la cavidad nasal es más una extensión del uso existente que un reposicionamiento novedoso. El puntaje alto del modelo (99.97%) es coherente con esta farmacología conocida.

La evidencia clínica disponible es limitada y, a juzgar por los títulos, de diseño no aleatorizado o poco claro. Incluye un informe de 2025 sobre un aerosol nasal con fenilefrina y un estudio de 2014 sobre agentes tópicos en cirugía endoscópica sinusal.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Evaluación experimental y clínica | Vestnik otorinolaringologii | Evalúa la seguridad y eficacia del aerosol Polydexa con fenilefrina en rinosinusitis aguda; no hay datos previos de toxicidad |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Revisión | Vestnik otorinolaringologii | Enfoque patogénico del tratamiento de enfermedades inflamatorias de la nariz y senos paranasales, buscando reducir hiperemia y edema de la mucosa |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Artículo clínico | Vestnik otorinolaringologii | Estado endoscópico de la mucosa nasal tras terapia local antiinflamatoria y antibacteriana (Polydexa con fenilefrina) |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | ECA | PloS one | Ácido tranexámico tópico en cirugía endoscópica sinusal por rinosinusitis crónica; la fenilefrina sería un comparador o agente de fondo |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Reporte de caso | Archives of ophthalmology | Toxicidad por cocaína intranasal y una reacción adicional a fenilefrina intranasal; relevancia solo indirecta |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19984 | PAX® DIA GRANULADO (cancelado) | Gránulos | Paracetamol combinaciones excluyendo sicolépticos |
| 19984369 | NOXPIRIN® SINUS TABLETA (cancelado) | Tableta cubierta con película | Fenilefrina combinaciones |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** hipertensión, insuficiencia hepática, enfermedad hepática, enfermedad renal, epilepsia, insomnio, EPOC, úlcera gástrica y péptica, porfiria, pancreatitis, enfermedad de la vesícula biliar, trombocitopenia, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, enfermedad inflamatoria intestinal, trastornos psicóticos y mentales, gastritis y dermatitis herpetiforme.
- **Interacciones farmacológicas:** los datos compilados solo muestran interacciones con receptores (alfa-1A, alfa-1B y alfa-1D), no con otros fármacos.
- **Riesgos del uso tópico:** el uso crónico puede causar congestión de rebote (rinitis medicamentosa), y la absorción sistémica puede elevar la presión arterial. El informe de 1980 sobre cocaína indica precaución en pacientes con enfermedad cardiovascular hipertensiva o con otros simpaticomiméticos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La predicción coincide con la farmacología conocida de la fenilefrina como descongestionante nasal, por lo que es una extensión de un uso existente. Sin embargo, no hay ensayos registrados, la literatura es de diseño limitado y los registros colombianos están cancelados.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales (brecha bloqueante)
- Obtener datos del mecanismo de acción desde DrugBank
- Ensayos clínicos controlados de fenilefrina en enfermedad nasal con desenlaces definidos
- Definir vía de administración (tópica nasal) y plan de monitoreo de presión arterial y de congestión de rebote
- Verificar la situación regulatoria actual en Colombia, dado que no hay registros vigentes

---

### Nota sobre otras predicciones

Las otras dos predicciones tienen evidencia más débil: **laringofaringitis aguda** (99.97%, L5, sin ensayos ni literatura; recomendación Hold) y **cefalea autonómica trigeminal** (99.30%, L4, solo estudios pupilométricos donde la fenilefrina se usa como sonda diagnóstica, sin evidencia terapéutica; pregunta de investigación).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

