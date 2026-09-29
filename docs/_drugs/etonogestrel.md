---
layout: default
title: Etonogestrel
parent: Solo Predicción del Modelo (L5)
nav_order: 189
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Etonogestrel: De Progestágeno + Estrógeno (Anticoncepción Hormonal) a Amenorrea

## Resumen en Una Frase

Etonogestrel es un progestágeno que en Colombia se comercializa en un sistema de liberación (anillo) combinado con un estrógeno, y su uso conocido es la anticoncepción hormonal.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero la predicción no tiene respaldo directo: hay **1 ensayo clínico** y **2 publicaciones**, todos indirectos o no relacionados con esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Progestágeno + estrógeno (categoría registrada ante INVIMA; uso comercializado: anticoncepción) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 (ningún estudio evalúa la amenorrea como objetivo terapéutico) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, etonogestrel es un progestágeno que suprime la ovulación y adelgaza el endometrio. Su eficacia como anticonceptivo está comprobada, pero no hay una vía mecanística documentada hacia el tratamiento de la amenorrea.

Aquí la predicción es poco plausible. La amenorrea es un efecto esperado del etonogestrel, no un objetivo terapéutico. El puntaje alto de TxGNN probablemente refleja una asociación fármaco-fenotipo del grafo de conocimiento (el fármaco provoca o se vincula con amenorrea), no una razón para tratarla. Usar un fármaco que induce amenorrea para tratar amenorrea no tiene sentido biológico sin una justificación adicional, por ejemplo un subtipo específico de amenorrea o un esquema de uso distinto.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fase 3 | Completado | 498 | Estudio abierto, multicéntrico y de brazo único sobre la eficacia anticonceptiva y la seguridad del implante de etonogestrel (MK-8415) entre el 4.º y el 5.º año de uso en mujeres de 35 años o menos. No evalúa la amenorrea como desenlace; es evidencia indirecta, a lo sumo de perfil de seguridad. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | ECA | Contraception | Comparó en China el implante de una varilla (Implanon) con el de seis cápsulas (Norplant) en 200 mujeres sanas durante 2 años. No hubo embarazos y se analizaron los patrones de sangrado. Es indirecto: no trata amenorrea. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Protocolo de ECA | Trials | Protocolo del estudio COVA (BIO101) para prevenir el deterioro respiratorio en COVID-19. No guarda relación con etonogestrel ni con amenorrea. |

## Información de Mercado en Colombia

Los cinco registros listados en el Evidence Pack corresponden al mismo registro sanitario, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128300 | EXELRING ® | Sistemas de liberación | Progestágeno + estrógeno |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay estudios que evalúen etonogestrel como tratamiento de la amenorrea. La evidencia disponible es solo anticonceptiva e indirecta, y el mecanismo del fármaco va en sentido contrario a la indicación predicha. Las otras cuatro predicciones (patologías benignas de mama) tampoco tienen ensayos ni literatura (L5).

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que bloquea el tamizaje de seguridad.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Confirmar si la predicción refleja solo la amenorrea como efecto adverso o asociado al fármaco, y no un uso terapéutico.
- Si se insiste en la indicación, definir un subtipo específico de amenorrea y buscar evidencia clínica directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

