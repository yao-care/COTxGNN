---
layout: default
title: Omalizumab
parent: Evidencia Moderada (L3-L4)
nav_order: 306
evidence_level: L4
indication_count: 10
---

# Omalizumab
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

# Omalizumab: De Asma Alérgica a Bronquitis

## Resumen en Una Frase

Omalizumab es un anticuerpo monoclonal anti-IgE, conocido por su uso en asma alérgica. El registro colombiano solo consigna el nombre del principio activo, sin texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero solo hay **2 ensayos clínicos** y **8 publicaciones** relacionados, y casi toda la evidencia corresponde a asma, no a bronquitis.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro (solo figura "OMALIZUMAB"); en la literatura se asocia con asma alérgica |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, omalizumab es un anticuerpo anti-IgE que neutraliza la IgE libre y reduce la activación de mastocitos y basófilos. Su eficacia en asma alérgica está bien establecida.

Es probable que el puntaje muy alto del modelo refleje la cercanía entre asma y bronquitis en el grafo de conocimiento. La evidencia recuperada trata de asma o de superposición asma-EPOC, no de bronquitis propiamente dicha.

Mecanísticamente, el fármaco podría ser aplicable a formas de bronquitis con componente eosinofílico o mediado por IgE. Un ensayo pequeño en bronquitis eosinofílica persistente apunta en esa dirección. Para otros tipos de bronquitis no hay ninguna base.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Fase 2/3 | Completado | 11 | ECA doble ciego controlado con placebo sobre el efecto ahorrador de esteroides de omalizumab en pacientes con asma y bronquitis eosinofílica persistente. Muestra muy pequeña y sin resultados en los datos disponibles |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Fase 2 | Completado | 382 | Estudio de búsqueda de dosis de QGE031 en urticaria crónica espontánea, con omalizumab como comparador activo. No evalúa bronquitis (evidencia indirecta) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohorte | Postepy Dermatol Alergol | Omalizumab en pacientes de mediana edad o mayores con asma alérgica grave y superposición asma-EPOC |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Revisión | Clin Rev Allergy Immunol | Aprobación y experiencia posterior de omalizumab en asma moderada a grave |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opin Pharmacother | Manejo del asma asociada a enfermedades de las vías aéreas por tabaquismo (incluye bronquitis crónica); los fumadores fueron excluidos de la mayoría de los ensayos |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Revisión | Masui | Manejo preoperatorio de pacientes con asma bronquial o bronquitis crónica; menciona omalizumab en asma alérgica grave |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Revisión | Rev Mal Respir | Revisión francesa sobre exacerbaciones de asma en adultos |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Revisión | Allergol Immunopathol | Anticuerpos monoclonales en pediatría, incluidas enfermedades alérgicas |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Análisis de seguridad agrupado | Curr Med Res Opin | Seguridad y tolerabilidad de omalizumab en niños con asma alérgica |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Reporte de caso | J Investig Allergol Clin Immunol | Caso raro de bronquitis plástica tras termoplastia bronquial |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20104049 | XOLAIR® SOLUCIÓN INYECTABLE (Novartis Pharma A.G.) | Solución inyectable | OMALIZUMAB (el registro no detalla la indicación) |

Los 5 registros recibidos corresponden al mismo número sanitario (20104049), por lo que se muestra una sola fila. El total informado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para bronquitis solo existe un ensayo de Fase 2/3 con 11 participantes, sin resultados disponibles. El resto de la evidencia es indirecta (asma, superposición asma-EPOC) y el puntaje alto de TxGNN parece reflejar proximidad en el grafo más que eficacia demostrada.

Dentro de las predicciones de este fármaco, "enfermedad pulmonar obstructiva" (a efectos prácticos, asma alérgica) tiene mucho mayor respaldo (L1). Sin embargo, es una indicación ya establecida y no un verdadero reposicionamiento.

**Para avanzar se necesita:**
- Resultados publicados de NCT02049294 y, de existir, ensayos más grandes en bronquitis eosinofílica o con componente mediado por IgE
- Definir qué tipo de bronquitis (aguda, crónica, eosinofílica) es el objetivo, ya que la evidencia no permite generalizar
- Datos de mecanismo de acción (MOA) consignados formalmente en el registro
- Advertencias y contraindicaciones del prospecto de INVIMA, hoy pendientes, para el tamizaje de seguridad
- Confirmar el texto de indicación aprobado en Colombia, pues el registro solo muestra el nombre del principio activo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

