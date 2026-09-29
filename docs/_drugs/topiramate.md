---
layout: default
title: Topiramate
parent: Solo Predicción del Modelo (L5)
nav_order: 389
evidence_level: L5
indication_count: 9
---

# Topiramate
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

# Topiramato: De Epilepsia a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

Topiramato es un antiepiléptico de amplio espectro, usado en epilepsia y prevención de migraña, y comercializado en Colombia bajo el nombre Topamac®.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice «TOPIRAMATO», sin indicación explícita. El uso clínico conocido es epilepsia y prevención de migraña |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, topiramato actúa mediante bloqueo de canales de sodio, potenciación de la actividad GABA-A, antagonismo de receptores AMPA/kainato e inhibición débil de la anhidrasa carbónica. Su eficacia en epilepsia está bien establecida.

Sin embargo, **no se identificó un vínculo mecanístico plausible** con la neoplasia del nervio trigémino. Ninguna de estas acciones está establecida como antineoplásica. Tampoco se ha evaluado la similitud entre la indicación original (un trastorno neurológico funcional) y la nueva (un tumor).

El puntaje de 99.70% (posición 3017 en el ranking del modelo) es solo una predicción. Sin ensayos ni publicaciones, no debe interpretarse como señal de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 213766 | TOPAMAC® 100 MG TABLETAS (Janssen Cilag S.A.) | Tableta | TOPIRAMATO (sin indicación detallada en el registro) |

Nota: las 5 entradas recuperadas corresponden al mismo registro sanitario y se muestran como una sola fila. En total hay 20 registros sanitarios y la única forma farmacéutica encontrada es oral (tableta).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones fármaco-fármaco. Los 4 hallazgos son dianas farmacológicas, todas isoformas de anhidrasa carbónica humana: CA1, CA4, CA7 y CA12. Esto es coherente con la inhibición débil de la anhidrasa carbónica descrita para topiramato.

Las advertencias y contraindicaciones no están disponibles. Consultar el prospecto de INVIMA para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que vincule topiramato con la neoplasia del nervio trigémino, y su mecanismo conocido no es antineoplásico. El único sustento es el puntaje del modelo (nivel L5).

Otras predicciones del mismo análisis, como epilepsia visual y «thinking seizures», tienen más literatura (nivel L2). Aun así, son subtipos de epilepsia, una indicación para la que topiramato ya se usa, por lo que no constituyen un reposicionamiento real.

**Para avanzar se necesita:**
- Estudios preclínicos o de mecanismo que muestren algún efecto de topiramato sobre células tumorales del nervio trigémino
- Revisar por qué el modelo asigna un puntaje tan alto sin respaldo bibliográfico, para descartar un artefacto de la ontología
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que actualmente bloquea el tamizaje de seguridad
- Obtener los datos detallados del mecanismo de acción desde DrugBank
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

