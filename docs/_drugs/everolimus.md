---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Everolimus
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

La skill confirma el contexto del pipeline TxGNN. Ahora procedo a generar el informe completo basado en el Evidence Pack proporcionado.

---

# Everolimus: De Carcinoma de Células Renales a Liposarcoma

## Resumen en Una Frase

Everolimus es un inhibidor de mTORC1 aprobado internacionalmente para el tratamiento del carcinoma de células renales, cáncer de mama avanzado y tumores neuroendocrinos, entre otras indicaciones oncológicas.
El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**,
con **1 ensayo clínico** y **5 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células renales (indicación internacional de referencia; sin registro activo en Colombia) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en la base regulatoria colombiana. Sin embargo, según la información disponible en la literatura científica incluida en este paquete de evidencia, Everolimus pertenece a la clase de inhibidores de mTORC1 (rapalogs), cuya eficacia en carcinoma de células renales, tumores neuroendocrinos y cáncer de mama HER2-negativo está ampliamente documentada a nivel internacional. Su mecanismo central consiste en bloquear la vía PI3K/AKT/mTOR, una ruta de señalización maestra que regula la proliferación, supervivencia y metabolismo celular en múltiples tipos de cáncer.

En el liposarcoma desdiferenciado (DDLPS) específicamente, estudios inmunohistoquímicos en 99 especímenes de pacientes han confirmado la activación de las vías AKT/mTOR y MAPK, con demostraciones in vitro de efectos antitumorales mediante inhibidores de mTOR (PMID 26518767). Este hallazgo proporciona una base mecanística directa y sólida para la aplicación de Everolimus en esta histología.

La racionalidad se fortalece adicionalmente por la sinergia con Ribociclib (inhibidor de CDK4/6): DDLPS frecuentemente presenta amplificación de CDK4, y la inhibición combinada de CDK4/6 (ciclo celular) y mTOR (señalización proliferativa) actúa sobre dos nodos críticos de forma complementaria. Esta hipótesis fue llevada a ensayo clínico formal (NCT03114527, Fase II), con resultados publicados en 2024 (PMID 37967116), completando el puente entre mecanismo molecular y evidencia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo (sin nuevas inscripciones) | 48 | Estudio de 2 brazos (Brazo A: DDLPS, Brazo B: LMS) evaluando Ribociclib 300 mg/día (3 semanas sí/1 semana no) + Everolimus 2.5 mg en pacientes con ≥1 terapia previa; resultados publicados en 2024 (PMID 37967116) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Ensayo Clínico Fase II | Clinical Cancer Research | Evaluación de Ribociclib + Everolimus en DDLPS y LMS avanzados; confirma CDK4/6 e inhibición de mTOR como dianas sinérgicas con actividad antitumoral en sarcomas de tejidos blandos |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Estudio Mecanístico/Traslacional | Tumour Biology | Activación de vías AKT/mTOR y MAPK demostrada en 99 especímenes de DDLPS; estudio in vitro confirma efectos antitumorales de inhibidor mTOR, proporcionando base mecanística directa |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisión | Frontiers in Oncology | Modelos PDOX de sarcomas para identificación de combinaciones efectivas con inhibidores CDK; respalda estrategias de combinación con agentes como inhibidores de mTOR en histologías de sarcoma |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclínico (In Vitro/In Vivo) | Anticancer Research | Eribulina en combinación con agentes de distinto mecanismo (incluyendo inhibidores de mTOR) en liposarcoma avanzado; provee contexto de eficacia combinada en esta histología |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclínico/Mecanístico | Oncogene | KPT-330 (Selinexor) altera el circuito transcripcional regulador central de DDLPS modulando el proceso de traducción; contextualiza la urgencia de nuevas terapias dirigidas en DDLPS de alta recurrencia |

---

## Información de Mercado en Colombia

Everolimus no cuenta con registros sanitarios activos en Colombia (INVIMA). No se han identificado licencias de comercialización para este principio activo en el mercado colombiano.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTORC1 — clase rapalogs/análogos de rapamicina) |
| Riesgo de Mielosupresión | Moderado (anemia, trombocitopenia y neutropenia descritas como efectos adversos frecuentes en ensayos clínicos oncológicos con Everolimus) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma completo con diferencial, función renal (creatinina), función hepática (transaminasas, bilirrubina), glucemia en ayunas, perfil lipídico, vigilancia activa de neumonitis no infecciosa (toxicidad pulmonar característica de inhibidores de mTOR) |
| Protección en Manejo | Seguir regulaciones estándar de manejo de fármacos antineoplásicos orales; precaución especial por efecto inmunosupresor concomitante; manipulación con guantes y sin triturar las tabletas/cápsulas |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El ensayo clínico de Fase II NCT03114527 evaluó directamente Everolimus en liposarcoma desdiferenciado avanzado con resultados publicados en 2024, y la evidencia mecanística confirma la activación de mTOR como driver en esta histología; sin embargo, la ausencia total de registro en Colombia y los datos de seguridad locales pendientes imponen guardrails regulatorios y clínicos antes de cualquier aplicación.

**Para avanzar se necesita:**
- Obtener datos completos de seguridad (advertencias de recuadro negro, contraindicaciones absolutas, principales interacciones farmacológicas) a partir del prospecto internacional de Everolimus (FDA, EMA o DrugBank)
- Evaluar la viabilidad de acceso en Colombia: vía importación por uso compasivo (resolución INVIMA), ensayo clínico local o tramitación de registro sanitario
- Revisar en detalle los resultados de eficacia del NCT03114527 (PMID 37967116) para cuantificar tasa de respuesta objetiva, SLP y perfil de toxicidad en DDLPS
- Confirmar el subtipo histológico de liposarcoma con mayor probabilidad de respuesta (el ensayo se enfocó en DDLPS; otros subtipos como liposarcoma mixoide/pleomórfico pueden tener diferente sensibilidad a mTOR)
- Considerar diseño de protocolo de estudio piloto en Colombia que incluya determinación de estado de activación de la vía mTOR como biomarcador de selección
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

