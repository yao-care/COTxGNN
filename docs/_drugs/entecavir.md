---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: De Hepatitis B Crónica a Hepatitis C Crónica (Evaluación Multi-Indicación)

## Resumen en Una Frase

Entecavir (ETV) es un análogo nucleósido de desoxiguanosina aprobado mundialmente para el tratamiento de la infección crónica por virus de hepatitis B (VHB), aunque actualmente no cuenta con registro sanitario en Colombia. El modelo TxGNN predice como primera indicación la **hepatitis C crónica** (puntaje 99.98%), predicción que el análisis mecanístico identifica como un **falso positivo computacional** sin base biológica; sin embargo, en este paquete multi-indicación la oportunidad más accionable es la **hepatitis B crónica** (Rango 2, Nivel L1, Proceed with Guardrails), respaldada por más de 30 ensayos clínicos de Fase 3 y múltiples meta-análisis, que representa la vía de entrada prioritaria al mercado colombiano.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hepatitis B crónica (indicación aprobada globalmente; sin registro INVIMA en Colombia) |
| Nueva Indicacion Predicha (TxGNN Rango 1) | Hepatitis C crónica |
| Puntaje de Prediccion TxGNN | 99.98% |
| Nivel de Evidencia | L5 — Sin estudios que demuestren actividad anti-VHC directa de ETV |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Numero de Registros Sanitarios | 0 |
| Decision Recomendada | **Hold** (VHC, Rango 1) — Ver hallazgo prioritario VHB (Rango 2) |

---

## Por que es Razonable esta Prediccion?

Entecavir actúa como inhibidor competitivo de la DNA polimerasa del VHB, mimetizando al dGTP (desoxiguanosina trifosfato), su sustrato natural. Con un IC₅₀ de aproximadamente 0.004 µM, ETV suprime con alta potencia la replicación del VHB incluyendo sus actividades de transcriptasa reversa, síntesis de primera y segunda cadena de DNA, y polimerasa de DNA circular covalentemente cerrado (cccDNA). Su desarrollo clínico fue respaldado originalmente en modelos de woodchuck hepatitis virus (WHV) y culminó en aprobación por la FDA en 2005, tras ensayos de Fase 3 que demostraron superioridad histológica y virológica sobre Lamivudina y Adefovir.

**Análisis de la predicción VHC (Rango 1): falso positivo computacional.** El virus de hepatitis C (VHC) es un virus de RNA de cadena positiva (familia Flaviviridae) que se replica exclusivamente mediante una RNA polimerasa dependiente de RNA (NS5B). Esta enzima tiene una estructura, un sustrato y un mecanismo completamente distintos a la DNA polimerasa del VHB sobre la que actúa ETV. No existe ningún estudio in vitro, preclínico ni clínico que demuestre actividad anti-VHC directa de Entecavir. El puntaje TxGNN de 99.98% refleja la abundancia de nodos compartidos en el grafo de conocimiento biomédico entre VHB y VHC (co-infección frecuente, contexto de hepatopatía crónica, rutas de transmisión compartidas), sin implicar actividad farmacológica cruzada.

**Hallazgo prioritario — Hepatitis B para Colombia (Rango 2):** Aunque la hepatitis B es la indicación aprobada de ETV a nivel global, el fármaco no cuenta con registro sanitario ante el INVIMA. La carga de hepatitis B crónica en Colombia hace de este registro una oportunidad clínica relevante con evidencia de Nivel L1. Esta es la indicación más robusta y accionable de todo el análisis.

**Nota sobre VIH/HBV (Rango 3):** Estudios in vitro y observacionales (PMID 17582071, PMID 18453854) confirman que ETV posee actividad inhibidora parcial sobre la transcriptasa reversa del VIH-1, con eficacia especial frente a cepas resistentes a Lamivudina (M184V/I). Sin embargo, la exposición subóptima a ETV como monoterapia selecciona rápidamente la mutación M184V del VIH, comprometiendo futuros tratamientos antirretrovirales. Su uso está contraindicado en co-infección VIH/VHB sin régimen antirretroviral completo.

---

## Evidencia de Ensayos Clinicos

> Los ensayos a continuación corresponden a la predicción TxGNN Rango 1 (hepatitis C crónica). Todos fueron catalogados con Relevancia Grado C, confirmando que ninguno evalúa ETV como tratamiento directo del VHC.

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Co-infección VHC/VHB: DAA trata el VHC, ETV previene reactivación del VHB. ETV no actúa sobre el VHC. |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Fase 1 | Completado | 56 | Estudio de interacción farmacocinética entre Morphothiadine/Ritonavir y ETV/TDF. Sin evaluación de eficacia anti-VHC. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Fase 3 | Completado | 195 | ETV 1 mg vs. Adefovir 10 mg en VHB con descompensación hepática. Exclusivamente para VHB. |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Fase 4 | Completado | 131 | Efecto antiviral de ETV en pacientes afroamericanos e hispanos con VHB naïve a nucleósidos. Sin relación con VHC. |
| [NCT01354652](https://clinicaltrials.gov/study/NCT01354652) | Fase 4 | Suspendido | 5 | Incidencia de acidosis láctica con ETV en VHB con cirrosis severa (MELD > 18). Estudio de seguridad; sin relación con VHC. |

> **Conclusión:** Ningún ensayo clínico registrado evalúa ETV como terapia directa para la infección por VHC. Todos los ensayos recuperados son estudios de VHB en los que ETV aparece como terapia de fondo o como comparador.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Observacional | Viruses | Reactivación de VHC en 66 pacientes VHB positivos tratados con análogos nucleósidos (incluyendo ETV). ETV suprime VHB; el VHC se reactiva al revertirse la supresión inmunológica, sin efecto inhibidor de ETV sobre el VHC. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento de la co-infección VHB/VHC. ETV para el componente VHB; agentes de acción directa (DAA) imprescindibles para VHC. Sin actividad cruzada. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Revisión / Caso | Clin Res Hepatol Gastroenterol | Co-infección VHB/VHC como desafío terapéutico. Manejo diferenciado con PEG-IFN+RBV para VHC y ETV para VHB. Sin evidencia de eficacia anti-VHC de ETV. |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Revisión | World J Gastroenterol | VHB y consumo de alcohol como principales causas emergentes de hepatocarcinoma (CHC) en la era post-DAA. Contexto epidemiológico; no documenta actividad anti-VHC de ETV. |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Revisión | Chinese Clin Oncol | Timing y manejo de VHB y VHC en pacientes con hepatocarcinoma. ETV indicado para VHB; DAA para VHC. Ausencia total de evidencia de actividad anti-VHC de ETV. |

---

## Hallazgo Prioritario: Hepatitis B Cronica (Rango 2, L1)

> Esta sección presenta la evidencia de la indicación con mayor respaldo para Colombia: la infección crónica por VHB, para la cual Entecavir no tiene registro INVIMA pese a contar con evidencia de Nivel L1 a nivel global.

### Ensayos Clinicos Clave — VHB

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01726439](https://clinicaltrials.gov/study/NCT01726439) | Observacional | Completado | 3,434 | Estudio prospectivo de 5 años (EVOLVE). ETV monotherapy comparado con regímenes basados en Lamivudina en práctica real. Mayor supresión viral con ETV. |
| [NCT01595685](https://clinicaltrials.gov/study/NCT01595685) | Fase 3 | Completado | 98 | ECA: Telbivudina vs. ETV en reducción de HBsAg en pacientes con HBV DNA indetectable tras ETV previo. Evaluación de endpoint funcional de curación. |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Fase 3 | Completado | 195 | ETV 1 mg vs. Adefovir 10 mg en VHB con descompensación hepática (96 semanas). Superioridad de ETV en supresión viral y mejora de función hepática. |
| [NCT03210506](https://clinicaltrials.gov/study/NCT03210506) | No aplica | Desconocido | 120 | Cambios de citocinas durante PEG-IFN y análogos nucleósidos en VHB. ETV como brazo NA; caracterización de perfil inmunológico de respuesta. |
| [NCT01706575](https://clinicaltrials.gov/study/NCT01706575) | Fase 2b | Completado | 76 | PEG-IFN añadido a NAs (incluyendo ETV) en VHB HBeAg negativo con VHB DNA suprimido. Evaluación de reducción de HBsAg como proxy de cura funcional. |

### Literatura Clave — VHB

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35985545](https://pubmed.ncbi.nlm.nih.gov/35985545/) | 2022 | ECA | J Hepatology | ETV + Biejia-Ruangan (antifibrótico) vs. ETV solo en VHB crónica. Reducción significativa del riesgo de hepatocarcinoma a largo plazo. |
| [24905092](https://pubmed.ncbi.nlm.nih.gov/24905092/) | 2014 | Meta-análisis | PloS One | Comparación sistemática de TDF vs. ETV en VHB crónica (11 estudios, 1,656 pacientes). Eficacia comparable; ETV con perfil favorable en resistencia. |
| [38991458](https://pubmed.ncbi.nlm.nih.gov/38991458/) | 2024 | Revisión sistemática / Meta-análisis | J Clin Virology | Riesgo de resistencia al VHB con ETV vs. TDF. Confirma la alta barrera genética de ETV; resistencia rara en naïve a nucleósidos. |
| [26226455](https://pubmed.ncbi.nlm.nih.gov/26226455/) | 2015 | Meta-análisis | PloS One | Meta-análisis de 11 ECAs (1,010 pacientes): terapia combinada ETV + IFN vs. ETV solo. Mayor tasa de HBeAg seroconversión con combinación. |
| [35697332](https://pubmed.ncbi.nlm.nih.gov/35697332/) | 2022 | ECA (Fase 2) | J Hepatology | Vebicorvir + ETV vs. ETV solo en pacientes VHB naïve. Mayor supresión del VHB DNA con combinación; perfil de seguridad manejable. |

---

## Informacion de Mercado en Colombia

Entecavir no cuenta con registros sanitarios vigentes ante el INVIMA. No se identificó ningún producto comercializado bajo esta denominación común internacional en Colombia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Advertencia crítica identificada en evidencia clínica (Rango 3 — Co-infección VIH/VHB):**
> ETV posee actividad inhibidora parcial sobre la transcriptasa reversa del VIH-1. En pacientes con co-infección VIH/VHB sin régimen antirretroviral completo, el uso de ETV puede seleccionar rápidamente la mutación de resistencia M184V en el VIH, comprometiendo la eficacia futura de Lamivudina (3TC) y Emtricitabina (FTC). Las guías internacionales de práctica clínica contraindican explícitamente el uso de ETV en este contexto sin cobertura antirretroviral plena.

---

## Resumen de Predicciones Multi-Indicacion (Top 10 TxGNN)

| Rango | Indicacion | Puntaje TxGNN | Nivel Evidencia | Decision | Comentario clave |
|-------|-----------|---------------|-----------------|----------|-----------------|
| 1 | Hepatitis C crónica | 99.98% | L5 | **Hold** | Falso positivo. ETV no inhibe NS5B (RdRP del VHC). |
| **2** | **Hepatitis B crónica** | **99.85%** | **L1** | **Proceed with Guardrails** | **Indicación aprobada globalmente. Prioridad de registro INVIMA.** |
| 3 | Infección por VIH | 99.80% | L3 | Research Question | Actividad in vitro confirmada; riesgo crítico de selección M184V sin ARV completo. |
| 4 | Hepatitis C (aguda) | 99.69% | L5 | Hold | Mismo falso positivo que Rango 1; predicción duplicada por nodos compartidos. |
| 5 | Síndrome inmunodeficiencia felina | 99.65% | L5 | Hold | Predicción de lentivirus; sin estudios directos. Interés veterinario teórico. |
| 6 | Infección por VIS (simio) | 99.65% | L5 | Hold | Predicción grupal de lentivirus; puntuación idéntica a Rango 5, indica inferencia de categoría. |
| 7 | Trastorno neurodesarrollo con ataxia | 99.64% | L5 | **Hold — Riesgo potencial** | Falso positivo peligroso: ETV puede inhibir la DNA polimerasa mitocondrial γ (POLG); contraindicado en enfermedades mitocondriales. |
| 8 | Hepatitis viral animal | 99.46% | L4 | Research Question | Modelo WHV/DHBV documentado históricamente. Relevancia investigativa y veterinaria. |
| 9 | Infección por virus hepatitis E | 99.45% | L5 | Hold | HEV es virus RNA (Hepeviridae); mecanismo incompatible. Contaminación por palabra clave "hepatitis". |
| 10 | Infección por virus hepatitis A | 99.44% | L5 | Hold | HAV es Picornaviridae RNA; mecanismo incompatible. Misma contaminación de búsqueda. |

---

## Conclusion y Proximos Pasos

**Decision: Hold (VHC, Rango 1) + Proceed with Guardrails (VHB, Rango 2)**

**Justificacion:**
La predicción TxGNN de mayor rango (hepatitis C crónica) no tiene base mecanística y debe descartarse como falso positivo computacional generado por la alta co-ocurrencia de VHB y VHC en el grafo de conocimiento biomédico. El hallazgo verdaderamente accionable de este análisis multi-indicación es la **hepatitis B crónica** (Rango 2): con Nivel L1 respaldado por múltiples ensayos de Fase 3, meta-análisis y guías internacionales, Entecavir es un candidato prioritario para solicitar registro sanitario ante el INVIMA y cubrir una necesidad clínica no atendida en Colombia. Adicionalmente, el uso en co-infección VIH/VHB (Rango 3) es una pregunta de investigación clínicamente relevante, condicionada a un protocolo de uso estricto con cobertura antirretroviral completa.

**Para avanzar se necesita:**
- Iniciar proceso de registro sanitario ante el INVIMA para la indicación de hepatitis B crónica (Nivel L1, Proceed with Guardrails)
- Obtener el prospecto oficial aprobado (FDA/EMA) para documentar formalmente advertencias, contraindicaciones y ajuste de dosis en insuficiencia renal
- Confirmar disponibilidad comercial del fabricante y existencia de versiones genéricas aprobadas para el mercado latinoamericano
- Para el contexto VIH/VHB (Rango 3): diseñar protocolo de farmacovigilancia que garantice cobertura antirretroviral completa antes de introducir ETV y monitoreo de mutación M184V
- Completar los datos de seguridad local (DG001: prospecto INVIMA/TFDA) antes de avanzar a la evaluación de seguridad formal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

