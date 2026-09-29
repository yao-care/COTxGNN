---
layout: default
title: Octreotide
parent: Solo Predicción del Modelo (L5)
nav_order: 300
evidence_level: L5
indication_count: 2
---

# Octreotide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Octreotida: De Tumores Productores de Hormona de Crecimiento a Queratosis Folicular Invertida Vulvar

## Resumen en Una Frase

Octreotida es un análogo de la somatostatina, utilizado originalmente en tumores productores de hormona de crecimiento y tumores hipofisarios secretores de TSH.
El modelo TxGNN predice que podría ser efectivo para **queratosis folicular invertida vulvar**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | OCTREOTIDO (el registro sanitario solo repite el nombre del principio activo, sin texto de indicación explícito) |
| Nueva Indicación Predicha | Queratosis folicular invertida vulvar |
| Puntaje de Predicción TxGNN | 99,58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información farmacológica disponible, octreotida es un péptido análogo de la somatostatina que actúa sobre los receptores de somatostatina SST2, SST3 y SST5 (genes SSTR2, SSTR3 y SSTR5). Su uso comprobado incluye tumores productores de hormona de crecimiento, tumores hipofisarios secretores de TSH y la obtención de imágenes en medicina nuclear de tumores neuroendocrinos que expresan receptores de somatostatina.

**Los datos no respaldan un vínculo mecanístico entre este mecanismo y la queratosis folicular invertida vulvar.** Esta es una lesión epitelial benigna, y no hay evidencia que conecte la señalización de somatostatina con ella. El único sustento es el puntaje del modelo (0,996), que es una salida computacional y no evidencia clínica ni preclínica. La relación entre la indicación original y la nueva sigue sin evaluarse.

Además, el modelo predijo como segunda indicación la **queratosis seborreica**, con un puntaje casi idéntico (99,55%) y también sin ensayos ni publicaciones. Esa similitud sugiere que el modelo podría estar captando un patrón de similitud entre enfermedades de la misma clase (lesiones queratinocíticas benignas) y no una señal específica del fármaco. Además, estas lesiones suelen tratarse con fines estéticos, por lo que la relación beneficio-riesgo de un péptido sistémico no está clara.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20007947 | SANDOSTATIN® AMPOLLAS 0.1 MG (NOVARTIS PHARMA AG) | Solución inyectable | OCTREOTIDO (sin indicación explícita en el registro) |

Los 12 registros indicados provienen de este mismo número de registro sanitario y producto; las cinco entradas recibidas eran idénticas. La única vía de administración registrada corresponde a solución inyectable.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos de interacciones recibidos corresponden a la unión con los receptores SST2, SST3 y SST5, es decir, información farmacológica de dianas. No incluyen interacciones con otros medicamentos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura y sin un vínculo mecanístico verificable. La forma inyectable sistémica tampoco tiene una compatibilidad de vía evaluada para una lesión cutánea benigna.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto aprobado por INVIMA (advertencias y contraindicaciones), requisito para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción del fármaco (por ejemplo, desde DrugBank) para evaluar un posible vínculo con la queratosis folicular invertida vulvar.
- Realizar una búsqueda dirigida de literatura y ensayos sobre somatostatina o análogos en lesiones queratinocíticas benignas.
- Evaluar la compatibilidad de vía de administración y la relación beneficio-riesgo frente a los tratamientos habituales.
- Verificar si el puntaje casi idéntico de las dos indicaciones predichas refleja un sesgo del modelo por clase de enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

