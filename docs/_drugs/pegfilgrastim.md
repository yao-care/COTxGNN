---
layout: default
title: Pegfilgrastim
parent: Solo Predicción del Modelo (L5)
nav_order: 504
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, pegfilgrastim es un análogo de G-CSF de acción prolongada que estimula la producción de neutrófilos y moviliza células progenitoras hematopoyéticas. Su uso establecido se relaciona con la recuperación de neutrófilos, y mecanísticamente podría ser aplicable a la retinopatía diabética por vías indirectas.

Una hipótesis posible es que la movilización de células progenitoras derivadas de la médula ósea favorezca la reparación vascular, o que module la inflamación. Además, la diabetes se asocia con una movilización deficiente de progenitores. Sin embargo, esta relación es especulativa y no ha sido verificada con los datos compilados para este informe.

También existe un riesgo opuesto: la activación de neutrófilos y la inflamación inducidas por G-CSF podrían agravar el daño vascular retiniano. La relación entre la indicación original (hematológica) y la nueva (microvascular ocular) es lejana, y la predicción se apoya únicamente en el puntaje del modelo.

Cabe señalar que la "retinopatía diabética" (puntaje 99.73%) es la categoría general de la indicación anterior y no aporta evidencia independiente.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20153351 | FULPHILA® | Solución inyectable | PEGFILGRASTIM | Cancelado |
| 19959519 | NEULASTIM® solución inyectable 6 mg/0.6 mL | Solución inyectable | PEGFILGRASTIM | Cancelado |
| 20066850 | GENFILGRAS® PEG | Solución inyectable | PEGFILGRASTIM | Cancelado |
| 20188047 | ZIEXTENZO® 6 mg/0.6 mL en jeringa precargada | Solución inyectable | PEGFILGRASTIM | Cancelado |

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
La predicción se sustenta solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo es incierto, con un posible efecto adverso sobre la inflamación retiniana, y los cuatro registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente actualmente.
- Complementar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Realizar una revisión de literatura y ensayos preclínicos sobre G-CSF y retinopatía diabética, incluyendo el riesgo de empeoramiento inflamatorio.
- Evaluar la viabilidad de la vía de administración y la situación regulatoria, dado que no hay registros vigentes.
- Contar con evidencia preclínica o clínica inicial antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

