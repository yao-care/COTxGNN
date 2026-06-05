---
layout: default
title: Trandolapril
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 6
---

# Trandolapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Trandolapril: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Trandolapril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado globalmente para el tratamiento de la hipertensión arterial y la insuficiencia cardíaca, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Hipertensión Renovascular Maligna**, con una puntuación de predicción del 99.92%.
Sin embargo, **no se encontraron ensayos clínicos ni literatura directamente relevante** que respalden esta indicación específica, y existe una paradoja de seguridad conocida que requiere evaluación cuidadosa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial / Insuficiencia cardíaca (indicación global; sin registro en Colombia) |
| Nueva Indicación Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este paquete de evidencia. Según la información conocida y los fundamentos de reposicionamiento incluidos en el análisis, Trandolapril es un IECA que bloquea el eje RAAS al inhibir la conversión de angiotensina I a angiotensina II (Ang II). Al reducir los niveles de Ang II, disminuye la vasoconstricción y la retención de sodio y agua, resultando en una reducción sostenida de la presión arterial sistémica y de la presión intraglomerular renal.

La hipertensión renovascular maligna es una forma grave de hipertensión secundaria vinculada a estenosis de la arteria renal, en la que el eje RAAS se encuentra marcadamente sobreactivado. Teóricamente, los IECAs representan el bloqueo directo del mecanismo fisiopatológico central, lo que sustenta la plausibilidad topológica de la predicción del modelo TxGNN. Esta similitud estructural en el grafo de conocimiento explica la puntuación elevada.

Sin embargo, existe una advertencia crítica reconocida: en pacientes con estenosis bilateral de la arteria renal o estenosis en riñón único funcionante, los IECAs pueden precipitar insuficiencia renal aguda al eliminar la vasoconstricción compensatoria de la arteriola eferente. Esta paradoja —mecanismo teóricamente favorable frente a riesgo de daño renal agudo— es la razón principal por la que la predicción no puede avanzar sin una evaluación clínica rigurosa de la población objetivo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Trandolapril en hipertensión renovascular maligna.

---

## Evidencia de Literatura

Actualmente no hay literatura directamente relacionada con Trandolapril en hipertensión renovascular maligna disponible.

> **Nota sobre el panorama de evidencia completo:** Para la indicación de rango 4 (hipertensión pulmonar por enfermedad pulmonar/hipoxia) se recuperaron 20 publicaciones en PubMed; sin embargo, todas corresponden a biología general de la hipoxia (HIF-1α, hipoxemia, etc.) sin evaluar trandolapril directamente, y no constituyen evidencia de nivel farmacológico. La evidencia más relevante de todo el paquete se encuentra en la indicación de rango 6 (enfermedad cardíaca pulmonar crónica), con un estudio preclínico directo sobre trandolapril (ver tabla a continuación).

### Evidencia de Literatura — Enfermedad Cardíaca Pulmonar Crónica (Indicación de Mayor Relevancia, Rango 6)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) | 1996 | Estudio Animal (Preclínico) | Journal of Cardiac Failure | Tratamiento prolongado con trandolapril mejoró las propiedades contráctiles alteradas de vasos en ratas con insuficiencia cardíaca crónica, sugiriendo que los IECAs corrigen la disfunción vascular aumentada en CHF |

---

## Información de Mercado en Colombia

Trandolapril **no cuenta con ningún registro sanitario activo en Colombia** y no se comercializa en el mercado colombiano en ninguna forma farmacéutica.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Alerta mecanística relevante:** Basado en el mecanismo de acción conocido de los IECAs y en el fundamento de reposicionamiento incluido en el paquete, se debe tener precaución especial ante el riesgo de **insuficiencia renal aguda** en pacientes con estenosis bilateral de la arteria renal —escenario directamente relacionado con la indicación predicha. Los datos formales de advertencias, contraindicaciones e interacciones farmacológicas no están disponibles en este paquete de evidencia y deben obtenerse antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para hipertensión renovascular maligna tiene plausibilidad mecanística razonable al involucrar la sobreactivación del eje RAAS, pero no existe ningún ensayo clínico ni literatura directa que respalde esta indicación específica, y la indicación predicha presenta un riesgo de seguridad conocido (insuficiencia renal aguda en estenosis bilateral) que puede ser contradictorio con el uso de IECAs en este subgrupo de pacientes.

**Para avanzar se necesita:**
- Completar datos formales de mecanismo de acción (MOA) desde DrugBank API
- Obtener advertencias, contraindicaciones e interacciones farmacológicas del prospecto oficial (actualmente todos en déficit de datos)
- Evaluar si ensayos clínicos existentes de IECAs en hipertensión renovascular incluyen subgrupos con estenosis unilateral donde el uso es más seguro
- Investigar datos de seguridad renal específicos de trandolapril en pacientes con estenosis de arteria renal antes de cualquier escalada de evidencia
- Considerar como indicación alternativa prioritaria la **enfermedad cardíaca pulmonar crónica** (Rango 6, Nivel L4), que cuenta con evidencia preclínica directa de trandolapril (PMID 8989645) y un mecanismo de acción más favorable sin la contraindicación de daño renal agudo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

