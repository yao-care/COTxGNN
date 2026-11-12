---
layout: default
title: Palonosetron
parent: Solo Predicción del Modelo (L5)
nav_order: 496
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Palonosetron: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"PALONO…"
monitor_inn: "PALONOSETRON"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Palonosetrón: De Antiemético (indicación no detallada en el registro) a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Palonosetrón es un antagonista del receptor 5-HT3, registrado en Colombia como solución inyectable; el texto de indicación del registro sanitario solo repite el nombre del fármaco, sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero **no hay ensayos clínicos** y la única publicación disponible es un reporte de caso que describe cefalea tipo migraña **inducida** por el fármaco, es decir, una señal de seguridad y no de beneficio.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "PALONOSETRON") |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, palonosetrón es un antagonista del receptor de serotonina 5-HT3, utilizado clásicamente para prevenir las náuseas y vómitos asociados a la quimioterapia y al periodo posoperatorio. Las vías serotoninérgicas participan en la fisiopatología de la migraña, lo cual podría explicar la asociación detectada por el modelo.

Sin embargo, la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La única publicación asociada (PMID 21132477) reporta que palonosetrón **provocó** cefalea tipo migraña, lo que va en dirección opuesta a un efecto terapéutico. Por ello, el vínculo mecanístico es especulativo y la dirección clínica del efecto es desfavorable.

Las otras predicciones del modelo tampoco cuentan con respaldo: "migraña con aura del tronco encefálico" (0.9967) deriva probablemente de su similitud con la migraña en general; "atrofodermia vermiculada" (0.9913) y "uleritema ofriógenes" (0.9907) son trastornos cutáneos raros sin ninguna justificación farmacológica identificable, probablemente reflejo de similitudes que el modelo aprendió entre enfermedades relacionadas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Reporte de caso | Can J Anaesth | Describe cefalea tipo migraña inducida por palonosetrón; es una señal de seguridad, no evidencia de beneficio terapéutico |

Nota: una revisión de 2026 (PMID 42748473, *Eur Heart J Cardiovasc Pharmacother*) sobre prolongación del QT asociada a antieméticos se vinculó a una predicción relacionada (susceptibilidad a migraña). Es relevante para la seguridad cardiaca, no para la eficacia en migraña.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20156752 | Palonosetron 250 mcg/5 mL solución inyectable (HB Human Bioscience S.A.S.) | Solución inyectable | PALONOSETRON (sin detalle de indicación) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las analizadas, las de nivel **mayor** incluyen:
  - Opioides y analgésicos: fentanilo, alfentanilo, tramadol
  - Dextrometorfano
  - Triptanes: almotriptán, sumatriptán
  - Antiarrítmicos y fármacos con riesgo de QT: amiodarona, amisulprida, anagrelida
  - Antidepresivo: amitriptilina

  Entre las de nivel **moderado** figuran abiraterona, dihidrocodeína, codeína, famotidina, formoterol, adenosina, salbutamol, alfuzosina, propofol y loperamida.

  Varias de estas combinaciones sugieren riesgo de síndrome serotoninérgico o de prolongación del QT. Cabe destacar que los triptanes, tratamiento habitual de la migraña, figuran como interacción mayor, lo que complicaría un eventual uso en esta indicación.
- **Señal de seguridad en la indicación propuesta**: reporte de cefalea tipo migraña inducida por palonosetrón.
- **Riesgo cardiaco**: la literatura reciente señala que los antieméticos pueden prolongar el intervalo QT.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5): no existen ensayos clínicos y la única publicación describe que el fármaco causa cefalea tipo migraña. Además, el resto de las predicciones carece de base mecanística.

<!-- review:begin co-lic-20261105-palonosetron-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado, y el resto de las predicciones carece de base mecanística." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-palonosetron-2 -->

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA con advertencias y contraindicaciones (brecha de datos bloqueante para el tamizaje de seguridad)
- Completar los datos de mecanismo de acción desde DrugBank
- Revisión sistemática de la literatura sobre antagonistas 5-HT3 y migraña, para determinar si existe algún efecto terapéutico o solo riesgo de cefalea
- Evidencia preclínica o clínica que revierta la señal de seguridad actual

<!-- review:begin co-lic-20261031-palonosetron-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Evidencia preclínica o clínica que revierta la señal de seguridad actual / Aclarar la situación regulatoria (registro cancelado) y la compatibilidad de vías de administración antes de cualquier desarrollo local" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 3 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-palonosetron-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registro cancelado) y la compatibilidad de vías de administración antes de cualquier desarrollo local" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado, y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

