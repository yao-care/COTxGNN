---
layout: default
title: Leuprolide
parent: Solo Predicción del Modelo (L5)
nav_order: 393
evidence_level: L5
indication_count: 2
---

# Leuprolide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Leuprolida: De Leuprorelina Acetato a Osteoartritis

## Resumen en Una Frase

Leuprolida (leuprorelina) es un agonista de la hormona liberadora de gonadotropinas (GnRH), registrado en Colombia como leuprorelina acetato en las presentaciones Eligard. Según la información farmacológica compilada, se usa en cáncer de próstata avanzado, miomas uterinos, endometriosis y pubertad precoz.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero con **0 ensayos clínicos** y **1 publicación** (un reporte de caso sin relación directa con la indicación), por lo que la evidencia es solo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leuprorelina acetato (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la leuprolida es un agonista del receptor GnRH1 (gen GNRHR). Tras una estimulación inicial, desensibiliza la hipófisis y suprime la producción de hormonas sexuales (testosterona y estrógenos).

Una relación con la osteoartritis es concebible, ya que las hormonas sexuales modulan el metabolismo del cartílago y del hueso subcondral. Sin embargo, esta vinculación es especulativa. La privación de hormonas sexuales se asocia en general con pérdida ósea y efectos musculoesqueléticos adversos, lo que apunta en contra de un beneficio.

El alto puntaje de TxGNN (0.997) es únicamente una predicción computacional, sin datos clínicos que la respalden. Además, la ausencia de datos documentados del mecanismo de acción impide anclar el razonamiento a un perfil de dianas definido.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Reporte de caso | Clinical Breast Cancer | Adenocarcinoma prostático metastásico que simulaba un carcinoma inflamatorio de mama en un hombre de 78 años. No aborda la osteoartritis. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19956218 (cancelado) | ELIGARD® 22.5 MG | Polvo liofilizado para reconstituir a solución inyectable | Leuprorelina acetato |
| 20032905 (cancelado) | ELIGARD® 45 MG | Polvo estéril para reconstituir a suspensión inyectable | Leuprorelina acetato |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (agonista de GnRH), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación según el grafo de conocimiento (no proviene del prospecto):** hipertensión, hiperglucemia, diabetes mellitus, cetoacidosis diabética, obesidad (incluida la monogénica), accidente cerebrovascular y trastornos cerebrovasculares, infarto cerebral, infarto de miocardio, trombosis coronaria, hemoglobinopatías y obstrucción de las vías urinarias.
- **Interacciones farmacológicas:** la consulta no identificó interacciones con otros fármacos; solo se registró la farmacología de la diana (receptor GnRH1).

Consultar el prospecto para información de advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para osteoartritis se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura pertinente. Además, el mecanismo de supresión hormonal sugiere posibles efectos adversos óseos, y actualmente no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto del INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura y estudios preclínicos sobre GnRH y metabolismo del cartílago y hueso.
- Evaluar el riesgo óseo y cardiometabólico de la supresión hormonal en pacientes con osteoartritis.
- Aclarar la situación regulatoria, dado que los registros están cancelados.
- Revisar la segunda predicción (pseudoacondroplasia, 99.69%), que tampoco cuenta con ensayos ni literatura y es igualmente especulativa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

