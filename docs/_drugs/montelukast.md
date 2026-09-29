---
layout: default
title: Montelukast
parent: Solo Predicción del Modelo (L5)
nav_order: 290
evidence_level: L5
indication_count: 5
---

# Montelukast
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

# Montelukast: De Asma (uso conocido) a Bronquitis

## Resumen en Una Frase

Montelukast es un antagonista del receptor de leucotrienos CysLT1, conocido y comercializado sobre todo para el asma. El modelo TxGNN predice que podría ser efectivo para **bronquitis**, con **20 ensayos clínicos** y **20 publicaciones** asociados. La evidencia directa en bronquitis es limitada: los ensayos más específicos tienen estado desconocido y no hay resultados publicados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo repite "MONTELUKAST"); el uso conocido es asma |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 (apoyado principalmente por un ensayo de Fase 3 en bronquiolitis y estudios en bronquitis eosinofílica) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos de DrugBank no incluyen el mecanismo de acción (MOA) de este farmaco. Según la literatura y el análisis de reposicionamiento, montelukast bloquea el receptor CysLT1. Así reduce la inflamación de las vías aéreas mediada por leucotrienos cisteínicos, el reclutamiento de eosinófilos y la broncoconstricción.

El asma y varias formas de bronquitis comparten esta vía inflamatoria, especialmente la bronquitis eosinofílica no asmática y la bronquitis obstructiva recurrente en niños. También es plausible en la sibilancia posviral y la bronquiolitis, donde se activa la vía de leucotrienos durante la infección por VRS.

Para la bronquitis infecciosa común, en cambio, la evidencia es débil. La predicción es más razonable para los subtipos eosinofílico y obstructivo que para la bronquitis en general.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Fase 4 | Desconocido | 100 | Montelukast en niños de 1 a 7 años con bronquitis obstructiva recurrente; sin resultados disponibles |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Fase 4 | Desconocido | 63 | Montelukast añadido a budesonida inhalada en bronquitis eosinofílica no asmática (tos); aleatorizado, doble ciego |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Fase 4 | Completado | 49 | Respuesta de la tos crónica a prednisolona o montelukast según feNO |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Fase 3 | Completado | 1125 | Dos dosis de montelukast frente a placebo en síntomas respiratorios de la bronquiolitis por VRS (niños de 3 a 24 meses) |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | NA | Completado | 141 | Montelukast diario frente a placebo sobre la duración de la enfermedad aguda en bronquiolitis viral |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | NA | Completado | 51 | Montelukast frente a placebo en bronquiolitis aguda por VRS; evalúa evolución clínica y citocinas |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | NA | Completado | 146 | Montelukast en bronquiolitis aguda y sibilancias posbronquiolitis en lactantes de 3 a 12 meses |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Fase 4 | Completado | 100 | Montelukast oral añadido al tratamiento estándar en preescolares hospitalizados por asma aguda |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Fase 2 | Completado | 25 | Montelukast en bronquiolitis obliterante tras trasplante de células madre |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Fase 2 | Completado | 36 | Combinación fluticasona, azitromicina y montelukast en bronquiolitis obliterante tras trasplante |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | ECA | Chin Med J | Montelukast añadido a budesonida frente a budesonida sola en bronquitis eosinofílica no asmática; evalúa inflamación, tos y calidad de vida |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | Estudio piloto | Respir Med | Montelukast añadido frente a budesonida en doble dosis en bronquitis eosinofílica no asmática |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Revisión sistemática | Pediatr Allergy Immunol | Eficacia de montelukast para prevenir las sibilancias posbronquiolitis |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Revisión | Ther Adv Respir Dis | Potencial terapéutico de montelukast en bronquiolitis obliterante tras trasplante de pulmón o de células madre |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Ensayo de Fase 2 | Transplant Cell Ther | Ensayo prospectivo de un solo brazo de montelukast en bronquiolitis obliterante tras trasplante hematopoyético |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Ensayo de Fase 2 | Biol Blood Marrow Transplant | Fluticasona, azitromicina y montelukast en bronquiolitis obliterante de inicio reciente (36 pacientes) |
| [25846070](https://pubmed.ncbi.nlm.nih.gov/25846070/) | 2016 | Estudio clínico | World J Pediatr | Bronquiolitis por VRS con coinfección por Mycoplasma y tratamiento adicional con montelukast |
| [18296556](https://pubmed.ncbi.nlm.nih.gov/18296556/) | 2008 | Farmacocinética | J Clin Pharmacol | Farmacocinética y tolerabilidad de montelukast en gránulos en 12 lactantes de 1 a 3 meses con bronquiolitis |
| [20442434](https://pubmed.ncbi.nlm.nih.gov/20442434/) | 2010 | Preclínico (ratón) | Am J Respir Crit Care Med | Montelukast durante la infección primaria por VRS previene hiperreactividad e inflamación tras la reinfección |
| [29308548](https://pubmed.ncbi.nlm.nih.gov/29308548/) | 2018 | Revisión | Indian J Pediatr | Manejo de la sibilancia recurrente en preescolares, incluida la bronquiolitis/bronquitis |

## Información de Mercado en Colombia

Los 5 registros listados en los datos corresponden al mismo número de registro sanitario y al mismo producto, por lo que se muestra una sola vez. El total reportado es de 10 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190806 | BONVENT® (TECNOFAR TQ S.A.S.) | Tableta masticable | Solo figura "MONTELUKAST" (sin indicación detallada) |

## Consideraciones de Seguridad

- **Advertencia neuropsiquiátrica (según la literatura)**: la FDA emitió en 2020 una advertencia en recuadro negro por eventos neuropsiquiátricos con montelukast. Los estudios observacionales posteriores dan resultados mixtos, especialmente en niños (por ejemplo, PMID 37758273 y 39836401). Esto importa porque la población pediátrica es la más relevante para esta predicción.

No se dispone de advertencias, contraindicaciones ni interacciones farmacológicas del prospecto de INVIMA. Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible y el puntaje TxGNN es muy alto. Sin embargo, la evidencia directa en bronquitis se limita a ensayos pequeños de bronquitis eosinofílica y a un ensayo de bronquitis obstructiva recurrente con estado desconocido. Las revisiones señalan resultados poco concluyentes en bronquiolitis. Además, falta el prospecto de INVIMA, un vacío bloqueante para el tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), incluida la advertencia neuropsiquiátrica.
- Confirmar el mecanismo de acción en DrugBank y las indicaciones originales aprobadas.
- Definir el subtipo objetivo (bronquitis eosinofílica u obstructiva recurrente en niños) y buscar resultados de NCT04613180 y NCT01121016.
- Realizar una revisión sistemática de los ensayos en bronquitis eosinofílica y bronquiolitis.
- Nota: las indicaciones predichas de asma (L1) y enfermedad pulmonar obstructiva (L1, sustentada sobre todo por asma) tienen evidencia más sólida, pero corresponden a usos ya conocidos y no a un reposicionamiento real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

