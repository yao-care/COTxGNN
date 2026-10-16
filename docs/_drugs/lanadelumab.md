---
layout: default
title: Lanadelumab
parent: Evidencia Alta (L1-L2)
nav_order: 377
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Lanadelumab: nueva indicación predicha, Deficiencia de inhibidor de C1 (nivel de evidencia L1). Indicación original: Lanadelumab"
---

# Lanadelumab
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Lanadelumab: De Lanadelumab (indicación no detallada en el registro) a Deficiencia de Inhibidor de C1

## Resumen en Una Frase

Lanadelumab es un anticuerpo monoclonal humano que inhibe la calicreína plasmática. En el registro sanitario colombiano figura solo con su nombre genérico, sin texto de indicación detallado.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de inhibidor de C1** (angioedema hereditario, AEH), con **5 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
Cabe aclarar que esta predicción coincide con la indicación ya establecida del fármaco (profilaxis del AEH), por lo que no es un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lanadelumab (el registro INVIMA solo repite el nombre del fármaco; no describe la indicación) |
| Nueva Indicación Predicha | Deficiencia de inhibidor de C1 |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Lanadelumab es un anticuerpo monoclonal completamente humano dirigido contra la calicreína plasmática (gen KLKB1). Los datos compilados no incluyen una descripción formal del mecanismo de acción, pero la literatura y la información farmacológica disponibles describen de forma consistente este mecanismo.

En la deficiencia de inhibidor de C1 (mutaciones en SERPING1), la calicreína plasmática pierde su freno natural. Esto genera un exceso de bradicinina, un vasodilatador que provoca los episodios de angioedema. Al inhibir directamente la calicreína, lanadelumab actúa sobre el origen de la cascada.

Esta indicación corresponde al uso establecido del fármaco: la FDA y la EMA lo aprobaron en 2018 para prevenir ataques de AEH tipos I y II en pacientes de 12 años o más. La ausencia de datos de mecanismo y el estado "solo cancelado" en Colombia podrían deberse a limitaciones en la calidad de los datos y conviene verificarlos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Fase 3 | Completado | 20 | Estudio abierto multicéntrico de seguridad, farmacocinética y eficacia en pacientes chinos con AEH (26 semanas de tratamiento) |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Fase 3 | Completado | 21 | Estudio SPRING: seguridad, farmacocinética y farmacodinamia en niños de 2 a <12 años con AEH |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Fase 3 | Completado | 12 | Eficacia y seguridad en pacientes japoneses con AEH tipo I o II |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | Activo, sin reclutamiento | 155 | Encuesta posterior a la comercialización en Japón sobre efectos adversos y mejoría de síntomas con uso prolongado |
| [NCT04583007](https://clinicaltrials.gov/study/NCT04583007) | N/A | Ya no disponible | N/A | Programa de acceso expandido para prevención de ataques en niños de 2 a <12 años y en angioedema no histaminérgico con C1-INH normal; no aporta evidencia de eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | ECA | JAMA | Ensayo aleatorizado (HELP) de lanadelumab frente a placebo en la prevención de ataques de AEH |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Extensión abierta | Allergy | Estudio HELP OLE: efectividad y seguridad a largo plazo en pacientes ≥12 años con AEH tipo 1/2 |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Metaanálisis en red | Drugs in R&D | Comparación indirecta de terapias de profilaxis a largo plazo en AEH |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Revisión sistemática | Clin Rev Allergy Immunol | Ataques en pacientes que reciben profilaxis a largo plazo |
| [40504359](https://pubmed.ncbi.nlm.nih.gov/40504359/) | 2025 | Cohorte | Adv Ther | Estudio EMPOWER: efectividad y seguridad en la práctica real hasta 36 meses |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Comparación indirecta | J Comp Eff Res | Lanadelumab frente a inhibidor de C1 en pacientes pediátricos con AEH |
| [31560114](https://pubmed.ncbi.nlm.nih.gov/31560114/) | 2019 | Revisión | Drugs | Revisión de lanadelumab en AEH; reducción significativa de ataques frente a placebo en el ensayo HELP |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Revisión | Drugs | Primera aprobación global; anticuerpo que inhibe la calicreína plasmática |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Reporte de caso | J Allergy Clin Immunol Pract | Eficacia de lanadelumab en angioedema adquirido con deficiencia de inhibidor de C1 |
| [39399485](https://pubmed.ncbi.nlm.nih.gov/39399485/) | 2024 | Reporte de caso | Front Immunol | Uso en paciente trasplantado renal con AEH y alto riesgo cardiovascular |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20154566 (cancelado) | TAKHZYRO® (Takeda Colombia S.A.S) | Solución inyectable | Lanadelumab |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó y devolvió un único registro, de naturaleza farmacológica y no de interacción con otro medicamento. Se trata de su blanco terapéutico, la calicreína plasmática (KLKB1), que lanadelumab inhibe. No se identificaron interacciones con otros fármacos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen un ECA de referencia (HELP, JAMA 2018), tres ensayos de Fase 3 completados y abundante evidencia de práctica real que respaldan el uso en AEH. Sin embargo, el registro en Colombia está cancelado y faltan datos de seguridad del prospecto, por lo que se requieren salvaguardas.

**Para avanzar se necesita:**
- Aclarar el estado regulatorio: confirmar por qué el registro 20154566 figura cancelado y si existe otro registro vigente.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Confirmar el mecanismo de acción en DrugBank.
- Verificar que la indicación original del registro corresponda a la profilaxis del AEH.
- Plan de monitoreo de seguridad para poblaciones específicas (pediátrica, trasplantados).

**Otras predicciones del modelo:** las demás indicaciones (serpinopatía con polimerización tóxica de serpina, pancreatitis, enfermedad de von Willebrand tipo plaquetario, trastornos de función plaquetaria, miopatías inflamatorias, trombastenia de Glanzmann, síndrome de Scott) no tienen ensayos ni literatura, carecen de un vínculo mecanístico plausible y se clasifican como L5 con decisión **Hold**. Probablemente son artefactos del grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

