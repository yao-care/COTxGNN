---
layout: default
title: Cysteine
parent: Solo Predicción del Modelo (L5)
nav_order: 144
evidence_level: L5
indication_count: 7
---

# Cysteine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Cisteína: De Combinaciones (registro sanitario) a Síndrome de Ojo Seco

## Resumen en Una Frase

La cisteína figura en Colombia como componente de una emulsión inyectable de combinación (NUMETA® G 19% E, Laboratorios Baxter), cuyo texto de indicación aprobada es solo "Combinaciones".
El modelo TxGNN predice que podría ser efectiva para el **síndrome de ojo seco**.
Se recuperaron **7 ensayos clínicos** y **20 publicaciones**, pero casi toda la evidencia clínica corresponde a **N-acetilcisteína (NAC)** y a conjugados de NAC, no a cisteína libre.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones (texto del registro NUMETA® G 19% E) |
| Nueva Indicación Predicha | Síndrome de ojo seco |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L3 (ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

**Nota sobre el nivel de evidencia:** el paquete de datos asigna L2. Según las reglas de este informe, L2 exige un ECA de Fase 2/3 completado, y aquí no existe ninguno en ojo seco. El único ensayo de Fase 2/3 (NCT01424033) está terminado prematuramente y trata otra enfermedad. Lo que sí hay son ECAs y una revisión con búsqueda sistemática sobre NAC, lo que corresponde a L3.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la cisteína en la fuente consultada. Según el análisis del paquete, la cisteína es el precursor limitante de la síntesis de glutatión. Su derivado NAC tiene actividad antioxidante y rompe puentes disulfuro en las mucinas. Esto podría reducir el estrés oxidativo de la superficie ocular y la viscosidad del moco de la película lagrimal, dos procesos implicados en el ojo seco. Varios trabajos recuperados señalan el papel de las especies reactivas de oxígeno (ROS) en esta enfermedad.

La indicación original registrada ("Combinaciones") no permite establecer una relación directa con el ojo seco, y la similitud con la indicación original no fue evaluada. La predicción se apoya en el mecanismo antioxidante y mucolítico, no en una afinidad con el uso aprobado.

Hay una limitación importante: los ensayos y estudios clínicos usan NAC o NAC conjugada con quitosano, no cisteína libre, así que extrapolar es indirecto. Además, un estudio en animales (PMID 30025127) usó NAC tópica para crear un modelo de ojo seco por deficiencia de mucina. Esto sugiere que el efecto mucolítico en la superficie ocular podría ser perjudicial según la dosis y la formulación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | N/A | Completado | 60 | ECA doble ciego de NAC para síntomas de sequedad en síndrome de Sjögren primario. Es el ensayo más relevante (grado B), aunque prueba NAC y la condición exacta no pudo confirmarse como ojo seco. |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Fase 2 | Reclutando | 45 | Gotas oculares tópicas de NAC para reducir el estrés oxidativo en distrofia endotelial corneal de Fuchs. Mecanismo ocular similar, pero otra enfermedad. |
| [NCT01424033](https://clinicaltrials.gov/study/NCT01424033) | Fase 2/3 | Terminado | 5 | Tolerabilidad y seguridad de NAC oral en enfermedad pulmonar intersticial asociada a enfermedades del tejido conectivo. Sin relación establecida con ojo seco. |
| [NCT04162210](https://clinicaltrials.gov/study/NCT04162210) | Fase 3 | Activo, sin reclutar | 325 | Belantamab mafodotin frente a pomalidomida/dexametasona en mieloma múltiple (DREAMM-3). Coincide por la toxicidad ocular del fármaco; no evalúa cisteína. |
| [NCT03525678](https://clinicaltrials.gov/study/NCT03525678) | Fase 2 | Completado | 221 | Belantamab mafodotin en mieloma múltiple (DREAMM-2). La queratopatía es un evento adverso; no evalúa cisteína. |
| [NCT03544281](https://clinicaltrials.gov/study/NCT03544281) | Fase 1/2 | Completado | 153 | Belantamab mafodotin combinado con lenalidomida o bortezomib en mieloma múltiple (DREAMM-6). Sin vínculo con cisteína u ojo seco. |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Fase 2 | Completado | 21 | Ciclosporina tópica 0,05% bajo oclusión en síndrome de uñas quebradizas. No evalúa cisteína. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | ECA | J Ocul Pharmacol Ther | Doble ciego controlado de gotas de quitosano-N-acetilcisteína sobre el grosor de la película lagrimal en ojo seco. El resumen disponible no muestra resultados. |
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | ECA | Clin Exp Rheumatol | NAC frente a placebo para síntomas de sequedad en enfermedad de Sjögren. El resumen disponible no muestra resultados. |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | Estudio clínico comparativo | Acta Med Croat | Acetilcisteína tópica frente a lágrimas artificiales en ojo seco; se plantea su efecto mucolítico sobre la acumulación de moco. |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Revisión (búsqueda sistemática) | Surv Ophthalmol | Revisa el papel de la NAC tópica en terapéutica ocular: mecanismos (mucólisis, captación de radicales hidroxilo), aplicaciones y efectos adversos, con 106 referencias. |
| [30025127](https://pubmed.ncbi.nlm.nih.gov/30025127/) | 2018 | Preclínico (animal) | Invest Ophthalmol Vis Sci | La NAC tópica se usó para generar un modelo de ojo seco con deficiencia de mucina; señal de precaución sobre el efecto mucolítico. |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | Preclínico (formulación) | Int J Biol Macromol | Conjugado quitosano-NAC sobre lípidos nanoestructurados con dexametasona para mejorar permeabilidad y retención precorneal en ojo seco. |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclínico (formulación) | Adv Mater | Nanoformulación de catalasa con quitosano modificado con cisteína, dirigida al exceso de ROS en ojo seco. |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclínico (formulación) | Int J Biol Macromol | Conjugado sulfato de condroitina-L-cisteína como material bioadhesivo para mejorar la retención corneal de dexametasona. |
| [41485487](https://pubmed.ncbi.nlm.nih.gov/41485487/) | 2026 | Preclínico | J Control Release | Profármaco de persulfuro sensible al anión superóxido para eliminar ROS en ojo seco. |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Estudio de mecanismo | Exp Eye Res | Las ROS activan inflamasomas NLRP3 en células epiteliales corneales y en pacientes con ojo seco; respalda el papel del estrés oxidativo. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20057807 | NUMETA® G 19% E (Laboratorios Baxter S.A.) | Emulsión inyectable | COMBINACIONES |

Se reportan 20 registros sanitarios en total, pero los cinco entregados en el paquete son entradas repetidas del mismo registro, por lo que solo se muestra una vez. La única forma farmacéutica disponible es inyectable, sin presentación oftálmica.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Hay señales aleatorizadas para NAC en ojo seco y en sequedad por síndrome de Sjögren, pero ningún estudio clínico evalúa cisteína libre. No se dispone de información de seguridad del prospecto de INVIMA, y el único producto comercializado es una emulsión inyectable. Por eso la predicción se considera una pregunta de investigación, no una candidata lista para avanzar.

**Para avanzar se necesita:**
- Definir si la hipótesis se refiere a cisteína, NAC o un conjugado, y buscar evidencia con cisteína libre.
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones); este vacío bloquea el cribado de seguridad.
- Obtener los resultados completos de los ECA PMID 28441068 y 39360368, y confirmar la condición de NCT04793646.
- Obtener datos de mecanismo de acción desde DrugBank.
- Evaluar la viabilidad de una formulación oftálmica, dado que la disponible es inyectable, y analizar el riesgo de efecto mucolítico excesivo (PMID 30025127).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

