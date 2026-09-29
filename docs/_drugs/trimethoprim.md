---
layout: default
title: Trimethoprim
parent: Solo Predicción del Modelo (L5)
nav_order: 398
evidence_level: L5
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Trimetoprim: De Sulfametoxazol/Trimetoprim (indicación no detallada) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Trimetoprim es un inhibidor de la dihidrofolato reductasa bacteriana. En Colombia está registrado como parte de la combinación sulfametoxazol/trimetoprim, y el registro no detalla la indicación.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sulfametoxazol y trimetoprim (combinación; el registro no detalla la indicación) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, trimetoprim inhibe la dihidrofolato reductasa bacteriana y se usa en combinación con sulfametoxazol. Su actividad es antibacteriana.

La queratoconjuntivitis epitelial punteada suele ser de origen viral (por ejemplo, adenovirus) o tóxico/inflamatorio. Por eso no hay un vínculo mecanístico claro con un antibacteriano. El puntaje alto (0.996) probablemente refleja una asociación en el grafo de conocimiento con la conjuntivitis, y no una señal terapéutica real.

Además, los productos oftálmicos con trimetoprim pueden causar toxicidad en la superficie ocular. Esto hace que la predicción sea poco convincente sin evidencia clínica.

## Segunda Predicción con Evidencia: Conjuntivitis

Esta sección complementa el informe. La segunda predicción del modelo, **conjuntivitis** (puntaje TxGNN 99.17%), sí tiene evidencia. El paquete le asigna nivel L2 y la recomendación "Proceed with Guardrails".

La evidencia directa proviene de un ensayo de Fase 4, no de un ECA de Fase 3 en conjuntivitis. Además, corresponde al producto tópico combinado (trimetoprim/polimixina B), no a trimetoprim sistémico. Es probable que se trate de un uso ya establecido y no de un uso realmente nuevo. La eficacia se limita a las causas bacterianas. No se espera beneficio en conjuntivitis viral o alérgica.

### Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Fase 4 | Completado | 124 | Polytrim (trimetoprim/polimixina B) frente a moxifloxacino oftálmico en conjuntivitis. Es evidencia directa, pero el ensayo es pequeño, el comparador es activo y no se presentan resultados. |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Fase 3 | Completado | 218 | Antibióticos profilácticos en sarampión, controlado con placebo. La conjuntivitis es a lo sumo una complicación secundaria, por lo que la evidencia es indirecta. |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Fase 4 | Completado | 252 | Resistencia a antibióticos y microbioma en niños de Burkina Faso. No evalúa la eficacia en conjuntivitis. |

### Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Revisión sistemática/metaanálisis | J Pediatric Infect Dis Soc | Tratamientos antibióticos (eritromicina, azitromicina y trimetoprim) para la conjuntivitis neonatal por clamidia. |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | Ensayo comparativo multicéntrico | J Pediatr Ophthalmol Strabismus | Velocidad de eficacia clínica de polimixina B/trimetoprim frente a moxifloxacino al 0.5% en conjuntivitis bacteriana. |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Evaluación clínica | Am J Ophthalmol | Eficacia y seguridad de soluciones oftálmicas con trimetoprim (con polimixina B, con o sin sulfacetamida) en conjuntivitis bacteriana o blefaritis. |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Cohorte/observacional | Antibiotics (Basel) | Características clínicas y moleculares de infecciones oculares por *S. aureus* sensible a meticilina en Taiwán. |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Encuesta | Clin Ther | Resultados en niños con conjuntivitis bacteriana aguda tratados con solución oftálmica de trimetoprim-polimixina B. |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Revisión | Paediatr Child Health | Etiología, cuadro clínico y manejo de la conjuntivitis infecciosa aguda en niños. |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Revisión | J Pediatr Ophthalmol Strabismus | Control de la conjuntivitis bacteriana contagiosa y uso de antimicrobianos para reducir el periodo infeccioso. |
| [24892274](https://pubmed.ncbi.nlm.nih.gov/24892274/) | 2015 | Reporte de caso | Ophthalmic Plast Reconstr Surg | Conjuntivitis crónica por *Nocardia nova* asociada a un stent de silicona, con cultivo sensible a trimetoprim/sulfametoxazol. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128365 | Trimetoprima Sulfametoxazol 160/800 mg tableta (Laboratorios Ecar S.A.) | Tableta (vía oral) | Sulfametoxazol y trimetoprim |

Las cinco entradas recibidas corresponden al mismo registro sanitario y se presentan una sola vez. El total reportado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para queratoconjuntivitis epitelial punteada no hay ensayos ni literatura (nivel L5). El mecanismo antibacteriano no encaja con una enfermedad usualmente viral o tóxica, y existe riesgo de toxicidad ocular. Para la conjuntivitis bacteriana la evidencia es más sólida (L2, "Proceed with Guardrails"), pero probablemente corresponde a un uso ya establecido del producto tópico combinado.

**Para avanzar se necesita:**
- Revisar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy es un vacío de datos bloqueante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Confirmar las indicaciones originales del fármaco para saber si la conjuntivitis es un uso nuevo o ya aprobado.
- Para conjuntivitis: confirmar si existe en Colombia una presentación oftálmica (trimetoprim/polimixina B). Los registros identificados son solo tabletas orales.
- Para queratoconjuntivitis epitelial punteada: buscar evidencia clínica o preclínica antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

