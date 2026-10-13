---
layout: default
title: Fluorouracil
parent: Solo Predicción del Modelo (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracilo: De Fluorouracilo tópico/inyectable (indicación no detallada en el registro) a Rabdomiosarcoma

## Resumen en Una Frase

Fluorouracilo es un antimetabolito (análogo de pirimidina) con registros sanitarios en Colombia en presentaciones tópicas e inyectables, cuyo texto de indicación en el registro solo menciona el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **rabdomiosarcoma**, con **0 ensayos clínicos** y **4 publicaciones indirectas** (antiguas, de revisión o de caso) que no demuestran eficacia específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FLUOROURACILO (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Rabdomiosarcoma embrionario botrioide de la vagina (predicción de mayor puntaje; el grupo de predicciones se concentra en rabdomiosarcoma) |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 (solo predicción del modelo para la predicción principal; la 2.ª predicción, rabdomiosarcoma general, alcanza L4) |
| Estado de Mercado en Colombia | Solo cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, el fluorouracilo es un antimetabolito que inhibe la timidilato sintasa e incorpora fluoronucleótidos al ARN y ADN, lo que altera la síntesis de ácidos nucleicos en células de rápida división. Por ello, mecanísticamente podría ser aplicable a tumores proliferativos como los sarcomas.

El rabdomiosarcoma es un sarcoma pediátrico de rápida proliferación, por lo que la lógica citotóxica general es plausible. Sin embargo, es importante ser claros: los esquemas estándar del rabdomiosarcoma se basan en vincristina, actinomicina D y ciclofosfamida/ifosfamida, y las fluoropirimidinas no forman parte de esa base. El puntaje alto de TxGNN (≈99.7%) es una predicción computacional sin respaldo clínico directo.

Las predicciones restantes (rabdomiosarcoma de próstata, parameníngeo, de vías biliares, sarcoma hepático) siguen la misma lógica general. Las predicciones de síndromes de células falciformes (puntaje 99.62%) se basan en una hipótesis especulativa de inducción de hemoglobina fetal y son poco favorables por la mielosupresión del fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las indicaciones predichas.

---

## Evidencia de Literatura

Para la predicción principal (rabdomiosarcoma embrionario botrioide de la vagina) no hay literatura disponible. La tabla siguiente corresponde a la segunda predicción, **rabdomiosarcoma (general)**, que es la más cercana con literatura recuperada:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Revisión | Cancer | Valor de la quimioterapia adyuvante en sarcomas infantiles, incluido el rabdomiosarcoma |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Revisión | Ann Acad Med Singapore | Curabilidad de cánceres avanzados con quimioterapia, incluidos cánceres infantiles como el rabdomiosarcoma |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohorte | Med Pediatr Oncol | Serie de 13 años de carcinoma nasofaríngeo indiferenciado infantil (histología distinta) |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Reporte de caso | Case Rep Oncol Med | Adulto joven con rabdomiosarcoma lingual: cisplatino + 5-FU provocó progresión; respondió a vincristina, actinomicina D y ciclofosfamida |

Ninguna publicación aporta evidencia controlada de eficacia del fluorouracilo en rabdomiosarcoma; el reporte de caso de 2026 incluso describe progresión con el esquema que contenía 5-FU.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19964018 | 5-Fluorouracil 5% Ungüento | Ungüento tópico | FLUOROURACILO | Cancelado |
| 216264 | 5-Fluorouracil Crema 2.5% | Crema tópica | FLUOROURACILO | Cancelado |
| 19930999 | 5-Fluorouracil 5% Gel | Gel tópico | FLUOROURACILO | Cancelado |
| 20071503 | Fluorouracilo Inyección 500 mg | Solución inyectable | FLUOROURACILO | Cancelado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase fluoropirimidina) |
| Riesgo de Mielosupresión | Alto (el grafo de conocimiento asocia el fármaco con trombocitopenia, neutropenia, agranulocitosis y leucopenia) |
| Clasificación de Emetogenicidad | Baja a moderada en uso sistémico (consultar el prospecto) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos; considerar tamizaje de deficiencia de dihidropirimidina deshidrogenasa (DPD) |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos en la presentación inyectable |

---

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación o precaución (grafo de conocimiento, no texto de prospecto):** enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, leucopenia, enfermedad diarreica, úlcera péptica activa, faringitis, estomatitis, piuria/pioureter y deficiencia de dihidropirimidina deshidrogenasa.
- **Interacciones farmacológicas:** se registran 361 interacciones. Las de nivel moderado incluyen **metronidazol** y **tinidazol**; las de nivel menor incluyen **cimetidina** y **levofloxacino**. Otras (por ejemplo calcitriol, doxiciclina, omeprazol, metformina, morfina) tienen nivel no clasificado.

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones carecen de ensayos clínicos y la literatura es indirecta, antigua o no específica; el mejor nivel alcanzado es L4 y la predicción principal es L5. Además, el fluorouracilo no es parte de los esquemas estándar del rabdomiosarcoma y su perfil de mielosupresión es desfavorable, sobre todo en las predicciones de hemoglobinopatías crónicas. Los cuatro registros en Colombia están cancelados.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos específicos de fluorouracilo en rabdomiosarcoma (por ejemplo, líneas celulares y modelos in vivo)
- Datos del mecanismo de acción desde DrugBank y análisis de vínculo mecanístico más detallado
- Advertencias y contraindicaciones del prospecto de INVIMA (actualmente un vacío bloqueante para el tamizaje de seguridad)
- Evaluación de compatibilidad de vía de administración, ya que los registros previos son tópicos e inyectables y no hay registros vigentes
- Comparación frente a los esquemas estándar (vincristina, actinomicina D, ciclofosfamida/ifosfamida) para justificar el valor incremental
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

