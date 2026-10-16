---
layout: default
title: Acetylcysteine
parent: Solo Predicción del Modelo (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acetylcysteine: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L5). Indicación original: Acetilcisteína"
---

# Acetylcysteine
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

# Acetilcisteína: De Acetilcisteína (mucolítico) a Enfermedad Trombótica

## Resumen en Una Frase

La acetilcisteína (N-acetilcisteína, NAC) es un agente mucolítico y antioxidante, registrado en Colombia bajo la indicación genérica "acetilcisteína".
El modelo TxGNN predice que podría ser efectivo para la **enfermedad trombótica**,
con **7 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque la evidencia se concentra en microangiopatías trombóticas (PTT y TA-TMA) y no en trombosis en general.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acetilcisteína (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 (según la clasificación de los datos compilados; ver nota en la conclusión) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, la acetilcisteína es un tiol con acción mucolítica y antioxidante, y su uso en patología respiratoria está bien establecido.

Mecanísticamente, el NAC puede reducir los puentes disulfuro del factor de von Willebrand (VWF), disminuyendo el tamaño de sus multímeros y su capacidad de unirse a las plaquetas. Esto está respaldado por modelos preclínicos en ratón y babuino de púrpura trombótica trombocitopénica (PTT). Además, su efecto antioxidante podría atenuar la lesión endotelial, relevante en la microangiopatía trombótica asociada a trasplante (TA-TMA).

Conviene precisar que la evidencia se concentra en microangiopatías trombóticas (PTT, TA-TMA) y en trombocitopenia inmune (PTI), y no en la trombosis en general. Existe un ensayo de Fase 3 completado, pero los datos disponibles no incluyen sus resultados, por lo que la eficacia no está confirmada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Fase 3 | Completado | 170 | NAC en microangiopatía trombótica asociada a trasplante (TA-TMA); sin resultados disponibles |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Fase 2/3 | Activo, no recluta | 44 | NAC de un solo brazo en TA-TMA; sin resultados disponibles |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Fase 2 | Completado | 40 | ECA doble ciego, cruzado: NAC para reducir el fenotipo trombótico en insuficiencia renal |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Fase 1 temprana | Completado | 3 | Estudio piloto de NAC intravenoso en sospecha de PTT; muestra demasiado pequeña |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Fase 2 | Desconocido | 44 | Dexametasona a dosis altas + NAC en trombocitopenia inmune (PTI) recién diagnosticada; relevancia indirecta |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Fase 1/2 | Desconocido | 200 | Atorvastatina + NAC + danazol en PTI resistente o recaída; relevancia indirecta |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Fase 1 temprana | Completado | 15 | Atorvastatina + NAC sobre el recuento plaquetario en PTI; relevancia indirecta |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Revisión sistemática | J Clin Med | Revisión sistemática y análisis crítico del NAC en PTT |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Revisión sistemática | Cureus | NAC como terapia adyuvante en PTT, recaída y enfermedad refractaria |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohorte retrospectiva | Ann Hematol | Asociación entre NAC y mortalidad hospitalaria en PTT adquirida; su uso sigue siendo controvertido |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclínico (ratón/babuino) | Blood | NAC en modelos animales de PTT |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revisión | Expert Rev Hematol | Fármacos reposicionados y nuevos agentes en PTT, incluido el NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revisión | Blood | Visión general de la PTT y su fisiopatología |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | J Clin Med | Fisiopatología, diagnóstico y manejo de la PTT |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Revisión | J Infect Public Health | NAC en COVID-19, con estado protrombótico y estrés oxidativo |
| [32614622](https://pubmed.ncbi.nlm.nih.gov/32614622/) | 2021 | Revisión | Platelets | Estrategias antiplaquetarias dirigidas a VWF y GPIb |
| [34448938](https://pubmed.ncbi.nlm.nih.gov/34448938/) | 2021 | Revisión | Lung | Uso de tioles en COVID-19 |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19970253 | Rinofluimucil® solución nasal (Zambon Colombia) | Solución nasal | Acetilcisteína (cancelado) |
| 20094856 | Fluiq® 600 mg (Eurofarma Colombia) | Polvo | Acetilcisteína (cancelado) |
| 19904497 | Fluimucil® 2% (Zambon Colombia) | Jarabe | Acetilcisteína (cancelado) |

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto de prospecto): úlcera péptica, trastorno hipotensivo, insuficiencia respiratoria, asma, enfermedad bronquial y várices esofágicas.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales con nivel clasificado:
  - Insulina humana inhalada de acción rápida: **moderada**.
  - Carbón activado: **leve**.
  - Otras (manitol, bupropión, calcitriol, pantoprazol, glimepirida, doxiciclina, morfina, metformina, omeprazol, sucralfato, entre otras): nivel no clasificado.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado (NCT03252925) y otro de Fase 2/3 en curso en TA-TMA, además de revisiones sistemáticas en PTT y respaldo preclínico del mecanismo. Sin embargo, no se dispone de resultados publicados de los ensayos, la evidencia se limita a microangiopatías trombóticas y el nivel L1 requiere ≥2 ECA de Fase 3 completados, criterio que los datos disponibles no cumplen estrictamente (solo hay un ensayo de Fase 3 completado), por lo que el nivel real podría ser inferior. Además, los tres registros sanitarios colombianos están cancelados.

**Para avanzar se necesita:**
- Obtener los resultados del ensayo NCT03252925 y del NCT07279610.
- Confirmar el nivel de evidencia con los resultados reales de los ensayos.
- Delimitar la indicación a microangiopatías trombóticas (PTT, TA-TMA) en lugar de enfermedad trombótica en general.
- Descargar y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones (brecha de seguridad bloqueante).
- Consultar el mecanismo de acción en DrugBank.
- Evaluar la situación regulatoria en Colombia, dado que no hay registros vigentes.
- Plan de monitoreo de seguridad, considerando las enfermedades con contraindicación en el grafo (asma, enfermedad bronquial, úlcera péptica, hipotensión, várices esofágicas).

---

### Otras indicaciones predichas (referencia)

| Indicación | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|
| Síndrome de ojo seco | 99.87% | L2 | Proceed with Guardrails (mayor respaldo para la formulación de quitosano-NAC; sin ensayo de Fase 3) |
| Enfermedad de la cavidad nasal | 99.92% | L4 | Hold |
| Faringitis | 99.80% | L4 | Hold |
| Enfermedad traqueal | 99.57% | L4 | Hold |
| Ataque isquémico transitorio | 99.53% | L4 | Hold |
| Glaucoma de ángulo cerrado, laringofaringitis aguda, laringotraqueítis | — | L5 | Hold (sin ensayos ni literatura) |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

