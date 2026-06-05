---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: De Sedación Clínica a Insomnio

## Resumen en Una Frase

Midazolam es un fármaco benzodiazepínico utilizado ampliamente en la práctica clínica como sedante, agente de preinducción anestésica y para procedimientos médicos que requieren sedación consciente, gracias a su rápido inicio de acción hipnótica. El modelo TxGNN predice que podría ser efectivo para el tratamiento del **Insomnio**, con **múltiples ensayos clínicos** y **al menos 6 publicaciones científicas** que respaldan esta dirección. Sin embargo, sus propiedades farmacocinéticas y el perfil de riesgo de dependencia limitan su aplicabilidad directa como tratamiento de primera línea para el insomnio crónico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sedación clínica y preanestesia |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Midazolam es un agonista positivo del receptor GABA-A de la clase benzodiazepínica. Su mecanismo de acción consiste en potenciar la inhibición GABAérgica del sistema nervioso central, lo que produce sedación, ansiolisis e inducción del sueño. Este mecanismo es precisamente el que utilizan los hipnóticos benzodiazepínicos clásicos (como triazolam o temazepam) para el tratamiento del insomnio, lo que explica la alta puntuación del modelo TxGNN (99.74%) y la coherencia mecánica de la predicción.

La relación entre el insomnio y la señalización GABAérgica está bien documentada: estudios en modelos animales (PMID 21396773) confirman que la reducción del tono GABAérgico cortical se asocia directamente con trastornos del sueño. Midazolam, al reforzar esta vía, podría restablecer la arquitectura del sueño en pacientes con insomnio, especialmente en contextos agudos o perioperatorios donde ya se ha estudiado su efecto sobre la calidad del sueño.

No obstante, existe una limitación farmacocinética importante: la vida media de midazolam es corta (t½ ≈ 2–6 horas), lo que lo hace adecuado para el insomnio de inicio pero no para el insomnio de mantenimiento. Además, como toda benzodiazepina, conlleva riesgo de tolerancia y dependencia con el uso crónico, factores que han impulsado el desarrollo de alternativas más modernas (zolpidem, lemborexant, suvorexant). En Colombia, midazolam no cuenta actualmente con registro sanitario activo, lo que representa una barrera regulatoria adicional.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Completado | 111 | Comparación directa de midazolam vs dexmedetomidina sobre calidad del sueño postoperatorio en pacientes con resección prostática transuretral; midazolam como control activo con medición cuantitativa de sueño |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Fase 3 | Desconocido | 120 | Eficacia sedante de dexmedetomidina vs midazolam en niños críticos con ventilación mecánica; calidad del sueño como objetivo secundario en contexto de UCI pediátrica |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Fase 2 | Desconocido | 60 | Comparación de dexmedetomidina, midazolam y remifentanilo para sedación en cirugía ortopédica bajo anestesia regional; calidad del sueño como parámetro observacional |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Reclutando | 280 | Midazolam oral preoperatorio en pacientes con trastorno del sueño o ansiedad sometidos a resección colorrectal laparoscópica; estudio doble ciego, controlado con placebo, con medición directa de calidad del sueño |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Fase 4 | Desconocido | 285 | Remimazolam (análogo de midazolam) para sedación en UCI; evalúa perfil de sueño en pacientes con ventilación mecánica postcirugía maxilofacial |
| [NCT01791296](https://clinicaltrials.gov/study/NCT01791296) | Fase 4 | Completado | 100 | Protocolo de sueño con dexmedetomidina nocturna vs tratamiento estándar (que incluye benzodiazepinas) en pacientes críticos; evalúa incidencia de delirium y calidad del sueño en UCI |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Fase 1 | Terminado | 6 | Comparación de agonistas α2 vs agonistas GABA (incluyendo midazolam) en estadios del sueño mediante polisomnografía en pacientes con ventilación mecánica; terminado prematuramente por baja captación |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | ECA | J Clin Psychopharmacol | Estudio multicéntrico, doble ciego, grupos paralelos que examina sueño, rendimiento y niveles plasmáticos en insomniacs crónicos durante 14 días de uso de flurazepam y midazolam; evaluó eficacia comparativa en pacientes con historial de uso de benzodiazepinas |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | ECA Multicéntrico | J Clin Psychopharmacol | Resumen ejecutivo del ECA multicéntrico sobre sueño en insomniacs crónicos durante 14 días con flurazepam vs midazolam; aporta datos comparativos de eficacia hipnótica a largo plazo |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | Ensayo Controlado | Br J Clin Pharmacol | Estudio doble ciego con placebo en 30 pacientes con insomnio secundario a enfermedad neuromuscular; midazolam 15 mg mostró eficacia hipnótica sostenida y mejor tolerabilidad que Vesparax (secobarbital + brallobarbital + hidroxizina), sin efecto resaca |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Estudio Dosis-Respuesta | Arzneimittelforschung | Estudio piloto multicéntrico en 75 pacientes hospitalizados con insomnio leve a moderado; estableció rango óptimo de dosis oral de midazolam (10–30 mg) y documentó eficacia sedante e hipnótica |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Revisión del uso clínico de hipnóticos benzodiazepínicos, incluyendo midazolam; analiza relación entre vida media de eliminación, dosis y eficacia, confirmando su efectividad clínica para el insomnio |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Estudio Animal | Pain | Confirma que la reducción de la transmisión GABAérgica cortical (diana molecular de midazolam) está directamente asociada con mayor vigilia y reducción del sueño NREM en modelos de dolor neuropático; provee sustento mecanístico para la indicación |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Cohorte Observacional | J Clin Med | Estudio piloto que evalúa lemborexant como alternativa a benzodiazepinas para insomnio en pacientes con riesgo de delirium; señala que las benzodiazepinas (incluyendo midazolam) pueden empeorar el delirium, subrayando la necesidad de alternativas más seguras |

---

## Información de Mercado en Colombia

Midazolam **no cuenta con registros sanitarios activos en Colombia** al momento del corte de datos (2026-06-04). No se encontraron licencias emitidas por INVIMA para este principio activo.

> Este hallazgo representa una barrera regulatoria significativa. Para cualquier iniciativa de reposicionamiento formal en Colombia, se requeriría gestionar un registro sanitario nuevo ante INVIMA antes de comercialización.

---

## Consideraciones de Seguridad

Consultar el prospecto oficial del fabricante para información completa de seguridad, incluyendo advertencias, contraindicaciones e interacciones farmacológicas. No se obtuvieron datos de advertencias clave, contraindicaciones ni interacciones farmacológicas a través de las fuentes consultadas en este ciclo de recopilación.

> **Nota clínica relevante derivada de la literatura:** Los estudios revisados señalan que las benzodiazepinas como midazolam pueden aumentar el riesgo de delirium en pacientes de alto riesgo (PMID 36615100). Su uso crónico conlleva riesgo de tolerancia, dependencia física y síndrome de abstinencia, factores que limitan su indicación para el insomnio crónico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque la predicción TxGNN tiene una base mecanística sólida (midazolam actúa directamente sobre receptores GABA-A, la misma diana del insomnio) y existen ECAs históricos que documentan su eficacia hipnótica, la combinación de ausencia de registro sanitario en Colombia, perfil de riesgo de dependencia conocido y la existencia de alternativas más modernas y seguras (zolpidem, lemborexant, suvorexant) posiciona este candidato como una pregunta de investigación antes que una oportunidad comercial inmediata.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto completo de midazolam para evaluar contraindicaciones e interacciones farmacológicas formales
- Confirmar el mecanismo de acción detallado (MOA) desde DrugBank API para completar el análisis de reposicionamiento
- Realizar un análisis de mercado en Colombia que identifique si existen formulaciones orales de midazolam (vs. formulaciones parenterales típicas) que sean viables para el tratamiento del insomnio
- Revisar si existe una ventana de reposicionamiento en nichos específicos (insomnio agudo situacional, insomnio perioperatorio) donde midazolam podría tener ventajas sobre los hipnóticos actuales disponibles en el mercado colombiano
- Evaluar el marco regulatorio de INVIMA para benzodiazepinas hipnóticas y los requisitos de un posible registro de la indicación de insomnio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

