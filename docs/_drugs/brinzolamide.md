---
layout: default
title: Brinzolamide
parent: Solo Predicción del Modelo (L5)
nav_order: 115
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Brinzolamide: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: BRINZOLAMIDA"
---

# Brinzolamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Brinzolamida: De Glaucoma/Hipertensión Ocular a Glaucoma Hereditario Primario
{: .text-alpha }

## Resumen en Una Frase

Brinzolamida es un inhibidor de la anhidrasa carbónica, utilizado para reducir la presión intraocular elevada en la hipertensión ocular y el glaucoma de ángulo abierto.
El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección; la predicción se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BRINZOLAMIDA (el registro sanitario no describe la indicación; según la información farmacológica, se usa en presión intraocular elevada, hipertensión ocular y glaucoma de ángulo abierto) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.48% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción detallado del fármaco. Según el conocimiento farmacológico general, la brinzolamida inhibe la anhidrasa carbónica (principalmente la isoenzima II). En el epitelio ciliar, esto reduce la formación de bicarbonato y la secreción de humor acuoso, lo que disminuye la presión intraocular (PIO). Los datos de farmacología compilados confirman que se une a las anhidrasas carbónicas 1, 7, 12 y 14 humanas.

La relación con la nueva indicación es directa: en el glaucoma hereditario, la PIO elevada causa la neuropatía óptica. Por ello, reducir la producción de humor acuoso es un mecanismo plausible. Sin embargo, el puntaje tan alto (0.995) probablemente refleja la asociación ya conocida entre esta clase de fármacos y el glaucoma, por lo que podría ser una **redescubierta de un uso existente** y no un verdadero hallazgo de reposicionamiento.

Conviene tener cautela: el glaucoma hereditario primario (por ejemplo, el glaucoma congénito primario, frecuentemente asociado a variantes de CYP1B1) es una anomalía del desarrollo de la malla trabecular, y el tratamiento médico suele ser solo un puente temporal hacia la cirugía. Los datos disponibles no establecen la eficacia en esta población específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20075435 | SIMBRINZA® SUSPENSION OFTALMICA | Suspensión oftálmica | BRINZOLAMIDA | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y devolvió 4 resultados, todos de tipo farmacológico (unión a dianas), sin nivel de gravedad asignado. Corresponden a la inhibición de las anhidrasas carbónicas humanas 1, 7, 12 y 14. No son interacciones medicamentosas clínicas documentadas.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y es probable que refleje un uso ya conocido de la clase farmacológica. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de seguridad que bloquea el avance.
- Confirmar el mecanismo de acción en DrugBank.
- Aclarar la indicación aprobada real, ya que el registro solo contiene el nombre del fármaco.
- Buscar ensayos clínicos y literatura específicos sobre glaucoma hereditario primario/congénito, y determinar si es un reposicionamiento real o un uso ya establecido.
- Verificar la situación comercial actual en Colombia (registro cancelado) y la disponibilidad de formulaciones oftálmicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

