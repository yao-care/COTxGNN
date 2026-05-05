---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 2
---

# Interferon Beta-1B
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

La habilidad `txgnn-pipeline` confirma el contexto del proyecto. Ahora procedo a generar el informe de evaluación basándome en el Evidence Pack proporcionado.

---

# Interferón Beta-1b: De Esclerosis Múltiple a Leucemia de Células Pilosas

## Resumen en Una Frase

Interferón Beta-1b (Betaseron®/Betaferon®) es un agente inmunomodulador biológico de la familia de los Interferones Tipo I, reconocido internacionalmente por su uso en el tratamiento de la Esclerosis Múltiple Remitente-Recurrente, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para la **Leucemia de Células Pilosas (Hairy Cell Leukemia)**, con **0 ensayos clínicos registrados** y **4 publicaciones científicas** que respaldan actualmente esta dirección.
La plausibilidad de la predicción descansa en la similitud mecanística con el Interferón Alfa, el cual ya es un tratamiento reconocido para esta enfermedad hematológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esclerosis Múltiple Remitente-Recurrente (reconocida internacionalmente; sin registro en Colombia) |
| Nueva Indicación Predicha | Leucemia de Células Pilosas (Hairy Cell Leukemia) |
| Puntaje de Predicción TxGNN | 99.16% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Interferón Beta-1b pertenece a la familia de los **Interferones Tipo I**, junto con el Interferón Alfa. Ambos ejercen sus efectos biológicos uniéndose a los mismos receptores de superficie celular (IFNAR1/IFNAR2), activando la cascada de señalización JAK1-TYK2→STAT1/STAT2 e induciendo la expresión de genes estimulados por interferón (ISGs). Estos ISGs median efectos antiproliferativos, inmunomoduladores y proapoptóticos que son relevantes en contextos neoplásicos.

El Interferón Alfa ya cuenta con evidencia clínica establecida en el tratamiento de la Leucemia de Células Pilosas, siendo históricamente uno de los pilares terapéuticos de esta enfermedad hematológica infrecuente. Dado que el IFN-β comparte el mismo receptor de membrana que el IFN-α, la racionalidad mecanística para esta indicación es biológicamente plausible. Sin embargo, existen diferencias importantes en afinidad receptorial y distribución tisular entre ambas isoformas que podrían traducirse en diferencias de eficacia clínica, aspecto que no ha sido evaluado en estudios cabeza a cabeza modernos.

La literatura de finales de los años ochenta documenta respuestas hematológicas en pacientes con Leucemia de Células Pilosas tratados con beta-serina-interferón (una forma de IFN-β recombinante), incluyendo normalización de recuentos sanguíneos periféricos en la mayoría de los casos evaluables. Estos reportes tempranos respaldan la señal biológica, aunque su nivel de evidencia es limitado por diseño y tamaño muestral.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Interferón Beta-1b en Leucemia de Células Pilosas.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|---------|
| [2736487](https://pubmed.ncbi.nlm.nih.gov/2736487/) | 1989 | Estudio Comparativo Prospectivo | Cancer | 10 pacientes con LCH tratados con rIFN-β-ser (90 MU SC, 3×/semana); 8 evaluables: 63% normalizó recuentos periféricos y 25% mostró mejora parcial; células pilosas persistentes en médula ósea de todos los respondedores |
| [2082943](https://pubmed.ncbi.nlm.nih.gov/2082943/) | 1990 | Serie de Casos | American Journal of Hematology | 12 pacientes con LCH (10 con terapia previa) tratados con beta-ser interferón IV (90 MU, 3×/semana); médula ósea con 90-100% de células pilosas al inicio |
| [3312839](https://pubmed.ncbi.nlm.nih.gov/3312839/) | 1987 | Reporte de Experiencia Retrospectiva | Leukemia | Experiencia UCLA con 51 pacientes en ensayos de interferón en LCH: mejora hematológica en 71% con rIFN-β-ser, 96% con rIFN-α-2b y 69% con IFN-α-N1 linfoblastoide |
| [2198792](https://pubmed.ncbi.nlm.nih.gov/2198792/) | 1990 | Reporte de Caso | American Journal of Clinical Oncology | 3 pacientes con fallo a IFN-α o IFN-β tratados con 2'-desoxicoformicina (DCF, 4 mg/m²): 100% respuesta completa sostenida (9+, 14+ y 15+ meses); DCF como rescate eficaz tras fallo de IFN-β |

---

## Información de Mercado en Colombia

Interferón Beta-1b no cuenta con registros sanitarios activos ante el INVIMA. El medicamento no se encuentra comercializado en el mercado colombiano. Para su uso en el país sería necesario gestionar importación bajo mecanismo de uso no incluido en registro sanitario (uso compasivo) o a través del trámite correspondiente de registro sanitario.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia disponible para esta indicación son 4 publicaciones de los años 1987–1990 (series de casos y reportes retrospectivos de nivel L3), sin ningún ensayo clínico registrado. Aunque la plausibilidad mecanística es sólida y existe precedente histórico de actividad biológica, la ausencia de datos prospectivos controlados modernos y el hecho de que el medicamento no esté comercializado en Colombia hacen que la evidencia sea insuficiente para recomendar avanzar sin investigación adicional.

**Para avanzar se necesita:**
- Diseñar y registrar un ensayo clínico prospectivo (mínimo Fase 2) que evalúe IFN-β-1b en Leucemia de Células Pilosas con criterios de respuesta estandarizados
- Obtener datos farmacológicos detallados (MOA, PK/PD) de IFN-β-1b en modelos hematológicos comparados con IFN-α
- Realizar una comparación directa (head-to-head) con IFN-α, actual estándar de tratamiento en LCH de segunda línea
- Evaluar la viabilidad regulatoria para importación o uso compasivo en Colombia ante el INVIMA
- Establecer un plan de monitoreo de seguridad específico para la población hematológica objetivo, incluyendo citopenias basales propias de la enfermedad
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

