---
layout: default
title: Miltefosine
parent: Solo Predicción del Modelo (L5)
nav_order: 446
evidence_level: L5
indication_count: 3
monitor_inn: "Miltefosine"
predicted_indications: ["echinococcus granulosus infectious disease", "alveolar echinococcosis", "Smouldering systemic mastocytosis"]
last_modified_at: 2026-10-28
description: "Miltefosine: nueva indicación predicha, Enfermedad infecciosa por Echinococcus granulosus (echinococcus granulosus infectious disease) (nivel de evidencia L5). Indicación original: MILTEFOSINA"
---

# Miltefosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Miltefosine: Enfermedad infecciosa por Echinococcus granulosus (echinococcus granulosus infectious disease)
{: .text-alpha }

## Resumen en Una Frase

Miltefosina es un alquilfosfocolina con actividad antiparasitaria, con registros sanitarios vigentes en Colombia cuyo texto de indicación solo indica el nombre del principio activo ("MILTEFOSINA"), sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad infecciosa por Echinococcus granulosus**, pero **no hay ensayos clínicos ni publicaciones** que estudien directamente esta enfermedad: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MILTEFOSINA |
| Nueva Indicación Predicha | Enfermedad infecciosa por Echinococcus granulosus (echinococcus granulosus infectious disease) |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los registros compilados. Según la información conocida, la miltefosina es un alquilfosfocolina con actividad antiparasitaria de amplio espectro; se utiliza en leishmaniasis y en infecciones por amebas de vida libre. Se describe que altera el metabolismo lipídico, la señalización de membrana (por ejemplo, la vía PI3K/Akt) y la homeostasis del calcio en los parásitos. En las bases farmacológicas consultadas, su diana humana registrada es AKT1.

La relación con la nueva indicación es de plausibilidad biológica: una extensión de esta actividad antiparasitaria a las fases larvarias de los cestodos (protoescólices) es posible. Sin embargo, esto es solo una hipótesis. Ningún estudio aportado evalúa la miltefosina frente a *E. granulosus*, y el alto puntaje de TxGNN es una predicción computacional sin validación clínica.

Como contexto, otras dos predicciones del modelo (equinococosis alveolar y mastocitosis sistémica indolente "smouldering") también carecen de evidencia directa. Para la equinococosis alveolar, el único artículo recuperado (PMID 16940089) estudió itraconazol, metiazol y nitazoxanida in vitro, no miltefosina.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta enfermedad.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20228850 | ANTYLEX® 10 | Cápsula dura | MILTEFOSINA (el texto no detalla la enfermedad) |
| 20131141 | ANTYLEX 50 MG CAPSULAS | Cápsula dura | MILTEFOSINA (el texto no detalla la enfermedad) |

Ambos registros son de producto de un solo principio activo, están vigentes y pertenecen a GENYX S.A.S.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Consultar las advertencias y precauciones del prospecto |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

La miltefosina también tiene usos descritos en oncología (uso tópico en metástasis cutáneas de cáncer de mama y designación huérfana en la UE para linfoma cutáneo de células T), por lo que se incluye esta sección.

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (relaciones del grafo de conocimiento TxGNN/PrimeKG, no texto de prospecto): síndrome de Sjögren-Larsson y eritrodermia ictiosiforme congénita.
- **Interacciones farmacológicas**: la consulta se completó y solo mostró una relación farmacológica con la diana AKT1 (AKT serina/treonina quinasa 1). No se identificaron interacciones con otros fármacos ni niveles de gravedad.

No se dispone de advertencias principales ni de contraindicaciones del prospecto; consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (0.9941) es solo computacional: no hay ensayos clínicos ni literatura que estudien la miltefosina en la infección por *E. granulosus*, por lo que el nivel de evidencia es L5. Además, faltan datos de seguridad del prospecto y del mecanismo de acción.

**Para avanzar se necesita:**
- Estudios preclínicos in vitro e in vivo de la miltefosina frente a protoescólices y metacestodos de *Echinococcus*
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad
- Confirmar el mecanismo de acción desde fuentes como DrugBank
- Aclarar la indicación autorizada en Colombia, ya que el texto del registro solo menciona el nombre del principio activo
- Comparar con los tratamientos actuales (benzimidazoles, como albendazol) para justificar el valor añadido
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

