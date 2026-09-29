---
layout: default
title: Irbesartan
parent: Solo Predicción del Modelo (L5)
nav_order: 230
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Irbesartán: De Indicación No Especificada en el Registro a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Irbesartán está comercializado en Colombia, pero el registro sanitario solo indica el nombre del principio activo y no declara una indicación original en texto.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice "IRBESARTAN") |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Como conocimiento farmacológico general (no como evidencia de los datos suministrados), el irbesartán es un bloqueador del receptor de angiotensina II tipo 1 (ARA-II). Este tipo de fármaco reduce la presión arterial y la presión dentro de los glomérulos del riñón.

Desde ese punto de vista, un vínculo con el daño renal causado por la hipertensión es biológicamente plausible. Sin embargo, el puntaje de TxGNN (0.993) es solo una predicción, y no hay estudios que la confirmen.

Además, la hipertensión maligna es una emergencia hipertensiva que normalmente se maneja con fármacos intravenosos de dosis ajustable. Un ARA-II oral no sería tratamiento de primera línea para la fase aguda. Un posible uso tendría que ser complementario o de control a largo plazo, y eso requeriría estudios específicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20048718 | CORIONAL® 300 MG TABLETAS RECUBIERTAS (CLOSTER PHARMA S.A.S.) | Tableta recubierta (vía oral) | IRBESARTAN (solo se indica el principio activo) |

Nota: el paquete de datos reporta 20 registros en total, pero las entradas disponibles corresponden todas al mismo registro sanitario, por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no hay ensayos clínicos ni literatura específica sobre irbesartán en esta indicación (nivel L5). Además, la hipertensión maligna se trata normalmente con fármacos intravenosos, y faltan los datos de seguridad del prospecto.

Las otras tres indicaciones predichas tampoco tienen respaldo suficiente:
- **Hipertensión renovascular maligna:** Hold. Los ARA-II tienen un riesgo renal conocido en la estenosis bilateral de la arteria renal, por lo que la seguridad debe revisarse antes de avanzar.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia:** Hold. Las 20 publicaciones recuperadas tratan de hipoxia en general y ninguna evalúa irbesartán ni otro ARA-II.
- **Hipertensión pulmonar de mecanismo multifactorial poco claro:** Hold. No hay ningún dato aparte del puntaje.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío de datos bloqueante.
- Obtener el mecanismo de acción desde DrugBank (DB01029).
- Hacer una búsqueda dirigida de literatura y ensayos sobre ARA-II en enfermedad renal hipertensiva maligna.
- Confirmar cuál es la indicación aprobada del irbesartán en el registro colombiano, ya que el texto actual solo trae el nombre del fármaco.
- Evaluar la compatibilidad de la vía de administración (oral) con el escenario clínico de una emergencia hipertensiva.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

