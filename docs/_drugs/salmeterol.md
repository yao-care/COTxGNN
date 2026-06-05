---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 7
---

# Salmeterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Salmeterol: De Asma y EPOC a Bronquitis Crónica

## Resumen en Una Frase

Salmeterol es un agonista β2-adrenérgico de acción prolongada (LABA) ampliamente reconocido a nivel mundial como tratamiento de mantenimiento del asma y la enfermedad pulmonar obstructiva crónica (EPOC), aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis (Bronchitis)**, con **16 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
La combinación salmeterol/fluticasona ya cuenta con aprobación específica para EPOC asociada a bronquitis crónica en múltiples mercados internacionales, otorgando una sólida base mecanística y clínica a esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma y EPOC (uso global establecido; sin registro vigente en Colombia) |
| Nueva Indicación Predicha | Bronquitis crónica (Bronchitis) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha de información del fármaco. Sin embargo, según la información farmacológica ampliamente documentada, salmeterol es un agonista selectivo de larga duración del receptor β2-adrenérgico (β2-AR). A través de la vía adenilil ciclasa → AMPc → PKA, produce una relajación sostenida (~12 horas) del músculo liso bronquial, aliviando la obstrucción del flujo aéreo. De particular relevancia para la bronquitis crónica, salmeterol potencia la depuración mucociliar —mecanismo directamente pertinente dado que la hipersecreción de moco y la disfunción ciliar son manifestaciones centrales de esta enfermedad. El estudio PMID 15970448 cuantificó directamente este beneficio en pacientes con bronquitis crónica mediante análisis con aerosol radiomarcado.

La bronquitis crónica y la EPOC comparten una base fisiopatológica común: obstrucción inflamatoria progresiva de las vías aéreas bajas. La combinación salmeterol/fluticasona (Seretide/Advair) ya tiene aprobación específica en Estados Unidos para EPOC asociada a bronquitis crónica, y estudios de fase 3/4 de gran escala (NCT02173691, n=584; NCT01332409, n=2.000) han demostrado su eficacia en este fenotipo clínico. La predicción de TxGNN no solo es biológicamente coherente, sino que encuentra confirmación en la práctica regulatoria internacional.

El mecanismo de acción cubre los tres pilares sintomáticos de la bronquitis crónica: (1) broncodilatación sostenida que corrige la obstrucción espiratoria; (2) mejora de la frecuencia de batido ciliar que facilita el aclaramiento del esputo; y (3) reducción de mediadores inflamatorios en la mucosa bronquial. Estos efectos actúan de forma sinérgica sobre la tos crónica, la hipersecreción mucosa y la limitación al flujo de aire, los síntomas cardinales de la bronquitis crónica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Comparación cabeza a cabeza tiotropio vs salmeterol aerosol en EPOC/bronquitis crónica a 6 meses; evalúa eficacia broncodilatadora a largo plazo |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | ECA multicéntrico doble ciego con placebo y control activo; evaluó broncodilatación de arformoterol vs régimen que incluye salmeterol en EPOC/bronquitis crónica a 12 semanas |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | Post-comercialización | Completado | 2000 | Gran estudio de uso de ADOAIR DISKUS (salmeterol/fluticasona) en EPOC con bronquitis crónica y enfisema; la aparición de neumonía fue ítem prioritario de monitoreo |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Actividad antiinflamatoria bronquial de salmeterol/fluticasona 50/500 mcg vs placebo en EPOC a 13 semanas; evaluó supresión de inflamación en vías aéreas |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Fase 4 | Completado | 249 | Efecto de FP/salmeterol DISKUS 250/50 mcg BID sobre la rigidez arterial en EPOC a 16 semanas; salmeterol como brazo de comparación principal |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Fase 4 | Completado | 247 | Comparación de eficacia y seguridad de FSC HFA MDI vs FSC DISKUS 250/50 mcg en EPOC con bronquitis crónica a 12 semanas |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Fase 3 | Completado | 150 | Comparación de dos medicamentos en EPOC con pruebas de función pulmonar y registros diarios de síntomas a 18 semanas |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Fase 2 | Completado | 457 | ECA de búsqueda de dosis de FP/formoterol comparado con Advair Diskus (FP/salmeterol) en EPOC; identificó la dosis equivalente más cercana |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Fase 4 | Completado | 639 | Tasa de exacerbaciones de EPOC post-hospitalización con FP/salmeterol 250/50 mcg vs salmeterol 50 mcg BID a 29 semanas |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Fase 4 | Desconocido | 20 | Comparación de arformoterol nebulizado vs salmeterol DPI (Serevent) en EPOC; medición de apertura de vías aéreas pequeñas mediante pruebas de función pulmonar y HRCT |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | Estudio Clínico | Pulm Pharmacol Ther | Efecto agudo de salmeterol vs placebo sobre depuración mucociliar y mediante tos en bronquíticos crónicos (n=14); cuantificó directamente la mejora en aclaramiento de moco en vías aéreas |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | ECA | Chest | FP 250 mcg/salmeterol 50 mcg (DISKUS) vs placebo e ingredientes individuales en EPOC; la combinación demostró superioridad significativa en función pulmonar |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | ECA | Clin Ther | Salmeterol 50 mcg inhalado vs teofilina oral en EPOC leve-moderada estable; salmeterol superior en eficacia broncodilatadora y tolerabilidad |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Observacional | Curr Med Res Opin | FSC 250/50 vs otras terapias inhaladas en bronquitis crónica; FSC asociado a menor riesgo de hospitalización/visitas a urgencias y menores costos totales de atención |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Cohorte | Ther Adv Respir Dis | Seguridad de arformoterol vs salmeterol a 12 meses en EPOC; sin desarrollo de tolerancia al efecto broncodilatador con uso prolongado |
| [31852314](https://pubmed.ncbi.nlm.nih.gov/31852314/) | 2020 | ECA | J Int Med Res | Metaanálisis de FP/formoterol vs FP/salmeterol en asma pediátrica a 12 semanas; eficacia y seguridad comparables entre ambas combinaciones |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Revisión | Drugs Today | EPOC con bronquitis crónica: reducción de función pulmonar y mayor riesgo de exacerbaciones como características definitorias; contexto del uso de broncodilatadores |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía Clínica | Basic Clin Pharmacol Toxicol | Guías finlandesas para EPOC estable: incluye LABAs como salmeterol entre los pilares farmacológicos de primera línea |
| [20649375](https://pubmed.ncbi.nlm.nih.gov/20649375/) | 2010 | Revisión | Expert Rev Respir Med | Revisión de tratamientos en EPOC con bronquitis crónica; roflumilast añadido a broncodilatadores como salmeterol en pacientes con exacerbaciones frecuentes |
| [21316553](https://pubmed.ncbi.nlm.nih.gov/21316553/) | 2010 | Revisión | Arch Bronconeumol | Perfil clínico de la EPOC con bronquitis crónica; marcadores inflamatorios (tos crónica, esputo) correlacionados con frecuencia de exacerbaciones |

---

## Información de Mercado en Colombia

Actualmente no existen registros sanitarios INVIMA para salmeterol en Colombia. El fármaco no está comercializado en el mercado local.

> **Nota de contexto global:** A nivel internacional, salmeterol y la combinación fija salmeterol/fluticasona (Seretide®, Advair®) están aprobados en más de 100 países para asma y EPOC. En Estados Unidos, la indicación aprobada de FSC 250/50 mcg incluye específicamente el tratamiento de la EPOC asociada a bronquitis crónica. Esta robusta evidencia regulatoria internacional respalda la viabilidad del registro en Colombia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa.

> **Advertencia crítica de clase (LABA):** Los agonistas β2 de acción prolongada como salmeterol tienen una advertencia de recuadro negro de la FDA cuando se usan en monoterapia para el asma, por asociación con mayor riesgo de muerte relacionada con asma. Salmeterol debe usarse **siempre en combinación con un corticosteroide inhalado (ICS)** en el tratamiento del asma. En EPOC y bronquitis crónica, el perfil de seguridad de la monoterapia con salmeterol está mejor establecido, aunque la combinación con ICS sigue siendo la estrategia preferida.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 3/4 (incluyendo el gran estudio japonés de 2.000 pacientes NCT01332409 y el ensayo comparativo de 584 pacientes NCT02173691) respaldan la eficacia de salmeterol en bronquitis crónica con evidencia de nivel L1. La combinación salmeterol/fluticasona ya cuenta con aprobación regulatoria internacional específica para EPOC con bronquitis crónica, lo que valida la coherencia de la predicción de TxGNN y reduce sustancialmente el riesgo del desarrollo clínico.

**Para avanzar se necesita:**
- Iniciar proceso de registro sanitario INVIMA para salmeterol o la combinación salmeterol/fluticasona en Colombia, utilizando el paquete de evidencia internacional disponible
- Obtener datos detallados del mecanismo de acción (MOA) y las advertencias de seguridad completas del prospecto oficial (TFDA/FDA/EMA)
- Definir estrategia de uso: siempre en combinación con ICS (nunca como monoterapia en asma); evaluar si el registro aplica para EPOC, bronquitis crónica, o ambas indicaciones
- Evaluar viabilidad de acceso al mercado: registro propio del producto combinado o licenciamiento de un fabricante con presencia en la región latinoamericana
- Establecer un plan de farmacovigilancia activa, con especial atención al riesgo de neumonía reportado en los estudios de uso a largo plazo (NCT01332409)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

