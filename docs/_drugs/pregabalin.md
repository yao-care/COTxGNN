---
layout: default
title: Pregabalin
parent: Solo Predicción del Modelo (L5)
nav_order: 532
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
description: "Pregabalin: nueva indicación predicha, Tendinitis (nivel de evidencia L4). Indicación original: Pregabalina"
monitor_inn: "Pregabalin"
predicted_indications: ["tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
---

# Pregabalin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Pregabalina: De Indicación Registrada (Pregabalina) a Tendinitis
{: .text-alpha }

## Resumen en Una Frase

Pregabalina es un ligando de la subunidad alfa2-delta de los canales de calcio dependientes de voltaje, registrada en Colombia bajo el nombre genérico "Pregabalina" (el registro no detalla una indicación específica).
El modelo TxGNN predice que podría ser efectivo para **tendinitis**, con **0 ensayos clínicos** y **6 publicaciones** de relevancia indirecta.
Cabe destacar que la indicación con mayor respaldo entre las predichas es la **migraña** (1 ensayo de Fase 3 retirado y varios ECA pediátricos), que se comenta en la conclusión.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pregabalina (el registro sanitario no especifica una indicación clínica) |
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos principal. Según la información conocida, pregabalina se une a la subunidad alfa2-delta de los canales de calcio dependientes de voltaje, lo que reduce la liberación de neurotransmisores excitadores y atenúa la señalización del dolor neuropático y de la sensibilización central.

Este mecanismo podría aliviar el dolor asociado a la tendinopatía, pero no hay evidencia de que actúe sobre la patología tendinosa de fondo. La literatura disponible es indirecta: analgesia perioperatoria tras reparación artroscópica del manguito rotador, reportes de caso y un reporte de discapacidad asociada a fluoroquinolonas. El puntaje TxGNN, muy alto, no está respaldado por datos clínicos directos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para tendinitis.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Cohorte retrospectiva (clasificada como ECA) | J Orthop Sci | Evalúa el efecto analgésico y ahorrador de opioides de pregabalina tras reparación artroscópica del manguito rotador; resultados previos conflictivos |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | ECA | Arthroscopy | Pregabalina perioperatoria vs. bloqueo interescalénico del plexo braquial tras reparación del manguito rotador; compara dolor posoperatorio y consumo de opioides |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Síndrome piriforme y síndrome glúteo profundo; sin relación directa con pregabalina en tendinitis |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Reporte de caso | Pain Pract | Pinzamiento del nervio cutáneo femoral posterior tras maratón, por tendinitis de isquiotibiales |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Revisión/Reporte de caso | Praxis | Discapacidad asociada a fluoroquinolonas (ciprofloxacino), que incluye tendinopatías |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclínico (animal) | Adv Pharmacol Pharm Sci | Extracto de *Cissus quadrangularis* atenúa la neuropatía periférica inducida por vincristina en ratas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190070 (cancelado) | LIMIAR ® 150 MG CÁPSULA DURA | Cápsula dura | PREGABALINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento TxGNN, no según el prospecto):** trastorno de ansiedad, trastorno neurótico, trastorno distímico, trombocitopenia, angioedema (adquirido, hereditario, no histamínico e inducido por bloqueadores del sistema renina-angiotensina-aldosterona), miopatía, enfermedad muscular y del músculo esquelético, parálisis periódica familiar, rabdomiólisis, fascitis nodular, insuficiencia renal y bloqueo auriculoventricular.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las principales:
  - **Mayor:** morfina y morfina liposomal.
  - **Moderada:** pioglitazona, rosiglitazona, troglitazona, difenoxina, difenoxilato, dronabinol, nabilona, metoclopramida, opio y sibutramina.
  - **Nivel no definido:** calcitriol, vitamina A, fentermina, pantoprazol, glimepirida, sucralfato, palonosetrón y nistatina.
- La combinación con opioides y otros depresores del sistema nervioso central merece especial atención.
- En la literatura de migraña se mencionan, además, sedación, disfunción sexual y riesgos relacionados con el sueño.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para tendinitis, la evidencia es solo indirecta (analgesia perioperatoria, reportes de caso y un estudio preclínico) y no hay ensayos clínicos. Además, el único registro sanitario en Colombia está cancelado, y no se dispone de advertencias ni contraindicaciones del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos bloqueante.
- Completar los datos del mecanismo de acción desde DrugBank.
- Diseñar estudios clínicos específicos de pregabalina en tendinopatía, con desenlaces sobre la patología y no solo sobre el dolor.
- Verificar la situación regulatoria actual de pregabalina en Colombia, dado que el único registro está cancelado.
- **Línea alternativa:** la **migraña** (puntaje TxGNN 0.9947, nivel L2) cuenta con ECA pediátricos frente a propranolol y valproato, una red de metaanálisis y evidencia preclínica de inhibición de la depresión cortical propagada. Su único ensayo de Fase 3 (NCT00447369) fue retirado, por lo que se recomienda tratarla como pregunta de investigación que requiere estudios controlados en adultos antes de cualquier recomendación.
- Las demás predicciones (miositis granulomatosa idiopática, miositis fibrosa, miositis por cuerpos de inclusión y migraña con aura de tronco encefálico) carecen de respaldo clínico y deben mantenerse en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

