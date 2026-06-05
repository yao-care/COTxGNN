---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: De Leucemia Linfocítica Crónica a LLC/SLL con Hipermutación Somática de IgHV

## Resumen en Una Frase

Ofatumumab es un anticuerpo monoclonal anti-CD20 totalmente humano, originalmente aprobado por la FDA en 2009 para el tratamiento de la leucemia linfocítica crónica (CLL) refractaria a fludarabina y alemtuzumab, sin registro sanitario vigente en Colombia.
El modelo TxGNN predice que podría ser efectivo para la **CLL/SLL con hipermutación somática de la región variable de cadena pesada de inmunoglobulina (IgHV)**, un subtipo molecular de pronóstico favorable dentro del espectro de la CLL.
Sin embargo, **no existen ensayos clínicos ni publicaciones** específicos para este subtipo molecular con ofatumumab; la evidencia es exclusivamente indirecta, derivada de estudios en CLL general.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfocítica crónica refractaria (aprobación FDA 2009; sin registro INVIMA en Colombia) |
| Nueva Indicación Predicha | CLL/SLL con hipermutación somática de IgHV (subtipo molecular IgHV-mutado) |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L4 (sin estudios clínicos directos en este subtipo molecular) |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción provenientes de la fuente primaria (DrugBank). Sin embargo, según la información clínica conocida, ofatumumab es un anticuerpo monoclonal IgG1κ de segunda generación dirigido contra el antígeno CD20. A diferencia de rituximab, se une a un epítopo único proximal a la membrana de la molécula CD20, lo que confiere una actividad de citotoxicidad dependiente del complemento (CDC) significativamente superior, además de actividad de citotoxicidad mediada por células dependiente de anticuerpos (ADCC). Su eficacia en CLL general ha sido ampliamente comprobada en múltiples ensayos clínicos Fase 2 y 3.

La CLL/SLL con mutación somática de IgHV es el subtipo molecular en el que las células B leucémicas han transitado por el centro germinal, acumulando mutaciones somáticas en la región variable de la cadena pesada de inmunoglobulina. Este subtipo se asocia a un perfil de pronóstico más favorable y a mayor sensibilidad a la quimioinmunoterapia. Dado que el antígeno CD20 se expresa en las células B malignas de ambos subtipos (IgHV-mutado e IgHV-no mutado), el mecanismo anti-CD20 de ofatumumab es teóricamente aplicable a esta clasificación molecular.

No obstante, el estado de mutación de IgHV no ha sido investigado de forma específica como variable predictiva de respuesta en los estudios clínicos de ofatumumab. La predicción de TxGNN se basa en la proximidad topológica en el grafo de conocimiento entre el fármaco y este subtipo, sin respaldo de datos clínicos directos. Esta indicación se clasifica actualmente como **Pregunta de Investigación** (L4) y requiere generación de hipótesis antes de avanzar a diseño de estudio.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos registrados que evalúen ofatumumab específicamente en CLL/SLL con hipermutación somática de IgHV.

> **Contexto:** Para CLL/SLL en general (indicación de rango 5 en este Evidence Pack), existe evidencia sólida con múltiples ensayos Fase 3 completados (incluyendo el estudio DUO y RESONATE), donde ofatumumab figura como brazo de control activo estándar, confirmando su eficacia en CLL refractaria/recaída. La aplicabilidad al subtipo IgHV-mutado requiere análisis de subgrupos en esos datos.

---

## Evidencia de Literatura

Actualmente no hay literatura publicada que evalúe específicamente ofatumumab en CLL/SLL con hipermutación somática de IgHV.

---

## Información de Mercado en Colombia

Ofatumumab no cuenta con registros sanitarios vigentes ante el INVIMA. El medicamento no se encuentra comercializado en Colombia a la fecha de corte de datos (junio 2026). No existen licencias aprobadas locales que consultar.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — anticuerpo monoclonal anti-CD20 de segunda generación (no citotóxico convencional) |
| Riesgo de Mielosupresión | Moderado — linfopenia B profunda esperada por mecanismo; riesgo de neutropenia e infecciones oportunistas (incluyendo reactivación de hepatitis B) |
| Clasificación de Emetogenicidad | Baja (anticuerpos monoclonales tienen potencial emetogénico mínimo) |
| Ítems de Monitoreo | Hemograma completo con diferencial antes de cada ciclo; serología de hepatitis B (HBsAg, Anti-HBc) previo al inicio; función hepática y renal periódica |
| Protección en Manejo | No requiere manejo como citotóxico convencional; seguir protocolos estándar para biológicos intravenosos; preparación y administración por personal entrenado en reacciones infusionales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica directa que evalúe ofatumumab en CLL/SLL con mutación somática de IgHV como subtipo molecular diferenciado; la predicción de TxGNN representa una hipótesis mecanística plausible basada en la expresión de CD20 en este subtipo, pero carece de sustento clínico independiente para avanzar sin generación previa de datos exploratorios.

**Para avanzar se necesita:**
- Análisis de subgrupos retrospectivos por estado de mutación IgHV en los ensayos existentes de ofatumumab en CLL (p. ej., RESONATE, DUO)
- Datos de expresión cuantitativa de CD20 comparando CLL IgHV-mutado frente a IgHV-no mutado
- Obtención y revisión del prospecto oficial (FDA/EMA) para completar datos de MOA, advertencias y contraindicaciones
- Evaluación de la viabilidad de acceso al medicamento en Colombia (importación por uso compasivo o programa de acceso especial ante el INVIMA), dado el estado de no comercialización
- Definición de hipótesis clínica y diseño de estudio prospectivo si el análisis de subgrupos es favorable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

