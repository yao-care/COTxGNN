---
layout: default
title: Deferasirox
parent: Evidencia Moderada (L3-L4)
nav_order: 152
evidence_level: L4
indication_count: 5
---

# Deferasirox
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Deferasirox: De Quelación de Hierro (Sobrecarga de Hierro) a Infección por VIH

## Resumen en Una Frase

Deferasirox es un quelante oral de hierro, utilizado en el manejo de la sobrecarga de hierro transfusional, por ejemplo en talasemia.
El modelo TxGNN predice que podría ser efectivo para la **infección por VIH**, pero la predicción se apoya solo en **0 ensayos clínicos** y **2 publicaciones** (un estudio mecanístico in vitro y una revisión general del fármaco). El único estudio mecanístico sugiere un efecto posiblemente contrario al deseado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo indica «DEFERASIROX») |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 99.40% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, deferasirox es un quelante de hierro, su uso en la sobrecarga de hierro transfusional está establecido, y la hipótesis es que la modulación del hierro celular podría influir en la biología del VIH.

La relación entre la indicación original y la nueva es indirecta. Un estudio de 2021 (PMID 34550543) muestra que el hierro en los endolisosomas **restringe** la transactivación del promotor viral (LTR) mediada por la proteína Tat del VIH-1, al aumentar la oligomerización de Tat y la expresión de β-catenina. Si esto es así, quelar el hierro con deferasirox podría **liberar esa restricción y favorecer la transcripción viral** en lugar de suprimirla.

Por eso la dirección del efecto es desfavorable o, en el mejor de los casos, incierta. El puntaje alto de TxGNN (0.994) proviene de una predicción basada en grafos de conocimiento, sin validación clínica. No debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Estudio preclínico/mecanístico in vitro | Journal of Neurovirology | El hierro endolisosomal restringe la transactivación del LTR del VIH-1 mediada por Tat, al aumentar la oligomerización de Tat y la expresión de β-catenina. Sugiere que quelar hierro podría ser desfavorable. |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Revisión (resumen de fármacos nuevos) | J Am Pharm Assoc | Revisión general de fármacos nuevos, entre ellos deferasirox. No es específica para VIH. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20176281 | THALADEF® 360 MG TABLETAS RECUBIERTAS (MSN Laboratories Private Limited) | Tableta recubierta | DEFERASIROX (el registro no detalla la indicación) |

Se reportan 20 registros en total. Los datos entregados detallan solo un registro sanitario distinto (repetido en varias filas). Por vía oral también existen tabletas dispersables.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos para VIH y la evidencia es de nivel L4, con un único estudio in vitro cuya dirección de efecto podría ser contraria a la hipótesis. El puntaje de TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de deferasirox (por ejemplo, desde DrugBank) para evaluar el vínculo con la biología del VIH.
- Estudios in vitro o in vivo que aclaren si quelar hierro favorece o inhibe la replicación del VIH.
- Advertencias y contraindicaciones del prospecto de INVIMA para el cribado de seguridad.
- Confirmar la indicación aprobada en los registros colombianos, porque el texto disponible solo dice «DEFERASIROX».

**Nota sobre otras predicciones (todas en Hold):**
- La hepatitis C crónica (rank 2, L4) tiene solo un vínculo indirecto: un posible beneficio de apoyo al reducir la carga de hierro hepático, no un efecto antiviral.
- «Hiperlipidemia combinada familiar obsoleta» (rank 4) corresponde a un término obsoleto de la ontología. Debe remapearse o excluirse.
- Las predicciones de rank 3 y 5 (trastorno del neurodesarrollo y dermatofibrosarcoma protuberans) no tienen ensayos ni literatura, y su nivel es L5.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

