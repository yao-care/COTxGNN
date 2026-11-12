---
layout: default
title: Ticagrelor
parent: Solo Predicción del Modelo (L5)
nav_order: 626
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Ticagrelor: nueva indicación predicha, Arteriosclerosis intracraneal (nivel de evidencia L5). Indicación original: No especificada en los registros"
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
---

# Ticagrelor
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

## Ticagrelor: De Indicación No Especificada a Arteriosclerosis Intracraneal
{: .text-alpha }

## Resumen en Una Frase

Ticagrelor es un antiagregante plaquetario inhibidor del receptor P2Y12; en los registros sanitarios colombianos el texto de indicación aprobada solo repite el nombre del fármaco, sin especificar una enfermedad.
El modelo TxGNN predice que podría ser efectivo para **arteriosclerosis intracraneal**, con **2 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto registrado es solo "Ticagrelor") |
| Nueva Indicación Predicha | Arteriosclerosis intracraneal |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 13 de 17) |
| Número de Registros Sanitarios | 17 (vigentes: 13) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ticagrelor es un inhibidor reversible del receptor plaquetario P2Y12, que reduce la agregación plaquetaria y la formación de trombos sobre placas ateroscleróticas.

La arteriosclerosis intracraneal sintomática provoca ictus por embolia arterio-arterial y trombosis in situ, procesos en los que participan las plaquetas. Por ello, la inhibición de P2Y12 tiene una base mecanística directa. El tratamiento habitual actual combina clopidogrel y aspirina durante 90 días, seguido de aspirina sola, pero el riesgo de ictus recurrente sigue siendo alto durante los primeros 12 meses.

Debe señalarse que la evidencia es indirecta para ticagrelor: el ensayo de Fase 3 CAPTIVA compara estrategias de anticoagulación y antiagregación, y ticagrelor no es claramente el agente experimental principal. Su papel se apoya sobre todo en datos de dosificación neurointervencionista y en datos de ictus/AIT con pérdida de función de CYP2C19 (CHANCE-2).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Fase 3 | Activo, sin reclutar | 1683 | CAPTIVA: evalúa si rivaroxabán, ticagrelor o ambos superan a clopidogrel para reducir ictus isquémico, hemorragia intracerebral o muerte vascular al año. Sin resultados aún |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | No aplica | Reclutando | 100 | Piloto de selección de inhibidor de P2Y12 guiada por genotipo frente a clopidogrel convencional en enfermedad aterosclerótica intracraneal sintomática. Poca potencia estadística |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohorte | J Neurointerv Surg | Experiencia con ticagrelor 60 mg dos veces al día más aspirina 81 mg frente al régimen estándar de aspirina y clopidogrel en el implante de stents intracraneales |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Revisión | Int J Stroke | Diseño y avance inicial del ensayo CAPTIVA en estenosis aterosclerótica intracraneal |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20235198 | Ticagrelor 90 mg tabletas | Tableta recubierta | Ticagrelor |
| 20224822 | Torplat® 60 mg tabletas recubiertas | Tableta recubierta | Ticagrelor |
| 20163351 | Tiare® tabletas 90 mg | Tableta recubierta | Ticagrelor |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar y hemorragia intracraneal.
- **Interacciones Farmacológicas:** se identificaron 100 interacciones; entre las principales mostradas:
  - **Mayor:** claritromicina.
  - **Moderadas:** aprepitant, morfina, ácido acetilsalicílico, dexametasona, budesonida, saxagliptina, eliglustat, naldemedina, metreleptina, miconazol, nitisinona, rolapitant, simvastatina, cisaprida, clotrimazol, dexfenfluramina.
  - **Menores:** naloxegol, prucaloprida.
- **Consideraciones adicionales:** riesgo de sangrado, carga de interacciones (inhibidores e inductores de CYP3A4) y dosis de aspirina concomitante.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es muy alto y existe un ensayo de Fase 3 en curso en la misma enfermedad, ticagrelor no es claramente el agente experimental, no hay resultados disponibles, y no se dispone de la información de advertencias y contraindicaciones del prospecto aprobado, lo que impide avanzar al tamizaje de seguridad. La clasificación L2 es la asignada en los datos compilados; los resultados de CAPTIVA aún no se han publicado.

<!-- review:begin co-lic-20261105-ticagrelor-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no existe actualmente un registro sanitario vigente en Colombia. La clasificación L2 es la asignada en los datos compilados; los resultados de CAPTIVA aún no se han publicado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 13); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ticagrelor-1 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), dato bloqueante pendiente.
- Obtener datos del mecanismo de acción desde DrugBank.
- Esperar los resultados de CAPTIVA (finalización estimada en enero de 2027) y del piloto guiado por genotipo.
- Definir un plan de gestión del riesgo hemorrágico, dada la contraindicación por hemorragia intracraneal señalada en el grafo de conocimiento, y un plan de manejo de interacciones (CYP3A4).

<!-- review:begin co-lic-20261105-ticagrelor-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Confirmar la situación regulatoria: los tres registros están cancelados. / Definir un plan de gestión del riesgo hemorrágico, dada la contraindicación por hemorragia intracraneal señalada en el grafo de conocimiento, y un plan de manejo de interacciones (CYP3A4)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 13); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ticagrelor-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, no existe actualmente un registro sanitario vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Confirmar la situación regulatoria: los tres registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

