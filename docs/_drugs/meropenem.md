---
layout: default
title: Meropenem
parent: Evidencia Moderada (L3-L4)
nav_order: 276
evidence_level: L4
indication_count: 10
---

# Meropenem
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Meropenem: De Antibacteriano Carbapenémico a Artritis Bacteriana

## Resumen en Una Frase

Meropenem es un antibiótico carbapenémico de amplio espectro que se usa por vía inyectable en infecciones bacterianas graves. En el registro sanitario colombiano, el texto de indicación aprobada solo dice "MEROPENEM", sin detalle.
El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana**, pero la evidencia directa es escasa: **1 ensayo clínico** (sin relación con meropenem) y **20 publicaciones**, en su mayoría revisiones, reportes de caso y estudios microbiológicos o farmacocinéticos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro solo indica "MEROPENEM", sin indicación específica descrita |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 3 (las tres entradas corresponden al mismo número, 20159905) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados de mecanismo de acción en DrugBank para este registro. Por su clase, meropenem se une a las proteínas fijadoras de penicilina (PBP) y bloquea la síntesis de la pared celular bacteriana, lo que produce la muerte de la bacteria. Su cobertura incluye bacilos Gram-negativos (también resistentes), cocos Gram-positivos y anaerobios.

Las infecciones de huesos y articulaciones pueden ser causadas por estos mismos grupos de bacterias, en particular Gram-negativos resistentes y *Burkholderia pseudomallei* (melioidosis). Por eso la predicción es biológicamente plausible. La literatura recuperada incluye series de melioidosis osteoarticular en las que los aislados fueron sensibles a meropenem, y un reporte de artritis séptica por *Klebsiella pneumoniae* productora de BLEE tratada con meropenem más amikacina y lavado artroscópico.

Conviene ser prudente: el puntaje de TxGNN es una predicción de grafos, no evidencia clínica. Ningún estudio recuperado compara meropenem con otros tratamientos en artritis bacteriana.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Fase 3 | Completado | 624 | Levofloxacino para prevenir bacteriemia en niños con leucemia aguda o trasplante de células madre. No incluye meropenem ni estudia artritis, por lo que no aporta respaldo directo. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Cohorte retrospectiva | Le infezioni in medicina | Caracterización de pacientes con melioidosis osteoarticular, una enfermedad poco reconocida. |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Revisión retrospectiva de casos | Indian J Med Microbiol | 22 casos de melioidosis musculoesquelética (9 con artritis séptica); todos los aislados fueron sensibles a meropenem. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión | Int J Antimicrob Agents | Uso fuera de indicación frente a recomendaciones formales de antibióticos en infecciones por bacterias multirresistentes. |
| [36678359](https://pubmed.ncbi.nlm.nih.gov/36678359/) | 2022 | Revisión | Pathogens | Opciones terapéuticas para melioidosis: antibióticos frente a terapia con fagos. |
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Reporte de caso | Joint Bone Spine | Dos pacientes inmunocomprometidos con artritis séptica por *K. pneumoniae* productora de BLEE, tratados con éxito con meropenem, amikacina y lavado artroscópico. |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Reporte de caso | J Med Case Rep | Melioidosis diseminada con artritis séptica, mal diagnosticada inicialmente como tuberculosis u otra infección bacteriana. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Estudio observacional/microbiológico | Clin Lab | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en menores de cuatro años. |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Estudio observacional/microbiológico | Eur J Orthop Surg Traumatol | Antibiograma para guiar la terapia empírica en infecciones ortopédicas no espinales, incluida la artritis séptica. |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | Estudio preclínico in vitro | J Bone Joint Surg Am | Estabilidad térmica y liberación in vitro de meropenem y otros antibióticos desde cemento óseo PMMA. |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | Farmacocinética poblacional | Clin Pharmacokinet | Farmacocinética de meropenem a lo largo de la vida adulta y regímenes de dosificación óptimos. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20159905 | MEROPENEM 0.5 G | Polvo estéril para reconstituir a solución inyectable | MEROPENEM (sin texto de indicación específico) |

*Nota: el registro lista tres entradas idénticas con el mismo número sanitario (fabricante: Vicarfarmacéutica S.A.); se muestran una sola vez.*

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es alto (99.92%) y el mecanismo es plausible. Sin embargo, la evidencia disponible es de nivel L4: el único ensayo Fase 3 no involucra meropenem, y la literatura se limita a revisiones, reportes de caso, datos de sensibilidad y estudios farmacocinéticos o preclínicos. Además, meropenem ya está disponible como opción de reserva para infecciones resistentes, por lo que no hay una señal clara de valor adicional.

**Para avanzar se necesita:**
- Estudios comparativos (idealmente ECA) o cohortes con meropenem en artritis séptica y osteoarticular, en especial para Gram-negativos resistentes y melioidosis.
- Obtener del INVIMA el prospecto con advertencias y contraindicaciones, para poder hacer el tamizaje de seguridad.
- Datos detallados del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada real del registro 20159905, que solo aparece como "MEROPENEM".
- Criterios de uso racional (estrategia de carbapenémicos, uso reservado a patógenos resistentes).

*Nota adicional:* entre las otras indicaciones predichas, **infección del tracto urinario** muestra el respaldo más fuerte (varios ensayos Fase 3 con meropenem probablemente como comparador). Antes de darlo por válido, hay que verificar en el registro de cada ensayo que meropenem fue efectivamente uno de los brazos.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

