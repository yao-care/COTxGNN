---
layout: default
title: Rifaximin
parent: Evidencia Moderada (L3-L4)
nav_order: 560
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Rifaximin: nueva indicación predicha, Candidiasis oral (nivel de evidencia L4). Indicación original: No especificada"
---

# Rifaximin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Rifaximina: De Rifaximina (indicación sin especificar) a Candidiasis Oral

## Resumen en Una Frase

Rifaximina es un antibiótico oral poco absorbido, con registros sanitarios en Colombia cuyo texto de indicación solo consigna el nombre del principio activo ("Rifaximina"), sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **candidiasis oral**, pero no hay **ningún ensayo clínico** y solo **1 publicación** observacional, que además sugiere un posible **daño** (mayor riesgo de infecciones por *Candida*) y no un beneficio.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "Rifaximina") |
| Nueva Indicación Predicha | Candidiasis oral |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la rifaximina es un antibiótico oral no absorbible, de acción principalmente intestinal, con actividad antibacteriana.

Mecanísticamente, la predicción **no es plausible**. La rifaximina no tiene actividad antifúngica conocida. La única publicación disponible (PMID 34180023) indica que su uso favoreció infecciones por *Candida* resistentes a micafungina en receptores de trasplante alogénico de células madre hematopoyéticas. Esto apunta a una posible señal de daño (disbiosis intestinal que favorece el sobrecrecimiento de *Candida*), no a un beneficio terapéutico.

El alto puntaje de TxGNN (0.997) no está respaldado por un mecanismo creíble y debe interpretarse con cautela, probablemente como un artefacto del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Estudio de cohorte | Annals of Hematology | En receptores de trasplante alogénico de células madre hematopoyéticas, el uso de rifaximina (propuesta como profilaxis de infecciones bacterianas intestinales y de la enfermedad injerto contra huésped aguda) se asoció con infecciones por *Candida* resistentes a micafungina. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20227193 | THYAM® 550 MG TABLETAS RECUBIERTAS | Tableta recubierta | Rifaximina | Cancelado |
| 20080133 | IFAXIM® 550MG | Cápsula blanda | Rifaximina | Cancelado |
| 20077580 | RIFAXIGAL® 100MG/5ML | Polvo para reconstituir a suspensión oral | Rifaximina | Cancelado |
| 20235706 | RIFADEXA 550 MG TABLETAS | Tableta recubierta | Rifaximina | Cancelado |

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (no proviene del prospecto): colitis por *Clostridium difficile* y enterocolitis necrotizante perinatal.
- **Interacciones farmacológicas**: se identificaron 69 interacciones; entre las 20 detalladas, una es de nivel **mayor**: la vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR). El resto son de nivel moderado, entre ellas warfarina, ciclosporina, tolvaptán, cabozantinib, alpelisib, apalutamida, daclatasvir y ledipasvir.
- **Señal de seguridad relacionada con la nueva indicación**: la evidencia disponible sugiere que la rifaximina podría favorecer infecciones por *Candida*, incluidas cepas resistentes a micafungina.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de un mecanismo plausible, y la única literatura disponible sugiere más bien un riesgo que un beneficio. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para la evaluación de seguridad.
- Evidencia preclínica o clínica que demuestre un beneficio real en candidiasis oral.
- Aclarar la indicación original autorizada, ya que el registro solo consigna el nombre del principio activo.
- Valorar si otras predicciones (por ejemplo, la candidiasis en general, que presenta la misma señal de riesgo) justifican seguimiento; las demás predicciones (fístula comisural del labio, osteorradionecrosis de la mandíbula, leucoedema oral y síndrome de boca ardiente) carecen de evidencia y de fundamento mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

