---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 5
---

# Benralizumab
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

El skill de txgnn-pipeline es sobre el flujo técnico del pipeline; las instrucciones de formato del reporte están completamente definidas en el sistema. Procedo a generar el informe con los datos del Evidence Pack.

---

# Benralizumab: De Asma Eosinofílica Severa a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Benralizumab (Fasenra) es un anticuerpo monoclonal anti-IL-5Rα aprobado globalmente para el tratamiento del asma eosinofílica severa, aunque no cuenta con registro sanitario en Colombia. El modelo TxGNN predice que podría ser efectivo para la **trombocitopenia por destrucción inmune**, sin embargo, **no existen ensayos clínicos ni publicaciones científicas** que respalden directamente esta indicación. La evidencia disponible proviene exclusivamente de la inferencia topológica del modelo de grafo neuronal, sin sustento experimental directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma eosinofílica severa (indicación global aprobada; sin registro en Colombia) |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de benralizumab en el Evidence Pack. Sin embargo, por su clase farmacológica conocida, benralizumab es un anticuerpo monoclonal dirigido contra el receptor alfa de la interleucina-5 (IL-5Rα), que depleciona eosinófilos y basófilos circulantes y tisulares mediante citotoxicidad celular dependiente de anticuerpos (ADCC). Su eficacia y seguridad en asma eosinofílica severa han sido ampliamente validadas en ensayos clínicos de Fase 3.

La racional mecanística propuesta por TxGNN sugiere que los eosinófilos, a través de la liberación de IL-5 e IL-3, podrían participar indirectamente en la destrucción inmune de plaquetas, y que un anticuerpo anti-IL-5Rα podría atenuar este proceso. No obstante, la trombocitopenia inmune primaria (PTI) está impulsada principalmente por autoanticuerpos IgG anti-plaquetarios y la disfunción del eje FcγRIII/linfocitos T, mecanismos en los que los eosinófilos juegan un papel extremadamente marginal. El modelo identifica una conexión de segundo o tercer orden en el grafo de conocimiento biológico, pero esta no tiene respaldo fisiopatológico directo.

En conclusión, esta predicción representa una inferencia topológica del grafo de conocimiento, sin sustento experimental en modelos preclínicos ni en estudios clínicos. La conexión biológica es especulativa y no alcanza el umbral mínimo para justificar una investigación clínica sin pasos exploratorios previos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para benralizumab en trombocitopenia por destrucción inmune.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para benralizumab en trombocitopenia por destrucción inmune.

---

## Información de Mercado en Colombia

Benralizumab no cuenta con ningún registro sanitario activo en Colombia (INVIMA). El fármaco no ha sido aprobado ni comercializado en el país bajo ninguna indicación.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para trombocitopenia por destrucción inmune carece de cualquier evidencia de soporte — cero ensayos clínicos, cero publicaciones científicas — y la conexión mecanística entre el bloqueo de IL-5Rα y la fisiopatología de la PTI es extremadamente débil. Avanzar sin investigación básica previa implicaría un riesgo científico y regulatorio injustificado.

**Para avanzar se necesita:**
- Estudios preclínicos que demuestren participación de eosinófilos o basófilos en modelos de trombocitopenia inmune
- Datos completos del mecanismo de acción (MOA) desde DrugBank API
- Información de seguridad (advertencias, contraindicaciones) obtenida del prospecto FDA/INVIMA
- Evaluación de redirigir el análisis hacia la indicación de **Dermatitis** (Rank 2, Nivel L2, 6 ensayos clínicos / 20 publicaciones), donde existe evidencia clínica sustancial, incluyendo el subtipo DRESS con alto potencial de beneficio (NCT06734884, Fase 2)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

