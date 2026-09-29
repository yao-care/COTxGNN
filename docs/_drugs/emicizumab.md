---
layout: default
title: Emicizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Emicizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Emicizumab: De Indicación Original No Especificada a Enfermedad de von Willebrand Tipo Plaquetario (Pseudo-von Willebrand)

## Resumen en Una Frase

Emicizumab es un anticuerpo biespecífico que imita al factor VIII activado y, según la literatura del paquete de evidencia, está aprobado para la hemofilia A congénita. El modelo TxGNN predice que podría ser efectivo para la **enfermedad pseudo-von Willebrand**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los datos (el registro sanitario solo repite el nombre "EMICIZUMAB") |
| Nueva Indicación Predicha | Enfermedad pseudo-von Willebrand |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, emicizumab actúa como sustituto del cofactor FVIIIa: une FIXa y FX en el complejo tenasa, sin depender del factor VIII. Por eso funciona incluso en presencia de inhibidores anti-FVIII.

La enfermedad pseudo-von Willebrand (von Willebrand tipo plaquetario) **no es un estado de deficiencia de FVIII**. Se caracteriza por una unión aumentada entre GPIb plaquetaria y el factor von Willebrand, con pérdida de multímeros grandes de VWF. Emicizumab no tiene un mecanismo establecido en este escenario, así que el vínculo mecanístico es débil.

El puntaje alto de TxGNN probablemente refleja una asociación en el grafo de conocimiento (trastornos hemorrágicos con vías de coagulación cercanas) y no una razón terapéutica sólida. Por eso el resultado debe leerse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Otras Indicaciones Predichas en el Paquete

Una de las otras nueve predicciones sí tiene evidencia real: el rango 5, **deficiencia adquirida de factores de coagulación**, con nivel L2 y decisión "Proceed with Guardrails".

| # | Indicación Predicha | Puntaje TxGNN | Nivel | Decisión |
|---|---------|------|------|------|
| 1 | Pseudo-von Willebrand | 99.99% | L5 | Hold |
| 2 | Trastorno primario de liberación plaquetaria | 99.99% | L5 | Hold |
| 3 | Trombastenia de Glanzmann | 99.98% | L4 | Hold |
| 4 | Síndrome de Scott | 99.92% | L5 | Hold |
| 5 | Deficiencia adquirida de factores de coagulación | 99.90% | L2 | Proceed with Guardrails |
| 6 | Diátesis hemorrágica por defecto del receptor de colágeno | 99.86% | L5 | Hold |
| 7 | Trastorno hemorrágico por trombocitopenia constitucional | 99.85% | L5 | Hold |
| 8 | Púrpura trombocitopénica trombótica | 99.61% | L5 | Hold |
| 9 | Trombocitopenia aloinmune fetal y neonatal | 99.52% | L5 | Hold |
| 10 | "Flood factor deficiency" (término ambiguo) | 99.41% | L5 | Hold |

**Sobre el rango 5:** la evidencia corresponde en realidad a la **hemofilia A adquirida (HAA)**, un subtipo de esa categoría. En la HAA, autoanticuerpos neutralizan el FVIII, y emicizumab actúa de forma independiente del FVIII. Los estudios principales son:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Fase 2, un solo brazo (GTH-AHA-EMI) | Lancet Haematol | Evalúa si emicizumab protege del sangrado en HAA y permite diferir la inmunosupresión durante las primeras 12 semanas |
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Fase 3, un solo brazo (AGEHA) | J Thromb Haemost | Primer estudio prospectivo de emicizumab en pacientes con HAA |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Fase 3, análisis final (AGEHA) | Thromb Haemost | Incluye pacientes con y sin inmunosupresión y datos de profilaxis a largo plazo |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Cohorte real multicéntrica | Blood Adv | 62 pacientes con HAA tratados fuera de indicación en 12 centros de hemofilia de EE. UU. |

Los estudios de fase 2 y 3 son de un solo brazo, no aleatorizados, por lo que no se cumple el nivel L1.

## Información de Mercado en Colombia

Los cinco registros de la muestra corresponden al mismo número de registro sanitario; se listan una sola vez. El paquete indica 20 registros en total.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20152900 | HEMLIBRA® 30 MG/ML SOLUCIÓN INYECTABLE (F. Hoffmann-La Roche) | Solución inyectable | Solo figura "EMICIZUMAB" (sin texto de indicación) |

## Consideraciones de Seguridad

No hay advertencias, contraindicaciones ni interacciones farmacológicas registradas en el paquete de evidencia. Consultar el prospecto para información de seguridad.

Se debe tener en cuenta que la microangiopatía trombótica y la trombosis son señales de seguridad conocidas de emicizumab, sobre todo con uso concomitante de aPCC o dosis altas de agentes de bypass. Esto es especialmente relevante en la púrpura trombocitopénica trombótica (rango 8), donde un agente procoagulante es en principio inadecuado.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- Para pseudo-von Willebrand no hay ensayos clínicos ni literatura, y el mecanismo de emicizumab no se relaciona con la fisiopatología (defecto GPIb-VWF, no deficiencia de FVIII). El puntaje de 99.99% no es suficiente por sí solo.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Consultar la API de DrugBank para obtener el mecanismo de acción.
- Aclarar la indicación aprobada registrada en INVIMA, que hoy solo dice "EMICIZUMAB".
- Priorizar la evaluación de la hemofilia A adquirida (rango 5) con guardrails: gestión del riesgo trombótico con aPCC, definición de la estrategia de inmunosupresión, y confirmación de que no se generaliza a otras deficiencias adquiridas (por ejemplo, VWF o FX).
- Verificar el mapeo ontológico del término "flood factor deficiency" antes de cualquier revisión.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

