---
layout: default
title: Ticagrelor
parent: Evidencia Alta (L1-L2)
nav_order: 626
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Ticagrelor: nueva indicación predicha, Arteriosclerosis intracraneal (nivel de evidencia L2). Indicación original: No especificada en los registros"
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "mesenteric vascular occlusion", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
---

# Ticagrelor
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Ticagrelor: De Indicación No Especificada a Arteriosclerosis Intracraneal

## Resumen en Una Frase

Ticagrelor es un antiagregante plaquetario inhibidor del receptor P2Y12; en los registros sanitarios colombianos el texto de indicación aprobada solo repite el nombre del fármaco, sin especificar una enfermedad.
El modelo TxGNN predice que podría ser efectivo para **arteriosclerosis intracraneal**, con **2 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto registrado es solo "Ticagrelor") |
| Nueva Indicación Predicha | Arteriosclerosis intracraneal |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
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
| 20235198 (cancelado) | Ticagrelor 90 mg tabletas | Tableta recubierta | Ticagrelor |
| 20224822 (cancelado) | Torplat® 60 mg tabletas recubiertas | Tableta recubierta | Ticagrelor |
| 20163351 (cancelado) | Tiare® tabletas 90 mg | Tableta recubierta | Ticagrelor |

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
Aunque el puntaje de TxGNN es muy alto y existe un ensayo de Fase 3 en curso en la misma enfermedad, ticagrelor no es claramente el agente experimental, no hay resultados disponibles, y no se dispone de la información de advertencias y contraindicaciones del prospecto aprobado, lo que impide avanzar al tamizaje de seguridad. Además, no existe actualmente un registro sanitario vigente en Colombia. La clasificación L2 es la asignada en los datos compilados; los resultados de CAPTIVA aún no se han publicado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), dato bloqueante pendiente.
- Obtener datos del mecanismo de acción desde DrugBank.
- Esperar los resultados de CAPTIVA (finalización estimada en enero de 2027) y del piloto guiado por genotipo.
- Confirmar la situación regulatoria: los tres registros están cancelados.
- Definir un plan de gestión del riesgo hemorrágico, dada la contraindicación por hemorragia intracraneal señalada en el grafo de conocimiento, y un plan de manejo de interacciones (CYP3A4).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

