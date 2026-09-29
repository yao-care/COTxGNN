---
layout: default
title: Cyclosporine
parent: Evidencia Moderada (L3-L4)
nav_order: 143
evidence_level: L4
indication_count: 7
---

# Cyclosporine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Ciclosporina: De Inmunosupresión en Trasplante a Enfermedad Granulomatosa Crónica Autosómica Recesiva

---

## Resumen en Una Frase

La ciclosporina es un inmunosupresor que inhibe la activación de los linfocitos T y se usa para evitar el rechazo en trasplantes de órganos y tejidos.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad granulomatosa crónica autosómica recesiva (EGC)**,
pero solo hay **1 ensayo clínico** (indirecto) y **1 publicación** (sobre trasplante de células madre), sin evidencia directa de eficacia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro INVIMA solo indica "CICLOSPORINA" (sin texto de indicación). Según la farmacología, se usa como inmunosupresor en trasplantes. |
| Nueva Indicación Predicha | Enfermedad granulomatosa crónica, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la ciclosporina es un inmunosupresor que bloquea la activación de los linfocitos T. Se une a las ciclofilinas (PPIA y PPID) y, por esa vía, inhibe la calcineurina. Su eficacia para prevenir el rechazo de injertos está comprobada.

La relación con la EGC aparece solo de forma indirecta. En la literatura, la ciclosporina figura como base de la profilaxis de la enfermedad injerto contra huésped (EICH) en el trasplante alogénico de células madre, que es el tratamiento curativo de la EGC. Es decir, es un apoyo del procedimiento y no trata el defecto de fondo, que está en la NADPH oxidasa.

Mecanísticamente no hay un vínculo que sugiera que inhibir la calcineurina corrija la patología de la EGC. Además, inmunosuprimir a pacientes que ya son propensos a infecciones graves podría aumentar el riesgo. El puntaje alto de TxGNN refleja una asociación del grafo de conocimiento y no evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Fase 1 | Completado | 10 | Abatacept combinado con ciclosporina y micofenolato como profilaxis de EICH en niños con trasplante de células madre no emparentado por enfermedades no malignas. La ciclosporina es tratamiento de fondo, no el fármaco en estudio, y el ensayo no es específico de EGC. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohorte | J Allergy Clin Immunol | Supervivencia excelente tras trasplante de células madre de donante hermano o no emparentado en EGC. El resumen disponible no evalúa la ciclosporina como tratamiento de la EGC. |

---

## Información de Mercado en Colombia

Se muestran los primeros registros sin repetir (el paquete incluye entradas duplicadas).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33038 | SANDIMMUN NEORAL® cápsulas blandas con microemulsión 25 mg (Novartis Pharma A.G.) | Cápsula blanda | CICLOSPORINA |
| 33037 | SANDIMMUN® NEORAL® cápsula blanda microemulsión 100 mg (Novartis Pharma A.G.) | Cápsula blanda | CICLOSPORINA |
| 20070206 | CITABICLOS® 100 (Megalabs Colombia S.A.S) | Cápsula blanda | CICLOSPORINA |

También existen presentaciones en solución inyectable y emulsión.

---

## Consideraciones de Seguridad

- **Interacciones y transportadores**: la consulta farmacológica identificó 7 dianas o transportadores con los que interactúa la ciclosporina: FPR1, ABCG2, SLC10A1, OATP1B1 (SLCO1B1), OATP1B3 (SLCO1B3), PPIA y PPID. La inhibición de transportadores como OATP1B1/1B3 y ABCG2 puede modificar la exposición a otros fármacos que dependan de ellos. No hay niveles de gravedad asignados.
- **Riesgo específico en EGC**: la inmunosupresión podría agravar el riesgo de infecciones graves en estos pacientes.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN (99.68%) no está respaldada por evidencia directa. Solo hay un ensayo de Fase 1 donde la ciclosporina es tratamiento de fondo y un estudio de cohorte sobre trasplante de células madre. No existe un mecanismo plausible que vincule la inhibición de calcineurina con la corrección de la EGC, y el perfil inmunosupresor añade un riesgo de infección en esta población.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las indicaciones originales (por ejemplo, desde la API de DrugBank).
- Prospecto de INVIMA con advertencias y contraindicaciones, para completar el tamizaje de seguridad.
- Estudios que evalúen la ciclosporina como tratamiento de la EGC y no solo como profilaxis de EICH en trasplante.
- Análisis de la relación beneficio-riesgo de la inmunosupresión en pacientes con EGC.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

