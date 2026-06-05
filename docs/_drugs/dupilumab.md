---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# DUPILUMAB: De Dermatitis Atópica a Bronquitis

## Resumen en Una Frase

Dupilumab es un anticuerpo monoclonal humanizado que bloquea el receptor de IL-4/IL-13 (IL-4Rα), aprobado globalmente para dermatitis atópica moderada a grave y asma eosinofílica, aunque no cuenta con registro sanitario vigente en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, con **1 ensayo clínico** y **6 publicaciones** que actualmente respaldan esta dirección.
La evidencia disponible proviene principalmente de estudios en asma y enfermedades respiratorias de tipo Th2, con mecanismo directamente aplicable a la inflamación bronquial eosinofílica, aunque sin ensayos clínicos diseñados específicamente para bronquitis.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Dermatitis atópica moderada-grave / Asma eosinofílica (aprobación global; sin registro en Colombia) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en fuentes regulatorias colombianas. Según la información conocida, dupilumab es un anticuerpo monoclonal IgG4 humanizado que bloquea la subunidad alfa del receptor de IL-4 (IL-4Rα), inhibiendo simultáneamente la señalización de IL-4 e IL-13 —citocinas centrales de la respuesta inflamatoria tipo Th2—. Su eficacia en asma eosinofílica y dermatitis atópica ha sido ampliamente comprobada en ensayos de Fase 3, y mecanisticamente podría ser aplicable a la bronquitis de fenotipo T2.

La bronquitis eosinofílica y la bronquitis plástica comparten con el asma alérgica un sustrato fisiopatológico común: hipersecreción de moco mediada por IL-13, infiltración eosinofílica de la vía aérea e hiperrespuesta bronquial impulsada por la señalización IL-4/IL-13 y la vía Th2. En la bronquitis plástica eosinofílica pediátrica, la formación de moldes bronquiales está directamente asociada a la activación de células caliciformes por IL-13. Al bloquear este eje, dupilumab ofrece una base mecanística sólida para su potencial aplicación en bronquitis de fenotipo T2 elevado.

La predicción del modelo TxGNN con un puntaje de 99.92% refleja la estrecha proximidad en la red de conocimiento entre el asma eosinofílica (indicación ya aprobada) y la bronquitis eosinofílica crónica. El único ensayo clínico disponible evalúa dupilumab en rinosinusitis crónica sin pólipos (CRSsNP) —inflamación tipo 2 de vías respiratorias superiores con mecanismo análogo— pero no aborda directamente el tracto respiratorio inferior. La literatura de Nivel 1 documenta eficacia en asma mediante el mismo mecanismo, y reportes especializados describen beneficio en bronquitis eosinofílica plástica pediátrica, lo que constituye respaldo indirecto pero científicamente relevante.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|------------|----------------------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Fase 2 | Completado | 33 | Evaluación de dupilumab en rinosinusitis crónica sin pólipos (CRSsNP); inflamación tipo 2 de vías respiratorias superiores con mecanismo compartido con bronquitis eosinofílica; estudia múltiples endotipos de CRS excluyendo pólipos nasales; evidencia indirecta de eficacia anti-T2 en mucosa respiratoria |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | ECA Fase 3 (extensión) | The Lancet Respiratory Medicine | TRAVERSE: seguridad y eficacia a largo plazo de dupilumab en asma moderada-grave durante más de 1 año; evidencia de beneficio sostenido en inflamación bronquial tipo Th2 más allá de los estudios pivotales de 1 año |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Metaanálisis | The Journal of Asthma | Metaanálisis de ECAs: dupilumab reduce significativamente las exacerbaciones asmáticas y mejora el FEV1 en asma no controlada; mayor beneficio en pacientes con fenotipo eosinofílico elevado |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revisión sistemática | Tuberculosis and Respiratory Diseases | Revisión integral de terapias farmacológicas para prevenir exacerbaciones de EPOC; incluye biológicos anti-Th2 como terapias emergentes para subgrupos con componente eosinofílico y solapamiento con bronquitis crónica |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revisión / Serie de casos | Pediatric Pulmonology | Terapias novedosas para bronquitis eosinofílica plástica pediátrica; describe dupilumab como opción terapéutica prometedora dado el papel central de IL-4/IL-13 en la formación de moldes bronquiales eosinofílicos |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Observacional / Mecanístico | Chest | Tratamiento anti-T2 (incluyendo dupilumab) mejora defectos de ventilación bronquial por RM en asma grave con eosinofilia en esputo; evidencia directa del impacto en obstrucción bronquial mediada por la vía Th2 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opinion on Pharmacotherapy | Manejo de asma con bronquitis crónica y enfisema inducidos por tabaco; discute solapamiento mecanístico asma-EPOC y el papel incierto de biológicos dirigidos en pacientes fumadores con inflamación mixta |

---

## Información de Mercado en Colombia

Dupilumab (DB12159) **no cuenta con ningún registro sanitario activo en Colombia (INVIMA)**. El medicamento no está comercializado en el mercado colombiano. Para su eventual uso, se requeriría iniciar un proceso de registro sanitario ante el INVIMA o gestionar una importación individual mediante autorización especial. No se encontraron fichas de licencias, formas farmacéuticas ni indicaciones aprobadas en el sistema regulatorio colombiano.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Si bien la base mecanística para dupilumab en bronquitis eosinofílica es científicamente sólida —compartiendo la misma vía IL-4/IL-13 con el asma eosinofílica globalmente aprobada—, la ausencia de ensayos clínicos diseñados específicamente para bronquitis como entidad diagnóstica primaria, combinada con la falta de registro sanitario en Colombia, impide recomendar avance clínico inmediato.

**Para avanzar se necesita:**
- Ensayos clínicos específicos en bronquitis eosinofílica crónica, particularmente en pacientes con biomarcadores T2 elevados (FeNO ≥25 ppb, eosinófilos en sangre ≥300/μL)
- Datos de seguridad formales: advertencias INVIMA, contraindicaciones locales y evaluación de interacciones farmacológicas
- Inicio del proceso de registro sanitario ante el INVIMA como requisito regulatorio previo a cualquier uso en Colombia
- Confirmación del perfil MOA completo mediante consulta de la ficha técnica oficial (DrugBank API o monografía del fabricante Sanofi/Regeneron)
- Definición de la subpoblación de bronquitis con fenotipo Th2 para maximizar la selección de pacientes respondedores y diseñar un estudio de prueba de concepto
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

