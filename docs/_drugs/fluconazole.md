---
layout: default
title: Fluconazole
parent: Solo Predicción del Modelo (L5)
nav_order: 289
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Fluconazol: De Indicación Antifúngica (FLUCONAZOL) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Fluconazol es un antifúngico triazólico, registrado en Colombia bajo el texto de indicación "FLUCONAZOL" (sin detalle de la enfermedad específica).
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FLUCONAZOL (el registro no detalla la enfermedad) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción original del fármaco. Según la información conocida, fluconazol es un antifúngico triazólico que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-demetilasa) y, con ello, bloquea la síntesis de ergosterol, un componente esencial de la membrana del hongo.

La relación con la nueva indicación es débil. La queratoconjuntivitis epitelial punteada suele ser de origen viral (por ejemplo, adenovirus) o estar asociada a ojo seco, toxicidad u otras inflamaciones no fúngicas. Un antifúngico no se esperaría que trate esas causas. Solo tendría sentido mecanístico si el cuadro tuviera un origen fúngico.

Por ello, el vínculo es **especulativo**: el único sustento es el puntaje alto del modelo (99.24%), sin un mecanismo explícito ni estudios reales que lo confirmen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20053245 | HONGIZOL® CÁPSULAS (cancelado) | Cápsula dura | FLUCONAZOL |
| 48561 | BATEN® 150 MG CÁPSULAS (cancelado) | Cápsula dura | FLUCONAZOL |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: síndrome de QT largo, síndrome de QT largo familiar, enfermedad renal, piouréter, enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; se muestran las de la muestra analizada.
  - **Mayor**: clorpropamida.
  - **Moderadas**: famotidina, rabeprazol, omeprazol, dexlansoprazol, hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida (incluida la nasal), loperamida, aprepitant, bisacodilo, ácido picosulfúrico, polietilenglicol 3350 con electrolitos y saxagliptina.
  - **Menores**: anfotericina B (incluido el complejo lipídico) y claritromicina.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto, ya que no se dispone de esos datos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo antifúngico no explica un beneficio en una enfermedad ocular mayormente viral o no infecciosa. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank para analizar el vínculo mecanístico.
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para el tamizaje de seguridad.
- Evidencia real (estudios preclínicos, series de casos o ensayos), por ejemplo en queratitis o queratoconjuntivitis de origen fúngico confirmado.
- Evaluación de la compatibilidad de la vía de administración (la forma registrada es oral; una indicación ocular requeriría valorar formulaciones oftálmicas).
- Evaluación del riesgo de prolongación del QT y de las interacciones farmacológicas antes de cualquier uso en esta indicación.
- Aclarar la situación regulatoria, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

