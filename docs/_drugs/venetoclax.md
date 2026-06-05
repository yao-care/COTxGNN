---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Venetoclax
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Venetoclax: De Leucemia Linfocítica Crónica a CLL/SLL de Origen Pregerminal

## Resumen en Una Frase

Venetoclax es un inhibidor oral selectivo de BCL-2 internacionalmente reconocido para el tratamiento de leucemia linfocítica crónica (CLL) y leucemia mieloide aguda (AML); sin embargo, actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para el subtipo **CLL/SLL de origen pregerminal del centro germinal** (U-CLL), con **0 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro sanitario en Colombia |
| Nueva Indicación Predicha | CLL/SLL de origen pregerminal del centro germinal |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el sistema de información consultado. No obstante, según la literatura científica disponible en este paquete de evidencia, venetoclax es un inhibidor oral selectivo y potente de la proteína antiapoptótica BCL-2 (B-cell lymphoma-2). Al unirse directamente a BCL-2 con alta afinidad, venetoclax desplaza las proteínas proapoptóticas BIM y BAX, permitiendo que las células tumorales activen la vía intrínseca de apoptosis mitocondrial. Este mecanismo ha demostrado eficacia clínica en múltiples neoplasias hematológicas que dependen de BCL-2 para su supervivencia.

La CLL/SLL de origen pregerminal corresponde al subtipo denominado U-CLL (unmutated IGHV), identificado en 1999 como el subconjunto de mayor riesgo clínico. Este subtipo se origina de células B naïve que no han atravesado el proceso de maduración por afinidad en el centro germinal, a diferencia del subtipo M-CLL (post-germinal) de mejor pronóstico. Las células U-CLL presentan mayor activación crónica del receptor de células B (BCR), mayor señalización de supervivencia y sobreexpresión sostenida de BCL-2. Esta dependencia de BCL-2 para evadir la apoptosis constituye la base mecanística central para el uso de venetoclax en este contexto.

La racionalidad del modelo TxGNN es sólida desde el punto de vista molecular: toda CLL/SLL, independientemente del estatus mutacional de IGHV, comparte la sobreexpresión de BCL-2 como característica central de su patogénesis. Sin embargo, la evidencia clínica que estratifique prospectivamente entre el subtipo pregerminal (U-CLL) y postgerminal (M-CLL) como indicaciones diferenciadas de venetoclax es prácticamente inexistente. Los ensayos pivotales de venetoclax en CLL (como el estudio MURANO, PMID 40009494) no evaluaron diferencias de respuesta por estatus IGHV de manera prospectiva como objetivo primario.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para CLL/SLL de origen pregerminal del centro germinal.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Traslacional/Mecanístico | Cancers | Análisis integral del receptor BCR en CLL; caracteriza los subtipos U-CLL (pregerminal, peor pronóstico) y M-CLL (postgerminal, mejor pronóstico), y sus implicaciones para el diseño de terapias dirigidas al BCR y proteínas de supervivencia como BCL-2 |

---

## Información de Mercado en Colombia

Venetoclax no cuenta con registros sanitarios en Colombia. No se identificaron licencias vigentes en la base de datos regulatoria de INVIMA.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida – Inhibidor selectivo BCL-2 (clase BH3-mimético; no es citotóxico convencional) |
| Riesgo de Mielosupresión | Moderado – La neutropenia es el evento adverso hematológico más frecuente; el riesgo se incrementa en combinación con quimioterapia o agentes hipometilantes |
| Clasificación de Emetogenicidad | Baja (agente oral sin potencial emetogénico directo significativo) |
| Items de Monitoreo | Hemograma completo con diferencial (monitoreo frecuente al inicio del tratamiento); función hepática y renal; electrolitos séricos (potasio, fosfato, calcio, ácido úrico) para vigilancia de síndrome de lisis tumoral (TLS), especialmente durante la rampa de dosis inicial |
| Protección en Manejo | Seguir regulaciones estándar de manejo de agentes antineoplásicos orales; requiere protocolo de rampa de dosis con monitoreo estrecho de TLS en la fase de inicio |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para CLL/SLL de origen pregerminal como indicación clínica específica y diferenciada de venetoclax se limita a un único estudio traslacional/mecanístico (nivel L4), sin ningún ensayo clínico registrado que evalúe este subtipo molecular de forma prospectiva. Aunque la racionalidad biológica es válida —toda CLL/SLL sobreexpresa BCL-2—, no existe actualmente diferenciación clínica demostrada entre U-CLL y M-CLL como indicaciones terapéuticas distintas de venetoclax.

**Para avanzar se necesita:**
- Análisis de subgrupos por estatus mutacional IGHV (U-CLL vs. M-CLL) en ensayos clínicos existentes de venetoclax en CLL (MURANO, CLL14, GAIA/CLL13)
- Ensayos prospectivos que evalúen venetoclax específicamente en U-CLL de primera línea y en recaída
- Completar la información de mecanismo de acción (MOA) desde DrugBank (actualmente no disponible en el sistema)
- Información completa de seguridad: advertencias, contraindicaciones e interacciones farmacológicas del prospecto oficial
- Gestión de registro sanitario ante INVIMA para habilitación comercial en Colombia, dado que el fármaco no está registrado en el país
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

