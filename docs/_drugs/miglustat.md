---
layout: default
title: Miglustat
parent: Solo Predicción del Modelo (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: De Enfermedad de Gaucher tipo 1 a Enfermedad de Tay-Sachs

## Resumen en Una Frase

Miglustat es un inhibidor oral de la glucosilceramida sintasa, desarrollado originalmente para la enfermedad de Gaucher tipo 1.
El modelo TxGNN lo predice para muchas enfermedades. La primera de la lista (ictiosis autosómica) no tiene ningún respaldo, así que este informe se centra en **Enfermedad de Tay-Sachs**, la predicción con evidencia real (posición 7 del ranking).
Tiene **5 ensayos clínicos** y **20 publicaciones**, pero la evidencia clínica **no respalda eficacia** de forma clara.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Gaucher tipo 1 (según la literatura; el registro INVIMA solo dice «MIGLUSTATO», sin texto de indicación) |
| Nueva Indicación Predicha | Enfermedad de Tay-Sachs (posición 7; la posición 1, ictiosis autosómica, es L5 sin evidencia) |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L2 (limitado por estudios pequeños de PK/seguridad, no ECA de eficacia) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 filas en el paquete (2 registros únicos: 20261973 y 20010809) |
| Decisión Recomendada | Hold (el paquete lo califica como «pregunta de investigación») |

## ¿Por qué es Razonable esta Predicción?

El paquete de datos no trae el mecanismo de acción desde DrugBank. Según la literatura incluida, miglustat inhibe la glucosilceramida sintasa y reduce la síntesis de glucoesfingolípidos. Esta estrategia se llama terapia de reducción de sustrato.

En la enfermedad de Tay-Sachs, la deficiencia de hexosaminidasa A provoca acumulación de gangliósido GM2 en las neuronas. Frenar su síntesis es, en teoría, una vía lógica. Esta es la relación más sólida entre la indicación original y la nueva, y hay ratones con Tay-Sachs donde un compuesto análogo (NB-DNJ) previno el almacenamiento de GM2 (PMID 9103204).

Sin embargo, en humanos los resultados no acompañan. Un ECA en Tay-Sachs de inicio tardío (12 meses) no mostró beneficio neurológico claro. En la forma infantil, dos pacientes no detuvieron su deterioro, aunque el fármaco alcanzó concentraciones significativas en LCR. Una revisión sistemática de 2023 concluye eficacia limitada o no concluyente.

### Otras predicciones del modelo

Ninguna tiene ensayos ni literatura. Todas son L5 y Hold.

| Enfermedad | Puntaje | Comentario |
|---|---|---|
| Ictiosis autosómica con curso fatal | 99.83% | Sin vínculo establecido. Inhibir la glucosilceramida sintasa reduciría, no restauraría, los lípidos epidérmicos |
| Enfermedad de depósito de ésteres de colesterilo | 99.82% | Es un trastorno de lipasa ácida lisosomal, no de glucoesfingolípidos. Probable cercanía en la red |
| Enfermedad de Krabbe | 99.78% | Vínculo indirecto: la galactosilceramida no depende de esta enzima |
| Leucodistrofia metacromática | 99.77% | Vínculo débil: el sulfátido deriva de galactosilceramida |
| Enfermedad de Wolman | 99.76% | Sin justificación mecanística (deficiencia de lipasa ácida lisosomal) |
| Encefalopatía por deficiencia de prosaposina | 99.75% | El vínculo más creíble entre las no-GM2, pero ultra rara y sin evidencia clínica |
| Neoplasia benigna de glándula suprarrenal | 99.74% | Sin vínculo plausible, probable artefacto del grafo |
| Ictiosis recesiva ligada al X | 99.73% | Vía no glucoesfingolipídica. El efecto sobre la barrera cutánea podría ser contraproducente |
| Neurodegeneración asociada a ácido graso hidroxilasa | 99.72% | Es un déficit de lípidos hidroxilados, no acumulación de sustrato. Requiere evidencia preclínica |

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Completado | 5 | Farmacocinética y tolerabilidad de dosis únicas y múltiples de miglustat en gangliosidosis GM2 juvenil |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Completado | 10 | Farmacocinética, seguridad y tolerabilidad en GM2 infantil (Tay-Sachs clásico y Sandhoff infantil). No es un ECA de eficacia |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Terminado | 30 | Encuesta de efectos de miglustat sobre síntomas neurológicos y sistémicos en formas infantiles de Sandhoff y Tay-Sachs. Terminado, lo que limita la interpretación |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Terminado | 16 | Syner-G: miglustat más dieta cetogénica en gangliosidosis. El efecto no puede atribuirse solo a miglustat |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Fase 2 | Reclutando | 21 | Estudio abierto a largo plazo de nizubaglustat (otro fármaco) en GM2 o Niemann-Pick C, con o sin miglustat previo. Solo apoyo contextual |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECA | Genet Med | Miglustat en Tay-Sachs de inicio tardío, 12 meses controlado más 24 de extensión. Sin beneficio neurológico claro |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revisión sistemática | Eur J Neurol | Eficacia y seguridad de miglustat en gangliosidosis GM2. Resultados previos inconsistentes, conclusión limitada |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Serie pequeña (2 pacientes) | Neurology | En Tay-Sachs infantil no detuvo el deterioro neurológico. Sí hubo concentración significativa en LCR y se previno la macrocefalia |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Cohorte de historia natural | Mol Genet Metab | Línea de tiempo clínica de gangliosidosis infantiles. Sin tratamientos aprobados. Miglustat limitado por efectos secundarios gastrointestinales |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Revisión | Int J Mol Sci | Características clínicas, fisiopatología y terapias actuales de las gangliosidosis GM2 |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revisión | Front Physiol | Nuevos enfoques terapéuticos para Tay-Sachs |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Revisión | Expert Rev Endocrinol Metab | Terapia de reducción de sustrato con miglustat en trastornos de glucoesfingolípidos con afectación cerebral |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Perfil del fármaco | Curr Opin Investig Drugs | Miglustat lanzado para Gaucher tipo 1 y en desarrollo para Tay-Sachs, Fabry y Niemann-Pick C |
| [16151419](https://pubmed.ncbi.nlm.nih.gov/16151419/) | 2005 | Reporte de caso | Bone Marrow Transplant | Trasplante alogénico de médula seguido de terapia de reducción de sustrato en un niño con Tay-Sachs subagudo (sin resumen disponible) |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Preclínico (ratón) | Science | El inhibidor NB-DNJ previno la acumulación de GM2 en cerebro de ratones con Tay-Sachs |

## Información de Mercado en Colombia

El paquete repite las mismas filas, así que aquí se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20010809 | ZAVESCA® 100 MG (Janssen Cilag S.A.) | Cápsula dura | Solo figura «MIGLUSTATO» |
| 20261973 | MIGLUSTAT 100 MG - CÁPSULAS DURAS (Global-Tec Colombia SAS) | Cápsula dura | Solo figura «MIGLUSTATO» |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. El paquete no incluye advertencias ni contraindicaciones de INVIMA, y no se encontraron interacciones farmacológicas registradas.

La literatura señala que el uso de miglustat está limitado por efectos secundarios gastrointestinales (PMID 28476546). Su perfil de seguridad se conoce por su uso comercializado.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo de reducción de sustrato es coherente con Tay-Sachs, pero los datos clínicos disponibles (ECA en inicio tardío, serie infantil, revisión sistemática de 2023) no muestran eficacia clara. Los estudios de Fase 3 son pequeños y de PK/seguridad, por lo que la evidencia queda en L2 y como pregunta de investigación. Las demás predicciones (incluida la de la posición 1) son solo del modelo, sin evidencia.

**Para avanzar se necesita:**
- Prospecto INVIMA con advertencias y contraindicaciones (brecha bloqueante DG001)
- Datos de mecanismo de acción desde DrugBank (DG002)
- Evaluación de regímenes combinados, como el estudio Syner-G (miglustat más dieta cetogénica), y comparación con inhibidores de la glucosilceramida sintasa que penetran mejor en el SNC
- Para la prosaposina, la única predicción no-GM2 con vínculo creíble: una señal preclínica o de casos antes de cualquier consideración clínica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

