---
layout: default
title: Mecasermin
parent: Solo Predicción del Modelo (L5)
nav_order: 420
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Mecasermin: nueva indicación predicha, Monosomía X (nivel de evidencia L5). Indicación original: MECASERMINA"
---

# Mecasermin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Mecasermina: De Deficiencia de IGF-1 a Monosomía X

## Resumen en Una Frase

Mecasermina (IGF-1 recombinante) se comercializó en Colombia bajo la marca Increlex®, con un registro sanitario cuyo texto de indicación solo dice "MECASERMINA".
El modelo TxGNN predice que podría ser efectivo para **monosomía X (síndrome de Turner)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción computacional con plausibilidad mecanística indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MECASERMINA (el registro no detalla la indicación; el texto solo repite el nombre del principio activo) |
| Nueva Indicación Predicha | Monosomía X |
| Puntaje de Predicción TxGNN | 99.59% |
| Nivel de Evidencia | L4 (solo plausibilidad mecanística indirecta; no hay estudios recuperados) |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, mecasermina es IGF-1 recombinante: actúa sobre el eje hormona de crecimiento (GH)–IGF-1 y corrige la deficiencia de IGF-1. Se utiliza en la deficiencia primaria grave de IGF-1, incluida la insensibilidad a la GH.

La monosomía X (síndrome de Turner) se caracteriza por talla baja y falla de crecimiento. Por eso existe una relación biológica plausible con una terapia que actúa sobre el eje del crecimiento. Sin embargo, el vínculo es **indirecto**: los pacientes con síndrome de Turner normalmente se tratan con hormona de crecimiento y, en general, no son insensibles a la GH de forma clásica.

El puntaje TxGNN muy alto es solo una predicción computacional. No se recuperaron ensayos ni literatura, por lo que la calificación L4 refleja plausibilidad mecanística y no estudios reales.

### Otras predicciones del modelo (para contexto)

| Enfermedad Predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Síndrome de insensibilidad a la GH con disregulación inmune tipo 2, autosómico dominante | 99.06% | L4 | Es el candidato biológicamente más coherente (insensibilidad a la GH con IGF-1 bajo, cercano a la indicación aprobada de mecasermina), aunque el componente inmunológico no se resolvería con IGF-1 |
| Enfermedad de Wolman con hipolipoproteinemia y acantocitosis | 99.09% | L5 | Sin vínculo mecanístico claro; especulativo |
| Várices esofágicas con sangrado | 99.03% | L5 | Sin vínculo mecanístico directo; la deficiencia de IGF-1 en hepatopatía es un marcador, no una justificación terapéutica |
| Várices esofágicas sin sangrado | 99.03% | L5 | Puntaje idéntico al anterior, probablemente un artefacto de nodos del grafo y no una señal independiente |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20154631 (cancelado) | INCRELEX® 10 MG/ML SOLUCIÓN INYECTABLE (IPSEN PHARMA S.A.S.) | Solución inyectable | MECASERMINA |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 24 interacciones de nivel moderado (fuente: DDInter). Las principales corresponden a fármacos hipoglucemiantes, con riesgo de hipoglucemia aditiva:
  - **Sulfonilureas y secretagogos**: clorpropamida, acetohexamida, glimepirida, glipizida, glibenclamida (gliburida) y nateglinida.
  - **Insulinas**: insulina humana (regular, isófana, zinc, zinc extendida, inhalada de acción rápida), aspart (incluida aspart protamina), degludec, detemir, glargina, glulisina y lispro (incluida lispro protamina).

  La lista incluye varias de estas entradas; el total reportado es de 24, aunque el detalle disponible muestra 20.
- Como consideración general del grupo, la hipoglucemia y el efecto del IGF-1 sobre el crecimiento tisular requerirían evaluación específica en cada población candidata (por ejemplo, pacientes cirróticos).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para monosomía X tiene un puntaje TxGNN alto, pero no cuenta con ensayos clínicos ni literatura recuperada, y el vínculo mecanístico es indirecto, ya que el síndrome de Turner se maneja habitualmente con hormona de crecimiento. Además, el único registro sanitario colombiano está cancelado, y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), actualmente un vacío de información bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y ensayos sobre IGF-1 en síndrome de Turner.
- Evaluar con prioridad el candidato de insensibilidad a la GH (STAT5B), que es el más coherente mecanísticamente.
- Confirmar la situación regulatoria y la disponibilidad actual del producto en Colombia, dado que el registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

