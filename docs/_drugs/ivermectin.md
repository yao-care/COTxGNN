---
layout: default
title: Ivermectin
parent: Solo Predicción del Modelo (L5)
nav_order: 234
evidence_level: L5
indication_count: 9
---

# Ivermectin
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

# Ivermectina: De Infecciones Parasitarias a Candidiasis Vulvovaginal

## Resumen en Una Frase

La ivermectina es un antiparasitario de uso oral (y tópico) que se emplea contra infecciones parasitarias y piojos de la cabeza.
El modelo TxGNN predice que podría ser efectiva para **candidiasis vulvovaginal**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro INVIMA solo indica "IVERMECTINA" (sin indicación explícita). Según la farmacología, infecciones parasitarias (excepto tenias) y pediculosis |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente. Según la información conocida, la ivermectina actúa sobre los canales de cloruro activados por glutamato de los invertebrados, lo que explica su eficacia antiparasitaria. En humanos, la base de datos farmacológica la vincula con el receptor de glicina, el receptor nicotínico α7 (CHRNA7) y los receptores P2X4 y P2X7.

Los hongos no tienen un blanco equivalente claro. Por eso no se puede establecer un vínculo mecanístico directo entre la ivermectina y *Candida* con los datos disponibles. El puntaje alto de TxGNN probablemente refleja cercanía en el grafo de conocimiento (por ejemplo, con nodos relacionados con candidiasis) y no una relación biológica demostrada.

La indicación original (parasitosis) y la nueva (infección fúngica de la mucosa vulvovaginal) son enfermedades infecciosas, pero de organismos distintos. Hoy la predicción debe tratarse como una hipótesis sin respaldo, no como una oportunidad de reposicionamiento validada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se listan los registros únicos entre los 20 registros sanitarios; la fuente repite algunas filas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20253293 | SIMPIOX | Solución oral | IVERMECTINA (sin indicación detallada en el registro) |
| 19979253 | IVERMECTINA 0.6% GOTAS | Solución oral | IVERMECTINA (sin indicación detallada en el registro) |
| 19980678 | QUANOX | Solución oral | IVERMECTINA (sin indicación detallada en el registro) |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta terminó sin interacciones fármaco-fármaco documentadas. Las 4 entradas devueltas son blancos farmacológicos: receptor de glicina, receptor nicotínico α7, P2X4 (rata) y P2X7. No son interacciones clínicas con otros medicamentos.
- **Poblaciones especiales**: dos predicciones del modelo (candidiasis congénita y neonatal) implicarían uso pediátrico o neonatal, que requeriría evidencia de seguridad propia.

Consultar el prospecto para información de seguridad, advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos ni literatura, y no hay un blanco fúngico plausible para la ivermectina. Las otras 8 predicciones (candidiasis esofágica, VPH anogenital, vulvovaginitis, etc.) tienen el mismo nivel de evidencia. Los dos artículos vinculados, sobre estrongiloidiasis y sarna costrosa, tratan usos antiparasitarios y no candidiasis.

**Para avanzar se necesita:**
- Actividad antifúngica in vitro de la ivermectina contra *Candida* (por ejemplo, CMI en *C. albicans* y *C. glabrata*)
- Datos del mecanismo de acción desde DrugBank, para evaluar un posible blanco fúngico
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para cualquier evaluación de seguridad
- Comparación con los tratamientos antifúngicos estándar (azoles, nistatina), que ya tienen eficacia demostrada
- Evidencia de seguridad específica antes de considerar poblaciones pediátricas o neonatales

*Este informe es solo de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

