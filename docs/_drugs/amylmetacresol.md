---
layout: default
title: Amylmetacresol
parent: Solo Predicción del Modelo (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Amylmetacresol: nueva indicación predicha, Síndrome de la cauda equina (nivel de evidencia L5). Indicación original: Dicloro­bencil alcohol"
monitor_inn: "amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Amilmetacresol: De Dicloro­bencil Alcohol (antiséptico orofaríngeo) a Síndrome de la Cauda Equina
{: .text-alpha }

## Resumen en Una Frase

Amilmetacresol es un antiséptico utilizado en pastillas para la garganta; en Colombia su registro (ADVITABS® tabletas) figura con la indicación "dicloro­bencil alcohol".
El modelo TxGNN predice que podría ser efectivo para **síndrome de la cauda equina**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dicloro­bencil alcohol (según el registro INVIMA) |
| Nueva Indicación Predicha | Síndrome de la cauda equina |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, amilmetacresol es un antiséptico que se usa en pastillas para la garganta, normalmente junto con alcohol dicloro­bencílico, y su uso se limita a la mucosa orofaríngea.

Con la información compilada, **no se identifica un vínculo mecanístico plausible** con el síndrome de la cauda equina. Esta es una condición neurológica compresiva que se maneja principalmente con cirugía, y un antiséptico de uso local no tiene una justificación terapéutica evidente. El puntaje alto de TxGNN (0.9999) es solo una predicción computacional y no está respaldado por evidencia clínica ni bibliográfica.

Otras predicciones del modelo muestran el mismo patrón. Las principales son vejiga neurogénica (término obsoleto en la ontología), síndrome del intestino irritable, y varias enfermedades oculares (cuerpo ciliar, panuveítis, enfermedad del iris, uveítis). Para el intestino irritable existe solo un vínculo especulativo: se ha propuesto un efecto tipo anestésico local (bloqueo de canales de sodio), pero el uso en pastillas implica una exposición sistémica o intestinal mínima. Para las indicaciones oculares no hay datos de seguridad ni de penetración, y los antisépticos fenólicos podrían ser irritantes o tóxicos en el ojo.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20209766 (cancelado) | ADVITABS® TABLETAS | Tableta (vía oral) | Dicloro­bencil alcohol |

El fabricante es HALEON COLOMBIA S.A.S. No hay registros vigentes en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5): no hay ensayos clínicos ni literatura, no existe un vínculo mecanístico plausible, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank)
- Prospecto de INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad
- Evidencia preclínica o clínica que justifique un vínculo con la nueva indicación
- Evaluación de compatibilidad de vía de administración (la forma oral actual es una pastilla de acción local)
- Considerar priorizar otras indicaciones o fármacos con mayor sustento, dado que ninguna de las 10 predicciones principales tiene evidencia de apoyo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

