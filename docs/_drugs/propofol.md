---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 5
---

# Propofol
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

# Propofol: De Anestésico General a Tratamiento de Migraña Refractaria

## Resumen en Una Frase

Propofol es un agente anestésico-hipnótico intravenoso de acción ultra-corta, ampliamente utilizado para la inducción y mantenimiento de la anestesia general y la sedación procedural.
El modelo TxGNN predice que podría ser efectivo para el tratamiento de la **Migraña** (migraine disorder),
con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anestesia general e inducción/mantenimiento de la sedación |
| Nueva Indicación Predicha | Migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Propofol (2,6-diisopropilfenol) es un agente anestésico intravenoso cuyo mecanismo primario consiste en la **modulación positiva de los receptores GABAₐ** en el sistema nervioso central, produciendo sedación, hipnosis e inhibición generalizada de la excitabilidad neuronal cortical. Aunque los datos formales de MOA del Evidence Pack requieren complementación desde la ficha técnica oficial, la literatura científica es consistente en describir este efecto inhibitorio como el fundamento de su actividad clínica.

La conexión con la migraña es mecanísticamente sólida: propofol suprime la **depresión cortical propagada (CSD)**, que constituye el correlato neurofisiológico del aura migrañosa y actúa como disparador del dolor vascular. Adicionalmente, propofol posee propiedades antiinflamatorias documentadas —inhibe COX-2 e IL-6— y reduce la hiperexcitabilidad del sistema trigeminovascular, que es el eje central de la fisiopatología de la migraña. Esta convergencia de mecanismos ofrece una base biológica plausible para su uso a **dosis subanestésicas** (10–30 mg IV) en el contexto de urgencias hospitalarias.

En la práctica clínica, el uso de propofol a bajas dosis para migraña refractaria en servicios de urgencias cuenta ya con experiencia acumulada en poblaciones adultas y pediátricas, especialmente en casos que han fallado los tratamientos de primera línea (AINEs, antagonistas dopaminérgicos). Estudios prospectivos aleatorizados, una revisión sistemática y una guía clínica de la American Headache Society (2026) han comenzado a formalizar esta indicación emergente.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Fase 2/3 | Completado | 74 | ECA de propofol en dosis subanestésica para migraña aguda en urgencias pediátricas; proporciona datos de seguridad y eficacia de mayor jerarquía disponibles para esta indicación |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completado | 40 | Infusión de propofol a bajas dosis como agente abortivo en migraña pediátrica; evalúa eficacia, rango de dosis seguro y duración del efecto |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminado | 12 | Propofol a bajas dosis para migraña refractaria severa en adultos en urgencias; terminado anticipadamente por baja inscripción, con valor únicamente exploratorio |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | Desconocido | 130 | Comparación de sevoflurano vs. propofol en anestesia general y ocurrencia de cefalea postoperatoria; proporciona evidencia indirecta del efecto protector de propofol sobre cefalea |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | NA | Completado | 315 | Estudio de electroacupuntura en cirugía cardíaca (OP-CABG); propofol no es la intervención principal y la relación directa con migraña es marginal |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía Clínica | Headache | Actualización 2025 de la guía AHS sobre farmacoterapias parenterales para migraña aguda en urgencias; incluye evaluación sistematizada de propofol |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revisión Sistemática | Headache | Revisión sistemática y análisis de red sobre agentes parenterales para reducir recaída en migraña aguda severa; compara propofol con otras opciones |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revisión Sistemática | Acad Emerg Med | Revisión sistemática de seguridad y eficacia de propofol para migraña aguda en urgencias; sintetiza la evidencia existente en entornos ambulatorios y hospitalarios |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | ECA | Arch Acad Emerg Med | ECA doble ciego: propofol + granisetron vs. propofol + metoclopramida en manejo sintomático de migraña aguda en urgencias |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | ECA | Arch Acad Emerg Med | ECA: sumatriptán solo vs. sumatriptán + propofol en migraña aguda; evalúa el beneficio incremental de la combinación |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | ECA | J Emerg Med | ECA prospectivo controlado de propofol a bajas dosis para migraña pediátrica en urgencias; evalúa eficacia y perfil de seguridad |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Revisión | Curr Pain Headache Rep | Revisión del tratamiento intravenoso de migraña en niños y adolescentes, con análisis del rol de propofol entre las opciones disponibles |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Retrospectivo | Expert Rev Neurother | Perfil farmacológico completo del propofol en dosis subanestésica para manejo de migraña refractaria/intratable en centro de cefalea |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Revisión | Headache | Revisión de terapias de rescate para migraña aguda (parte 2); evalúa propofol junto a neurolépticos, antihistamínicos y otros agentes en urgencias |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Serie de Casos | Headache | Primer reporte de efectividad de propofol IV en migraña intratable en entorno ambulatorio; describe experiencia inicial que motivó investigación posterior |

---

## Información de Mercado en Colombia

Actualmente no existen registros sanitarios INVIMA para propofol en Colombia según los datos disponibles. El medicamento no se encuentra comercializado a través de canales regulares; su uso requeriría importación hospitalaria o trámite de registro ante INVIMA.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un mecanismo biológico plausible y bien sustentado (inhibición de CSD vía modulación GABAₐ, propiedades antiinflamatorias, reducción de la hiperexcitabilidad trigeminovascular), respaldado por un ECA de Fase 2/3 completado (NCT01604785, n=74), dos ECAs adicionales en adultos, una revisión sistemática y la mención en la guía clínica 2025 de la American Headache Society. Sin embargo, la ausencia de registro sanitario en Colombia, los datos de seguridad formales pendientes y la exigencia de administración IV monitorizada limitan su aplicabilidad fuera del ámbito hospitalario especializado.

**Para avanzar se necesita:**
- Completar los datos de MOA y advertencias de seguridad desde la ficha técnica oficial (DrugBank API, prospecto FDA/EMA)
- Evaluar viabilidad regulatoria para uso hospitalario en urgencias en Colombia (trámite INVIMA)
- Confirmar disponibilidad del medicamento en el mercado colombiano (importación hospitalaria autorizada)
- Diseñar protocolo clínico de administración: dosis subanestésica (10–30 mg IV), monitoreo de sedación, supervisión anestesiológica y criterios de exclusión (alergias a huevo/soja, inestabilidad hemodinámica)
- Revisar interacciones farmacológicas con medicamentos de uso concomitante habitual en urgencias (opioides, benzodiazepinas, antieméticos)
- Considerar un estudio piloto local dado que la evidencia de mayor calidad proviene de poblaciones pediátricas y contextos externos a Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

