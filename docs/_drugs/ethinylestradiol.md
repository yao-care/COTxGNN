---
layout: default
title: Ethinylestradiol
parent: Solo Predicción del Modelo (L5)
nav_order: 267
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Ethinylestradiol: nueva indicación predicha, Zinc plasmático elevado (nivel de evidencia L5). Indicación original: Dienogest y etinilestradiol"
monitor_inn: "Ethinylestradiol"
predicted_indications: ["zinc, elevated plasma"]
---

# Ethinylestradiol
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

## Etinilestradiol: De Dienogest y Etinilestradiol (anticoncepción oral) a Zinc Plasmático Elevado
{: .text-alpha }

## Resumen en Una Frase

Etinilestradiol es un estrógeno sintético que en Colombia se registró en combinación con dienogest (producto DIENILLE®, comprimido recubierto).
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dienogest y etinilestradiol |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el etinilestradiol es un estrógeno sintético que actúa sobre los receptores de estrógeno alfa (ESR1) y beta (ESR2), y su eficacia como componente de anticonceptivos orales combinados con dienogest está establecida. Mecanísticamente, podría relacionarse con el zinc plasmático, aunque esta vía no está verificada.

Los estrógenos, incluido el etinilestradiol, influyen en los metales traza circulantes: elevan la ceruloplasmina y el cobre, y pueden alterar la unión del zinc a la albúmina y otras proteínas. Esto sería una ruta plausible hacia cambios en el zinc plasmático, pero corresponde a un efecto sobre un biomarcador y no a un efecto terapéutico.

Debe interpretarse con cautela: el zinc plasmático elevado es un hallazgo de laboratorio, no una enfermedad claramente definida como objetivo terapéutico. No se ha establecido la dirección del efecto (reducir o aumentar el zinc) ni un beneficio clínico. La puntuación procede del modelo TxGNN (aprendizaje profundo) y podría reflejar similitudes que el modelo ha aprendido entre enfermedades relacionadas, no evidencia biológica ni una señal terapéutica real. La relación con la indicación original (anticoncepción hormonal) no está evaluada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20093177 | DIENILLE® comprimido recubierto | Tableta recubierta | Dienogest y etinilestradiol | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no provienen del prospecto): hipertensión, epilepsia, trastornos de ansiedad, trastornos neuróticos, distimia, porfiria hereditaria y otros trastornos del metabolismo de porfirinas, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, insuficiencia cardíaca congestiva, hipercalcemia (incluida la hipercalcemia humoral de neoplasias), insuficiencia suprarrenal y enfermedad de Addison, hipotiroidismo (incluidos mixedema e hipotiroidismo congénito), lupus eritematoso sistémico (incluido el pediátrico), asma (intrínseca y alérgica) e hiperplasia prostática benigna.
- **Interacciones y farmacología**: el etinilestradiol actúa sobre los receptores de estrógeno alfa (ESR1) y beta (ESR2) y sobre el transportador de aminoácidos acoplado a protones 1 (SLC36A1). No se identificaron interacciones con otros fármacos con nivel de gravedad clasificado.

Consultar el prospecto para la información completa de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje alto del modelo (nivel L5), sin ensayos clínicos ni literatura, y la indicación predicha es un hallazgo de laboratorio sin dirección terapéutica definida. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Definir si "zinc plasmático elevado" es un objetivo terapéutico válido y en qué dirección actuaría el fármaco
- Revisión de literatura sobre estrógenos y homeostasis del zinc para evaluar plausibilidad biológica
- Evaluar compatibilidad de vías de administración y similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

