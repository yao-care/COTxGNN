---
layout: default
title: Lopinavir
parent: Evidencia Moderada (L3-L4)
nav_order: 262
evidence_level: L4
indication_count: 3
---

# Lopinavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Lopinavir: De Infección por VIH a Infección por el Virus de Inmunodeficiencia de los Simios

## Resumen en Una Frase

Lopinavir es un inhibidor de la proteasa del VIH-1 que se comercializa en Colombia combinado con ritonavir, en registros sanitarios que no detallan la indicación. El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de inmunodeficiencia de los simios (SIV)**, con **0 ensayos clínicos** y **3 publicaciones** preclínicas en macacos que respaldan esta dirección. Como el SIV no infecta a los humanos, no se trata de una nueva oportunidad de reposicionamiento en humanos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lopinavir y ritonavir (el registro no detalla la indicación; el uso conocido es la infección por VIH) |
| Nueva Indicación Predicha | Infección por el virus de inmunodeficiencia de los simios |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, lopinavir es un inhibidor de la proteasa del VIH-1 que se usa junto con ritonavir. Su eficacia en la infección por VIH está establecida, y mecanísticamente podría ser aplicable al SIV.

El SIV es un lentivirus muy cercano al VIH y tiene una proteasa homóloga, por lo que la actividad del fármaco es biológicamente plausible. Los estudios disponibles se hicieron en macacos infectados con SIV o con virus quiméricos (SHIV), lo que los hace evidencia preclínica e indirecta.

El SIV es una infección de primates no humanos. Por eso no existen ensayos en humanos, y la predicción sirve sobre todo para modelos animales de investigación. El mecanismo se infiere de conocimiento general y no del registro suministrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudio animal | Journal of Virology | Cuatro macacos cynomolgus infectados con SIVmac251 recibieron 7 días de terapia antirretroviral cuádruple. Se observó un descenso viral rápido. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Modelo preclínico | Microbes and Infection | Construcción de un SHIV con el gen de la proteasa del VIH-1. Un inhibidor de la proteasa bloqueó su crecimiento en cultivo celular. En dos macacos rhesus produjo una viremia débil pero duradera. Es útil como herramienta para probar inhibidores de proteasa. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudio animal | Journal of Virological Methods | Dos macacos rhesus con infección crónica por SHIV 89.6P recibieron por vía oral AZT, 3TC y lopinavir/ritonavir durante 28 días. Se evaluó el efecto sobre el subconjunto de linfocitos CD8. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20215036 | LOPARTA® 40MG/10MG (Mylan Laboratories Limited) | Gránulos | Lopinavir y ritonavir |
| 20115574 | LOPINAVIR 200 MG + RITONAVIR 50 MG (Aurobindo Pharma Ltd) | Tableta recubierta | Lopinavir y ritonavir |

Los datos indican 8 registros en total. La tabla muestra solo los dos números de registro distintos que aparecen en la información recibida.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo preclínica (L4), en macacos, y el SIV no infecta a los humanos. La contraparte humana, el VIH, ya es un uso conocido de lopinavir, así que no hay una nueva oportunidad clínica. Las otras dos predicciones con puntajes casi idénticos tampoco tienen sustento. El SIDA felino es una condición veterinaria sin ensayos ni literatura (L5). El trastorno del neurodesarrollo con marcha atáxica no muestra ningún vínculo mecanístico plausible y probablemente es un artefacto del grafo de conocimiento (L5).

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones, que es un vacío bloqueante para el tamizaje de seguridad.
- Obtener el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Definir si el SIV tiene interés para investigación animal, dado que no hay una vía de reposicionamiento clínico en humanos.
- Hacer revisión manual de las predicciones L5 antes de cualquier trabajo adicional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

