---
layout: default
title: Ambroxol
parent: Solo Predicción del Modelo (L5)
nav_order: 46
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Ambroxol: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L4). Indicación original: Ambroxol"
monitor_inn: "ambroxol"
predicted_indications: ["nasal cavity disease", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder"]
---

# Ambroxol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Ambroxol: De Mucolítico/Expectorante a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

Ambroxol es un agente mucolítico y expectorante, utilizado originalmente en jarabes y soluciones orales para facilitar la eliminación de secreciones respiratorias, incluso en combinación con dextrometorfano.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, pero actualmente solo hay **0 ensayos clínicos** y **1 publicación** (una revisión sobre tos aguda) que respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ambroxol (mucolítico/expectorante; el registro sanitario solo indica "Ambroxol" o "Combinaciones") |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 5) |
| Número de Registros Sanitarios | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según el conocimiento farmacológico general, el ambroxol es un agente mucolítico/secretolítico que aumenta la eliminación del moco de las vías respiratorias. Además, tiene un efecto anestésico local leve (bloqueo de canales de sodio) y propiedades antiinflamatorias.

Estas propiedades se relacionan de forma plausible con afecciones de las vías respiratorias superiores, como las de la cavidad nasal. Sin embargo, la única publicación vinculada trata sobre el tratamiento de la tos aguda, por lo que la conexión con la enfermedad de la cavidad nasal es indirecta.

El puntaje de 0.9991 es una predicción computacional, no una validación clínica. Por otro lado, los datos compilados indican que el ambroxol (como clorhidrato) se está reposicionando para enfermedades neurodegenerativas, como la enfermedad de Parkinson asociada a variantes del gen GBA1 y la esclerosis lateral amiotrófica (la EMA otorgó designación de medicamento huérfano en julio de 2018). Esto es independiente de la indicación predicha en este informe.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Revisión | Vestnik otorinolaringologii | Revisión sobre nuevas posibilidades de tratamiento de la tos aguda asociada a gripe e infecciones respiratorias virales agudas; la tos suele ser seca y resolverse en 2-3 semanas, aunque en ciertos casos es productiva con expectoración abundante |

---

## Información de Mercado en Colombia

Los 5 registros sanitarios están cancelados; actualmente no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52467 | AMBROXOL CLORHIDRATO JARABE 15 MG/5ML | Jarabe | Ambroxol |
| 1980176 | MUCOSOLVAN COMPOSITUM JARABE ADULTOS | Jarabe | Combinaciones |
| 16779 | AMBROXOL 15 MG/5ML SOLUCIÓN ORAL | Solución oral | Ambroxol |
| 19949895 | AMBROXOL CLORHIDRATO 30 MG/5 ML | Jarabe | Ambroxol |
| 20005160 | TRIATUSIC® JARABE | Jarabe | Ambroxol |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se registró una interacción de tipo farmacológico con la glucosilceramidasa beta (GBA1). El ambroxol actúa como chaperona de la enzima GCase: a pH neutro (por ejemplo, en líquido cefalorraquídeo sin células) inhibe su actividad, mientras que dentro de las células y sus lisosomas ácidos aumenta la actividad intracelular de la enzima al elevar la masa de enzima que llega al lisosoma. No se especificó un nivel de gravedad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo TxGNN y en una revisión indirecta sobre tos aguda, sin ensayos clínicos para enfermedad de la cavidad nasal. Además, el medicamento está comercializado en Colombia y cuenta con 5 registros sanitarios vigentes.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco
- Información de seguridad del prospecto (advertencias y contraindicaciones), actualmente no disponible
- Literatura y ensayos clínicos específicos sobre ambroxol en enfermedades de la cavidad nasal
- Aclarar la situación regulatoria en Colombia (motivo de las cancelaciones y viabilidad de un nuevo registro)
- Evaluar la compatibilidad de vías de administración (las formas registradas son jarabe y solución oral)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

