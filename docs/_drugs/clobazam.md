---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Clobazam
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

Con el contexto del skill cargado, procedo a generar el informe de evaluación basándome en el Evidence Pack de CLOBAZAM.

---

# Clobazam: De Antiepiléptico Adjunto (Uso General) a Síndrome de Epilepsia Febril Infecciosa (FIRES)

## Resumen en Una Frase

Clobazam es una benzodiacepina 1,5 de amplio espectro, conocida internacionalmente por su uso como agente ansiolítico y antiepiléptico adjunto —con aprobación FDA para el síndrome de Lennox-Gastaut—, aunque **no cuenta con registros sanitarios en Colombia**. El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Epilepsia Febril Infecciosa (FIRES)**, con **0 ensayos clínicos** y **2 publicaciones** que respaldan esta dirección de manera indirecta (ninguna evalúa Clobazam directamente en FIRES). La evidencia disponible es de nivel L4, basada únicamente en analogía de clase farmacológica y razonamiento mecanístico.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin registro formal en Colombia (uso establecido internacionalmente: epilepsia adjunta / ansiolítico) |
| Nueva Indicación Predicha | Síndrome de Epilepsia Febril Infecciosa (FIRES) |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos (DrugBank). Según la información contenida en la literatura del Evidence Pack, Clobazam es una benzodiacepina 1,5-benzodiazepina de amplio espectro antiepiléptico; su eficacia como terapia adjunta en epilepsia focal, generalizada y, especialmente, en el síndrome de Lennox-Gastaut ha sido comprobada. Mecanísticamente, actúa como modulador alostérico positivo de los receptores GABA-A —con preferencia por las subunidades α2— potenciando la transmisión inhibitoria y reduciendo la hiperexcitabilidad neuronal. A diferencia de las benzodiacepinas 1,4, su perfil podría asociarse a menor sedación y tolerancia, lo que lo hace atractivo para uso crónico.

El FIRES es una forma de estado epiléptico superrefractario de nuevo inicio (NORSE) que afecta a niños previamente sanos, mediada por mecanismos neuroinflamatorios aún no completamente dilucidados. En la fase aguda, las benzodiacepinas intravenosas (principalmente midazolam) son pilares del manejo del estado epiléptico. La extrapolación al uso de Clobazam —benzodiacepina de larga duración— en la fase crónica post-FIRES tiene una base teórica razonable: la modulación GABA-A sostenida podría contribuir al control de las crisis residuales.

Sin embargo, es crucial advertir que las dos publicaciones recuperadas en el Evidence Pack no evalúan Clobazam directamente: una analiza lorazepam enteral como sustituto del midazolam (PMID 35770765) y la otra explora perampanel (PMID 39958143). La predicción del modelo TxGNN se apoya en analogía de clase benzodiacepínica y similitud en redes de conocimiento biomédico, lo que la sitúa como evidencia indirecta (L4) que requiere estudios prospectivos específicos para validarse.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Serie de Casos / Retrospectivo | Epileptic Disorders | Lorazepam enteral como estrategia eficaz de destete en pacientes con FIRES dependientes de midazolam; **no evalúa Clobazam directamente** |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Reporte de Caso | Cureus | Potencial rol de perampanel para reducir dependencia a barbitúricos en FIRES en niño de 13 años; **no evalúa Clobazam directamente** |

> ⚠️ **Advertencia de relevancia:** Ninguna de las publicaciones disponibles evalúa Clobazam específicamente en FIRES. Ambas son evidencia indirecta por analogía de clase farmacológica o co-manejo de la misma condición.

---

## Información de Mercado en Colombia

Clobazam **no cuenta con registros sanitarios activos en Colombia** (INVIMA). No existe ninguna licencia registrada para este medicamento en el país, por lo que actualmente no está disponible comercialmente ni bajo ninguna presentación farmacéutica aprobada a nivel nacional.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN de Clobazam en FIRES se fundamenta únicamente en analogía de clase benzodiacepínica y similitud de grafos de conocimiento biomédico, sin ningún ensayo clínico registrado ni literatura que evalúe Clobazam directamente en esta indicación. Con un nivel de evidencia L4 y barreras regulatorias significativas en Colombia (0 registros sanitarios), no existe suficiente soporte clínico para recomendar avance en este momento.

> 📌 **Nota sobre predicciones de mayor jerarquía clínica:** Aunque FIRES ocupa el puesto #1 por puntaje TxGNN, la indicación de rango #6 —**Epilepsia Encefalopatía de Inicio en la Infancia (incluye LGS)**— presenta nivel de evidencia **L1** (múltiples revisiones sistemáticas y guías AAN/ILAE que mencionan explícitamente Clobazam, incluyendo aprobación FDA para LGS) y una recomendación de **Proceed with Guardrails**. Esa indicación debería priorizarse para cualquier evaluación de reposicionamiento con perspectiva de mercado en Colombia.

**Para avanzar se necesita:**
- Estudios prospectivos que evalúen específicamente Clobazam en la fase crónica/mantenimiento post-FIRES
- Datos completos de mecanismo de acción (MOA) desde DrugBank o fuentes equivalentes
- Información de seguridad integral: advertencias, contraindicaciones e interacciones farmacológicas del prospecto oficial
- Proceso de registro sanitario ante el INVIMA para habilitar comercialización en Colombia
- Revisión de si la indicación LGS (rango #6, L1) puede servir como punto de entrada regulatoria para ampliar el acceso a Clobazam en Colombia, abriendo la puerta a uso en epilepsias encefalopatías relacionadas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

