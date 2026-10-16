---
layout: default
title: Lansoprazole
parent: Evidencia Moderada (L3-L4)
nav_order: 380
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Lansoprazole: nueva indicación predicha, Reflujo duodenogástrico (nivel de evidencia L4). Indicación original: LANSOPRAZOL"
---

# Lansoprazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Lansoprazol: De Lansoprazol (indicación no detallada) a Reflujo Duodenogástrico

## Resumen en Una Frase

Lansoprazol es un inhibidor de la bomba de protones, registrado en Colombia bajo el producto LANZOR® 30 mg cápsula; el registro sanitario no detalla una indicación específica más allá del nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **Reflujo Duodenogástrico**, pero actualmente no hay ensayos clínicos y solo **1 publicación** (una revisión general sobre inhibidores de la bomba de protones) respalda esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LANSOPRAZOL (el registro no especifica la indicación) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, lansoprazol pertenece a la clase de los inhibidores de la bomba de protones (IBP), que suprimen la secreción de ácido gástrico.

El reflujo duodenogástrico consiste en el paso de contenido duodenal (bilis y secreciones pancreáticas) hacia el estómago. La supresión ácida podría reducir la lesión de la mucosa y los síntomas en un reflujo mixto ácido/biliar, pero no evita el reflujo en sí. Por lo tanto, el vínculo es sintomático e indirecto.

El puntaje alto de TxGNN (0.997) es una predicción computacional y no constituye evidencia clínica. La relación mecanística se apoya únicamente en el mecanismo conocido de la clase de los IBP.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | European Journal of Clinical Pharmacology | Actualización del uso clínico y la farmacocinética de los IBP, que son de primera elección en úlcera péptica, infección por *H. pylori*, enfermedad por reflujo gastroesofágico, lesiones por AINE y síndrome de Zollinger-Ellison. No aborda directamente el reflujo duodenogástrico. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20057384 (cancelado) | LANZOR® 30 MG CÁPSULA | Cápsula dura | LANSOPRAZOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (PrimeKG, no provienen del prospecto):** hipertensión, síndrome de QT largo, torsades de pointes, insuficiencia hepática, porfiria, enfermedad renal, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, osteoporosis, trastornos de coagulación, accidente cerebrovascular, infarto de miocardio, anemia, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y miastenia gravis. Estas relaciones son asociaciones del grafo y deben verificarse con la información oficial del producto.
- **Interacciones farmacológicas:** se identificaron 100 interacciones; las primeras 20 incluyen:
  - **Mayores:** acalabrutinib, atazanavir.
  - **Moderadas:** hidroclorotiazida, anfotericina B, amikacina, anfetamina, ampicilina, fenofibrato, apalutamida, aprepitant, atorvastatina, bosutinib, brigatinib, bromocriptina, entre otras.
  - **Menores:** ácido acetilsalicílico, axitinib, brivaracetam, cianocobalamina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en una revisión general de IBP, sin ensayos clínicos específicos para reflujo duodenogástrico. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Estudios clínicos o literatura específica sobre lansoprazol en reflujo duodenogástrico.
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto oficial de INVIMA con advertencias y contraindicaciones.
- Verificar la situación regulatoria actual (registro cancelado) y la viabilidad de comercialización.
- Evaluar de forma clínica las contraindicaciones del grafo de conocimiento y las interacciones mayores.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

