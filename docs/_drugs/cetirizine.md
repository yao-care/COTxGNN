---
layout: default
title: Cetirizine
parent: Evidencia Alta (L1-L2)
nav_order: 120
evidence_level: L2
indication_count: 6
---

# Cetirizine
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **6** 
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

# Cetirizina: De Antihistamínico H1 (Rinitis Alérgica) a Urticaria Alérgica

## Resumen en Una Frase

La cetirizina es un antihistamínico H1 de segunda generación, usado para la rinitis alérgica, la urticaria crónica y el asma inducida por polen.
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**, con **3 ensayos clínicos** y **18 publicaciones** que respaldan esta dirección.
La urticaria ya es un uso establecido de los antihistamínicos, así que esta predicción confirma un uso conocido más que descubrir uno nuevo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No declarada en los registros (el texto del registro solo dice «CETIRIZINA»). Según la farmacología: rinitis alérgica, urticaria crónica y asma por polen |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en el campo original de la ficha. La información farmacológica disponible indica que la cetirizina es un agonista inverso selectivo del receptor de histamina H1 periférico (gen *HRH1*). En roedores, casi no penetra el cerebro ni se une a receptores H1 cerebrales, lo que explica su perfil poco sedante.

En la urticaria, la histamina liberada por los mastocitos causa el habón, el eritema y el prurito. Bloquear el receptor H1 ataca directamente ese mecanismo, y por eso el puntaje del modelo es tan alto.

Conviene aclarar dos cosas. El campo de indicaciones originales llegó vacío, lo cual es una brecha de datos y no evidencia de un uso nuevo. Además, el ensayo NCT02023164 figura como Fase 3, pero es un piloto de factibilidad con 36 pacientes. No se cuenta como un ECA de Fase 3 definitivo, y por eso el nivel es L2 y no L1.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Fase 3 (piloto) | Completado | 36 | Cetirizina IV 10 mg vs. difenhidramina IV 50 mg en urticaria aguda. Estudio piloto multicéntrico, doble ciego y aleatorizado, de factibilidad; la muestra pequeña limita las conclusiones de eficacia |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completado | 75 | Añadir un ciclo corto de corticoide al tratamiento con antihistamínicos H1 en urticaria. Evidencia indirecta: lo evaluado es el corticoide |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminado | 11 | Efecto de levocetirizina (enantiómero activo de la cetirizina) sobre mediadores inflamatorios de la piel en dermografismo y urticaria idiopática crónica. Estudio de mecanismo, muy pequeño |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41209777](https://pubmed.ncbi.nlm.nih.gov/41209777/) | 2025 | ECA abierto | Perspect Clin Res | Compara eficacia y tolerabilidad de cetirizina y bilastina, pero en rinitis alérgica, no en urticaria |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Revisión | Drugs | Propiedades farmacológicas y potencial clínico de la cetirizina en rinitis alérgica, asma por polen y urticaria crónica; sin efectos depresores del SNC a 10 mg/día |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Revisión | Allergy | Estudios clínicos con cetirizina en rinitis alérgica y urticaria crónica |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Revisión | Drugs | Reevaluación: eficaz y bien tolerada en rinitis alérgica y urticaria idiopática crónica en adultos |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Revisión | Ann Pharmacother | Eficacia y seguridad de antihistamínicos de primera y nueva generación en rinitis alérgica y urticaria idiopática crónica |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Revisión | Drugs | Reconocimiento, causas y tratamiento de la urticaria; los antihistamínicos no sedantes son la base del tratamiento en la urticaria idiopática crónica |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Revisión | Allergy Asthma Proc | Levocetirizina (R-enantiómero de la cetirizina) en rinitis alérgica y urticaria idiopática crónica |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Revisión | Clin Ther | Levocetirizina en rinitis alérgica y urticaria idiopática crónica en adultos y niños |
| [35593100](https://pubmed.ncbi.nlm.nih.gov/35593100/) | 2022 | Revisión sistemática y metaanálisis de ECA | Am J Rhinol Allergy | Bilastina en rinitis alérgica y urticaria crónica; evidencia de otro antihistamínico, indirecta para la cetirizina |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Reporte de caso | Cureus | Prurito y urticaria de rebote tras suspender el uso crónico de cetirizina |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20149297 | CETISWISS | Cápsula blanda | CETIRIZINA |
| 20152795 | PARAGRIP CAPSULAS | Cápsula dura | Preparaciones de otras combinaciones para el resfriado común |

Los datos entregados muestran solo 2 registros únicos (con filas repetidas), aunque el total declarado es 20.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones fármaco-fármaco registradas. La consulta solo devolvió la relación farmacológica con su diana, el receptor H1.
- **Rebote al suspender**: un reporte de caso de 2025 describe prurito y urticaria de rebote tras suspender el uso crónico de cetirizina.
- **Advertencias y contraindicaciones**: consultar el prospecto de INVIMA, porque no hay datos disponibles.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo completado (piloto de Fase 3) y múltiples revisiones que respaldan el uso de la cetirizina en urticaria, con un mecanismo claro (bloqueo H1). Sin embargo, no hay ECA de Fase 3 definitivos, y esta predicción es en gran parte la confirmación de un uso ya conocido.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que bloquea el cribado de seguridad
- Completar el mecanismo de acción desde DrugBank
- Verificar en el registro de ClinicalTrials.gov si hay ECA de cetirizina en urticaria que hayan quedado fuera de esta búsqueda
- Definir un plan de seguimiento para el prurito de rebote tras suspender el tratamiento

Otras predicciones del modelo: urticaria por frío (L2, Proceed with Guardrails), enfermedad de la cavidad nasal (L4, pregunta de investigación), y laringofaringitis aguda, conjuntivitis por rosácea y dermatitis atópica recalcitrante (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

