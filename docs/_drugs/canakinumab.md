---
layout: default
title: Canakinumab
parent: Solo Predicción del Modelo (L5)
nav_order: 129
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Canakinumab: nueva indicación predicha, Infarto hepático (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
---

# Canakinumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Canakinumab: De Indicación No Especificada en el Registro a Infarto Hepático
{: .text-alpha }

## Resumen en Una Frase

Canakinumab es un anticuerpo monoclonal que bloquea la interleucina-1β (IL-1β). En Colombia su registro sanitario solo menciona el nombre del principio activo, sin una indicación específica. El modelo TxGNN predice que podría ser efectivo para **infarto hepático**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo indica "Canakinumab") |
| Nueva Indicación Predicha | Infarto hepático |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Canakinumab (traducción no oficial): «Canakinumab es un anticuerpo monoclonal humano anti-IL-1β humana del isotipo IgG1/κ. Canakinumab se une a la IL-1β humana y neutraliza su actividad al bloquear su interacción con los receptores de IL-1, pero no se une a la IL-1α ni al antagonista del receptor de IL-1 (IL-1ra).» Texto original en inglés: "Canakinumab is a human monoclonal anti-human IL-1β antibody of the IgG1/κ isotype. Canakinumab binds to human IL-1β and neutralizes its activity by blocking its interaction with IL-1 receptors, but it does not bind IL-1α or IL-1 receptor antagonist (IL-1ra)." ([DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e), versión del 2026-06-08; consultado el 2026-11-19). Según la información conocida, canakinumab neutraliza la IL-1β, una citocina clave en las enfermedades autoinflamatorias.

El infarto hepático es una necrosis isquémica del hígado causada por un evento vascular, es decir, una interrupción del flujo sanguíneo. No existe un fundamento mecanístico establecido que relacione el bloqueo de la IL-1β con esta condición. La relación entre la indicación original y la nueva no ha sido evaluada.

La predicción se basa únicamente en el puntaje del modelo. Sin estudios que la respalden, debe tomarse como una hipótesis y no como una señal de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-canakinumab-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Este registro se encuentra **cancelado**, por lo que actualmente no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-canakinumab-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20135091 | ILARIS® Solución Inyectable 150 mg/mL (Novartis Pharma A.G.) | Solución inyectable | Canakinumab (sin indicación específica) |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 100 interacciones potenciales. Las principales, de nivel moderado salvo indicación contraria, son:
- **Corticosteroides:** hidrocortisona, triamcinolona (incluida la oftálmica), dexametasona, betametasona, budesonida, prednisolona y prednisona.
- **Anticoagulantes:** apixabán, dicumarol, rivaroxabán y warfarina.
- **Estatinas:** simvastatina.
- **Radiofármacos y anticuerpos radiomarcados:** ibritumomab tiuxetán, iobenguano (I-131), tositumomab y tositumomab (I-131).
- **Interacciones menores:** sales de zinc (acetato, gluconato y sulfato).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para infarto hepático es solo del modelo (L5): no hay ensayos ni literatura, y no existe una relación mecanística plausible entre el bloqueo de IL-1β y un evento isquémico vascular.

<!-- review:begin co-lic-20261105-canakinumab-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para infarto hepático es solo del modelo (L5): no hay ensayos ni literatura, y no existe una relación mecanística plausible entre el bloqueo de IL-1β y un evento isquémico vascular. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-canakinumab-2 -->

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que sustenten un papel de la IL-1β en el infarto hepático.
- Datos detallados del mecanismo de acción y análisis de su relación con la nueva indicación.
- Información de seguridad del prospecto (advertencias y contraindicaciones).
- Verificar la situación regulatoria y de acceso.

<!-- review:begin co-lic-20261105-canakinumab-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Verificar la situación regulatoria y de acceso, dado que el registro está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-canakinumab-3 -->

**Nota adicional:** entre las demás predicciones del modelo para canakinumab, la **fiebre mediterránea familiar** tiene evidencia mucho más sólida (nivel L1). Cuenta con tres ensayos de Fase 3 completados, aunque abiertos, pequeños y centrados en síndromes periódicos asociados a criopirina, además de revisiones sistemáticas y metaanálisis. Se recomienda evaluarla en un informe aparte, con salvaguardas como limitar su uso a pacientes resistentes o intolerantes a colchicina y monitorear infecciones.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Este registro se encuentra **cancelado**, por lo que actualmente no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

