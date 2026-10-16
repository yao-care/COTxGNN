---
layout: default
title: Norepinephrine
parent: Evidencia Moderada (L3-L4)
nav_order: 471
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Norepinephrine: nueva indicación predicha, Enfermedad pulmonar obstructiva (nivel de evidencia L4). Indicación original: Norepinefrina"
monitor_inn: "norepinephrine"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome"]
---

# Norepinephrine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Norepinefrina: De Indicación Original (Norepinefrina inyectable) a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

La norepinefrina es un vasopresor inyectable que actúa sobre los receptores adrenérgicos; en los registros sanitarios de Colombia figura simplemente como "norepinefrina" en solución inyectable, sin un texto de indicación detallado.
El modelo TxGNN predice que podría ser efectivo para **enfermedad pulmonar obstructiva**, pero solo hay **1 ensayo clínico** de relevancia baja (no evalúa norepinefrina para esta enfermedad) y **20 publicaciones** de carácter descriptivo.
La predicción es, por ahora, una hipótesis computacional sin respaldo clínico directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Norepinefrina (el registro no detalla la indicación; uso como vasopresor inyectable) |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la norepinefrina es una catecolamina que activa los receptores adrenérgicos alfa y beta-1, con efecto vasopresor sistémico.

La literatura recuperada indica que la señalización adrenérgica y neuroinmune participa en el tono de la vía aérea, la inflamación y la fisiopatología del asma y la EPOC (por ejemplo, PMID 29696025, 41601146 y 21271508). Esto aporta un vínculo biológico plausible con la enfermedad pulmonar obstructiva.

Sin embargo, el vínculo es indirecto y descriptivo. La norepinefrina sistémica no tiene un papel establecido como broncodilatador, y sus efectos alfa y beta-1 podrían aumentar el riesgo cardíaco y hemodinámico en pacientes con EPOC e hipoxemia. El puntaje alto de TxGNN (0.998) es solo una predicción computacional y no constituye evidencia clínica.

Otras dos indicaciones predichas tienen aún menos sustento: "malformación respiratoria" (nivel L5; la literatura se refiere a neurofisiología básica y a exposición prenatal a psicofármacos, sin beneficio terapéutico plausible) y "síndrome de Rienhoff" (nivel L5; sin ensayos ni literatura).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Fase 1 | Reclutando | 420 | Función vascular, rehabilitación en hipertensión y retroalimentación aferente del músculo esquelético con ejercicio. No evalúa norepinefrina para enfermedad pulmonar obstructiva; relevancia baja (grado C). |

---

## Evidencia de Literatura

Se presentan las publicaciones más relevantes; no se identificaron ensayos clínicos aleatorizados.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29696025](https://pubmed.ncbi.nlm.nih.gov/29696025/) | 2018 | Revisión | Front Immunol | Señalización adrenérgica en la interfaz entre asma alérgica e infecciones virales |
| [41601146](https://pubmed.ncbi.nlm.nih.gov/41601146/) | 2026 | Revisión | Ann Med | Circuitos neuroinmunes en la fisiopatología respiratoria |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Revisión | Pneumologie | Inervación de las vías aéreas en asma y EPOC; papel de la norepinefrina en fibras simpáticas |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Revisión | Crit Care Clin | Catecolaminas (norepinefrina, epinefrina, dopamina) en cuidados críticos |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Revisión | Semin Immunol | Regulación neuroendocrina de la inflamación |
| [40870471](https://pubmed.ncbi.nlm.nih.gov/40870471/) | 2025 | Revisión | Medicina (Kaunas) | Ansiedad y depresión como comorbilidades de la EPOC |
| [3966494](https://pubmed.ncbi.nlm.nih.gov/3966494/) | 1985 | Cohorte | Am J Med | Efecto de la hipoxemia sobre la excreción de sodio y agua en enfermedad pulmonar obstructiva crónica |
| [22005192](https://pubmed.ncbi.nlm.nih.gov/22005192/) | 2011 | Cohorte | Adv Cardiol | Cambios hemodinámicos y autonómicos en adultos con apnea obstructiva del sueño |
| [27219496](https://pubmed.ncbi.nlm.nih.gov/27219496/) | 2016 | Guía | Endocr Pract | Guías de práctica clínica para el manejo de la obesidad (relación indirecta con la indicación) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20273430 | PRIDAM® 4MG / 4ML SOLUCIÓN INYECTABLE | Solución inyectable | Norepinefrina | Cancelado |
| 19940783 | ADS-NOLTRON® SOLUCIÓN INYECTABLE 4 MG/4 ML | Solución inyectable | Norepinefrina | Cancelado |
| 20056358 | NOREPINEFRINA 4 MG/4ML | Solución inyectable | Norepinefrina | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: el grafo de conocimiento de TxGNN asocia la norepinefrina con contraindicación en trastorno hipertensivo, hipertensión y enfermedad trombótica.
- **Interacciones farmacológicas**: se identificaron 70 interacciones; las principales mostradas, todas de nivel moderado, incluyen antidiabéticos (acarbosa, metformina, pioglitazona, repaglinida, insulinas aspart, degludec y detemir), agonistas GLP-1 (albiglutida, dulaglutida, semaglutida), inhibidores de DPP-4 (alogliptina, linagliptina, saxagliptina, sitagliptina), inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), clorpropamida, y los anorexígenos dietilpropión y fentermina.
- **Consideración adicional**: en pacientes con EPOC e hipoxemia, la acción vasopresora y cardioestimulante podría elevar el riesgo hemodinámico y cardíaco.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en literatura mecanística indirecta (nivel L4). No hay ensayos que evalúen norepinefrina en enfermedad pulmonar obstructiva, no existe papel terapéutico establecido como broncodilatador, y todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), ya que actualmente impide el tamizaje de seguridad.
- Completar los datos del mecanismo de acción (consulta a DrugBank).
- Estudios preclínicos o de mecanismo que justifiquen un efecto beneficioso en vía aérea sin riesgo cardiovascular inaceptable.
- Evaluar la viabilidad regulatoria y comercial, dado que no hay registros vigentes en Colombia.
- Definir vía de administración y formulación adecuadas para el uso pulmonar, si se justificara continuar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

