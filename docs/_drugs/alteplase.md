---
layout: default
title: Alteplase
parent: Solo Predicción del Modelo (L5)
nav_order: 42
evidence_level: L5
indication_count: 9
---

# Alteplase
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

# Alteplasa: De Indicación Registrada (Alteplasa) a Infarto de Miocardio Posteroinferior

## Resumen en Una Frase

Alteplasa es un activador del plasminógeno tisular recombinante (trombolítico), registrado en Colombia con el producto Actilyse 50 mg, cuyo registro sanitario figura hoy como cancelado.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posteroinferior**, pero **no hay ensayos clínicos ni publicaciones** específicos para esta indicación que respalden la predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Alteplasa (el registro no detalla la indicación aprobada más allá del nombre del principio activo) |
| Nueva Indicación Predicha | Infarto de miocardio posteroinferior |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, alteplasa es un activador del plasminógeno tisular recombinante: convierte el plasminógeno en plasmina, que disuelve la fibrina de los coágulos.

En el infarto de miocardio, la causa habitual es un trombo que ocluye una arteria coronaria. La disolución del trombo es, por tanto, un enfoque mecanísticamente coherente. Esto explica el puntaje alto del modelo (99.79%).

Un matiz importante: la trombólisis ya es una estrategia establecida en el infarto con elevación del ST en general. El infarto posteroinferior es probablemente un subtipo de un uso ya conocido y no un reposicionamiento genuino. El puntaje es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para infarto de miocardio posteroinferior.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

### Otras indicaciones predichas con evidencia (contexto)

Las siguientes predicciones secundarias sí cuentan con algo de evidencia, aunque mayormente indirecta:

| Indicación | Puntaje TxGNN | Nivel | Evidencia disponible |
|------|------|------|---------|
| Infarto de miocardio septal | 99.77% | L4 | 3 publicaciones: un estudio de 1996 sobre función ventricular izquierda tras trombólisis tardía con alteplasa ([8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/)), un reporte de caso de 2023 ([37754803](https://pubmed.ncbi.nlm.nih.gov/37754803/)) y una cohorte de 2025 ([40281444](https://pubmed.ncbi.nlm.nih.gov/40281444/)). Indirecta, no específica del subtipo |
| Trombofilia | 99.43% | L2 | 1 ensayo Fase 2 en reclutamiento ([NCT05540834](https://clinicaltrials.gov/study/NCT05540834), 70 participantes, tPA guiado por pruebas viscoelásticas en insuficiencia respiratoria aguda protrombótica) y numerosos reportes de caso |
| Estenosis coronaria | 99.14% | L2 | Sin ensayos registrados. Incluye un ensayo aleatorizado doble ciego de alteplasa vs. placebo en dolor torácico en reposo ([8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/), 1993) y un estudio en angina inestable ([8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/), 1996) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33103 (cancelado) | ACTILYSE 50 MG (Boehringer Ingelheim International GmbH) | Polvo liofilizado para reconstituir a solución inyectable | ALTEPLASE |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Debe consultarse el prospecto para esa información. Tampoco se identificaron contraindicaciones en el grafo de conocimiento.

- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las revisadas:
  - **Mayores**: abciximab, fondaparinux, apixabán, acalabrutinib, anisindiona, deferasirox, ibritumomab tiuxetán y tositumomab. En su mayoría implican un riesgo aditivo de sangrado.
  - **Moderadas**: ácido acetilsalicílico, ibuprofeno, ketorolaco, fluvoxamina, fosinopril, ácido aminocaproico, aprotinina, fenfluramina, dexfenfluramina y sibutramina.
- Por su mecanismo, el sangrado es el riesgo central a vigilar, sobre todo en combinación con anticoagulantes y antiagregantes.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el infarto posteroinferior carece de ensayos y literatura específicos (L5). Además, probablemente corresponde a un subtipo de un uso ya establecido de la trombólisis, y no a un reposicionamiento real. El único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Aclarar si esta indicación aporta algo más allá de la trombólisis ya establecida en infarto con elevación del ST.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, ya que su ausencia impide el análisis de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Confirmar la situación regulatoria vigente de alteplasa en Colombia (registro cancelado) y la disponibilidad de otros productos.
- Si se busca una línea con más potencial, evaluar la trombofilia (ensayo Fase 2 NCT05540834 en curso) o la estenosis coronaria, siempre con atención al riesgo de sangrado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

