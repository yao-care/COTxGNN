---
layout: default
title: Acetylcysteine
parent: Evidencia Alta (L1-L2)
nav_order: 24
evidence_level: L2
indication_count: 10
---

# Acetylcysteine
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Acetilcisteína: De Mucolítico (indicación no detallada en el registro) a Enfermedad Trombótica

## Resumen en Una Frase

La acetilcisteína (NAC) es un fármaco mucolítico y antioxidante comercializado en Colombia. Los registros sanitarios solo mencionan el principio activo y no detallan la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **enfermedad trombótica**, sobre todo en púrpura trombocitopénica trombótica (PTT) y microangiopatía trombótica asociada a trasplante (MAT-AT).
Hay **10 ensayos clínicos** y **20 publicaciones** asociados a esta predicción. Solo un ensayo de Fase 3 está completado y no se aportaron resultados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro (el texto registrado es solo "Acetilcisteína"); uso conocido como mucolítico |
| Nueva Indicación Predicha | Enfermedad trombótica (thrombotic disease) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la acetilcisteína actúa como mucolítico rompiendo puentes disulfuro en el moco, y también como antioxidante que repone glutatión.

Esa misma capacidad de reducir puentes disulfuro es la base de la hipótesis trombótica. La NAC podría reducir los multímeros ultragrandes del factor de von Willebrand (VWF), disminuyendo su capacidad de unirse a plaquetas. Esto sería relevante en la PTT, donde la deficiencia de ADAMTS13 permite acumular esos multímeros y formar trombos microvasculares. Además, su efecto antioxidante podría reducir el daño endotelial, lo que apoya su uso en la MAT-AT.

La relación con la indicación original es indirecta: no es la misma enfermedad, pero comparte el mecanismo bioquímico (acción sobre puentes disulfuro y estrés oxidativo). Hay respaldo preclínico en modelos de PTT en ratón y babuino, además de ensayos clínicos en humanos. La señal es más fuerte en PTT y MAT-AT que en otras condiciones trombóticas.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Fase 3 | Completado | 170 | Seguridad y eficacia de NAC en MAT asociada a trasplante de progenitores hematopoyéticos. Evidencia directa, sin resultados disponibles |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Fase 3 | Desconocido | 260 | NAC para prevenir eventos trombóticos tras trasplante alogénico de progenitores hematopoyéticos. Sin resultados |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Fase 2/3 | Activo, sin reclutar | 44 | Estudio de un solo brazo de NAC como tratamiento de MAT-AT. Resultados aún no disponibles |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Fase 2 | Completado | 40 | RENACTIF: ECA doble ciego cruzado de NAC para reducir el fenotipo trombótico en insuficiencia renal |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Fase 1 temprana | Completado | 3 | Piloto de NAC intravenosa en sospecha de PTT en pacientes con plasmaféresis. Muestra muy pequeña, solo genera hipótesis |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Fase 1/2 | Desconocido | 200 | Atorvastatina + NAC + danazol en trombocitopenia inmune (PTI) resistente o recidivante. Relevancia indirecta (trombocitopenia, no trombosis) |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Fase 2 | Desconocido | 44 | Dexametasona a dosis altas + NAC en PTI recién diagnosticada. Relevancia indirecta |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Fase 2 | Desconocido | 30 | NAC para favorecer la recuperación hematopoyética en anemia aplásica grave tras trasplante. No es indicación trombótica |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Fase 1 temprana | Completado | 15 | Atorvastatina + NAC sobre el recuento plaquetario en PTI. Relevancia indirecta |
| [NCT07662525](https://clinicaltrials.gov/study/NCT07662525) | No aplica | Aún sin reclutar | 50 | Atorvastatina + NAC + romiplostim en PTI resistente a corticoides. Relevancia indirecta |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | ECA | Transplant Cell Ther | Ensayo abierto, aleatorizado y controlado con placebo de NAC como profilaxis de MAT-AT tras trasplante (Soochow). El resumen disponible no incluye los resultados |
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Revisión sistemática | J Clin Med | Revisión sistemática y valoración crítica de la NAC en PTT refractaria o recidivante |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Revisión sistemática | Cureus | La NAC se ha explorado como terapia adyuvante en PTT por su capacidad de reducir puentes disulfuro |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohorte | Ann Hematol | Cohorte retrospectiva sobre la asociación entre NAC y mortalidad hospitalaria en PTT adquirida. Su uso sigue siendo controvertido |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclínico | Blood | NAC en modelos de PTT en ratón y babuino, que respaldan el mecanismo sobre el VWF |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revisión | Expert Rev Hematol | Fármacos reposicionados y nuevos agentes en PTT, entre ellos la NAC junto a rituximab, bortezomib y caplacizumab |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisión | J Clin Med | Fisiopatología, diagnóstico y manejo de la PTT (contexto de la enfermedad) |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revisión | Blood | Revisión general de la PTT y su relación con la deficiencia de ADAMTS13 |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | Reporte de caso | J Pediatr Hematol Oncol | Caso de PTT congénita con insuficiencia renal aguda tratado con plasmaféresis y NAC |
| [28961512](https://pubmed.ncbi.nlm.nih.gov/28961512/) | 2018 | Preclínico | Redox Biol | En diabetes, la NAC atenúa la activación plaquetaria sistémica y la trombosis de vasos cerebrales |

## Información de Mercado en Colombia

El paquete lista 20 registros sanitarios. Los datos entregados incluyen entradas repetidas de solo 2 registros únicos, que se muestran a continuación. También hay una forma en jarabe en las formas farmacéuticas registradas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19970253 | Rinofluimucil® Solución Nasal | Solución nasal | Acetilcisteína (el registro no detalla la indicación) |
| 20094856 | Fluiq® 600 mg | Polvo | Acetilcisteína (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La señal es prometedora en PTT y MAT-AT, con un ensayo de Fase 3 completado, otro de Fase 2/3 en curso y respaldo preclínico. Sin embargo, no hay resultados publicados de esos ensayos y falta la información de seguridad del prospecto, lo que bloquea el tamizaje de seguridad. Por ello, por ahora es una pregunta de investigación y no una recomendación de uso.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener los resultados de NCT03252925, del ECA de PMID 35940529 y de NCT07279610.
- Confirmar la vía de administración: los estudios en PTT usaron NAC intravenosa, y en los datos de Colombia solo aparecen solución nasal, polvo y jarabe.
- Consultar los datos de mecanismo de acción en DrugBank para completar el análisis mecanístico.
- Definir la población objetivo (PTT frente a MAT-AT frente a prevención de trombosis) antes de un estudio piloto local.

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

