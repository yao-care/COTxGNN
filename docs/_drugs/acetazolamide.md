---
layout: default
title: Acetazolamide
parent: Solo Predicción del Modelo (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Acetazolamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Acetazolamida: De Glaucoma, Epilepsia y Edema a Hipertermia Maligna Inducida por Ejercicio

## Resumen en Una Frase

La acetazolamida es un inhibidor de la anhidrasa carbónica, usado para tratar glaucoma, epilepsia y edema. El modelo TxGNN predice que podría ser efectiva para la **hipertermia maligna inducida por ejercicio**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Se apoya únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma, epilepsia y edema. Los registros INVIMA solo indican "ACETAZOLAMIDA" como texto de indicación; estos usos provienen de los datos de farmacología. |
| Nueva Indicación Predicha | Hipertermia maligna inducida por ejercicio |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo de mecanismo del fármaco. Según los datos de farmacología, la acetazolamida inhibe varias isoformas de la anhidrasa carbónica (CA1, CA4, CA7, CA12, CA14 en humanos, y CA13 en ratón). Esto altera el equilibrio ácido-base y el balance de iones, lo que explica su efecto diurético, su reducción de la presión ocular y su efecto antiepiléptico.

La relación con la nueva indicación es débil. La hipertermia maligna inducida por ejercicio se asocia a fallas en el manejo del calcio muscular (receptor de rianodina). Nada en los datos conecta la inhibición de la anhidrasa carbónica con esa vía. El vínculo mecanístico no está claro y la predicción descansa solo en el modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19973358 | VICLEAR® (COLMED LTDA) | Tableta | Acetazolamida (el registro no detalla la indicación) |

Nota: los 5 registros detallados en los datos corresponden al mismo número sanitario (19973358) y se muestran una sola vez. El total reportado es de 10 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos de seguridad de INVIMA (advertencias y contraindicaciones) no están disponibles. La sección de interacciones contiene únicamente blancos farmacológicos (anhidrasas carbónicas), no interacciones con otros medicamentos.

Para las poblaciones de otras predicciones, los datos señalan dos riesgos:
- En cirrosis, la acetazolamida puede precipitar hiperamonemia y encefalopatía.
- Puede causar hipopotasemia y acidosis metabólica.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción tiene nivel de evidencia L5: no hay ensayos, no hay publicaciones y no existe un vínculo mecanístico identificado.
- Entre las demás predicciones, la de **cardiomiopatía** (L4, etapa S1) tiene más respaldo, con 3 ensayos en insuficiencia cardíaca. Aun así es indirecta, porque la insuficiencia cardíaca no es cardiomiopatía y los ensayos siguen reclutando sin resultados.

**Para avanzar se necesita:**
- Prospecto de INVIMA con advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad).
- Datos de mecanismo de acción desde DrugBank.
- Búsqueda dirigida de literatura sobre acetazolamida e hipertermia maligna o canalopatías musculares.
- Evaluar si conviene priorizar la indicación de cardiomiopatía en lugar de esta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

