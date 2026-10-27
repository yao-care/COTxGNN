---
layout: default
title: Capecitabine
parent: Evidencia Alta (L1-L2)
nav_order: 132
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Capecitabine: nueva indicación predicha, Adenocarcinoma gástrico tubular (nivel de evidencia L1). Indicación original: CAPECITABINA"
---

# Capecitabine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Capecitabina: De Capecitabina (indicación registrada sin detalle) a Adenocarcinoma Gástrico Tubular
{: .text-alpha }

## Resumen en Una Frase

Capecitabina es un profármaco oral del 5-fluorouracilo (5-FU), registrado en Colombia bajo el texto genérico "CAPECITABINA", sin que el registro especifique una indicación detallada. El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma gástrico tubular**, respaldado por **20 publicaciones** (incluidos múltiples ensayos de Fase 3) y **ningún ensayo clínico registrado** en los datos compilados para esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CAPECITABINA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Adenocarcinoma gástrico tubular (predicción de mayor evidencia entre las 10 candidatas) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la selección:** la primera predicción por puntaje (adenocarcinoma gástrico con poliposis proximal del estómago, síndrome GAPPS) carece de ensayos y literatura (L5, Hold). Por ello este informe se centra en el adenocarcinoma gástrico tubular (segunda en el ranking), que tiene puntaje prácticamente idéntico y evidencia sustancial. Al final se resumen las demás candidatas.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico establecido, la capecitabina se convierte preferentemente en 5-FU dentro del tejido tumoral, e inhibe la timidilato sintasa (TYMS), enzima necesaria para la síntesis de ADN. Los datos de farmacología compilados confirman que TYMS es su diana humana.

La indicación original y la nueva son oncológicas y comparten el mismo mecanismo: la capecitabina es una base de los esquemas de fluoropirimidina con platino (CAPOX) en el adenocarcinoma gástrico. El ensayo de Fase 3 CLASSIC (PMID 22226517) mostró beneficio adyuvante tras gastrectomía D2, y varios ensayos de Fase 3 de primera línea usan CAPOX como esquema quimioterápico base.

Conviene aclarar que la capecitabina ya está establecida en cáncer gástrico, por lo que esto es más una confirmación que un reposicionamiento genuino. Además, los registros locales figuran como cancelados, por lo que la situación del etiquetado en Colombia debe verificarse.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para adenocarcinoma gástrico tubular en los datos compilados. La evidencia proviene de la literatura publicada, que incluye ensayos de Fase 3 con capecitabina como parte del esquema.

---

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones, priorizando ensayos aleatorizados de Fase 3 donde capecitabina o CAPOX forma parte del esquema o del comparador.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | ECA Fase 3 | Lancet | CLASSIC: capecitabina + oxaliplatino adyuvante tras gastrectomía D2 vs. cirugía sola, en cáncer gástrico estadio II-IIIB |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | ECA Fase 3 | Lancet Oncol | RESOLVE: S-1 + oxaliplatino perioperatorio vs. capecitabina + oxaliplatino posoperatorio en cáncer gástrico localmente avanzado |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | ECA Fase 3 | Lancet Oncol | Informe final de RESOLVE con análisis actualizado de supervivencia global |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | ECA Fase 3 | Nature Medicine | GLOW: zolbetuximab + CAPOX en adenocarcinoma gástrico/de la unión gastroesofágica CLDN18.2 positivo |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | ECA Fase 3 | Lancet | CheckMate 649: nivolumab + quimioterapia vs. quimioterapia sola en primera línea |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | ECA Fase 3 | Lancet Oncol | KEYNOTE-859: pembrolizumab + quimioterapia en cáncer gástrico HER2 negativo avanzado |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | ECA Fase 3 | BMJ | RATIONALE-305: tislelizumab + quimioterapia en primera línea |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | ECA Fase 3 | JAMA | ORIENT-16: sintilimab + quimioterapia en cáncer gástrico irresecable |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | ECA Fase 3 | Lancet | ToGA: trastuzumab + quimioterapia en cáncer gástrico HER2 positivo avanzado |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | ECA Fase 2/3 | Lancet | FLOT4: FLOT vs. esquemas con 5-FU o capecitabina + cisplatino + epirrubicina (el comparador contiene capecitabina) |

**Limitación importante:** en varios de estos ensayos la capecitabina forma parte del esquema de quimioterapia de fondo o del comparador; no se evaluó de forma aislada. Ningún estudio es específico del subtipo histológico "tubular".

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155908 (cancelado) | KAPIXA® 500 MG TABLETAS RECUBIERTAS | Tableta recubierta | CAPECITABINA |
| 20060296 (cancelado) | CAPEC® 500 MG TABLETAS RECUBIERTAS | Tableta recubierta | CAPECITABINA |

No hay registros vigentes en este momento.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (fluoropirimidina, profármaco del 5-FU) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. Las relaciones con neutropenia, trombocitopenia, anemia y agranulocitosis aparecen entre las contraindicaciones del grafo de conocimiento |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática (incluida bilirrubina) y función renal |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones extraídas de un prospecto (el prospecto de INVIMA no pudo analizarse). Consultar el prospecto para información de seguridad completa.

- **Condiciones asociadas a contraindicación según el grafo de conocimiento TxGNN (PrimeKG; no es texto de etiqueta):** deficiencia de dihidropirimidina deshidrogenasa, neutropenia, trombocitopenia, agranulocitosis, anemia (incluida la macrocítica), enfermedad hepática, hiperbilirrubinemia (incluidos hereditaria y síndrome de Gilbert), enfermedad de la vesícula biliar, función renal alterada, enfermedad arterial coronaria, paro cardíaco súbito, enfermedad de conducción cardíaca, enterocolitis necrosante, estomatitis y enfermedades infecciosas.
- **Interacciones farmacológicas:** la consulta se completó y solo mostró la interacción farmacológica con la diana timidilato sintasa (TYMS), sin nivel de gravedad asignado. No se identificaron interacciones con otros fármacos en estos datos.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
- Existe evidencia de Fase 3 (CLASSIC y varios ensayos con CAPOX como base) que respalda la capecitabina en adenocarcinoma gástrico, pero no hay ensayos registrados ni estudios específicos del subtipo tubular, y la seguridad local no pudo verificarse.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), ya que es un vacío de datos bloqueante.
- Confirmar el mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: los dos registros están cancelados, por lo que se requeriría un registro vigente o una vía de importación.
- Evaluar la relevancia de cada publicación (aún pendiente) y verificar el rol específico de la capecitabina en cada ensayo.
- Definir un plan de monitoreo hematológico, hepático y renal, y un tamizaje de deficiencia de DPD antes del tratamiento.

---

## Resumen de las Otras Candidatas Predichas

| Indicación predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Cáncer gástrico del cardias (adenocarcinoma) | 99.91% | L2 | Proceed with Guardrails (Fase 2 completado de oxaliplatino + capecitabina, NCT00040859) |
| Carcinoma de cuerpo gástrico | 99.90% | L1 | Proceed with Guardrails (evidencia indirecta; Fase 3 NCT02494583) |
| Adenocarcinoma gástrico de células en anillo de sello | 99.94% | L2 | Proceed with Guardrails (evidencia mayormente extrapolada; un Fase 2 aún sin reclutar) |
| Carcinoma gástrico asociado a virus de Epstein-Barr | 99.90% | L3 | Research Question |
| Carcinoma de tipo glándula salival del estómago | 99.91% | L3 | Research Question |
| Carcinoma del píloro gástrico | 99.91% | L4 | Research Question |
| Adenocarcinoma gástrico con poliposis proximal (GAPPS) | 99.94% | L5 | Hold |
| Cáncer gástrico microinvasivo | 99.94% | L5 | Hold |
| Tumor maligno gástrico de células granulares | 99.89% | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

