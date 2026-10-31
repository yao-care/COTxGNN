---
layout: default
title: Serine
parent: Solo Predicción del Modelo (L5)
nav_order: 583
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
description: "Serine: nueva indicación predicha, Miopatía visceral familiar (nivel de evidencia L5). Indicación original: Emulsiones lipídicas"
monitor_inn: "Serine"
predicted_indications: ["familial visceral myopathy", "intestinal obstruction", "unclassified intestinal pseudoobstruction", "myopathic intestinal pseudoobstruction", "neuronal intestinal dysplasia, type B", "intestinal pseudoobstruction, neuronal, chronic idiopathic, X-linked", "exercise-induced malignant hyperthermia", "aqueous misdirection"]
---

# Serine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Serina: De Emulsiones Lipídicas a Miopatía Visceral Familiar
{: .text-alpha }

## Resumen en Una Frase

La serina es un aminoácido proteinogénico que en Colombia solo aparece registrado como componente de una emulsión lipídica de nutrición parenteral (NUTRIFLEX® OMEGA SPECIAL NOVO), cuyo registro está cancelado.
El modelo TxGNN predice que podría ser efectiva para **miopatía visceral familiar**, pero no hay **ningún ensayo clínico** ni **publicación** que respalde esta predicción específica.
Se trata de una predicción puramente computacional (nivel de evidencia L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Emulsiones lipídicas |
| Nueva Indicación Predicha | Miopatía visceral familiar |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la serina es un aminoácido proteinogénico que forma parte de una formulación de nutrición parenteral. Su uso registrado se limita al aporte nutricional, no a un efecto terapéutico sobre una enfermedad específica.

Los datos compilados no respaldan un vínculo mecanístico entre la serina y la patología del músculo liso visceral (por ejemplo, las variantes del gen ACTG2 asociadas a la miopatía visceral familiar). La alta puntuación (0.9999) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Cabe señalar que las otras predicciones de mayor rango (seudoobstrucción intestinal, obstrucción intestinal, displasia neuronal intestinal) pertenecen al mismo grupo de trastornos de motilidad intestinal, lo que sugiere una señal compartida aprendida por el modelo TxGNN (aprendizaje profundo) y no evidencia específica para cada enfermedad. La similitud con la indicación original queda pendiente de evaluar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para miopatía visceral familiar.

Como referencia, la segunda predicción (obstrucción intestinal) recuperó publicaciones, pero ninguna evalúa la serina como tratamiento. Provienen de coincidencias con la palabra «serina» (por ejemplo, la quinasa serina/treonina STK11 en el síndrome de Peutz-Jeghers), por lo que no constituyen evidencia a favor del fármaco. Lo mismo ocurre con las publicaciones sobre PRSS56 (una serina proteasa) en glaucoma de ángulo cerrado.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20216947 (cancelado) | NUTRIFLEX® OMEGA SPECIAL NOVO (B. Braun Medical S.A.) | Emulsión inyectable | Emulsiones lipídicas |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no provenientes del prospecto): epilepsia, trastornos de ansiedad y otros trastornos mentales (neuróticos, psicóticos, esquizoafectivos, distimia), abuso/dependencia de sustancias, enfermedad renal (incluida enfermedad renal crónica y terminal, nefrolitiasis, nefrocalcinosis, nefropatía aguda por uratos), diabetes mellitus y cetoacidosis diabética, hipercalcemia (incluida la de origen maligno), trastornos del metabolismo del fósforo, sarcoidosis, enfermedad cardíaca y cardiovascular, fibrilación ventricular, intoxicación digitálica, déficit de vitamina B12 y anemia megaloblástica. Estas señales deben verificarse y no sustituyen la información del prospecto.
- **Interacciones farmacológicas**: no se encontraron registros en la consulta realizada.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no estaban disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura que evalúen la serina para miopatía visceral familiar. Además, el único registro sanitario en Colombia está cancelado y la literatura recuperada para otras indicaciones proviene de coincidencias con el término «serina».

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), una brecha de datos bloqueante para el tamizaje de seguridad.
- Consultar el mecanismo de acción en DrugBank y evaluar un posible vínculo con la fisiopatología de la miopatía visceral familiar.
- Realizar una búsqueda dirigida de literatura y ensayos que evalúen la serina (no términos relacionados) en trastornos de motilidad intestinal.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original (hoy pendientes).
- Considerar estudios preclínicos antes de cualquier avance clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

