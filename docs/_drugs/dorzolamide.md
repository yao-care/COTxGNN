---
layout: default
title: Dorzolamide
parent: Evidencia Alta (L1-L2)
nav_order: 166
evidence_level: L2
indication_count: 10
---

# Dorzolamide
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Dorzolamida: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Dorzolamida es un inhibidor de la anhidrasa carbónica que se aplica en gotas oftálmicas para reducir la presión intraocular en el glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**,
con **1 ensayo clínico** (Fase 2) y **ninguna publicación** que respalden actualmente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones con timolol (texto del registro sanitario). DrugBank no lista indicaciones originales; el uso clínico conocido es reducir la presión intraocular en glaucoma de ángulo abierto e hipertensión ocular |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la farmacología conocida, la dorzolamida inhibe la anhidrasa carbónica II en el cuerpo ciliar. Esto reduce la secreción de humor acuoso y baja la presión intraocular.

Este efecto no depende de la causa del glaucoma, así que es plausible que sirva también en las formas hereditarias. Aun así, la dorzolamida ya está comercializada para glaucoma. Por eso esta predicción se parece más a una extensión de su uso actual que a un reposicionamiento verdadero.

Otras indicaciones predichas por el modelo (alopecia, hipotricosis, insuficiencia cardíaca congestiva, insuficiencia respiratoria) no tienen un vínculo mecanístico creíble ni evidencia clínica. Probablemente son artefactos del grafo de conocimiento. Las entradas de glaucoma de ángulo abierto (posiciones 6 y 7) corresponden al uso ya aprobado y tienen evidencia L1.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Fase 2 | Completado | 37 | Evalúa el efecto hipotensor ocular de latanoprost y dorzolamida en glaucoma pediátrico primario refractario a cirugía, y su seguridad. No se pudo confirmar la población exacta (congénito o hereditario del adulto) ni que la dorzolamida fuera el inhibidor de anhidrasa carbónica usado. Muestra pequeña |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20254363 | DORZOTRISOL T SOLUCIÓN OFTÁLMICA (Laboratorios Incobra S.A.) | Solución oftálmica | Timolol combinaciones |

Los datos recibidos indican 12 registros en total, pero las 5 filas entregadas corresponden todas al mismo registro sanitario. Por eso solo se muestra uno.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó, pero solo devolvió interacciones farmacológicas con dianas (anhidrasa carbónica 1, 7, 12 y 14), no interacciones con otros medicamentos.
- No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA. Consultar el prospecto para la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para esta indicación es un único ensayo de Fase 2 pequeño (n=37), cuya población y uso de dorzolamida no se pudieron confirmar, y no hay publicaciones. Además, faltan los datos de seguridad del prospecto de INVIMA. El uso en glaucoma de ángulo abierto ya está respaldado (L1), pero eso no valida el glaucoma hereditario primario.

**Para avanzar se necesita:**
- Confirmar en el registro del ensayo NCT01527682 la población incluida y si la dorzolamida fue el inhibidor de anhidrasa carbónica usado.
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que actualmente bloquea el tamizaje de seguridad.
- Datos de mecanismo de acción desde DrugBank.
- Búsqueda de literatura específica sobre dorzolamida en glaucoma hereditario o pediátrico.
- Si se avanza, incluir salvaguardas por alergia a sulfonamidas, compromiso del endotelio corneal e insuficiencia renal, según el análisis del Evidence Pack.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

