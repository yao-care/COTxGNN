---
layout: default
title: Sertaconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 584
evidence_level: L4
indication_count: 10
---

# Sertaconazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Sertaconazol: De Sertaconazol (antifúngico) a Dermatofitosis de la Ingle y el Área Perianal

## Resumen en Una Frase

Sertaconazol es un antifúngico imidazólico de uso tópico, registrado en Colombia en presentaciones de óvulo vaginal y crema tópica (ZALAIN®).
El modelo TxGNN predice que podría ser efectivo para **dermatofitosis de la ingle y el área perianal**, aunque para esta indicación específica no se encontraron ensayos clínicos ni publicaciones directas; la evidencia disponible es indirecta (estudios en otras tiñas, como la tinea corporis y la tinea cruris).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sertaconazol (el registro sanitario solo indica el nombre del principio activo, sin describir la indicación) |
| Nueva Indicación Predicha | Dermatofitosis de la ingle y el área perianal |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida de la literatura, el sertaconazol es un antifúngico imidazólico que inhibe la síntesis de ergosterol (mediante la inhibición de la lanosterol 14-alfa-desmetilasa) y, gracias a su anillo de benzotiofeno, puede alterar la membrana del hongo. A concentraciones altas se une a lípidos no esteroles de la pared fúngica, aumentando su permeabilidad y provocando la muerte celular.

La dermatofitosis de la ingle (tinea cruris) está causada por dermatofitos (Trichophyton, Microsporum, Epidermophyton), contra los cuales el sertaconazol ha mostrado actividad fungistática y fungicida in vitro. Por ello, el mecanismo es coherente con la predicción del modelo.

Es importante señalar que, para esta indicación específica, no se recuperaron ensayos ni literatura. El apoyo es indirecto: proviene de estudios en tinea corporis y tinea cruris combinadas, que se presentan en la sección de indicaciones alternativas más abajo. El puntaje de TxGNN es muy alto, pero sigue siendo una predicción del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

Como referencia indirecta, un estudio comparativo en tinea corporis y tinea cruris localizadas (terbinafina 1% vs. sertaconazol 2%) fue identificado dentro de las indicaciones relacionadas (PMID [24249898](https://pubmed.ncbi.nlm.nih.gov/24249898/), *Indian J Dermatol*, 2013).

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19971199 | ZALAIN® 300MG ÓVULOS VAGINALES | Óvulo | Sertaconazol | Cancelado |
| 19972887 | ZALAIN® 2% CREMA | Crema tópica | Sertaconazol | Cancelado |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Otras Indicaciones Predichas con Mayor Respaldo

Aunque la indicación principal queda en espera, otras predicciones del modelo cuentan con más evidencia:

| Indicación | Puntaje TxGNN | Nivel | Recomendación | Evidencia destacada |
|------|------|------|------|------|
| Tinea corporis | 99.94% | L3 | Proceed with Guardrails | Varios estudios comparativos (vs. eberconazol, terbinafina, clotrimazol, butenafina, amorolfina) |
| Micosis superficial | 99.55% | L3 | Proceed with Guardrails | Ensayo doble ciego multicéntrico vs. miconazol (n=631, 1992) y múltiples revisiones |
| Candidiasis cutánea | 99.63% | L3 | Proceed with Guardrails | Estudio de fase II (1992) y revisiones |
| Pitiriasis versicolor | 99.45% | L3 | Proceed with Guardrails | Estudio clínico de 1992 (n=21) y revisiones |
| Dermatofitosis de cuero cabelludo o barba | 99.55% | L4 | Hold | Solo revisiones y estudio in vitro |
| Infecciones ectothrix, endothrix, granuloma de Majocchi, tinea profunda | 99.37%–99.59% | L5 | Hold | Sin evidencia; la penetración tópica es limitada y suele requerirse terapia sistémica |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para la dermatofitosis de la ingle y el área perianal no hay ensayos ni literatura directa; solo existe una predicción del modelo y un mecanismo plausible (nivel L4). Además, los dos registros sanitarios en Colombia están cancelados y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Revisar los estudios comparativos de tinea corporis/tinea cruris (por ejemplo, PMID 24249898 y 28066103) y evaluar si sus datos permiten sustentar esta indicación.
- Descargar y analizar el prospecto del INVIMA para obtener advertencias y contraindicaciones (brecha de datos bloqueante).
- Confirmar el mecanismo de acción en DrugBank.
- Verificar la situación del estado "solo cancelados" en Colombia, dado que el fármaco se comercializa en otros países, y definir la vía de acceso (nuevo registro o reactivación).
- Considerar priorizar la tinea corporis (L3), que cuenta con mayor respaldo clínico y es la indicación con mejor relación evidencia–viabilidad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

