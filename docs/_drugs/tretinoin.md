---
layout: default
title: Tretinoin
parent: Solo Predicción del Modelo (L5)
nav_order: 643
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tretinoin: nueva indicación predicha, Nódulos reumatoides (rheumatoid nodulosis) (nivel de evidencia L5). Indicación original: Tretinoína en combinaciones"
---

# Tretinoin
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

# Tretinoína: De Combinaciones Tópicas/Cápsulas de Tretinoína a Nódulos Reumatoides

## Resumen en Una Frase

Tretinoína (ácido retinoico todo-trans) se registró en Colombia en formulaciones tópicas (loción capilar, crema) y en cápsulas blandas (Vesanoid®), todas con registros hoy cancelados.
El modelo TxGNN predice que podría ser efectivo para **nódulos reumatoides (rheumatoid nodulosis)**, con una puntuación alta pero **sin ensayos clínicos y sin publicaciones relevantes** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tretinoína en combinaciones (registro INVIMA; el texto de indicación aprobado solo consigna el nombre de la sustancia o combinación) |
| Nueva Indicación Predicha | Nódulos reumatoides (rheumatoid nodulosis) |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, tretinoína es un retinoide que actúa como agonista de los receptores de ácido retinoico (RARα, RARβ y RARγ). También muestra interacción farmacológica con otros receptores nucleares como PPARβ/δ, RORβ, TR4 y TLX. Se usa en trastornos cutáneos (acné, daño por radiación UV, trastornos de queratinización) y como agente diferenciador en leucemia promielocítica aguda.

La relación con los nódulos reumatoides es indirecta. Los retinoides tienen efectos inmunomoduladores (por ejemplo, sobre el equilibrio Th17/Treg), lo que podría relacionarse con la inflamación reumatoide. Sin embargo, esto es una hipótesis teórica: no hay ensayos ni literatura que evalúen tretinoína en esta enfermedad, y la similitud con la indicación original aún no se ha analizado.

Cabe señalar que las otras nueve predicciones principales (artritis idiopática juvenil y sus variantes, espondiloartropatía, osteoartritis, displasias esqueléticas, foliculitis decalvante) también carecen de evidencia directa. Varias de ellas forman un grupo de sinónimos y no constituyen evidencia independiente. En espondiloartropatía, los retinoides se asocian con cambios esqueléticos a dosis altas o crónicas, por lo que el efecto podría ser adverso y no terapéutico. La predicción de plausibilidad dermatológica más razonable es la foliculitis decalvante, aunque tampoco tiene respaldo directo para tretinoína.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para nódulos reumatoides.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19950832 | Folister Hair Lotion | Solución tópica | Tetrinoína, combinaciones | Cancelado |
| 27207 | Vesanoid® 10 mg | Cápsula blanda | Tretinoína | Cancelado |
| 19931579 | Tri-Luma® Crema | Crema tópica | Combinaciones de corticosteroides | Cancelado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Agente diferenciador utilizado en leucemia promielocítica aguda (no citotóxico convencional clásico) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, perfil lipídico (según práctica clínica con retinoides sistémicos) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen de textos de prospecto):** quemadura solar; trastornos de ansiedad, neuróticos y distímicos; trastornos psicóticos y otros trastornos mentales (esquizofreniforme, esquizoafectivo); enfermedad renal; enfermedad hepática; enfermedad de la vesícula biliar; pancreatitis; insuficiencia cardíaca congestiva; insuficiencia suprarrenal y enfermedad de Addison; enfermedad de Crohn y enfermedad inflamatoria intestinal; dermatitis atópica; osteoporosis (incluida la posmenopáusica); diabetes mellitus y cetoacidosis diabética; micosis fungoide y linfomas cutáneos de células T relacionados; piouréter.
- **Interacciones farmacológicas:** los datos compilados corresponden a interacciones farmacológicas con dianas (RARα, RARβ, RARγ, PPARβ/δ, RORβ, TR4, TLX), no a interacciones con otros medicamentos.
- **Consideración adicional:** el uso sistémico en niños (relevante para las predicciones de artritis juvenil) plantea preocupaciones de teratogenicidad y toxicidad ósea y mucocutánea.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5): no hay ensayos clínicos ni literatura que evalúen tretinoína en nódulos reumatoides. Además, no hay registros vigentes en Colombia, y las dos publicaciones recuperadas para otra predicción (osteoartritis) no tienen relación con tretinoína.

**Para avanzar se necesita:**
- Obtener el prospecto oficial de INVIMA para completar la revisión de advertencias y contraindicaciones (brecha de datos bloqueante).
- Completar los datos del mecanismo de acción desde DrugBank y analizar el vínculo mecanístico y la similitud con la indicación original.
- Realizar una revisión sistemática de literatura preclínica sobre retinoides en inflamación reumatoide y nódulos reumatoides.
- Evaluar la compatibilidad de vía de administración (actualmente pendiente) y la situación regulatoria, dado que todos los registros están cancelados.
- Realizar una evaluación de seguridad específica, dado el perfil teratogénico de los retinoides sistémicos y la lista extensa de contraindicaciones del grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

