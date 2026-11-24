---
layout: default
title: Pegfilgrastim
parent: Solo Predicción del Modelo (L5)
nav_order: 504
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Pegfilgrastim: nueva indicación predicha, Retinopatía diabética no proliferativa grave (nivel de evidencia L5). Indicación original: PEGFILGRASTIM"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Pegfilgrastim: De Pegfilgrastim (indicación sin detallar) a Retinopatía Diabética No Proliferativa Grave
{: .text-alpha }

## Resumen en Una Frase

Pegfilgrastim es un factor estimulante de colonias de granulocitos (G-CSF) de acción prolongada, registrado en Colombia bajo licencias que solo mencionan el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa grave**, con un puntaje muy alto, pero **sin ensayos clínicos ni publicaciones** que respalden actualmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PEGFILGRASTIM (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Pegfilgrastim (traducción no oficial): «Los productos de pegfilgrastim son un factor estimulante de colonias que actúa sobre las células hematopoyéticas mediante la unión a receptores específicos de la superficie celular, con lo que estimula la proliferación, la diferenciación, el compromiso y la activación funcional de las células terminales.» Texto original en inglés: "Pegfilgrastim products are colony-stimulating factor that acts on hematopoietic cells by binding to specific cell surface receptors, thereby stimulating proliferation, differentiation, commitment, and end cell functional activation." ([DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83), versión del 2026-10-29; consultado el 2026-11-19). Según la información conocida, pegfilgrastim es un análogo de G-CSF de acción prolongada que estimula la producción de neutrófilos y moviliza células progenitoras hematopoyéticas. Su uso establecido se relaciona con la recuperación de neutrófilos, y mecanísticamente podría ser aplicable a la retinopatía diabética por vías indirectas.

Una hipótesis posible es que la movilización de células progenitoras derivadas de la médula ósea favorezca la reparación vascular, o que module la inflamación. Además, la diabetes se asocia con una movilización deficiente de progenitores. Sin embargo, esta relación es especulativa y no ha sido verificada con los datos compilados para este informe.

También existe un riesgo opuesto: la activación de neutrófilos y la inflamación inducidas por G-CSF podrían agravar el daño vascular retiniano. La relación entre la indicación original (hematológica) y la nueva (microvascular ocular) es lejana, y la predicción se apoya únicamente en el puntaje del modelo.

Cabe señalar que la "retinopatía diabética" (puntaje 0.9973) es la categoría general de la indicación anterior y no aporta evidencia independiente.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20066850 | GENFILGRAS® PEG | SOLUCION INYECTABLE | PEGFILGRASTIM | Vigente |
| 20153351 | FULPHILA® | SOLUCION INYECTABLE | PEGFILGRASTIM | Vigente |
| 20127676 | PEG-GRAFEEL SOLUCIÓN INYECTABLE 6MG/0.6ML | SOLUCION INYECTABLE | PEGFILGRASTIM | Vigente |
| 19959519 | NEULASTIM ® SOLUCION INYECTABLE 6 MG/0.6 ML | SOLUCION INYECTABLE | PEGFILGRASTIM | Temp. no comerc - Vigente |
| 20188047 | ZIEXTENZO® 6MG/0.6 ML SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | SOLUCION INYECTABLE | PEGFILGRASTIM | Temp. no comerc - Vigente |

Se muestran los 5 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Citotoxicidad

Pegfilgrastim no es un fármaco antineoplásico citotóxico (es un factor de crecimiento hematopoyético), por lo que esta sección no aplica.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se identificaron 100 interacciones en total. Entre las 20 revisadas, todas son de nivel **moderado**. Las principales incluyen:
  - Antineoplásicos y quimioterápicos: paclitaxel, mercaptopurina, azacitidina, trióxido de arsénico, altretamina, trimetrexato, asparaginasa, abemaciclib.
  - Anticuerpos y terapias biológicas: alemtuzumab, aldesleukina, belantamab mafodotina, ibritumomab tiuxetán, tositumomab (incluido el marcado con I-131).
  - Radiofármacos: iobenguano (I-131), fludesoxiglucosa (18F).
  - Otros: pegvaliasa, levamisol, acalabrutinib, avapritinib.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se sustenta solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo es incierto, con un posible efecto adverso sobre la inflamación retiniana.

<!-- review:begin co-lic-20261105-pegfilgrastim-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el mecanismo es incierto, con un posible efecto adverso sobre la inflamación retiniana, y los cuatro registros sanitarios en Colombia están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-pegfilgrastim-1 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente actualmente.
- Complementar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Realizar una revisión de literatura y ensayos preclínicos sobre G-CSF y retinopatía diabética, incluyendo el riesgo de empeoramiento inflamatorio.
- Evaluar la viabilidad de la vía de administración y la situación regulatoria.
- Contar con evidencia preclínica o clínica inicial antes de reconsiderar la decisión.

<!-- review:begin co-lic-20261105-pegfilgrastim-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la viabilidad de la vía de administración y la situación regulatoria, dado que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-pegfilgrastim-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y los cuatro registros sanitarios en Colombia están cancelados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

