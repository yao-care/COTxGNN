---
layout: default
title: Salbutamol
parent: Solo Predicción del Modelo (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Salbutamol: nueva indicación predicha, Conjuntivitis papilar (nivel de evidencia L5). Indicación original: SALBUTAMOL"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture", "obstructive lung disease"]
---

# Salbutamol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Salbutamol: De Broncodilatador a Conjuntivitis Papilar

## Resumen en Una Frase

Salbutamol es un agonista selectivo de los receptores β2-adrenérgicos, utilizado originalmente como broncodilatador para el asma y la EPOC.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**, pero hasta ahora **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SALBUTAMOL (el registro sanitario no detalla una indicación más específica; clínicamente se usa en asma y EPOC) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según la información farmacológica conocida, salbutamol es un agonista altamente selectivo del receptor β2-adrenérgico (ADRB2), usado en el tratamiento del asma y la EPOC, y recientemente aprobado en EE. UU. también para broncoespasmo y broncoespasmo inducido por ejercicio.

La relación con la nueva indicación es especulativa. Trabajos preclínicos sugieren que los agonistas β2 tienen cierta actividad antiinflamatoria y antialérgica en la conjuntiva (por ejemplo, reducción de la permeabilidad microvascular y estabilización de mastocitos), lo que podría ser relevante en una conjuntivitis de base inflamatoria/alérgica. Sin embargo, no se recuperaron ensayos clínicos ni literatura para esta indicación, por lo que el vínculo mecanístico no está respaldado por datos directos.

Además, la compatibilidad de vía de administración está pendiente de evaluación: la presentación registrada en Colombia es un aerosol inhalado, y una indicación ocular probablemente exigiría una formulación tópica oftálmica distinta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19992498 (cancelado) | SACRUSYT® | Aerosoles | SALBUTAMOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones (relaciones del grafo de conocimiento, no del prospecto):** el grafo de conocimiento asocia salbutamol con contraindicación o precaución en: hipertensión arterial e hipertensión ocular, síndrome de QT largo (incluido el familiar), paro cardíaco súbito y enfermedad de la conducción cardíaca, isquemia miocárdica y enfermedad coronaria, epilepsia, déficit de potasio, diabetes mellitus y cetoacidosis diabética, acidosis metabólica, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hiperplasia prostática benigna y obstrucción del cuello vesical, y glaucoma de ángulo cerrado.
- **Nota relevante para la indicación ocular propuesta:** la asociación con hipertensión ocular y glaucoma de ángulo cerrado exige especial cautela si se considerara cualquier uso oftálmico.
- **Señal adicional:** se identificó un reporte de caso de anafilaxia causada por el propio salbutamol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para conjuntivitis papilar es de puntaje muy alto, pero no tiene ningún respaldo clínico ni bibliográfico (nivel L5). Además, el único registro sanitario en Colombia está cancelado y el perfil de seguridad del grafo incluye contraindicaciones oculares relevantes.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y revisión de la literatura preclínica sobre agonistas β2 en la conjuntiva.
- Evaluación de la compatibilidad de vía de administración (formulación oftálmica tópica) y de la similitud con la indicación original.
- Obtención y análisis del prospecto oficial (INVIMA) para completar el cribado de seguridad.
- Estudios preclínicos y, de ser favorables, un ensayo clínico exploratorio en conjuntivitis alérgica o papilar.
- Aclarar la situación regulatoria, dado que no existen registros vigentes en Colombia.

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, la **enfermedad pulmonar obstructiva** muestra el mayor respaldo (nivel L1, incluido un ensayo de Fase 3 con 1118 participantes), pero coincide con el uso ya establecido del fármaco, por lo que es una confirmación y no un reposicionamiento. La **anafilaxia** (L4) cuenta con un ensayo de Fase 3 terminado prematuramente con solo 24 participantes, sin conclusiones fiables de eficacia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

