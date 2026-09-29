---
layout: default
title: Tenofovir Alafenamide
parent: Solo Predicción del Modelo (L5)
nav_order: 376
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tenofovir alafenamida: De Hepatitis B crónica a infección por virus de inmunodeficiencia simia (SIV)

## Resumen en Una Frase

Tenofovir alafenamida (TAF) es un profármaco de tenofovir, comercializado en Colombia como VEMLIDY® y usado para tratar la infección crónica por el virus de la hepatitis B (también está aprobado para VIH-1).
El modelo TxGNN predice que podría ser efectivo para la **infección por virus de inmunodeficiencia simia (SIV)**, con **1 ensayo clínico** poco relevante y **10 publicaciones**, todas en modelos animales o metodológicas.
Como el SIV no es una enfermedad humana, esta predicción no representa una indicación nueva para personas.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis B crónica (según la ficha de farmacología; el texto del registro INVIMA solo dice "TENOFOVIR ALAFENAMIDA", sin indicación) |
| Nueva Indicación Predicha | Infección por virus de inmunodeficiencia simia (SIV) |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L4 (solo estudios preclínicos en animales) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambas entradas corresponden al mismo registro, 20134171) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, TAF es un profármaco de tenofovir, un inhibidor nucleotídico de la transcriptasa inversa. Su eficacia en VIH-1 y en hepatitis B ya está comprobada, y mecanísticamente podría ser aplicable a virus con transcriptasa inversa, como el SIV.

El SIV es el modelo en primates no humanos del VIH. La literatura en macacos es coherente con la plausibilidad biológica: TAF, solo o combinado, se ha probado como profilaxis y en estrategias de remisión.

Sin embargo, la relación entre la indicación original y la predicha es de cercanía con el VIH, que ya es un uso aprobado. Lo más probable es que el puntaje alto (99.89%) refleje esa proximidad en el grafo de conocimiento y no una señal nueva de reposicionamiento.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Fase 1/2 | Desconocido | 12 | Vedolizumab combinado con terapia antirretroviral para lograr remisión virológica permanente en personas con VIH sin tratamiento previo. Es un estudio en VIH humano, no en SIV; TAF probablemente forma parte del esquema antirretroviral base y no es el fármaco en investigación (el título está truncado y no puede confirmarse). Relevancia baja (grado C). |

## Evidencia de Literatura

Todas las publicaciones son estudios en animales o metodológicos, sin estudios en humanos. Solo una usa SIV; las demás usan SHIV (virus quimérico simio/humano).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Estudio animal (macaco, SHIV) | J Infect Dis | Insertos vaginales con TAF/elvitegravir dieron protección extendida tras la exposición; el trabajo previo del grupo mostró 93% y 100% de protección al aplicarlos 4 horas antes o después de la exposición. |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Estudio animal (macaco, SHIV) | J Infect Dis | Compara TAF/emtricitabina oral con TAF solo frente a exposiciones vaginales repetidas. El resumen disponible no incluye los resultados. |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Estudio animal (macaco, SHIV) | J Infect Dis | La combinación oral de emtricitabina y TAF protegió a macacos de la infección rectal por SHIV. |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Estudio animal (macaco) | J Antimicrob Chemother | Evalúa seguridad y eficacia de un implante biodegradable de TAF para protección vaginal. El resumen disponible no incluye los resultados. |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Estudio animal (macaco infantil, SIV) | J Acquir Immune Defic Syndr | Evalúa tenofovir disoproxil oral y GS-7340 (TAF) tópico frente a exposiciones orales repetidas a SIV virulento. Es la única publicación con SIV. |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Estudio animal (macaco, RT-SHIV) | Nat Commun | Emtricitabina/TAF oral más cabotegravir/rilpivirina de acción prolongada, con y sin un agente inmune (n=4 por grupo), en busca de remisión viral. |
| [41342257](https://pubmed.ncbi.nlm.nih.gov/41342257/) | 2026 | Estudio animal (macaco, SHIV) | J Infect Dis | Insertos rectales con TAF/elvitegravir dieron protección parcial tras la exposición (82.9%). |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Desarrollo de modelo animal | Front Immunol | Modelo de ratón humanizado para probar estrategias antivirales contra SIV y VIH. |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Protocolo metodológico | PLoS One | Protocolo para dar antirretrovirales orales a macacos con alto cumplimiento. |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Estudio animal (macaco, SHIV) | J Infect Dis | La profilaxis oral previa a la exposición redujo la inflamación y la pérdida de CD4 en la infección aguda por SHIV con brecha de protección. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20134171 | VEMLIDY® (GILEAD SCIENCES IRELAND UC.) | Tableta recubierta | El registro solo indica el principio activo "TENOFOVIR ALAFENAMIDA", sin texto de indicación |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó con un solo registro, que es una relación de farmacología con el receptor del gusto TAS2R39, sin nivel de gravedad. No es una interacción medicamentosa clínica.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El SIV es un virus de primates no humanos, por lo que no existe una indicación clínica nueva que evaluar. La evidencia es solo preclínica (L4) y sirve como modelo del uso ya aprobado en VIH. El puntaje alto de TxGNN parece reflejar la cercanía con el VIH en el grafo de conocimiento.

Las otras dos predicciones tampoco justifican avanzar: el sida felino y el trastorno del neurodesarrollo con marcha atáxica no tienen ensayos ni literatura. La segunda no muestra un vínculo mecanístico plausible.

**Para avanzar se necesita:**
- Confirmar con el equipo si la predicción sobre SIV debe descartarse como indicación humana y tratarse solo como validación del modelo.
- Descargar y revisar el prospecto de INVIMA, para completar advertencias y contraindicaciones.
- Corregir el campo de indicación del registro sanitario, que solo contiene el nombre del principio activo.
- Complementar el mecanismo de acción desde DrugBank.
- Revisar por qué el registro 20134171 aparece duplicado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

