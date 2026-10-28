---
layout: default
title: Benralizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 99
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Benralizumab: nueva indicación predicha, Trombocitopenia por destrucción inmune (nivel de evidencia L5). Indicación original: Benralizumab"
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
---

# Benralizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Benralizumab: De Benralizumab (indicación no detallada en el registro) a Trombocitopenia por Destrucción Inmune
{: .text-alpha }

## Resumen en Una Frase

Benralizumab es un anticuerpo monoclonal dirigido contra el receptor alfa de la interleucina 5 (IL-5Rα), comercializado en Colombia como FASENRA®. Según la información de otras fuentes, se usa como tratamiento de mantenimiento adicional en asma eosinofílica grave.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Benralizumab (el registro sanitario no detalla la indicación; según otras fuentes: asma eosinofílica grave) |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 0.9934 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Benralizumab es un anticuerpo anti-IL-5Rα que depleta eosinófilos y basófilos mediante citotoxicidad celular dependiente de anticuerpos (ADCC). Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe; la descripción anterior proviene del análisis mecanístico general del fármaco.

Los datos compilados no respaldan una ruta mecanística clara entre la depleción de eosinófilos y la trombocitopenia inmune. Solo en casos raros de citopenias autoinmunes asociadas a eosinófilos podría existir alguna relevancia, y esto es especulativo.

El puntaje alto (0.9934) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Sin estudios reales, esta predicción debe considerarse una hipótesis sin validar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20145261 (cancelado) | FASENRA® (AstraZeneca Colombia S.A.S.) | Solución inyectable | Benralizumab |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** La consulta se completó y solo identificó la interacción farmacológica con su diana, el receptor alfa de la interleucina 5 (IL5RA), sin nivel de gravedad clínica asignado.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe una vía mecanística plausible entre la depleción de eosinófilos y la trombocitopenia inmune. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad
- Revisión mecanística y de literatura que justifique un vínculo con la trombocitopenia inmune
- Aclarar la situación regulatoria (registro cancelado) y la disponibilidad del producto en Colombia

---

**Nota sobre otras predicciones:** Entre las otras indicaciones predichas, la **dermatitis** (TxGNN 0.9916) es la que tiene más respaldo, con nivel L2 y recomendación de "pregunta de investigación". Incluye 3 ensayos de Fase 2: NCT03563066 (completado, n=20, estudio mecanístico en dermatitis atópica), NCT04605094 (terminado, n=194, controlado con placebo; debe verificarse el motivo de terminación) y NCT06734884 (aún no reclutando, n=96, DRESS). La literatura asociada consiste mayormente en revisiones y no en datos directos de eficacia. Las predicciones de acné queloide y dermatomiositis (neonatal y amiopática) carecen de evidencia (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

