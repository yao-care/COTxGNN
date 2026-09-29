---
layout: default
title: Dexamethasone
parent: Solo Predicción del Modelo (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexametasona: De Dexametasona con Antiinfecciosos (Uso Oftálmico y Ótico) a Alopecia Areata

## Resumen en Una Frase

En Colombia, la dexametasona se comercializa en productos oftálmicos y óticos combinados con antiinfecciosos.
El modelo TxGNN predice que podría ser efectiva para la **alopecia areata**.
Esta dirección cuenta con **13 publicaciones clínicas** sobre corticoides sistémicos o dexametasona en pulsos (entre ellas 1 ensayo aleatorizado pequeño y 1 metaanálisis en red), pero **ningún ensayo clínico registrado** para esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dexametasona y antiinfecciosos |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 (basado en un ECA publicado, pequeño y abierto; no hay ensayo de Fase 2/3 registrado para esta indicación) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Los datos farmacológicos disponibles indican que la dexametasona se une al receptor de glucocorticoides (NR3C1) y al receptor de mineralocorticoides (NR3C2). También aparece asociada al receptor X de pregnano (registrado en ratón). La dexametasona es un glucocorticoide sintético potente con acción antiinflamatoria e inmunosupresora.

La alopecia areata es un ataque autoinmune mediado por linfocitos T contra el folículo piloso, tras la pérdida de su privilegio inmune. Un glucocorticoide que frena la activación de los linfocitos T y las citocinas proinflamatorias encaja con esa biología. Este razonamiento se infiere de la farmacología general de los glucocorticoides y de los títulos de la literatura, no de datos del registro del fármaco.

El puntaje de 99.99 % es solo una predicción del modelo y no se usa como evidencia clínica. Además, la evidencia publicada se refiere a dexametasona **sistémica** en mini-pulsos orales o pulsos intravenosos. Los productos que aparecen en el mercado colombiano son oftálmicos y óticos, una diferencia importante de vía de administración.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con alopecia areata registrados. Se recuperaron 15 ensayos, todos de oncología o de otras áreas (mieloma múltiple, cáncer de pulmón, mesotelioma, linfoma y otros). En ellos la dexametasona es un medicamento acompañante o de soporte, y ninguno incluye pacientes con alopecia areata, por lo que no se usan como respaldo.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | ECA | Dermatol Ther | Estudio aleatorizado abierto en 30 niños con alopecia areata grave no progresiva. Compara mini-pulso oral de dexametasona con sensibilización de contacto con difenciclopropenona (DPCP). El resumen disponible no incluye los resultados. |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Revisión sistemática y metaanálisis en red | Arch Dermatol Res | Compara esteroides sistémicos, inhibidores de JAK e inmunoterapia de contacto en alopecia areata grave. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revisión | Pediatr Dermatol | Revisa dosis, esquemas y efectos secundarios de la terapia de pulsos de corticoides en niños con alopecia areata. |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Cohorte prospectiva | J Clin Med | Datos de vida real sobre eficacia y seguridad del mini-pulso oral de dexametasona, con análisis de factores asociados a la respuesta. |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Estudio multicéntrico | Dermatol Ther | Mini-pulso oral de dexametasona en alopecia areata moderada a grave. El diseño exacto no es claro en el resumen. |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Estudio prospectivo | Dermatol Ther | 73 niños con alopecia areata grave. Compara pulsos intravenosos de dexametasona de 1 día frente a 3 días cada mes, más clobetasol tópico. |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Seguimiento a largo plazo | Dermatol Ther | 65 niños y adolescentes tratados con dexametasona oral una vez cada 4 semanas más corticoide tópico. Seguimiento mediano de 96 meses. |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Serie de casos | J Dermatol | 30 pacientes con alopecia areata extensa que recibieron pulso oral de 5 mg de dexametasona dos días consecutivos por semana. |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Revisión retrospectiva de historias | Eur J Dermatol | 19 pacientes con alopecia areata grave. Baricitinib con corticoide tópico y rescate con pulsos de dexametasona en quienes no respondieron. |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Caso clínico y revisión | J Dermatolog Treat | Remisión duradera de alopecia areata grave con mini-pulso oral de dexametasona cuando los inhibidores de JAK no son una opción. |

---

## Información de Mercado en Colombia

Hay 20 registros en total. La tabla muestra solo los distintos, porque algunos aparecen repetidos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20174553 | OFTALMAX® | Solución oftálmica | Dexametasona y antiinfecciosos |
| 20004823 | FIXAMICIN DEXACIPRO GOTAS OTICAS | Suspensión ótica | Dexametasona y antiinfecciosos; ciprofloxacina |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones medicamentosas registradas. Los 3 registros de la consulta son dianas farmacológicas (receptor de glucocorticoides, receptor de mineralocorticoides y receptor X de pregnano), no fármacos que interactúen.

Para advertencias y contraindicaciones, consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay literatura clínica consistente sobre dexametasona en mini-pulsos para alopecia areata, con un ECA pequeño, un metaanálisis en red y varias cohortes. Sin embargo, no hay ensayos registrados para esta indicación, y los estudios son en su mayoría observacionales o de bajo tamaño. Además, la vía estudiada (oral o intravenosa) no coincide con los productos oftálmicos y óticos mostrados en Colombia.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para obtener advertencias y contraindicaciones.
- Confirmar si existe en Colombia una presentación sistémica (oral o inyectable) de dexametasona entre los 20 registros, ya que la tabla solo muestra productos oftálmicos y óticos.
- Revisar el texto completo del ECA (PMID 36086930) y de las cohortes clave para conocer las tasas de respuesta y de recaída.
- Definir un plan de monitoreo de seguridad para el uso sistémico repetido de corticoides, con especial atención en población pediátrica.
- Comparar con las alternativas actuales, como los inhibidores de JAK, según acceso y costo.

Las otras 9 indicaciones predichas (por ejemplo, alopecia mucinosa y telogen effluvium) solo cuentan con predicción del modelo o con literatura irrelevante. Su nivel es L5 y su decisión es Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

