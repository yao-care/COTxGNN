---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: De Leucemia Mieloide Crónica a Sarcoma de Ewing

## Resumen en Una Frase

Dasatinib es un inhibidor oral de múltiples tirosina quinasas (BCR-ABL/Src), aprobado globalmente para el tratamiento de la leucemia mieloide crónica (LMC) y la leucemia linfoblástica aguda Philadelphia positiva, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para el **Sarcoma de Ewing**, con **2 ensayos clínicos relevantes** (incluyendo un Fase II completado en sarcomas avanzados con 366 pacientes) y **9 publicaciones** que actualmente respaldan esta dirección.
La base mecanística se sustenta en la dependencia del Sarcoma de Ewing de la quinasa Src, objetivo molecular directo de dasatinib.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide crónica (LMC) / Leucemia linfoblástica aguda Philadelphia positiva |
| Nueva Indicación Predicha | Sarcoma de Ewing |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dasatinib es un inhibidor de tirosina quinasa de amplio espectro que actúa potentemente sobre BCR-ABL, las quinasas de la familia Src, c-KIT y el receptor del factor de crecimiento derivado de plaquetas (PDGFR), con una potencia más de 325 veces superior a la del imatinib frente a BCR-ABL. Aunque los datos detallados de mecanismo de acción no están disponibles en el conjunto de datos actual, su clase farmacológica (inhibidor dual BCR-ABL/Src) está bien establecida en la literatura.

El Sarcoma de Ewing es un tumor óseo y de tejidos blandos que afecta predominantemente a adolescentes y adultos jóvenes, con pronóstico sombrío en estadios metastásicos o recurrentes. Estudios mecanísticos han demostrado que el estrés microambiental induce la activación de Src en las células de Sarcoma de Ewing, promoviendo la formación de invadopodios y el fenotipo invasivo (PMID 27566104). Adicionalmente, la proteína de fusión EWS-FLI1 interactúa con el complejo FAK-Src en vías de señalización prometastásicas (PMID 35655525), lo que ubica a Src como un conductor clave del comportamiento maligno de este tumor.

Dado que dasatinib inhibe simultáneamente Src, FAK (vía Src) y c-KIT, su perfil molecular cubre las principales vías de progresión descritas en el Sarcoma de Ewing. Estudios in vitro han confirmado actividad antiproliferativa y antimigratoria directa en líneas celulares de este tumor (PMID 18202781, PMID 17363602). Sin embargo, los datos del ensayo Fase II en sarcomas avanzados (NCT00464620) sugieren que la monoterapia con dasatinib presenta eficacia limitada en este subtipo específico, orientando la investigación hacia estrategias de combinación con quimioterapia convencional.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Fase 2 | Completado | 366 | Dasatinib en sarcomas avanzados (cohorte amplia incluyendo Sarcoma de Ewing); evaluación de tasa de respuesta y supervivencia libre de progresión a 6 meses; provee datos de subgrupo aplicables a Ewing |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Fase 1/2 | Terminado | 7 | Dasatinib + ifosfamida/carboplatino/etopósido (ICE) en sarcomas pediátricos, incluyendo explícitamente Sarcoma de Ewing; terminado prematuramente por dificultades de reclutamiento; aporta datos preliminares de seguridad de la combinación |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclínico in vitro | Cancer Research | Dasatinib inhibe migración e invasión en diversas líneas celulares de sarcomas humanos e induce apoptosis en sarcomas óseos dependientes de Src; primera demostración preclínica directa en mesénquima |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclínico in vitro | Oncology Reports | Actividad antiproliferativa y antimigratoria de dasatinib confirmada en líneas celulares de Sarcoma de Ewing; c-KIT y PDGFR identificados como blancos relevantes en este subtipo |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Traslacional/Mecanístico | Neoplasia | Estrés microambiental induce activación dependiente de Src y formación de invadopodios en Sarcoma de Ewing; establece el fundamento mecanístico central para inhibición de Src |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Traslacional/Mecanístico | Neoplasia | Tenascina C coopera con Src para promover invasión en Sarcoma de Ewing; amplía el modelo de activación Src en el contexto del microambiente tumoral |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclínico/Traslacional | Sarcoma | Complejo FAK-Src como blanco terapéutico en Sarcoma de Ewing, DSRCT y rabdomiosarcoma; dasatinib como agente único fue insuficiente en Fase II, sugiriendo que la combinación FAK+Src es la estrategia a explorar |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revisión | Oncology Letters | Revisión sistemática sobre el papel crítico de la señalización Src en proliferación, apoptosis, invasión y microambiente tumoral en sarcomas; sustenta a Src como blanco terapéutico válido en la clase |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa — clase BCR-ABL/Src/c-KIT/PDGFR) |
| Riesgo de Mielosupresión | Moderado (neutropenia y trombocitopenia reportadas con frecuencia en estudios de LMC; vigilancia hematológica obligatoria) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma completo con diferencial (semanal en inducción), función hepática y renal, monitoreo de retención de líquidos y efusión pleural/pericárdica |
| Protección en Manejo | Seguir regulaciones estándar de manejo de fármacos antineoplásicos; precauciones de preparación y administración según normativa vigente |

---

## Consideraciones de Seguridad

Consultar el prospecto para información completa de seguridad. Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no están disponibles en el conjunto de datos actual. Cabe destacar que la literatura reporta efusión pleural como evento adverso relevante asociado a dasatinib en tratamientos prolongados (PMID 36448074, PMID 36346055), lo cual debe considerarse en el diseño del monitoreo clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe una base mecanística sólida (inhibición Src/FAK/c-KIT) respaldada por múltiples estudios preclínicos y traslacionales en Sarcoma de Ewing; sin embargo, el único ensayo Fase II clínico completado en sarcomas avanzados (NCT00464620) documentó que dasatinib como agente único no demostró eficacia suficiente en el subtipo Ewing, lo que limita la recomendación de avanzar a uso clínico sin datos específicos de combinación.

**Para avanzar se necesita:**
- Análisis de subgrupo específico para Sarcoma de Ewing derivado del ensayo NCT00464620
- Datos completos de mecanismo de acción (MOA) y perfil de seguridad oficial (prospecto INVIMA o referencia internacional reconocida)
- Diseño de ensayo clínico dedicado a Sarcoma de Ewing con dasatinib en combinación (ej. con régimen ICE u otros esquemas de quimioterapia en segunda línea)
- Obtención de registro sanitario ante INVIMA como requisito previo para cualquier uso clínico en Colombia
- Plan de monitoreo de efusión pleural y parámetros hematológicos adaptado a la población pediátrica y de adultos jóvenes predominante en esta indicación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

