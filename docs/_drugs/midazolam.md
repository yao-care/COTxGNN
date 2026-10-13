---
layout: default
title: Midazolam
parent: Evidencia Moderada (L3-L4)
nav_order: 442
evidence_level: L3
indication_count: 1
---

# Midazolam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

# Midazolam: De Midazolam (indicación no especificada en el registro) a Insomnio

## Resumen en Una Frase

Midazolam es una benzodiazepina de acción corta; en Colombia sus registros sanitarios solo mencionan "Midazolam" como indicación, sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, con **2 ensayos clínicos** (de relevancia indirecta) y **10 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Midazolam (el registro no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico de la clase, el midazolam es una benzodiazepina de acción corta que actúa como modulador alostérico positivo de los receptores GABA-A, potenciando la neurotransmisión inhibitoria y produciendo efectos sedantes e hipnóticos.

Este mecanismo es compartido con benzodiazepinas hipnóticas ya aprobadas (por ejemplo, flurazepam y triazolam), por lo que el vínculo biológico con el insomnio es plausible y coherente con el alto puntaje de TxGNN. Esta relación se infiere de la farmacología de la clase, no de datos directos del registro.

Además, el midazolam por vía oral fue estudiado y usado históricamente como hipnótico en varios países. Por ello, esta predicción se parece más a un "redescubrimiento" de un uso ya estudiado que a un reposicionamiento verdaderamente novedoso.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Completado | 111 | Compara la calidad del sueño posoperatorio con dexmedetomidina vs. midazolam en resección transuretral de próstata. Contexto de sedación perioperatoria; el midazolam es comparador (evidencia indirecta). |
| [NCT00886314](https://clinicaltrials.gov/study/NCT00886314) | N/A | Desconocido | 80 | Médicos payaso vs. premedicación sedante (midazolam) para la ansiedad de niños en cirugía. El desenlace es ansiedad, no sueño; relevancia mínima. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | ECA | J Clin Psychopharmacol | Estudio multicéntrico, doble ciego, de 14 días en insomnes crónicos: compara sueño, desempeño y estado de ánimo con flurazepam y midazolam. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | ECA | J Clin Psychopharmacol | Resumen ejecutivo del estudio multicéntrico de flurazepam vs. midazolam en insomnio crónico (sin resumen disponible). |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | ECA | Arzneimittel-Forschung | Estudio piloto de búsqueda de dosis (10–30 mg orales) en 75 pacientes hospitalizados con insomnio leve a moderado. |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | Estudio clínico | Br J Clin Pharmacol | Doble ciego en 30 mujeres con insomnio secundario a enfermedad neuromuscular: midazolam 15 mg fue un hipnótico eficaz, mejor tolerado que Vesparax y sin somnolencia residual. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Revisión del uso clínico de hipnóticos y de la necesidad de variedad de benzodiazepinas con distintos perfiles farmacocinéticos. |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Revisión | Orvosi Hetilap | Revisión sobre insomnio e hipoperfusión cerebral (relevancia general, no específica de midazolam). |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20198997 | RELACUM® SOLUCIÓN INYECTABLE | Solución inyectable | Midazolam (estado: cancelado) |
| 20209565 | SERRACLINICS | Solución inyectable | Midazolam (estado: cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): enfermedad pulmonar obstructiva crónica (incluida la de inicio temprano grave), cirrosis hepática, glaucoma de ángulo cerrado, enfermedad renal crónica, insuficiencia renal crónica e insuficiencia renal terminal.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las principales de nivel moderado figuran morfina, claritromicina, aprepitant, bupropión, cimetidina, ranitidina, omeprazol, metoclopramida, miconazol, clotrimazol, dronabinol, nabilona, eluxadolina, teduglutida y fenilbutirato de glicerol. De nivel menor: dexametasona, betametasona, óxido de magnesio, hidróxido de aluminio y carbonato de calcio. Cabe destacar los depresores del SNC, los opioides y los inhibidores de CYP3A4.

No se dispone de advertencias del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe plausibilidad mecanística y estudios históricos de midazolam oral en insomnio, pero la evidencia es antigua, los ensayos clínicos registrados son solo indirectos, y los dos registros sanitarios en Colombia están cancelados. Además, falta la información de seguridad del prospecto, lo que impide el tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante.
- Confirmar el mecanismo de acción mediante DrugBank.
- Definir la viabilidad regulatoria y comercial, dado que no hay registros vigentes y no se dispone de una forma oral aprobada.
- Evaluar alternativas ya aprobadas para insomnio, dado el perfil de interacciones y las contraindicaciones.
- Revisar evidencia más reciente que compare midazolam oral con hipnóticos actuales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

