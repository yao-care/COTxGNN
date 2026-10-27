---
layout: default
title: Dexpanthenol
parent: Solo Predicción del Modelo (L5)
nav_order: 214
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Dexpanthenol: nueva indicación predicha, Estenosis anorrectal (nivel de evidencia L5). Indicación original: Multivitaminas y elementos traza"
monitor_inn: "dexpanthenol"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "exanthem (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Dexpanthenol
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

## Dexpanthenol: De Multivitaminas y Elementos Traza a Estenosis Anorrectal
{: .text-alpha }

## Resumen en Una Frase

Dexpanthenol es un provitamina del ácido pantoténico (vitamina B5), registrado en Colombia como parte del producto CERNEVIT® para multivitaminas y elementos traza.
El modelo TxGNN predice que podría ser efectivo para **estenosis anorrectal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y elementos traza |
| Nueva Indicación Predicha | Estenosis anorrectal |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el dexpanthenol se convierte en ácido pantoténico y luego en coenzima A, y se considera que favorece la reparación epitelial y la cicatrización de heridas.

La relación con la indicación original (aporte de vitaminas) es indirecta: el producto aprobado en Colombia es un suplemento vitamínico parenteral, mientras que la predicción se refiere a una afección estructural del canal anorrectal. Mecanísticamente, el apoyo a la cicatrización de mucosas podría relacionarse con la fibrosis o curación de la mucosa, pero no existe evidencia mecanística ni clínica directa que vincule el fármaco con la estenosis anorrectal.

Por ello, la predicción debe considerarse una hipótesis generada por el modelo, no un hallazgo respaldado por estudios.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para estenosis anorrectal.

Como referencia, entre las otras indicaciones predichas existe un ensayo relacionado con exantema (rango 6 del modelo):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Fase 3 | Completado | 160 | Crema Bepanthen® vs. crema de cetomacrogol para prevenir la erupción papulopustulosa en pacientes que reciben inhibidores del EGFR; aleatorizado y doble ciego. La relación con exantema es parcial. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 215439 (cancelado) | CERNEVIT® | Polvo liofilizado para reconstituir a solución inyectable | Multivitaminas y elementos traza |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia el fármaco con una contraindicación en **hemofilia**. Esta información no proviene del texto de la etiqueta y debe verificarse.
- **Interacciones Farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura para estenosis anorrectal, y el único registro sanitario en Colombia está cancelado. Además, el producto aprobado es un multivitamínico inyectable, cuya vía y formulación no se corresponden de forma evidente con la indicación predicha.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones)
- Complementar los datos del mecanismo de acción desde DrugBank
- Realizar una búsqueda dirigida de literatura sobre dexpanthenol en estenosis anorrectal y cicatrización de mucosa
- Evaluar la compatibilidad de vía de administración y formulación (p. ej., tópica o rectal) frente a la presentación inyectable aprobada
- Verificar la señal de contraindicación en hemofilia
- Considerar, como alternativa, priorizar la indicación de exantema (nivel L4, con un ensayo de Fase 3 completado), cuya relevancia es parcial y requiere revisar el registro completo del ensayo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

