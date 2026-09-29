---
layout: default
title: Rifapentine
parent: Solo Predicción del Modelo (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Rifapentine
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

# Rifapentina: De Tuberculosis a Lepra

## Resumen en Una Frase

Rifapentina es una rifamicina usada contra la tuberculosis. En Colombia se comercializa en la combinación rifapentina + isoniazida (RIFANIL-INH®); el registro sanitario solo indica el nombre del principio activo, no una indicación. El modelo TxGNN predice que podría ser efectiva para **lepra**, con **0 ensayos clínicos registrados** y **20 publicaciones** que respaldan esta dirección, incluido un ECA publicado en NEJM (2023) sobre profilaxis en contactos domiciliarios.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis (inferida de la evidencia y del producto; el registro INVIMA solo dice "RIFAPENTIN") |
| Nueva Indicación Predicha | Lepra (leprosy) |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L2 (con reservas, ver la conclusión) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo de DrugBank. Según la información conocida, la rifapentina es una rifamicina que inhibe la ARN polimerasa dependiente de ADN bacteriana, igual que la rifampicina.

La rifampicina es la base del tratamiento multifármaco (MDT) de la lepra y de la profilaxis posexposición. Al compartir clase y mecanismo, es lógico que la rifapentina tenga actividad contra *Mycobacterium leprae*, el agente de la lepra, también una micobacteria. Los estudios en ratón indican actividad bactericida de la rifapentina contra *M. leprae*.

**Alcance de la evidencia:** la evidencia clínica más fuerte se refiere a **prevención** con dosis única en contactos domiciliarios de pacientes. No demuestra tratamiento de la enfermedad ya establecida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37195940](https://pubmed.ncbi.nlm.nih.gov/37195940/) | 2023 | ECA | N Engl J Med | Rifapentina en dosis única en contactos domiciliarios de pacientes con lepra. El resumen disponible no incluye resultados. |
| [37585641](https://pubmed.ncbi.nlm.nih.gov/37585641/) | 2023 | Clasificado como ECA (probable comentario; sin resumen) | N Engl J Med | Texto sobre el mismo estudio en contactos domiciliarios. El tipo se infiere del título. |
| [40278757](https://pubmed.ncbi.nlm.nih.gov/40278757/) | 2025 | Revisión | Trop Med Infect Dis | Revisa eficacia, seguridad y factibilidad de la quimioprofilaxis posexposición con rifamicinas. Cita una reducción del 57% en la incidencia (estudio COLEP, con rifampicina). |
| [38440733](https://pubmed.ncbi.nlm.nih.gov/38440733/) | 2024 | Revisión | Front Immunol | Tratamiento, prevención y respuesta inmune en lepra. Señala que aparecen cepas resistentes a rifampicina. |
| [37385746](https://pubmed.ncbi.nlm.nih.gov/37385746/) | 2023 | Protocolo de programa | BMJ Open | Tamizaje poblacional y administración masiva de fármacos en Kiribati. No se confirma el uso de rifapentina. |
| [32936818](https://pubmed.ncbi.nlm.nih.gov/32936818/) | 2020 | Preclínico (modelo animal) | PLoS Negl Trop Dis | Compara rifampicina, rifapentina, moxifloxacino, minociclina y claritromicina como profilaxis posexposición en el modelo de almohadilla plantar de ratón. |
| [30207440](https://pubmed.ncbi.nlm.nih.gov/30207440/) | 2016 | Preclínico | Indian J Lepr | Actividad antibacteriana de rifapentina y combinaciones en lepra resistente a rifampicina en ratón. |
| [30207441](https://pubmed.ncbi.nlm.nih.gov/30207441/) | 2016 | Preclínico | Indian J Lepr | Fármacos nuevos y combinaciones (incluida rifapentina) en ratón, en busca de esquemas más cortos. |
| [11201894](https://pubmed.ncbi.nlm.nih.gov/11201894/) | 2000 | Preclínico | Lepr Rev | Combinación rifapentina-moxifloxacino-minociclina, adecuada para administración mensual supervisada. |
| [29071280](https://pubmed.ncbi.nlm.nih.gov/29071280/) | 2017 | Simulación molecular | Mol Biol Res Commun | Evalúa la resistencia cruzada de rifabutina y rifapentina con rifampicina en lepra resistente. |

Se excluyó el estudio PMID 33758553 (hepatotoxicidad en pacientes con VIH), que no es específico de lepra y fue retractado (PMID 33958898).

## Información de Mercado en Colombia

Se informan 8 registros. El detalle disponible muestra un solo registro (20242586), repetido en las entradas recibidas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20242586 | RIFANIL-INH® TABLETAS RECUBIERTAS (VESALIUS PHARMA S.A.S.) | Tableta recubierta (vía oral) | RIFAPENTIN (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La búsqueda de interacciones farmacológicas no arrojó resultados.

Nota tomada de la evidencia de otras indicaciones (no de la sección de seguridad): las rifamicinas inducen CYP3A4. Ensayos con rifapentina documentan interacciones con antirretrovirales como dolutegravir y tenofovir.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
- El mecanismo es coherente (misma clase que la rifampicina, base del tratamiento de la lepra).
- Existe un ECA publicado en NEJM sobre profilaxis en contactos, además de estudios preclínicos consistentes.
- No hay ensayos registrados y la evidencia no cubre el tratamiento de la enfermedad establecida. Esto justifica avanzar con cautela.

**Para avanzar se necesita:**
- Revisar el texto completo de los PMID 37195940 y 37585641 para confirmar fase, diseño y resultados. La clasificación L2 se basa en títulos y no en un ensayo de Fase 2/3 registrado.
- Buscar ensayos de lepra en registros (ClinicalTrials.gov, ICTRP) que incluyan rifapentina.
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y el mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada en Colombia, ya que el registro solo lista el principio activo.
- Definir un plan de monitoreo de hepatotoxicidad e interacciones farmacológicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

