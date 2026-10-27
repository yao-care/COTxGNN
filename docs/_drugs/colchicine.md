---
layout: default
title: Colchicine
parent: Solo Predicción del Modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Colchicine: nueva indicación predicha, Fiebre mediterránea familiar, autosómica dominante (nivel de evidencia L5). Indicación original: Colchicina"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Colchicina: De Colchicina (indicación no detallada en el registro) a Fiebre Mediterránea Familiar
{: .text-alpha }

## Resumen en Una Frase

La colchicina es un fármaco de uso oral con registros sanitarios en Colombia, que hoy figuran todos como cancelados. Según fuentes farmacológicas, se usa sobre todo para la gota y para enfermedades autoinflamatorias como la enfermedad de Behçet.
El modelo TxGNN predice que podría ser efectiva para **fiebre mediterránea familiar (forma autosómica dominante)**, respaldada por **0 ensayos clínicos** y **19 publicaciones**, en su mayoría revisiones. Este uso ya es conocido y está establecido, por lo que no constituye un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colchicina (el registro sanitario no detalla la indicación; según fuentes farmacológicas, gota y enfermedades autoinflamatorias) |
| Nueva Indicación Predicha | Fiebre mediterránea familiar, autosómica dominante |
| Puntaje de Predicción TxGNN | 99.38% |
| Nivel de Evidencia | L4 (según los datos aportados; probablemente subestima la evidencia clínica real) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 5 (0 vigentes, 5 cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de fármacos. Según la información compilada, la colchicina se une a la tubulina (en particular a la tubulina beta clase I) e inhibe el ensamblaje de los microtúbulos. Esto reduce la quimiotaxis de neutrófilos y la activación del inflamasoma NLRP3.

La fiebre mediterránea familiar (FMF) es la enfermedad autoinflamatoria prototípica. Está causada por mutaciones de ganancia de función en el gen *MEFV* (proteína pirina), que provocan inflamación neutrofílica mediada por IL-1β. La colchicina es el tratamiento de primera línea desde hace décadas: previene las crisis y la amiloidosis renal. Las revisiones recuperadas lo confirman, y señalan que entre un 5% y un 10% de los pacientes son resistentes o intolerantes, en cuyo caso se usan agentes biológicos como canakinumab.

Hay una salvedad: la entrada de la enfermedad corresponde a la forma autosómica dominante, mientras que la forma clásica es autosómica recesiva. Debe verificarse la correspondencia del subtipo. Además, como este uso ya está respaldado por guías clínicas, conviene marcarlo como **indicación ya conocida**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en los datos compilados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de 19 recuperadas), priorizando revisiones y comentarios de mayor nivel.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37298536](https://pubmed.ncbi.nlm.nih.gov/37298536/) | 2023 | Revisión | Int J Mol Sci | Actualización sobre FMF, resistencia al tratamiento y adherencia |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Revisión | Turk J Med Sci | Patogénesis (mutaciones de *MEFV*/pirina), diagnóstico y enfoques terapéuticos |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Revisión | N Engl J Med | Canakinumab en síndromes de fiebre recurrente autoinflamatoria, incluida la FMF |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Revisión | Presse Med | FMF como el síndrome de fiebre periódica hereditario más frecuente |
| [28413100](https://pubmed.ncbi.nlm.nih.gov/28413100/) | 2017 | Revisión | Semin Arthritis Rheum | La colchicina es el tratamiento de referencia; definición y causas de resistencia o intolerancia |
| [38925725](https://pubmed.ncbi.nlm.nih.gov/38925725/) | 2024 | Revisión/Comentario | J Am Coll Cardiol | Inflamación, colchicina y enfermedad aterosclerótica, con la FMF como caso de referencia |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Revisión | Clin Exp Rheumatol | La colchicina es el fármaco de elección desde 1972; inhibición de IL-1 en casos con problemas |
| [41460254](https://pubmed.ncbi.nlm.nih.gov/41460254/) | 2025 | Estudio observacional | Eur J Pediatr | Crecimiento y desarrollo puberal en niños con FMF tratados con colchicina |

---

## Información de Mercado en Colombia

Los 5 registros sanitarios están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20055858 | Colchicina 0.5 mg tabletas | Tableta | Colchicina |
| 20253882 | Sovusta® | Tableta | Colchicina |
| 20010760 | Colchicina tabletas 0.5 mg | Tableta | Colchicina |
| 36324 | Colchimedio 0.5 mg tabletas | Tableta | Colchicina |
| 19948217 | Colchicina 0.5 mg tabletas | Tableta | Colchicina |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, deterioro de la función renal, enfermedades hematológicas (trombocitopenia, leucopenia, agranulocitosis, neutropenia y sus variantes congénitas, anemia aplásica), úlcera péptica, enfermedades diarreicas, y miopatías o rabdomiólisis.
- **Interacciones y dianas farmacológicas:** se registraron 7 asociaciones farmacológicas con receptores de glicina (GLRA1, GLRA2), receptores del gusto (TAS2R4, TAS2R46), BRD4 y tubulina beta clase I. Son dianas moleculares, no interacciones medicamentosas clínicas.
- La literatura indica un índice terapéutico estrecho. Los niveles del fármaco dependen de la glicoproteína P y del CYP3A4, por lo que conviene vigilar los inhibidores de estas vías.

No se dispone de advertencias del prospecto; se debe consultar el prospecto del producto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La colchicina es el tratamiento de primera línea establecido para la fiebre mediterránea familiar y la literatura lo respalda de forma consistente. Sin embargo, los datos aportados no incluyen ensayos clínicos, y hoy no hay registros vigentes en Colombia. Por eso se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Verificar el subtipo de la enfermedad (forma autosómica dominante frente a la clásica recesiva).
- Confirmar que se trata de una indicación ya conocida y no de un reposicionamiento novedoso.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Aclarar el estado regulatorio: todos los registros están cancelados, así que habría que reactivarlos o tramitar uno nuevo.
- Definir un plan de monitoreo de seguridad (función renal y hepática, hemograma, interacciones con inhibidores de CYP3A4 y glicoproteína P).

**Otras predicciones del modelo (no recomendadas por ahora):**
- *Malaria por Plasmodium falciparum* (99.60%, L5, Hold): la evidencia es solo indirecta (estudios preclínicos sobre curcumina y pfmdr1) y la toxicidad del huésped a dosis antiparasitarias limita la plausibilidad.
- *Dermatofibrosarcoma protuberans* (99.37%, L5, Hold): no hay ensayos ni literatura; la enfermedad se trata con cirugía e imatinib y no hay evidencia que la conecte con la colchicina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

