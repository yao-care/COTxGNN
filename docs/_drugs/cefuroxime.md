---
layout: default
title: Cefuroxime
parent: Solo Predicción del Modelo (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefuroxime: nueva indicación predicha, Hiperamilasemia (nivel de evidencia L5). Indicación original: Cefuroxima"
---

# Cefuroxime
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

# Cefuroxima: De Antibiótico Cefalosporínico (indicación no detallada en el registro) a Hiperamilasemia

## Resumen en Una Frase

Cefuroxima es un antibiótico cefalosporínico de segunda generación. Su único registro sanitario colombiano en los datos compilados solo menciona el nombre del principio activo, sin detallar la indicación.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata de una predicción basada únicamente en el grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cefuroxima (el registro solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, cefuroxima es una cefalosporina de segunda generación que inhibe la síntesis de la pared celular bacteriana. Su uso establecido es el tratamiento de infecciones bacterianas.

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre) y no una infección. No tiene una diana antibacteriana, por lo que **no se identificó ningún vínculo mecanístico plausible** entre el fármaco y esta condición.

El puntaje alto de TxGNN (99.76%) refleja una asociación estadística dentro del grafo de conocimiento, no evidencia biológica ni clínica. Sin ensayos, literatura ni un mecanismo que la sustente, esta predicción debe considerarse especulativa.

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
| 20099285 (cancelado) | Cefuroxima axetil tabletas 500 mg | Tableta cubierta con película | Cefuroxima (sin detalle de indicación) |

El único registro identificado está cancelado, por lo que no hay producto vigente en el mercado según los datos compilados.

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto de prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de la coagulación sanguínea, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y deficiencia congénita de protrombina.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de la muestra revisada son de nivel moderado, entre ellas:
  - Antiácidos: hidróxido de aluminio, carbonato de calcio, magaldrato, y carbonato, hidróxido y óxido de magnesio.
  - Antagonistas H2: famotidina, ranitidina, cimetidina, nizatidina.
  - Inhibidores de la bomba de protones: omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol.
  - Aminoglucósidos: kanamicina y neomicina.
  - Balsalazida.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde el uso de cefuroxima en hiperamilasemia, y no hay un mecanismo plausible que lo explique. Además, el único registro sanitario colombiano está cancelado.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble que conecte la inhibición de la síntesis de pared bacteriana con la elevación de amilasa, o descartar la predicción como artefacto del grafo.
- Estudios preclínicos o clínicos que evalúen la relación entre cefuroxima y la hiperamilasemia.
- Los datos oficiales de advertencias y contraindicaciones del prospecto autorizado.
- Confirmar si existe algún producto con cefuroxima vigente en Colombia.

**Observación adicional:** entre las otras predicciones del modelo, la infección del tracto urinario es la que cuenta con más respaldo (nivel L3, con un estudio completado de 973 pacientes con pielonefritis y varias revisiones). Sin embargo, se trata de un uso antibacteriano ya establecido y no de un reposicionamiento propiamente dicho. Si se desea priorizar candidatos con evidencia, conviene evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

