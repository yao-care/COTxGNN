---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

A continuación el informe completo, generado a partir del Evidence Pack de IPILIMUMAB. Dado que la predicción de mayor rango TxGNN (choroideremia, rank 1) carece de toda base biológica y recibe recomendación Hold/L5 —según indica explícitamente el propio `repurposing_rationale`—, el informe se centra en la segunda predicción (**Melanoma No Cutáneo**, rank 2, L2, Proceed with Guardrails), que es la indicación accionable con evidencia real. Se incluye una nota explicativa sobre choroideremia al final.

---

# Ipilimumab: De Melanoma Cutáneo a Melanoma No Cutáneo

## Resumen en Una Frase

Ipilimumab (Yervoy®) es un anticuerpo monoclonal anti-CTLA-4 aprobado globalmente para el tratamiento del melanoma avanzado, pero actualmente **no comercializado en Colombia**. El modelo TxGNN predice que podría ser efectivo para **Melanoma No Cutáneo** (variantes uveal, mucosal y leptomeníngeo), con **más de 30 ensayos clínicos registrados** —incluyendo estudios de Fase 2 completados específicamente en melanoma uveal y metástasis leptomeníngeas— y **5 publicaciones** que respaldan esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Melanoma avanzado (cutáneo) — aprobación global; sin registro en Colombia |
| Nueva Indicación Predicha | Melanoma No Cutáneo (uveal, mucosal, leptomeníngeo) |
| Puntaje de Predicción TxGNN | 99.02% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Ipilimumab actúa bloqueando CTLA-4 (Cytotoxic T-Lymphocyte Antigen-4), un receptor inhibitorio expresado en la superficie de los linfocitos T. En condiciones normales, CTLA-4 amortigua la activación de las células T tras su encuentro con células presentadoras de antígeno; al bloquearlo, ipilimumab elimina este "freno" e intensifica la respuesta inmune antitumoral. Este mecanismo es esencialmente independiente del tejido de origen del tumor, siempre que el tumor exprese antígenos reconocibles por los linfocitos T. (Nota: el campo `original_moa` figura como Data Gap en el pack de datos; la descripción anterior corresponde al mecanismo globalmente documentado para este fármaco.)

El melanoma no cutáneo —uveal, mucosal y las metástasis leptomeníngeas— comparte con el melanoma cutáneo el origen en melanocitos y la expresión de antígenos tumorales reconocibles por linfocitos T (MART-1, gp100, NY-ESO-1). Esto otorga una base mecanística razonable para extender la indicación. Sin embargo, existen diferencias clínicamente importantes entre subtipos: el melanoma uveal presenta una carga mutacional tumoral (TMB) baja y un microambiente inmune "frío" (escasa infiltración linfocitaria), lo que limita la respuesta a los inhibidores de checkpoint; el melanoma mucosal puede tener TMB más elevada y, en teoría, mejor respuesta. El grado de respuesta es, por tanto, heterogéneo y dependiente del subtipo.

La predicción TxGNN de 99.02% refleja la proximidad topológica en el grafo del conocimiento entre melanoma cutáneo —indicación establecida de ipilimumab— y las variantes no cutáneas. Esta predicción no es puramente especulativa: existen ensayos de Fase 2 completados específicamente diseñados para melanoma uveal (NCT02626962, n=52) y metástasis leptomeníngeas (NCT02939300, n=18), así como análisis retrospectivos en práctica clínica real que incluyen subtipos no cutáneos, lo que otorga soporte empírico al razonamiento mecanístico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT02939300](https://clinicaltrials.gov/study/NCT02939300) | Fase 2 | Completado | 18 | Ipilimumab + nivolumab en metástasis leptomeníngeas (uno de los patrones de diseminación más frecuentes en melanoma no cutáneo); evaluó actividad clínica de la doble inhibición de checkpoint en SNC |
| [NCT02626962](https://clinicaltrials.gov/study/NCT02626962) | Fase 2 | Completado | 52 | Estudio multicéntrico de nivolumab + ipilimumab en melanoma uveal metastásico no tratado previamente; caracterización directa de seguridad y actividad clínica en el subtipo no cutáneo más prevalente |
| [NCT01730157](https://clinicaltrials.gov/study/NCT01730157) | Early Fase 1 | Terminado | 6 | Piloto de radioembolización hepática secuencial + ipilimumab en melanoma uveal con metástasis hepáticas; exploró sinergia entre abordaje local y bloqueo CTLA-4 sistémico |
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Fase 3 | Activo (sin reclutamiento) | 267 | DREAMseq: ipilimumab + nivolumab seguido de dabrafenib + trametinib vs secuencia inversa en melanoma avanzado BRAF V600 mutado; marco de referencia para terapia combinada en melanoma de alto riesgo |
| [NCT01927419](https://clinicaltrials.gov/study/NCT01927419) | Fase 2 | Completado | 142 | Comparación aleatorizada doble ciego de nivolumab + ipilimumab vs ipilimumab solo en melanoma no tratado; evidenció superioridad de la combinación en tasa de respuesta objetiva |
| [NCT04949113](https://clinicaltrials.gov/study/NCT04949113) | Fase 3 | Activo (sin reclutamiento) | 423 | NADINA: ipilimumab + nivolumab neoadyuvante vs nivolumab adyuvante estándar en melanoma Estadio III; datos clave sobre el uso perioperatorio de la combinación |
| [NCT01654692](https://clinicaltrials.gov/study/NCT01654692) | Fase 2 | Completado | 86 | Ipilimumab + fotemustine en melanoma avanzado irresecable o metastásico; evaluó eficacia y seguridad de la combinación citotóxica-inmunoterápica; población posiblemente mixta cutánea/no cutánea |
| [NCT04133948](https://clinicaltrials.gov/study/NCT04133948) | Fase 1/2 | Completado | 44 | DONIMI: domatinostat (inhibidor de HDAC) + nivolumab ± ipilimumab en melanoma Estadio III con firma IFN-γ baja; abordó el microambiente tumoral "frío", hipótesis directamente aplicable al melanoma uveal |
| [NCT01515189](https://clinicaltrials.gov/study/NCT01515189) | Fase 3 | Completado | 831 | Comparación de ipilimumab 3 mg/kg vs 10 mg/kg en melanoma metastásico; datos fundamentales de dosificación, supervivencia y perfil de seguridad por dosis |
| [NCT03220009](https://clinicaltrials.gov/study/NCT03220009) | Fase 2 | Retirado | 0 | Melanoma mucosal de alto riesgo: ipilimumab + nivolumab neoadyuvante seguido de nivolumab adyuvante vs observación; estudio retirado antes de iniciar reclutamiento, pero confirma interés clínico formal en el subtipo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohorte retrospectiva multitipo | Med J Australia | Evaluó eficacia y tolerabilidad de ipilimumab en práctica clínica real en melanoma cutáneo, uveal y mucosal; análisis comparativo por subtipo con datos de respuesta y eventos adversos inmuno-relacionados (irAE) |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohorte de mundo real | Current Oncology | Efectividad de anti-PD-1 solo o combinado con ipilimumab en adultos jóvenes (<65) vs mayores (≥65) con melanoma avanzado; datos de supervivencia global en práctica real multicéntrica |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Revisión sistemática | Curr Cancer Drug Targets | Revisión de principales ensayos Fase I-III (2000–2015) sobre tratamiento adyuvante del melanoma; sitúa a ipilimumab en el contexto histórico del arsenal terapéutico del melanoma |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Revisión clínica | Discovery Medicine | Actualización clínica de anti-PD-1 en monoterapia o combinado con ipilimumab para melanoma avanzado; incluye datos maduros de supervivencia de ensayos Fase 3 y posicionamiento terapéutico vigente |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Reporte de caso | Cureus | Metástasis colónica de melanoma tratada con resección quirúrgica e inmunoterapia; documenta perforación gastrointestinal como complicación rara pero grave asociada a ipilimumab, de relevancia para el monitoreo de seguridad |

---

## Información de Mercado en Colombia

Ipilimumab **no cuenta con registros sanitarios activos ante el INVIMA**. El fármaco no está comercializado en Colombia y no existe ninguna licencia vigente. El acceso actual requeriría importación bajo régimen de uso especial (importación por paciente individual o ensayo clínico) conforme a la normativa colombiana de medicamentos no comercializados.

---

## Citotoxicidad

| Ítem | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Inmunoterapia — Inhibidor de punto de control inmunitario (anti-CTLA-4); no es un agente citotóxico convencional |
| Riesgo de Mielosupresión | Bajo (la mielosupresión no es toxicidad predominante; el riesgo principal son los eventos adversos inmuno-relacionados) |
| Clasificación de Emetogenicidad | Baja |
| Ítems de Monitoreo | Función hepática (ALT/AST/bilirrubina), función tiroidea (TSH/T4L), cortisol/ACTH (hipofisitis), hemograma completo, función renal (creatinina), síntomas digestivos (colitis), síntomas pulmonares (neumonitis), piel (dermatitis) |
| Protección en Manejo | Anticuerpo monoclonal administrado por vía IV; seguir protocolos estándar para biológicos; no requiere manipulación bajo normas de citotóxicos convencionales |

---

## Consideraciones de Seguridad

Los datos de seguridad específicos del INVIMA no están disponibles dado que ipilimumab carece de registro en Colombia. Con base en la información internacional documentada:

- **Advertencias Principales**: Eventos adversos inmuno-relacionados (irAEs) graves y potencialmente fatales: colitis, hepatitis, endocrinopatías (hipofisitis, tiroiditis, insuficiencia suprarrenal), neumonitis, nefritis, dermatitis severa. Pueden presentarse durante el tratamiento o semanas a meses después de su finalización. Requieren manejo temprano con corticosteroides sistémicos.
- **Contraindicaciones**: Hipersensibilidad conocida al principio activo o excipientes de la formulación. Precaución significativa en pacientes con enfermedad autoinmune activa preexistente.

> Consultar el prospecto internacional (EMA/FDA — Yervoy®) para información de seguridad completa mientras no exista ficha técnica aprobada por INVIMA.

---

## Nota: Choroideremia (Predicción #1 de TxGNN — Descartada)

La predicción de mayor puntaje TxGNN (choroideremia, score 99.06%, rango 6880 en el modelo) fue evaluada y recibe recomendación **Hold / L5**. Choroideremia es una enfermedad degenerativa de la retina de origen monogénico (mutación en el gen *CHM* que codifica REP1, Rab escort protein 1), sin ningún componente inmune mediado por linfocitos T. El mecanismo de acción de ipilimumab (bloqueo CTLA-4, activación de inmunidad antitumoral) no tiene ningún punto de intersección con la fisiopatología de choroideremia. No existe evidencia clínica, preclínica ni hipótesis biológica publicada que respalde este uso. El alto puntaje TxGNN refleja exclusivamente similitud topológica en el grafo del conocimiento, sin traducción clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen ensayos clínicos de Fase 2 completados que evalúan específicamente ipilimumab en subtipos de melanoma no cutáneo —melanoma uveal (NCT02626962, n=52) y metástasis leptomeníngeas (NCT02939300, n=18)—, así como análisis retrospectivos en práctica clínica real que incluyen subtipos no cutáneos (PMID 24999899). La base mecanística es sólida (mismo origen melanocítico, mismos antígenos tumorales reconocibles por linfocitos T), aunque la magnitud de la respuesta varía significativamente por subtipo y perfil inmune del tumor.

**Para avanzar se necesita:**
- Gestionar autorización de importación o uso especial ante el INVIMA, dado que ipilimumab no está comercializado en Colombia
- Estratificar pacientes por subtipo específico de melanoma no cutáneo (uveal vs. mucosal vs. leptomeníngeo) antes de cualquier protocolo, ya que la respuesta es heterogénea
- Revisar ficha técnica internacional (FDA Label / EMA SmPC de Yervoy®) para datos completos de seguridad y dosificación
- Evaluar biomarcadores predictivos de respuesta: TMB, expresión de PD-L1, firma IFN-γ tumoral y densidad de infiltración linfocitaria (TIL) para seleccionar los pacientes con mayor probabilidad de beneficio
- Considerar la inclusión de pacientes colombianos en ensayos clínicos activos relevantes (ej. NCT04949113 — NADINA, NCT02224781 — DREAMseq) como vía de acceso regulado al fármaco con monitoreo prospectivo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

