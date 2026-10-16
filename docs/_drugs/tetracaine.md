---
layout: default
title: Tetracaine
parent: Solo Predicción del Modelo (L5)
nav_order: 621
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Tetracaine: nueva indicación predicha, Acrodermatitis crónica atrófica (nivel de evidencia L5). Indicación original: Combinaciones"
monitor_inn: "tetracaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
---

# Tetracaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Tetracaína: De Combinaciones (anestesia oftálmica) a Dermatitis Crónica Atrófica Acrodermatitis

## Resumen en Una Frase

La tetracaína es un anestésico local tipo éster, registrado en Colombia como solución oftálmica (producto PONTI OFTENO) con la indicación genérica "COMBINACIONES".
El modelo TxGNN predice que podría ser efectivo para **acrodermatitis crónica atrófica**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
La evidencia disponible es únicamente la predicción del modelo (nivel L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la tetracaína es un anestésico local tipo éster que bloquea los canales de sodio y, con ello, la conducción del impulso nervioso. Su uso aprobado en Colombia fue como solución oftálmica.

**No se identificó un vínculo mecanístico plausible.** La acrodermatitis crónica atrófica es una manifestación cutánea tardía de la infección por *Borrelia*, cuyo tratamiento requiere antibióticos. El bloqueo de canales de sodio no actúa sobre la causa ni la fisiopatología de esta enfermedad. El puntaje alto del modelo proviene de asociaciones en el grafo de conocimiento, sin respaldo clínico ni bibliográfico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal predicha.

Como referencia, entre otras predicciones secundarias existe un ensayo relacionado con la tetracaína:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02372786](https://clinicaltrials.gov/study/NCT02372786) | Fase 4 | Completado | 30 | Crema de lidocaína 7%/tetracaína 7% frente a lidocaína/prilocaína 2,5% para anestesia local durante láser en acné queloideo de la nuca y retiro de tatuajes. Evidencia indirecta: evalúa el control del dolor, no el tratamiento de la enfermedad. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20051507 (cancelado) | PONTI OFTENO | Solución oftálmica | COMBINACIONES |

Fabricante: Laboratorios Sophia S.A. de C.V. No hay registros vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** epilepsia; enfermedad renal, hepática y de la vesícula biliar; enfermedad cardíaca y cardiovascular, paro cardíaco súbito y trastornos de la conducción cardíaca; insuficiencia respiratoria; miastenia gravis y enfermedades de la unión neuromuscular; deficiencia de butirilcolinesterasa; hipertiroidismo, enfermedad de Graves y tirotoxicosis; uveítis, enfermedades del iris y del cuerpo ciliar, panuveítis, infecciones oculares y conjuntivitis.
- **Interacciones farmacológicas:** se identificaron 32 interacciones; entre las principales:
  - **Mayores:** ácido nitroso y bupivacaína liposomal.
  - **Moderadas:** otros anestésicos locales (lidocaína, benzocaína, cocaína, proparacaína, oxibuprocaína, cincocaína), benzodiacepinas (alprazolam, clordiazepóxido, clobazam, clonazepam, diazepam, estazolam, clorazepato) y sulfonamidas (sulfasalazina, sulfametoxazol).
  - **Menor:** hialuronidasa.
- **Señal de seguridad relevante:** la literatura describe síndrome de cauda equina tras anestesia espinal con tetracaína (reportes de caso, estudios preclínicos y revisiones). Este hallazgo debe tratarse como riesgo de neurotoxicidad, no como oportunidad terapéutica.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para acrodermatitis crónica atrófica carece de ensayos, literatura y vínculo mecanístico plausible, y la enfermedad requiere tratamiento antibiótico. Además, el único registro sanitario en Colombia está cancelado. Las demás predicciones del modelo (dermatomiositis, bronquitis, síndrome intestinal irritable, acné queloideo, entre otras) tampoco muestran respaldo terapéutico; la asociación con síndrome de cauda equina refleja toxicidad, no beneficio.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank).
- Prospecto de INVIMA con advertencias y contraindicaciones oficiales.
- Evidencia preclínica o clínica que justifique un posible efecto sobre la enfermedad predicha.
- Evaluación de compatibilidad de vía de administración (la presentación disponible fue oftálmica) y de la situación regulatoria, dado que el registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

