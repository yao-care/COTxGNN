---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 5
---

# Palonosetron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Palonosetron: De Antiemético (Náuseas por Quimioterapia) a Trastorno de Migraña

## Resumen en Una Frase

Palonosetron es un antagonista selectivo del receptor de serotonina 5-HT3, utilizado como antiemético para prevenir náuseas y vómitos inducidos por quimioterapia y en el período postoperatorio. El modelo TxGNN predice que podría ser efectivo para el **trastorno de migraña** con un puntaje de 99.74%; sin embargo, la única publicación identificada corresponde a un reporte de caso de cefalea tipo migraña *causada* por palonosetron como efecto adverso —evidencia opuesta a la hipótesis de reposicionamiento— y no existen ensayos clínicos registrados que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de náuseas y vómitos por quimioterapia (CINV) y postoperatorio (PONV) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Con base en el conocimiento farmacológico establecido, palonosetron es un antagonista selectivo del receptor 5-HT3 de segunda generación con mayor afinidad de unión y semivida plasmática notablemente más larga que los de primera generación (ondansetrón, granisetrón). Su eficacia como antiemético está ampliamente validada en el contexto de quimioterapia de alta y moderada emetogenicidad.

La conexión mecánica con la migraña es indirecta: la serotonina participa en la fisiopatología de la migraña a través de la vía trigeminovascular, y existen múltiples subtipos de receptores serotoninérgicos implicados. Sin embargo, los fármacos serotoninérgicos aprobados para el tratamiento agudo de la migraña —los triptanos— actúan como **agonistas 5-HT1B/1D**, mecanismo opuesto al bloqueo 5-HT3 de palonosetron. No existe fundamento clínico ni preclínico documentado que sustente que el antagonismo 5-HT3 produzca beneficio antinociceptivo en la migraña.

El elemento más crítico es que la única evidencia clínica recuperada apunta en sentido contrario: un reporte de caso describe cefalea tipo migraña **inducida** por palonosetron como reacción adversa. Esto convierte la evidencia disponible en señal de riesgo, no de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Reporte de caso (Evento adverso) | Canadian Journal of Anaesthesia | Describe cefalea tipo migraña **inducida por palonosetron** como efecto adverso. Esta publicación constituye evidencia de riesgo, no de eficacia terapéutica en migraña. |

> **Nota sobre la búsqueda bibliográfica:** Para la indicación de rango 2 (migraña con aura de tronco encefálico) no se recuperó ninguna publicación. Para el rango 3 (susceptibilidad genética a migraña con o sin aura), los 20 artículos recuperados corresponden mayoritariamente a genética y modelos animales de **epilepsia** (SCN1A, POLG, EEG, neuroinflammación), con relevancia pendiente de curación; no examinan el uso de palonosetron en migraña y deben considerarse resultados no pertinentes del sistema de búsqueda bibliográfica.

---

## Información de Mercado en Colombia

Palonosetron no cuenta con ningún registro sanitario activo en Colombia. No hay productos ni formas farmacéuticas aprobadas por INVIMA.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para palonosetron en trastorno de migraña carece de soporte clínico positivo: el único artículo identificado reporta migraña como efecto adverso del fármaco, el mecanismo de acción (antagonismo 5-HT3) es opuesto al de los agentes antimi­grañosos validados (agonismo 5-HT1B/1D), y no existe ningún ensayo clínico registrado. El fármaco tampoco está comercializado en Colombia, lo que añade una barrera regulatoria adicional.

**Para avanzar se necesita:**

- Completar los datos de mecanismo de acción (MOA) desde DrugBank para confirmar si existe alguna acción secundaria sobre rutas relevantes en migraña
- Obtener advertencias, contraindicaciones e interacciones farmacológicas (DDI) del prospecto de referencia
- Realizar búsqueda dirigida de estudios preclínicos de palonosetron en modelos de dolor nociceptivo o trigeminovascular
- Determinar si la predicción TxGNN deriva de similitudes en el grafo de conocimiento con otros antagonistas 5-HT3 que sí cuenten con datos en migraña, para evaluar la robustez del modelo
- Confirmar el estado regulatorio ante INVIMA antes de cualquier iniciativa de registro en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

