---
layout: default
title: Esomeprazole
parent: Evidencia Moderada (L3-L4)
nav_order: 263
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Esomeprazole: nueva indicación predicha, Reflujo duodenogástrico (nivel de evidencia L4). Indicación original: ESOMEPRAZOL"
---

# Esomeprazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Esomeprazol: De Trastornos Relacionados con la Acidez Gástrica a Reflujo Duodenogástrico

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones, usado originalmente para reducir la secreción de ácido gástrico en trastornos relacionados con la acidez. El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** (una revisión general sobre inhibidores de la bomba de protones) que respaldan esta dirección, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ESOMEPRAZOL (el registro sanitario solo indica el nombre del fármaco; se trata de un inhibidor de la bomba de protones para trastornos relacionados con la acidez) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Esomeprazol es el S-isómero del omeprazol. Inhibe de forma irreversible la H+/K+ ATPasa gástrica (la bomba de protones, codificada por el gen ATP4A) en las células parietales, y con ello suprime la secreción de ácido. Los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción en el campo correspondiente. Lo anterior proviene de la información farmacológica del blanco molecular y del análisis mecanístico de la predicción.

El reflujo duodenogástrico (o reflujo biliar) se produce por el flujo retrógrado del contenido duodenal hacia el estómago, y no por un exceso de ácido. Por eso, suprimir el ácido podría aliviar los síntomas asociados y el daño de la mucosa, pero no corrige la causa subyacente. El vínculo es plausible, aunque indirecto.

La única publicación disponible es una revisión general sobre el uso clínico y la farmacocinética de los inhibidores de la bomba de protones. No evalúa específicamente el reflujo duodenogástrico, así que la predicción se apoya sobre todo en el modelo y en un razonamiento mecanístico indirecto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | European Journal of Clinical Pharmacology | Actualiza el uso clínico y la farmacocinética de los inhibidores de la bomba de protones, fármacos de primera elección en úlcera péptica, infección por *H. pylori*, enfermedad por reflujo gastroesofágico, lesiones por antiinflamatorios no esteroideos y síndrome de Zollinger-Ellison. No aborda el reflujo duodenogástrico. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155892 | ACIDPRAZOL® 40 MG CÁPSULA | Cápsula dura | ESOMEPRAZOL |
| 20235954 | ESIO® 20MG | Tableta con recubrimiento entérico | ESOMEPRAZOL |

Ambos registros figuran como **cancelados**. Actualmente no hay registros vigentes de esomeprazol como monofármaco ni en combinación.

---

## Consideraciones de Seguridad

- **Señales de contraindicación del grafo de conocimiento** (provienen de relaciones fármaco-enfermedad del grafo PrimeKG, no del texto del prospecto): insuficiencia hepática, osteoporosis, osteoporosis posmenopáusica, fractura ósea y gastritis atrófica crónica. Deben verificarse contra el prospecto antes de cualquier uso.
- **Interacciones farmacológicas**: la consulta se completó, pero el único registro corresponde al blanco farmacológico del esomeprazol (ATP4A, la bomba de protones gástrica) y no a una interacción con otro medicamento. No se dispone de datos de interacciones clínicamente relevantes.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en una revisión general, sin ensayos clínicos específicos. El mecanismo es indirecto, porque el reflujo duodenogástrico no depende principalmente del ácido. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Estudios clínicos o literatura que evalúen esomeprazol específicamente en reflujo duodenogástrico (síntomas, daño de la mucosa).
- Datos formales del mecanismo de acción y análisis de la similitud entre la indicación original y la nueva.
- Verificar la situación regulatoria: motivo de la cancelación de los registros y viabilidad de una nueva solicitud o de otra vía de acceso.
- Obtener el prospecto oficial (INVIMA) para confirmar advertencias, contraindicaciones e interacciones.
- Confirmar la compatibilidad de vías de administración, pendiente de evaluar.

**Nota adicional:** el modelo también predijo otras indicaciones con mayor respaldo. La más destacable es la **úlcera duodenal**, con múltiples ensayos de Fase 3 completados y puntaje de evidencia L1. Sin embargo, esa indicación probablemente no constituye un reposicionamiento real, porque es un uso ya establecido del esomeprazol. Conviene evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

