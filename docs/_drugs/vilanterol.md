---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: De Broncodilatador LABA a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

Vilanterol es un agonista β2-adrenérgico de larga duración (LABA) desarrollado como componente de terapias inhaladas combinadas — FF/UMEC/VI (Trelegy Ellipta) y UMEC/VI (Anoro Ellipta) — aprobadas por FDA y EMA para el tratamiento de EPOC y asma, aunque actualmente sin registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Enfermedad Pulmonar Obstructiva (EPOC/Asma)**,
con **50 ensayos clínicos** y **20 publicaciones** que respaldan sólidamente esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Sin indicación registrada en Colombia (aprobado por FDA/EMA en combinaciones para EPOC y asma) |
| Nueva Indicación Predicha | Enfermedad Pulmonar Obstructiva (obstructive lung disease) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Vilanterol (GW642444) es un agonista β2-adrenérgico de alta selectividad con actividad intrínseca de 24 horas in vitro. Su mecanismo consiste en unirse a los receptores β2 de la musculatura lisa bronquial, activando la adenilil ciclasa, lo que eleva el AMPc intracelular, activa la PKA y produce relajación del músculo liso de la vía aérea. Adicionalmente, inhibe la liberación de mediadores inflamatorios por mastocitos. Esta combinación de broncodilatación potente y prolongada con efecto antiinflamatorio local constituye el fundamento de su uso en enfermedades obstructivas crónicas.

La enfermedad pulmonar obstructiva —EPOC y asma persistente moderada a grave— es precisamente la indicación para la que fue desarrollado Vilanterol. Las combinaciones que lo contienen cuentan con aprobaciones regulatorias en EE. UU., Europa y otras regiones. El modelo TxGNN asigna el puntaje más alto de toda la lista de predicciones (99.97%), lo que refleja la fuerte correspondencia entre el mecanismo del fármaco y la fisiopatología de la obstrucción bronquial reversible. En este caso, la predicción no es un reposicionamiento convencional, sino una validación computacional de un uso ya establecido globalmente.

En Colombia, sin embargo, ninguna combinación que contenga Vilanterol dispone de registro sanitario vigente, lo que convierte esta predicción en una señal de oportunidad de acceso terapéutico: existe una brecha entre la evidencia global de nivel L1 y la disponibilidad local. El IMPACT trial (NEJM, n=10.355) y el SUMMIT trial (n=16.568) han demostrado reducción de exacerbaciones, mejora de función pulmonar y disminución de mortalidad por todas las causas, ofreciendo uno de los paquetes de evidencia más sólidos disponibles para una terapia inhalada en EPOC.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Fase 3 | Completado | 1.621 | FF/VI 100/25 mcg vs VI 25 mcg en COPD durante 12 semanas: evaluó la contribución del corticosteroide inhalado (FF) a la mejoría de trough FEV1 sobre la broncodilatación sola |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Fase 3 | Completado | 717 | UMEC/VI vs fluticasona propionato/salmeterol en COPD: estudio multicéntrico doble ciego doble placebo, comparación directa de dos combinaciones LAMA/LABA e ICS/LABA |
| [NCT01817764](https://clinicaltrials.gov/study/NCT01817764) | Fase 3 | Completado | 707 | Segunda réplica multicéntrica: UMEC/VI vs FP/salmeterol en COPD, diseño idéntico para confirmar robustez del beneficio en función pulmonar |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Fase 3 | Completado | 905 | UMEC/VI 62.5/25 mcg vs Tiotropio 18 mcg durante 24 semanas: evaluación espirométrica (trough FEV1) en COPD |
| [NCT01313650](https://clinicaltrials.gov/study/NCT01313650) | Fase 3 | Completado | 1.538 | UMEC/VI, UMEC, VI y placebo administrados una vez al día durante 24 semanas en COPD: estudio controlado con placebo de eficacia y seguridad |
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Fase 3 | Completado | 16.568 | SUMMIT trial: FF/VI vs placebo en COPD moderado con alto riesgo cardiovascular — evaluó supervivencia y eventos cardiovasculares a largo plazo |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Fase 4 | Completado | 800 | FF/UMEC/VI (triple en un solo inhalador) vs tiotropio en monoterapia durante 12 semanas: función pulmonar y síntomas en COPD |
| [NCT05535972](https://clinicaltrials.gov/study/NCT05535972) | Fase 4 | Completado | 463 | Efectividad real de Trelegy Ellipta en COPD sintomático: estado de salud (CAT), disnea y función pulmonar en práctica clínica |
| [NCT05169424](https://clinicaltrials.gov/study/NCT05169424) | N/A | Completado | 9.117 | Stiolto Respimat vs Trelegy Ellipta en COPD naïve a mantenimiento: tiempo hasta primera exacerbación usando datos de claims farmacéuticos durante 3,5 años |
| [NCT06474039](https://clinicaltrials.gov/study/NCT06474039) | Fase 3 | Reclutando | 50 | FF/VI/UMEC triple vs VI/UMEC dual en COPD: efectos sobre air trapping y niveles de citocinas en sangre y vía aérea — acumula evidencia de primera línea en curso |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | ECA | N Engl J Med | IMPACT trial: FF/UMEC/VI una vez al día redujo significativamente las exacerbaciones moderadas/graves vs terapia dual (ICS/LABA o LAMA/LABA), con señal de reducción de mortalidad por todas las causas |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | ECA (análisis secundario) | Am J Respir Crit Care Med | Análisis definitivo de mortalidad del IMPACT trial: FF/UMEC/VI redujo significativamente el riesgo de muerte por todas las causas vs UMEC/VI, con estado vital completo de todos los participantes |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | ECA | Am J Respir Crit Care Med | FULFIL trial: FF/UMEC/VI una vez al día demostró superioridad sobre budesonida/formoterol dos veces al día en función pulmonar (trough FEV1) y calidad de vida relacionada con la salud (SGRQ) en COPD |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | ECA (análisis de subgrupos) | Eur Respir J | Historia de exacerbaciones en IMPACT: el beneficio de FF/UMEC/VI es mayor en pacientes con ≥2 exacerbaciones moderadas o ≥1 grave; el recuento de eosinófilos en sangre modifica el efecto de los ICS |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Metaanálisis en red | Adv Ther | NMA de FF/UMEC/VI frente a otras terapias triples y duales: FF/UMEC/VI es superior a múltiples comparadores en exacerbaciones moderadas/graves, función pulmonar y calidad de vida |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Revisión sistemática | BMC Pulm Med | UMEC/VI asociado a mejoría clínicamente significativa en FEV1 y calidad de vida en COPD leve a moderado frente a broncodilatadores en monoterapia o combinaciones duales |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohorte | BMJ | Efectividad y seguridad comparativa de FF/UMEC/VI vs budesonida/glicopirronio/formoterol en COPD en práctica clínica real: ambas terapias triples muestran beneficios similares |
| [39731707](https://pubmed.ncbi.nlm.nih.gov/39731707/) | 2025 | Cohorte | Adv Ther | FF/UMEC/VI vs BUD/GLY/FORM en pacientes estadounidenses con COPD: estudio de efectividad comparativa en mundo real sobre exacerbaciones y resultados clínicos |
| [37213116](https://pubmed.ncbi.nlm.nih.gov/37213116/) | 2023 | Cohorte | JAMA Intern Med | LAMA/LABA (incluyendo UMEC/VI) vs ICS/LABA en COPD: menor incidencia de hospitalización por neumonía con LAMA/LABA, con datos de práctica clínica real alineados con guías GOLD |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Revisión sistemática | Clin Resp J | UMEC/VI como combinación de dosis fija en COPD: revisión comprensiva de eficacia, seguridad y posicionamiento tras aprobación FDA 2013; sustenta el perfil riesgo-beneficio |

---

## Información de Mercado en Colombia

Actualmente no existe ningún registro sanitario vigente en Colombia para Vilanterol, ya sea en formulación simple o en las combinaciones que lo contienen (FF/UMEC/VI, UMEC/VI, FF/VI). El fármaco no está disponible en el mercado colombiano.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Vilanterol en combinaciones inhaladas cuenta con evidencia de Nivel L1 avalada por múltiples ECAs de Fase 3 y Fase 4 con decenas de miles de pacientes (IMPACT: n=10.355; SUMMIT: n=16.568), metaanálisis en red y datos de mundo real robustos. La ausencia de registro en Colombia representa una brecha de acceso a una terapia de eficacia y seguridad bien establecidas globalmente, lo que justifica avanzar con las salvaguardas regulatorias locales.

**Para avanzar se necesita:**
- Obtener la ficha técnica completa de FDA/EMA (advertencias, contraindicaciones, interacciones farmacológicas) para caracterizar el perfil de seguridad antes de la solicitud ante INVIMA
- Iniciar proceso de registro sanitario ante INVIMA para al menos una de las combinaciones que contienen Vilanterol (Trelegy Ellipta y/o Anoro Ellipta), con dosier técnico completo
- Verificar viabilidad de cadena de suministro, estrategia de precio y condiciones de conservación del inhalador seco ELLIPTA para el mercado colombiano
- Revisar guías GOLD actualizadas para identificar el perfil de paciente colombiano que más se beneficiaría (GOLD B/E con historial de exacerbaciones frecuentes o grave)
- Diseñar un plan de farmacovigilancia local que contemple los riesgos conocidos: neumonía (en triple terapia con ICS), efectos cardiovasculares (taquicardia, prolongación QT), hipopotasemia y taquifilaxia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

