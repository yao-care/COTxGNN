---
layout: default
title: Lamotrigine
parent: Solo Predicción del Modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Lamotrigina: De Epilepsia y Trastorno Bipolar a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

La lamotrigina es un anticonvulsivante usado para tratar la epilepsia y el trastorno bipolar. El modelo TxGNN predice que podría ser efectiva para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos** y solo hay **2 publicaciones** relacionadas con el nervio trigémino. Ninguna de ellas estudia un efecto antitumoral, así que la predicción parece reflejar una cercanía en el grafo con la neuralgia del trigémino y no una acción contra el tumor.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LAMOTRIGINA (el registro sanitario solo repite el nombre del fármaco y no describe la indicación; el uso conocido es epilepsia y trastorno bipolar) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la lamotrigina bloquea los canales de sodio dependientes de voltaje. Las fuentes farmacológicas la relacionan con el canal Nav1.2 (dato de rata), aunque no hay datos públicos de afinidad que lo confirmen. Su eficacia en epilepsia está comprobada.

En este caso, la razonabilidad de la predicción es **baja**. El puntaje alto del modelo probablemente refleja la cercanía en el grafo con la **neuralgia del trigémino**, un síndrome de dolor neuropático que responde a fármacos que actúan sobre los canales de sodio. No refleja un efecto antitumoral. La lamotrigina no tiene un mecanismo antineoplásico plausible. Cualquier beneficio sería un alivio sintomático del dolor, que ya está cubierto por la entrada de neuralgia del trigémino.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Rev Neurother | Revisión de los tratamientos médicos y quirúrgicos de la neuralgia del trigémino. Trata dolor neuropático, no tumores. |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Reporte de caso | Stereotact Funct Neurosurg | Radiocirugía Gamma Knife en neuralgia del trigémino causada por una malformación cavernosa. No involucra lamotrigina ni neoplasia. |

Ambas publicaciones tratan la neuralgia del trigémino. Ninguna respalda un uso de la lamotrigina en neoplasia.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20067216 | LAMOTRIGINA 50MG (Tecnoquímicas S.A.) | Tableta dispersable | LAMOTRIGINA (sin descripción de indicación) |

Las cinco entradas devueltas corresponden al mismo registro sanitario, por eso se muestra una sola fila. En total hay 20 registros, todos de vía oral según los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción de neoplasia del nervio trigémino solo tiene respaldo del modelo (L5), sin ensayos clínicos ni literatura sobre efecto antitumoral, y sin mecanismo plausible.
- Dentro del mismo paquete, la **neuralgia del trigémino** (puntaje 99.89%) tiene mejor respaldo: 1 ensayo de Fase 2/3 completado ([NCT00913107](https://clinicaltrials.gov/study/NCT00913107), lamotrigina vs. carbamazepina, n=21) y un mecanismo coherente. Eso corresponde a nivel L2 y recomendación "Research Question". Las guías la ubican solo como alternativa o terapia adicional.

**Para avanzar se necesita:**
- Descartar la neoplasia del nervio trigémino como candidata y redirigir el análisis hacia la neuralgia del trigémino.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones. Este dato bloquea el tamizaje de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada en los registros sanitarios, porque el texto actual solo contiene el nombre del fármaco.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

