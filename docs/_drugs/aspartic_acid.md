---
layout: default
title: Aspartic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 69
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Aspartic Acid: nueva indicación predicha, Acidosis tubular renal (nivel de evidencia L5). Indicación original: Aminoácidos"
monitor_inn: "aspartic acid"
predicted_indications: ["renal tubular acidosis"]
---

# Aspartic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Ácido aspártico: De Aminoácidos (nutrición parenteral) a Acidosis Tubular Renal

## Resumen en Una Frase

El ácido aspártico se comercializó en Colombia como componente de una solución inyectable de aminoácidos (AMINOPLASMAL® 10% E), utilizada como aporte nutricional parenteral.
El modelo TxGNN predice que podría ser efectivo para **Acidosis Tubular Renal**, pero **no hay ensayos clínicos** y solo **4 publicaciones** de relevancia limitada (genética, fisiología básica y un reporte de caso) que se relacionan con esta dirección, sin respaldo mecanístico creíble.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Aminoácidos |
| Nueva Indicación Predicha | Acidosis tubular renal |
| Puntaje de Predicción TxGNN | 99.47% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido aspártico es un aminoácido no esencial que participa en el ciclo de la urea, la gluconeogénesis y la lanzadera malato-aspartato. En Colombia se registró como parte de una mezcla de aminoácidos para nutrición parenteral.

**En este caso, la predicción no resulta razonable desde el punto de vista mecanístico.** La acidosis tubular renal se debe principalmente a defectos en transportadores tubulares (por ejemplo SLC4A1/AE1, ATP6V1B1, ATP6V0A4) que alteran la secreción de protones o la reabsorción de bicarbonato. El tratamiento estándar es la terapia alcalina (bicarbonato o citrato), con un mecanismo distinto al del ácido aspártico. Además, al ser un aminoácido ácido, no cabría esperar que corrija la acidosis metabólica; incluso podría aumentar la carga ácida.

El puntaje alto de TxGNN (0.995) parece reflejar una predicción basada en la estructura de la red de conocimiento, sin respaldo mecanístico ni clínico. La ausencia de datos de mecanismo de acción impide contrastar la predicción con un mecanismo conocido.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Estudio genético diagnóstico | Jornal de Pediatria | Secuenciación del exoma completo para el diagnóstico genético de cuatro niños con acidosis tubular renal distal |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Serie de casos genética | Nephron Physiology | Mutaciones del gen SLC4A1 (AE1, Banda 3) como causa de acidosis tubular renal distal en niños filipinos |
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Reporte de caso | J Inherit Metab Dis | Neonato con deficiencia de piruvato carboxilasa, acidosis tubular renal proximal y cistinuria; mejoró al suplementar la dieta con ácido aspártico, asparagina y otros aminoácidos (resumen incompleto) |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Estudio de fisiología básica | Am J Physiol | Relación entre el pH de las células tubulares y la producción renal de amoníaco (sin resumen disponible) |

Ninguna de estas publicaciones evalúa el ácido aspártico como tratamiento de la acidosis tubular renal. El reporte de caso de 1983 es la única mención de una suplementación con este aminoácido, en un contexto de enfermedad metabólica congénita compleja.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20086182 (cancelado) | AMINOPLASMAL® 10% E | Solución inyectable | Aminoácidos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** enfermedad renal, piouréter, enfermedad diarreica (incluida la diarrea crónica), bloqueo auriculoventricular, parálisis periódica hiperpotasémica, parálisis periódica, hipoaldosteronismo, miotonía congénita y gastroparesia.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para información de advertencias y contraindicaciones oficiales; la información del prospecto de INVIMA no pudo obtenerse.

La presencia de enfermedad renal entre las contraindicaciones del grafo es especialmente relevante, dado que la acidosis tubular renal es un trastorno renal.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (L5): no hay ensayos clínicos, la literatura disponible no evalúa el fármaco como tratamiento, y el mecanismo propuesto es contrario a lo esperado (un aminoácido ácido en una enfermedad de acidosis). Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble que justifique el uso en acidosis tubular renal, ya que actualmente no existe.
- Datos del mecanismo de acción desde DrugBank.
- El prospecto de INVIMA con advertencias y contraindicaciones, para completar la evaluación de seguridad.
- Evaluar la contraindicación en enfermedad renal indicada por el grafo de conocimiento.
- Estudios preclínicos que respalden cualquier efecto sobre la excreción ácida o la reabsorción de bicarbonato antes de considerar estudios clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

