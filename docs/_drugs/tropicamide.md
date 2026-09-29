---
layout: default
title: Tropicamide
parent: Solo Predicción del Modelo (L5)
nav_order: 399
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tropicamida: De Midriasis Oftálmica a Síndrome de Cauda Equina

---

## Resumen en Una Frase

Tropicamida es un anticolinérgico de uso oftálmico tópico, utilizado originalmente como midriático de acción corta para examinar el cristalino, el humor vítreo y la retina.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de cauda equina**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tropicamida en combinaciones (midriático oftálmico) |
| Nueva Indicación Predicha | Síndrome de cauda equina |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Tropicamida es un antagonista muscarínico. Según los datos de farmacología disponibles, actúa sobre los receptores muscarínicos M2, M3, M4 y M5. Se usa en forma de solución oftálmica para dilatar la pupila durante exámenes del ojo. No se dispone de una descripción detallada del mecanismo de acción en el registro; lo anterior se basa en sus dianas farmacológicas conocidas.

La relación con el síndrome de cauda equina es solo indirecta. Los antimuscarínicos pueden reducir la hiperactividad del detrusor en la disfunción vesical neurogénica que sigue a este síndrome, y por eso el modelo pudo asociar el fármaco con la enfermedad. Sin embargo, el síndrome de cauda equina es una urgencia quirúrgica por compresión nerviosa. Aliviar síntomas no resolvería la enfermedad de fondo.

Además, la tropicamida oftálmica tiene una exposición sistémica mínima, por lo que no hay una vía plausible para llegar al efecto buscado. El puntaje alto (99.53%) puede reflejar una asociación general con la clase anticolinérgica y no un efecto específico de la tropicamida. Este razonamiento se apoya en farmacología general, no en datos propios del registro.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Se reportan 20 registros sanitarios en total. Los cinco primeros del listado corresponden al mismo registro, por lo que se muestra una sola vez:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20069775 | T-P OFTENO (Laboratorios Sophia S.A. de C.V.) | Solución oftálmica | Tropicamida combinaciones |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos ni literatura (nivel L5). Además, la tropicamida oftálmica no alcanza una exposición sistémica relevante, y el síndrome de cauda equina requiere tratamiento quirúrgico urgente, no sintomático.

Las otras dos predicciones (vejiga neurogénica e intestino irritable) también quedan en Hold por las mismas razones: no hay evidencia y ya existen antimuscarínicos orales establecidos.

**Para avanzar se necesita:**
- Datos formales del mecanismo de acción y de la exposición sistémica tras la administración oftálmica.
- Prospecto de INVIMA con advertencias y contraindicaciones, para poder hacer el tamizaje de seguridad.
- Para la predicción de vejiga neurogénica, remapear el término obsoleto de la ontología a uno vigente (por ejemplo, hiperactividad neurogénica del detrusor) antes de reevaluar.
- Estudios preclínicos o de farmacocinética que justifiquen una vía de administración distinta a la oftálmica.

*Los resultados de este informe son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

