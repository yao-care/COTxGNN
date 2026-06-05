---
layout: default
title: Clioquinol
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 7
---

# Clioquinol
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

Usando el skill `txgnn-pipeline` como contexto de referencia del pipeline de reposicionamiento. Procedo a generar el informe de evaluación con base en el Evidence Pack proporcionado.

---

# Clioquinol: De Antiséptico Tópico a Candidiasis Cutánea

## Resumen en Una Frase

Clioquinol (Vioform) es un derivado de la 8-hidroxiquinolina históricamente utilizado como antiséptico y antifúngico tópico en formulaciones combinadas para infecciones cutáneas secundarias. El modelo TxGNN predice que podría ser efectivo para **Candidiasis Cutánea**, con **0 ensayos clínicos** modernos registrados y **6 publicaciones** (principalmente de los años 1965–1988) que respaldan esta dirección. La evidencia disponible corresponde a estudios comparativos y series clínicas, sin ECAs actualizados ni registro sanitario activo en Colombia.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrado en Colombia; uso histórico como antiséptico tópico (Vioform / Locacorten-Vioform) |
| Nueva Indicación Predicha | Candidiasis Cutánea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos oficiales del mecanismo de acción en este paquete de evidencia. Con base en la clase farmacológica conocida, clioquinol es un derivado de la **8-hidroxiquinolina** con actividad antifúngica y antibacteriana. Su acción frente a *Candida spp.* se atribuye principalmente a la **quelación de iones Cu²⁺ y Zn²⁺** esenciales para el metabolismo fúngico: al privar al hongo de estos metales, se alteran enzimas críticas como la superóxido dismutasa (SOD) y los citocromos de la cadena respiratoria, comprometiendo adicionalmente la integridad de la membrana celular fúngica. Este mecanismo es distinto al de los azoles (inhibición de la síntesis de ergosterol) y los polienos (formación de poros en la membrana), lo que lo posiciona como candidato a terapia complementaria o de rescate.

La relación entre el uso histórico de clioquinol y la candidiasis cutánea no es especulativa: la formulación **Locacorten-Vioform** (clioquinol 3% + flumetasona tópica) fue ampliamente utilizada en los años 1970–1980 para dermatosis inflamatorias complicadas con infección secundaria por *Candida* y bacterias. Los estudios recuperados documentan directamente esta experiencia clínica, lo que confiere al puntaje TxGNN de 99.84% una base histórica concreta en lugar de una extrapolación teórica pura.

Sin embargo, la evidencia existente es antigua (ninguna publicación posterior a 1988 en esta indicación específica), los diseños metodológicos son limitados para los estándares actuales, y el perfil de seguridad sistémico de clioquinol —asociado a neuropatía subaguda mielo-óptica (SMON) en uso oral, documentado principalmente en Japón— exige que cualquier aplicación clínica futura se restrinja exclusivamente a formulaciones tópicas de baja concentración (≤3%) con monitoreo dermatológico activo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Estudio Comparativo Aleatorizado | J Int Med Res | En 154 pacientes (67 con candidiasis cutánea), la crema BGI (conteniendo yodoclorohidroxiquina/clioquinol) mostró respuesta terapéutica equivalente a la crema HNN; evidencia de eficacia comparable del clioquinol tópico |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Serie Clínica (doble ciego) | Dermatologica | En 430 pacientes, Locacorten-Vioform (clioquinol 3%) fue altamente eficaz en dermatosis complicadas con infección secundaria; mayor conversión microbiológica vs. monoterapias y placebo |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Ensayo Clínico No Aleatorizado | Curr Ther Res | Evaluación clínica de combinación halcinonida-antifúngico que incluye clioquinol en candidiasis cutánea; resultados clínicos favorables |
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Estudio Comparativo | Curr Med Res Opin | En 40 pacientes con candidiasis cutánea, HNA (halcinonida-neomicina-anfotericina) logró 95% de respuesta excelente vs. 43% para yodoclorohidroxiquina-hidrocortisona (clioquinol como comparador activo); sugiere eficacia inferior frente a antifúngicos más modernos |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Observacional (in vitro) | Przegl Dermatol | Entre múltiples aditivos evaluados sobre *C. albicans*, clioquinol mostró el efecto fungicida más potente en soluciones jabonosas alcalinas |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Reporte de Caso | Z Haut Geschlechtskr | Reporte sobre el rol de levaduras en la etiología de la acrodermatitis enteropática de Danbolt-Closs con referencia al uso de clioquinol |

---

## Información de Mercado en Colombia

Clioquinol no cuenta con registros sanitarios activos en Colombia. INVIMA no registra ninguna licencia vigente para este principio activo (consulta actualizada a mayo de 2026). No existen formulaciones aprobadas bajo este INN en el mercado colombiano actual.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota de alerta histórica:** El uso sistémico (oral) de clioquinol fue retirado o severamente restringido en múltiples países a partir de los años 1970 debido a casos de **neuropatía subaguda mielo-óptica (SMON)**, documentada principalmente en Japón. Las formulaciones tópicas en concentraciones bajas (≤3%) se consideran de menor riesgo sistémico, pero deben utilizarse bajo supervisión médica, en áreas limitadas y por períodos cortos. Se requiere revisión completa del prospecto antes de cualquier uso clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación de clioquinol tópico para candidiasis cutánea cuenta con evidencia histórica de nivel L3 —incluyendo un ensayo doble ciego en 430 pacientes y estudios comparativos aleatorizados— que documenta eficacia real en formulaciones tipo Locacorten-Vioform. Sin embargo, la antigüedad de los datos (todos anteriores a 1990), la ausencia de ensayos clínicos modernos, los resultados mixtos de eficacia comparativa (43% vs. antifúngicos más potentes) y el perfil de seguridad sistémico (SMON por vía oral) exigen guardrails claros antes de cualquier desarrollo clínico.

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción completo (MOA) mediante consulta a DrugBank API — pendiente según el paquete de evidencia (DG002)
- Obtener y revisar prospectos de formulaciones tópicas actualmente autorizadas en la UE, EE. UU. o Japón para validar el perfil de seguridad por vía tópica
- Investigar si existen formulaciones combinadas que contengan clioquinol (p. ej., clioquinol + corticoesteroide) registradas en INVIMA o en proceso de registro bajo otro INN
- Evaluar la posibilidad de realizar un estudio clínico moderno (fase 2 observacional o retrospectivo) que actualice la evidencia en candidiasis cutánea
- Establecer criterios de exclusión explícitos: pacientes con antecedentes neurológicos, aplicación en áreas extensas, uso superior a 4 semanas, o riesgo de absorción sistémica aumentada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

