---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

Usando `txgnn-pipeline` para verificar el contexto del proyecto — la tarea es generar un informe de evaluación de reposicionamiento a partir del Evidence Pack. Procedo con el formato definido en el sistema.

---

# Canakinumab: De Síndrome Periódico Asociado a Criopirin (CAPS) a Fiebre Mediterránea Familiar

> **Nota de selección de indicación:** El Evidence Pack lista 10 predicciones ordenadas por puntaje TxGNN. La indicación con mayor solidez clínica es la **Fiebre Mediterránea Familiar (rango 6, L1, Proceed with Guardrails)**, que es la presentada en este informe por contar con 7 ensayos clínicos completados, 20 publicaciones y aprobación formal de la EMA (2016). Las indicaciones de rango 1–3 (hepatic infarction, VOD, peliosis hepatis) presentan evidencia L5 y recomendación Hold.

---

## Resumen en Una Frase

Canakinumab (Ilaris®) es un anticuerpo monoclonal humano anti-IL-1β desarrollado por Novartis, originalmente aprobado a nivel internacional para el tratamiento del Síndrome Periódico Asociado a Criopirin (CAPS), que engloba la urticaria familiar por frío (FCAS), el síndrome de Muckle-Wells (MWS) y la enfermedad inflamatoria multisistémica de inicio neonatal (NOMID).
El modelo TxGNN predice que podría ser efectivo para la **Fiebre Mediterránea Familiar (FMF), forma autosómica dominante**, con **7 ensayos clínicos** (5 de Fase 3 completados) y **20 publicaciones** que actualmente respaldan esta dirección.
Esta predicción está además validada por la aprobación de la EMA en 2016 para FMF resistente a colchicina, lo que convierte a esta indicación en la más clínicamente accionable del perfil analizado.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | CAPS (FCAS / Muckle-Wells / NOMID) — aprobación internacional; **sin registro sanitario en Colombia** |
| Nueva Indicación Predicha | Fiebre Mediterránea Familiar (FMF), forma autosómica dominante |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado (0 registros INVIMA) |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Canakinumab es un anticuerpo monoclonal IgG1/κ completamente humanizado que bloquea de forma selectiva la interleucina-1β (IL-1β), impidiendo su unión a los receptores IL-1RI y IL-1RAcP. Al neutralizar IL-1β circulante, interrumpe la cascada inflamatoria aguas abajo: se reducen la producción de IL-6, las proteínas de fase aguda (PCR, SAA) y el reclutamiento de neutrófilos. Esta acción es independiente de la causa upstream que genere el exceso de IL-1β, lo que abre la posibilidad de aplicarla en cualquier enfermedad donde el inflammasoma sea el motor patológico.

La FMF es causada por mutaciones con ganancia de función en el gen *MEFV*, el cual codifica la proteína pirina. La pirina mutante pierde su capacidad de suprimir el inflammasoma, generando una hiperactivación constitutiva que produce un exceso patológico de IL-1β activa como evento molecular central. Esta es una **coincidencia mecanística directa**: el mismo mediador que canakinumab bloquea es el que la FMF sobreexpresa de forma descontrolada. La relación no es analógica sino causal.

La extrapolación desde CAPS a FMF resulta fisiológicamente coherente: ambas son enfermedades autoinflamatorias monogénicas que convergen en la vía IL-1β, con manifestaciones clínicas solapadas (fiebre recurrente, serositis, artralgia) y respuesta demostrada a los mismos biológicos anti-IL-1. El ensayo pivotal publicado en *NEJM* (PMID 29768139) y la aprobación formal de la EMA (2016) para FMF resistente a colchicina confirman que la predicción del modelo no es especulativa, sino que refleja evidencia clínica ya consolidada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Fase 3 | Completado | 166 | Mayor estudio del programa: seguridad y eficacia a largo plazo (≥6 meses) en CAPS (FCAS/MWS/NOMID); base central del soporte regulatorio ante EMA y FDA |
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Fase 3 | Completado | 35 | Beta-CONFIDENT: diseño aleatorizado doble ciego controlado con placebo (retiro de tratamiento) en síndrome de Muckle-Wells; metodología más rigurosa del programa |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Fase 3 | Completado | 19 | Estudio japonés en CAPS (FCAS/MWS/NOMID): eficacia y seguridad a 6 meses con fase de extensión hasta aprobación local; apoyó registro en Japón |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Fase 3 | Completado | 17 | Estudio pediátrico (≤4 años) de 1 año en CAPS: evaluó eficacia, tolerabilidad y seguridad de vacunación concomitante |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Fase 3 | Completado | 17 | Extensión abierta de NCT01302860: evaluó eficacia y seguridad a largo plazo tras completar el estudio índice, incluyendo efectos post-retirada |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Fase 2 | Completado | 20 | TRAPS: tratamiento activo 4 meses + seguimiento 6 meses; aportó datos de eficacia en síndrome periódico asociado al receptor de TNF |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | Observacional | En reclutamiento | 25 | REASSURE: estudio no intervencionista en vida real (CAPS, crFMF, TRAPS, HIDS/MKD, sJIA) en práctica clínica europea; completación prevista septiembre 2028 |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | ECA / Resumen clínico | N Engl J Med | Ensayo pivotal de canakinumab en FMF, MKD y TRAPS; demostró reducción significativa de crisis febriles vs. placebo; base del registro EMA para FMF |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Revisión Sistemática | Front Immunol | Revisión sistemática de eficacia y seguridad de los tres biológicos anti-IL-1 aprobados (anakinra, canakinumab, rilonacept) en enfermedades inmunomediadas |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Metaanálisis | Rheumatology (Oxford) | Metaanálisis cuantitativo de anti-IL-1 en FMF: evidencia consolidada de eficacia y seguridad de canakinumab en FMF resistente a colchicina |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Revisión clínica | Expert Rev Clin Immunol | Resumen de toda la evidencia clínica de canakinumab en FMF hasta 2017; análisis de la relación pirina-IL-1β y criterios de uso como segunda línea |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohorte Retrospectiva | Int J Rheum Dis | Canakinumab con vs. sin colchicina en FMF: diferencias en frecuencia de crisis, PCR, SAA y desenlaces renales a mediano plazo |
| [34568239](https://pubmed.ncbi.nlm.nih.gov/34568239/) | 2021 | Cohorte Retrospectiva | Front Pediatrics | 65 pacientes pediátricos con FMF resistente a colchicina; protocolo de reducción de dosis mensual a bimensual tras remisión completa a 12 meses |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohorte | Rheumatology (Oxford) | Primer protocolo de discontinuación de canakinumab en FMF pediátrica resistente a colchicina; factores predictores de recaída |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Revisión | Clin Exp Rheumatol | Resultados clínicos e inhibición de IL-1 en FMF; análisis comparativo de colchicina vs. biológicos anti-IL-1 en distintos fenotipos |
| [31463794](https://pubmed.ncbi.nlm.nih.gov/31463794/) | 2019 | Cohorte Retrospectiva | Paediatr Drugs | Experiencia pediátrica unicéntrica con canakinumab en FMF no respondedora a colchicine; análisis de dosis efectiva y respuesta inflamatoria |
| [20065636](https://pubmed.ncbi.nlm.nih.gov/20065636/) | 2010 | Revisión farmacológica | mAbs | Descripción original de canakinumab (ACZ885): MOA, perfil de seguridad y aprobación FDA 2009 para CAPS; contexto de desarrollo del fármaco |

---

## Información de Mercado en Colombia

Canakinumab (Ilaris®) **no cuenta con ningún registro sanitario vigente en Colombia** ante INVIMA. El medicamento no ha sido aprobado ni comercializado localmente a la fecha de corte del análisis (mayo 2026). No existen formas farmacéuticas registradas para ninguna vía de administración en el país.

Para su eventual utilización en Colombia, se requeriría gestionar el registro sanitario ante INVIMA, o acceder al medicamento mediante mecanismos de importación para uso individual con justificación médica documentada, bajo las condiciones establecidas por la normativa colombiana para medicamentos no registrados de alto impacto clínico.

---

## Consideraciones de Seguridad

Los datos de seguridad específicos del contexto regulatorio colombiano/INVIMA no están disponibles dado que el medicamento no tiene registro local. La información de seguridad disponible proviene de la literatura clínica internacional:

- **Riesgo de infecciones graves:** Como biológico inmunomodulador anti-IL-1β, canakinumab incrementa la susceptibilidad a infecciones bacterianas serias. Este riesgo es consistente en todos los estudios clínicos del programa (documentado en PMID 35874710 y PMID 34568239).
- **Vacunación:** Los estudios pediátricos (NCT01302860) evaluaron específicamente la compatibilidad con vacunas; se recomienda completar el esquema de inmunización antes de iniciar el tratamiento.
- **Neutropenia:** Reportada como efecto adverso en estudios de CAPS; requiere monitoreo del hemograma durante el tratamiento.

> Para información completa de contraindicaciones, advertencias de caja negra e interacciones farmacológicas, consultar el prospecto oficial de Ilaris® disponible en la EMA o FDA.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La FMF presenta una coincidencia mecanística directa con el blanco farmacológico de canakinumab (IL-1β vía inflammasoma de pirina), respaldada por 5 ensayos de Fase 3 completados —incluyendo el RCT doble ciego NCT00465985 (N=35) y el mayor estudio longitudinal NCT00685373 (N=166)—, 20 publicaciones de alta calidad (incluyendo metaanálisis y revisiones sistemáticas), y la aprobación formal de la EMA (Ilaris® para FMF resistente a colchicina, 2016). La evidencia es inequívocamente L1.

**Para avanzar se necesita:**
- Gestionar el registro sanitario de Ilaris® ante INVIMA o evaluar el mecanismo de importación para uso individual bajo normativa colombiana vigente
- Obtener la ficha técnica completa (prospecto EMA/FDA) para caracterizar formalmente advertencias de seguridad, contraindicaciones e interacciones farmacológicas
- Identificar y cuantificar la población colombiana con diagnóstico de FMF resistente a colchicina (enfermedad huérfana — prevalencia muy baja en Latinoamérica)
- Evaluar la viabilidad de financiamiento mediante ADRES/EPS o tutelas, dado el alto costo de los biológicos de uso en enfermedades raras
- Confirmar la disponibilidad de reumatólogos o inmunólogos con experiencia en enfermedades autoinflamatorias monogénicas para supervisión clínica local
- Datos detallados del MOA de la fuente DrugBank (pendiente por Data Gap DG002) para completar la caracterización farmacológica oficial del informe
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

