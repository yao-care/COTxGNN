---
layout: default
title: Chlorthalidone
parent: Solo Predicción del Modelo (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# Clortalidona: De Hipertensión Arterial a Glaucoma Hereditario Primario

## Resumen en Una Frase

La clortalidona es un diurético tipo tiazida, usado principalmente como antihipertensivo y para reducir edemas de causas específicas.
El modelo TxGNN predice que podría ser efectiva para **glaucoma hereditario primario**, pero por ahora es solo una predicción del modelo,
con **0 ensayos clínicos** y **0 publicaciones** que la respalden.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial y edema (según datos de farmacología; el registro INVIMA solo lista el nombre "Clortalidona", sin texto de indicación) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la clortalidona es un diurético tipo tiazida con eficacia comprobada en hipertensión. Los datos de farmacología la asocian con varias anhidrasas carbónicas (CA1, CA4, CA7, CA12 y CA14) y con la enzima NAPEPLD.

El único vínculo mecanístico plausible con el glaucoma es su actividad débil como inhibidora de la anhidrasa carbónica. Esa enzima participa en la producción del humor acuoso, así que en teoría podría influir en la presión intraocular. Es el mismo mecanismo de fármacos como la acetazolamida.

Este vínculo es débil. Los diuréticos tiazídicos no son una terapia establecida para bajar la presión intraocular. Además, el glaucoma hereditario primario tiene un origen genético, lo que debilita aún más la relación. El puntaje alto del modelo (posición 985) no está respaldado por ninguna señal clínica en los datos disponibles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se encontraron 20 registros en total. Varias filas del paquete estaban duplicadas, así que se muestran los registros únicos:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20101174 | CARDIOL 25 MG® | Tableta recubierta | Clortalidona (el registro no detalla indicación) |
| 20061697 | HIDROTEN® 25 MG TABLETAS | Tableta | Clortalidona (el registro no detalla indicación) |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta devolvió 6 registros, pero corresponden a dianas farmacológicas (anhidrasas carbónicas 1, 4, 7, 12 y 14, y NAPEPLD), no a interacciones con otros medicamentos.

Consultar el prospecto para informacion de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y el mecanismo plausible (inhibición débil de la anhidrasa carbónica) no está respaldado por uso clínico. Además, la causa genética del glaucoma hereditario primario y el hecho de que los diuréticos sistémicos no se usan para bajar la presión intraocular hacen poco probable un beneficio real.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Estudios preclínicos o clínicos sobre el efecto de la clortalidona en la presión intraocular
- Evaluación de la vía de administración (la forma disponible es oral)
- Como línea alternativa, la predicción de *enfermedad pulmonar cardíaca crónica* (rango 8) tiene nivel L4, con un reporte de 1967 sobre clortalidona en insuficiencia cardíaca congestiva por cor pulmonale crónico. Sería una pregunta de investigación más razonable, aunque su diseño no está verificado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

