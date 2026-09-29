---
layout: default
title: Phenobarbital
parent: Evidencia Moderada (L3-L4)
nav_order: 324
evidence_level: L4
indication_count: 10
---

# Phenobarbital
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Fenobarbital: De Convulsiones (Epilepsia) a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

Fenobarbital es un barbitúrico anticonvulsivante, usado para tratar casi todos los tipos de crisis epilépticas, salvo las crisis de ausencia.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, con un puntaje muy alto (99.96%).
Sin embargo, hay **0 ensayos clínicos** y solo **1 publicación** (una serie de casos sobre síndrome de Sturge-Weber), que no respalda un efecto sobre el tumor.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice «FENOBARBITAL», sin indicación explícita. Según la farmacología, su uso clínico es el tratamiento de crisis epilépticas (excepto ausencias). |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 5 (correspondientes a 3 números de registro distintos) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Por ahora la predicción **no es razonable desde el punto de vista mecanístico**. No hay datos detallados del mecanismo de acción en DrugBank. Por conocimiento farmacológico, el fenobarbital es un modulador alostérico positivo del receptor GABA-A. Potencia la inhibición neuronal, y por eso controla las convulsiones. También se sabe que interactúa con el receptor X de pregnano (PXR, gen NR1I2), lo que explica su fuerte inducción de enzimas metabolizadoras.

La relación entre la indicación original y la nueva es débil. La epilepsia es un trastorno de hiperexcitabilidad neuronal, mientras que una neoplasia del nervio trigémino es un tumor. El único artículo vinculado describe una serie de casos de síndrome de Sturge-Weber (angiomatosis trigeminal con convulsiones). Allí el fármaco actúa sobre las crisis, no sobre la neoplasia.

Por lo tanto, cualquier beneficio sería solo un control sintomático de las convulsiones asociadas, y no un efecto antitumoral. El puntaje alto de TxGNN no está respaldado por evidencia clínica ni mecanística.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales españoles de pediatría | Revisión de 14 casos de síndrome de Sturge-Weber seguidos durante 25 años, para evaluar características clínicas, evolución y respuesta terapéutica. No evalúa neoplasias del trigémino. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20108399 | FENOBARBITAL 0.4 % SOLUCIÓN ORAL | Solución oral | FENOBARBITAL (sin indicación detallada) |
| 19905550 | FENOBARBITAL TABLETAS 50 MG. | Tableta | FENOBARBITAL (sin indicación detallada) |
| 20101277 | FENOBARBITAL 10 MG TABLETAS | Tableta | FENOBARBITAL (sin indicación detallada) |

Todos los productos son fabricados por el Fondo Nacional de Estupefacientes (Ministerio de Salud y Protección Social). El paquete de datos incluye 5 registros, pero los números 20108399 y 19905550 aparecen duplicados.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: fenobarbital interactúa con el receptor X de pregnano (NR1I2). Por su fuerte inducción enzimática (CYP), puede reducir los niveles de otros fármacos administrados al mismo tiempo. Esto pesa más en pacientes que ya toman varios medicamentos.

Para las advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos, la única publicación no aborda la neoplasia, y no existe una vía mecanística directa entre el fenobarbital y un tumor del trigémino. El puntaje TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos o mecanísticos que muestren un efecto real sobre este tipo de tumor
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Obtener el mecanismo de acción desde DrugBank
- Considerar que otras indicaciones predichas relacionadas con convulsiones (por ejemplo, convulsiones reflejas) tienen un fundamento más plausible como línea de investigación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

