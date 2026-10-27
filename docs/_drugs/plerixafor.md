---
layout: default
title: Plerixafor
parent: Solo Predicción del Modelo (L5)
nav_order: 520
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Plerixafor: nueva indicación predicha, Mieloma de células plasmáticas indolente (nivel de evidencia L5). Indicación original: El registro sanitario solo indica el nombre del principio activo (\"PL…"
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
---

# Plerixafor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Plerixafor: De Movilizador de Células Madre Hematopoyéticas a Mieloma de Células Plasmáticas Indolente
{: .text-alpha }

## Resumen en Una Frase

Plerixafor es un antagonista del receptor CXCR4, utilizado como movilizador de células madre hematopoyéticas en pacientes con linfoma no Hodgkin y mieloma múltiple que requieren trasplante autólogo.
El modelo TxGNN predice que podría ser efectivo para **mieloma de células plasmáticas indolente**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; por ahora es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo indica el nombre del principio activo ("PLERIXAFOR"); según los datos farmacológicos, movilización de células madre hematopoyéticas |
| Nueva Indicación Predicha | Mieloma de células plasmáticas indolente |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Plerixafor bloquea el receptor CXCR4 (y también interactúa con ACKR3). Al interrumpir el eje CXCL12-CXCR4, que mantiene las células ancladas en la médula ósea, libera células madre hacia la sangre periférica. Por eso se usa para recolectarlas antes de un trasplante. Los datos compilados no incluyen una descripción detallada del mecanismo de acción, pero este efecto farmacológico está bien documentado.

La relación con la nueva indicación es plausible. Las células de mieloma dependen del nicho de la médula ósea, y bloquear CXCR4 podría alterar ese anclaje. Sin embargo, el uso actual de plerixafor en mieloma múltiple es de **apoyo** (recolectar células para el trasplante), no una acción sobre la enfermedad. No hay datos que demuestren actividad contra la enfermedad en su forma indolente.

La predicción debe tomarse como una hipótesis. El puntaje del modelo es muy alto, pero no se aportó ningún estudio que lo confirme.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20255171 | Plerixafor 24 mg solución inyectable (Avalon Pharmaceutical S.A.) | Solución inyectable | Plerixafor (sin texto de indicación detallado) |
| 20056150 | Mozobil® (Genzyme Corporation) | Solución inyectable | Plerixafor (sin texto de indicación detallado) |
| 20187826 | Aurople­ristem 20 mg/ml (Eugia Pharma Specialities Limited) | Solución inyectable | Plerixafor (sin texto de indicación detallado) |

Los tres registros están **cancelados**; actualmente no hay registros vigentes en Colombia.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no provienen del texto del prospecto): trombocitopenia, enfermedad con función renal alterada y leucemia.
- **Interacciones farmacológicas**: la consulta no identificó interacciones con otros fármacos. Solo se registraron los blancos farmacológicos de plerixafor, CXCR4 y ACKR3.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación solo cuenta con una predicción del modelo (nivel L5), sin ensayos ni literatura, y el uso actual de plerixafor en mieloma es de apoyo y no sobre la enfermedad. Además, no hay registros sanitarios vigentes en Colombia.

**Nota sobre otras predicciones:** Entre las indicaciones predichas, la **leucemia mieloide** es la que tiene más respaldo (27 ensayos de fase 1 y 1/2, y revisiones sobre CXCR4 en leucemia mieloide aguda; nivel L2). Aun así, los ensayos son pequeños, de brazo único y varios terminaron antes de tiempo, por lo que no se ha demostrado superioridad frente al tratamiento estándar. Si se busca una línea de reposicionamiento, conviene evaluarla como pregunta de investigación.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos de plerixafor específicos en mieloma de células plasmáticas indolente
- Datos detallados del mecanismo de acción
- Prospecto con advertencias y contraindicaciones oficiales
- Aclarar la situación regulatoria en Colombia, ya que los tres registros están cancelados
- Evaluación de seguridad dadas las contraindicaciones señaladas (trombocitopenia, alteración renal)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

