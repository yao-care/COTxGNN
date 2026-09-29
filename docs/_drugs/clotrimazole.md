---
layout: default
title: Clotrimazole
parent: Evidencia Moderada (L3-L4)
nav_order: 137
evidence_level: L4
indication_count: 3
---

# Clotrimazole
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

# Clotrimazol: De Infecciones Fúngicas Tópicas a Acné

## Resumen en Una Frase

Clotrimazol es un antifúngico azólico de uso local, empleado en infecciones por hongos y levaduras de la piel y en candidiasis vaginal.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero la evidencia es muy débil: **1 ensayo clínico** (suspendido, sin resultados, con una combinación de tres fármacos) y **ninguna publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro solo indica el principio activo ("CLOTRIMAZOL"), sin texto de indicación. Según farmacología, se usa en infecciones fúngicas tópicas (tiña, pie de atleta) y candidiasis vaginal |
| Nueva Indicación Predicha | Acné (acne, disease) |
| Puntaje de Predicción TxGNN | 99,86 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, el clotrimazol es un antifúngico azólico que inhibe la síntesis de ergosterol (enzima CYP51) y altera la membrana del hongo. Tiene además cierta actividad antibacteriana y antiinflamatoria.

La relación con el acné es limitada. Podría tener sentido en cuadros como la foliculitis por *Malassezia* o la sobreinfección secundaria, pero no en el acné vulgar clásico. El puntaje de TxGNN es muy alto, pero no está respaldado por un mecanismo documentado.

Además, el único ensayo evalúa una combinación fija (beclometasona + gentamicina + clotrimazol), por lo que no se puede aislar el efecto del clotrimazol.

**Nota:** en el Evidence Pack, la segunda predicción (vulvovaginitis) sí cuenta con respaldo amplio (múltiples ensayos y ECAs con clotrimazol como comparador o tratamiento). Corresponde a un uso ya establecido, y la ausencia de indicaciones originales probablemente es un vacío de datos y no una nueva oportunidad de reposicionamiento.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la eficacia de beclometasona + gentamicina + clotrimazol en crema tópica en dermatosis contaminada con lesiones bilaterales simétricas. Sin resultados publicados. El aporte del clotrimazol no se puede separar y el vínculo con acné no está confirmado |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 20 registros incluyen entradas repetidas. La tabla muestra los registros únicos con sus indicaciones combinadas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19971011 | CUTAMYCON 500 MG | Cápsula blanda | CLOTRIMAZOL |
| 20018316 | DERMA Q CREMA TÓPICA | Crema tópica | MOMETASONA, CLOTRIMAZOL, COMBINACIONES |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con 8 resultados, pero corresponden a dianas moleculares del clotrimazol (base de farmacología) y no a interacciones clínicas con otros medicamentos documentadas. Las dianas son:
  - Canales de potasio KCa1.1 y KCa3.1.
  - Canales TRPM2, TRPM3 (en ratón), TRPM4 y TRPM8.
  - Receptor X de pregnano (PXR) y receptor constitutivo de androstano (CAR).

  PXR y CAR regulan enzimas metabolizadoras de fármacos, por lo que conviene evaluar posibles interacciones al usar el clotrimazol de forma sistémica.

Consultar el prospecto para advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no hay mecanismo documentado, no hay literatura y el único ensayo está suspendido, sin resultados y con una combinación de tres fármacos. No hay base para avanzar en acné.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para confirmar indicaciones, advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción (consultar la API de DrugBank).
- Conocer el estado y los resultados de NCT01244256 y, de ser posible, un ensayo con clotrimazol solo en acné.
- Definir si el caso de interés es realmente vulvovaginitis (uso ya establecido) y, en ese caso, evaluarlo por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

