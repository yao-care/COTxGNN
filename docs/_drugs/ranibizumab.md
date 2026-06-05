---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: De Degeneración Macular Asociada a la Edad a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Ranibizumab (Lucentis®) es un fragmento de anticuerpo monoclonal humanizado anti-VEGF-A originalmente utilizado para el tratamiento de la degeneración macular neovascular asociada a la edad (DMAE húmeda) y el edema macular diabético.
El modelo TxGNN predice que podría ser efectivo para la **Retinopatía Diabética No Proliferativa Grave (RDNPG)**,
con **6 ensayos clínicos** y **19 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Degeneración macular neovascular (húmeda) / Edema macular diabético |
| Nueva Indicación Predicha | Retinopatía Diabética No Proliferativa Grave |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Con base en la información publicada, ranibizumab es un fragmento Fab de anticuerpo monoclonal humanizado que inhibe selectivamente el factor de crecimiento endotelial vascular A (VEGF-A), bloqueando su unión a los receptores VEGFR-1 y VEGFR-2 en la superficie de las células endoteliales. Esta inhibición reduce la permeabilidad vascular patológica, la inflamación y la formación de nuevos vasos sanguíneos anómalos en la retina.

En la retinopatía diabética no proliferativa grave, el VEGF-A se encuentra crónicamente elevado y actúa como el principal impulsor de microaneurismas, isquemia retiniana, manchas algodonosas e IRMA (anomalías microvasculares intrarretinianas). Al bloquear esta vía, ranibizumab puede interrumpir la cascada patológica y prevenir la progresión hacia la retinopatía diabética proliferativa (RDP), estadio asociado a riesgo elevado de hemorragia vítrea y pérdida visual irreversible.

La conexión mecanística es directa: tanto la DMAE húmeda como la RDNPG severa comparten el eje VEGF-A como conductor fisiopatológico central. Los ensayos de Fase 3 RIDE y RISE ya demostraron que ranibizumab duplica la tasa de mejoría en la escala de severidad de retinopatía diabética (DRSS) en comparación con placebo, lo que convierte esta predicción del modelo TxGNN en una extensión clínicamente lógica y bien sustentada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Fase 3 | Completado | 174 | Sistema de liberación continua (PDS) con ranibizumab vs brazo comparador en pacientes con DR sin DME de centro involucrado; evalúa eficacia y seguridad en retinopatía diabética no proliferativa con administración de larga duración |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Fase 3 | Completado | 399 | Anti-VEGF intravítreo para prevención de complicaciones que amenazan la visión en ojos con DR de alto riesgo; diseño directamente orientado a RDNPG severa como población objetivo principal |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Fase 4 | Completado | 25 | Ranibizumab intravítreo en retinopatía diabética no proliferativa con DME; evaluó efectos sobre microaneurismas y área de no perfusión retiniana como marcadores de progresión de la enfermedad |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Fase 3 | Completado | 691 | DRCR.net Protocol I: ranibizumab ± láser vs láser solo en DME; análisis secundarios mostraron mejoría de la severidad de DR en la escala DRSS como hallazgo consistente con ranibizumab |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Fase 3 | Desconocido | 118 | Ranibizumab intravítreo vs inyecciones simuladas para prevención de progresión en DR de alto riesgo, incluyendo RDNPG severa; estado no confirmado reduce la confiabilidad del resultado |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Desconocido | 1000 | Estudio observacional de terapia anti-VEGF (ranibizumab, aflibercept, conbercept) en DMAE exudativa, RDP y DME en condiciones del mundo real; soporte indirecto |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECA Fase 3 | JAMA Ophthalmology | Ensayo Pavilion: PDS con ranibizumab vs monitorización en RDNP sin DME; el sistema de liberación continua redujo la frecuencia de tratamiento manteniendo control de la progresión |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Revisión Sistemática / Metaanálisis | Health Technology Assessment | Anti-VEGF vs fotocoagulación láser en DR; evaluación exhaustiva de eficacia comparativa en formas proliferativas y no proliferativas de retinopatía diabética |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Revisión Sistemática | Expert Opinion on Biological Therapy | Síntesis de evidencia de ranibizumab en DR; confirma beneficio en DME y mejoría consistente de DRSS como efecto de clase del anti-VEGF |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Metaanálisis de ECA Fase 3 | Ophthalmology Retina | Tiempo a resolución de DME con ranibizumab según severidad basal de DR; la RDNPG severa se asoció a respuesta diferida pero sostenida al tratamiento |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Análisis secundario de ECA Fase 3 | Clinical Ophthalmology | Predictores de regresión temprana de DR con ranibizumab en RIDE/RISE; menor severidad basal y tratamiento mensual sostenido fueron predictores de mejoría ≥2 pasos en DRSS |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Análisis secundario de ECA | Retina | DRCR.net Protocol I a 5 años: ranibizumab mejoró la severidad de DR en proporción significativa de pacientes con DME, efecto sostenido más allá del tratamiento activo |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Análisis secundario de ECA | JAMA Ophthalmology | Cambio en DR a 2 años con aflibercept, bevacizumab y ranibizumab; los tres anti-VEGF mejoraron la severidad de DR frente a placebo, confirmando efecto de clase |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Modelización de simulación | BMJ Open Ophthalmology | Simulación del impacto a largo plazo del anti-VEGF intravítreo en RDNPG severa; el tratamiento proactivo redujo progresión a RDP y eventos de pérdida visual vs estrategia diferida |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Desarrollo y validación de nomograma | Frontiers in Endocrinology | Predictores de respuesta a anti-VEGF + láser en RDNPG severa; nomograma multimodal para cuantificar probabilidad de respuesta individualizada (30–45% tasa de subóptimos) |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Revisión | Journal of Diabetes and Its Complications | Avances en tratamiento de DR; VEGF-A como diana central en etapas no proliferativas y proliferativas, con anti-VEGF emergiendo como estándar terapéutico |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 3 completados —incluyendo el ensayo Pavilion publicado en JAMA Ophthalmology en 2025— respaldan la eficacia de ranibizumab en retinopatía diabética no proliferativa, con un mecanismo anti-VEGF directamente pertinente a la fisiopatología de la RDNPG severa. La evidencia alcanza nivel L1; sin embargo, el fármaco no cuenta con registro sanitario en Colombia, lo que requiere gestiones regulatorias antes de su uso clínico formal.

**Para avanzar se necesita:**
- Obtener e interpretar el prospecto oficial (ficha técnica) de ranibizumab para documentar advertencias de seguridad, contraindicaciones y eventos adversos oculares conocidos (endoftalmitis, desprendimiento de retina, eventos tromboembólicos arteriales)
- Iniciar trámite de registro o importación ante INVIMA, o verificar si existe producto importado bajo régimen especial
- Evaluar el posicionamiento comparativo frente a aflibercept (con mayor cobertura de indicaciones aprobadas internacionalmente en DR) para definir la ventaja diferencial de ranibizumab en el contexto colombiano
- Diseñar un plan de farmacovigilancia activa para la población objetivo, con énfasis en monitoreo de presión intraocular, agudeza visual y eventos sistémicos en pacientes diabéticos con comorbilidades cardiovasculares
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

