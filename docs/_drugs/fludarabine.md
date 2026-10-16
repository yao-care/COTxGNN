---
layout: default
title: Fludarabine
parent: Evidencia Alta (L1-L2)
nav_order: 291
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Fludarabine: nueva indicación predicha, Mieloma de células plasmáticas (plasma cell myeloma) (nivel de evidencia L1). Indicación original: No especificada en el registro sanitario (el texto solo indi…"
---

# Fludarabine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Fludarabina: De Indicación Registrada (sin texto descriptivo) a Mieloma de Células Plasmáticas

## Resumen en Una Frase

Fludarabina es un análogo de purinas (antimetabolito) con registros sanitarios en Colombia, hoy cancelados; el texto de indicación registrado solo repite el nombre del fármaco, sin detallar la enfermedad. El modelo TxGNN predice que podría ser efectivo para **mieloma de células plasmáticas**, con **27 ensayos clínicos** y **20 publicaciones** compilados para esta predicción. Casi toda la evidencia corresponde a su uso como parte del acondicionamiento previo a trasplantes o de la linfodepleción antes de terapia CAR-T, y no como tratamiento antimieloma directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto solo indica "FLUDARABINA") |
| Nueva Indicación Predicha | Mieloma de células plasmáticas (plasma cell myeloma) |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, fludarabina es un análogo de nucleósidos de purina con efecto citotóxico y linfodepletor. Su uso en neoplasias linfoides (como la leucemia linfocítica crónica y los linfomas indolentes) está bien establecido en la práctica clínica.

El mieloma múltiple y la leucemia linfocítica crónica son cánceres de linfocitos B estrechamente relacionados. La relación más sólida con el mieloma no es la de un tratamiento directo: fludarabina forma parte del acondicionamiento de trasplante alogénico (con efecto injerto contra mieloma) y de la linfodepleción, junto con ciclofosfamida, previa a la terapia CAR-T anti-BCMA. Existen además datos preclínicos de actividad antimieloma directa in vitro e in vivo (PMID 17976186), aunque su beneficio clínico proviene sobre todo de hacer posible la terapia celular.

Por ello, la predicción es plausible, pero con una salvedad importante: el fármaco actúa como agente de apoyo dentro de regímenes combinados, y los ensayos no aíslan su contribución individual.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes de los 27 compilados (hasta 10).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Fase 3 | Activo, sin reclutar | 79 | Ide-cel + lenalidomida vs. lenalidomida sola en mieloma de nuevo diagnóstico con respuesta subóptima tras trasplante autólogo; fludarabina forma parte de la linfodepleción |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Fase 3 | Reclutando | 750 | Consolidación con CAR-T dual BCMA/CD19 (AZD0120) vs. terapia continua en mieloma no elegible para trasplante; sin resultados aún |
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Fase 2 | Terminado | 6 | Busulfán, fludarabina y ciclofosfamida con trasplante de donante en mieloma o mielofibrosis; terminado con solo 6 participantes |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Fase 2 | Completado | 16 | Trasplante autólogo seguido de alogénico no mieloablativo haploidéntico con acondicionamiento basado en fludarabina |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Fase 2 | Completado | 213 | Trasplante de cordón umbilical con ciclofosfamida/fludarabina/irradiación corporal total; el mieloma es un subgrupo |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Fase 1 | Completado | 20 | Fludarabina + metoxiamina (TRC102) en neoplasias hematológicas recidivantes o refractarias |
| [NCT03093168](https://clinicaltrials.gov/study/NCT03093168) | Fase 1 | Desconocido | 10 | Células T dirigidas a BCMA en mieloma; fludarabina solo como linfodepleción |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Fase 1 | Activo, sin reclutar | 16 | Células CAR-T TriPRIL en mieloma recidivante/refractario; fludarabina y ciclofosfamida para linfodepleción |
| [NCT00909948](https://clinicaltrials.gov/study/NCT00909948) | Fase 1 | Terminado | 7 | Rechazo intencional del injerto del donante tras trasplante alogénico no mieloablativo |
| [NCT05577000](https://clinicaltrials.gov/study/NCT05577000) | Fase 1 | Activo, sin reclutar | 5 | CAR-T anti-BCMA en mieloma recidivante/refractario |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | Estudio de práctica real | Transplantation and Cellular Therapy | La exposición a fludarabina en la linfodepleción se asocia con toxicidades tras ide-cel en mieloma recidivante/refractario |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Cohorte | J Hematol Oncol | Seguimiento a 5 años de LEGEND-2 con CAR-T anti-BCMA: remisiones profundas y duraderas |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohorte | Blood | Cilta-cel en práctica habitual para mieloma recidivante/refractario |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Fase 1 | Am J Clin Oncol | Bortezomib, fludarabina y melfalán, con o sin irradiación medular total, como acondicionamiento en mieloma de alto riesgo |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Análisis retrospectivo multicéntrico | Bone Marrow Transplant | Acondicionamiento de toxicidad reducida con fludarabina y treosulfán en 34 pacientes con mieloma |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Fase 2 | Leukemia Research Reports | Trasplante alogénico con busulfán fraccionado, fludarabina y ciclofosfamida; 6 pacientes (4 con mielofibrosis, 2 con mieloma); mortalidad no atribuible a recaída del 33,3 % al año |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Cohorte | J Clin Oncol | Seguimiento a largo plazo de CAR-T BCMA + CD19 en mieloma |
| [1415309](https://pubmed.ncbi.nlm.nih.gov/1415309/) | 1992 | Revisión | Am J Med | Paralelos y contrastes entre mieloma múltiple y leucemia linfocítica crónica |
| [24686988](https://pubmed.ncbi.nlm.nih.gov/24686988/) | 2014 | Revisión (posición de consenso) | Bone Marrow Transplant | Movilización de células madre autólogas en mieloma y linfoma |
| [14642177](https://pubmed.ncbi.nlm.nih.gov/14642177/) | 2003 | Serie de casos | Zhonghua Xue Ye Xue Za Zhi | 17 casos de trasplante no mieloablativo con acondicionamiento que incluye fludarabina |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 203335 (cancelado) | FLUDARA® | Polvo liofilizado para reconstituir a solución inyectable | FLUDARABINA |
| 20026268 (cancelado) | FLUDARABINA 50 MG INYECTABLE | Polvo liofilizado para reconstituir a solución inyectable | FLUDARABINA |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósidos de purina / antimetabolito) |
| Riesgo de Mielosupresión | Alto (se usa para linfodepleción y acondicionamiento de trasplante; la bibliografía describe mielosupresión significativa) |
| Clasificación de Emetogenicidad | Baja a moderada (clasificación general de la clase; consultar el prospecto) |
| Items de Monitoreo | Hemograma con diferencial, función renal y hepática, signos neurológicos (neurotoxicidad descrita a dosis altas) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 369 interacciones potenciales. Entre las clasificadas con nivel de gravedad están las de nivel moderado con metronidazol, rosuvastatina, simvastatina y tinidazol, y de nivel menor con levofloxacino. Otras (por ejemplo, anfotericina B, ácido acetilsalicílico, metformina, omeprazol, morfina) figuran con nivel desconocido.
- **Otros riesgos descritos en la literatura**: neurotoxicidad a dosis altas, mielosupresión significativa y riesgo de síndrome mielodisplásico/leucemia mieloide aguda secundarios tras combinaciones con fludarabina. Los datos de la literatura también asocian una mayor exposición a fludarabina con más toxicidad tras CAR-T.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen ensayos de Fase 3 que incorporan fludarabina en la linfodepleción para terapias CAR-T en mieloma, además de varios estudios de acondicionamiento de trasplante y datos preclínicos de actividad directa. Sin embargo, el fármaco actúa como componente de regímenes combinados y no como tratamiento antimieloma independiente. Además, los ensayos de Fase 3 siguen en curso, sin resultados, y no aíslan su efecto.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde fuentes farmacológicas
- Obtener y analizar el prospecto (advertencias y contraindicaciones), actualmente sin datos
- Aclarar el estado regulatorio: los dos registros sanitarios en Colombia están cancelados, por lo que cualquier uso requeriría un registro vigente o una vía de importación
- Definir el papel específico de fludarabina (linfodepleción o acondicionamiento) y su dosificación, con vigilancia de toxicidad y función renal
- Resultados de los ensayos de Fase 3 en curso (NCT06045806, NCT07764978)

**Nota sobre otras predicciones:** las demás indicaciones predichas con puntaje alto, como hipertiroidismo, nefropatía diabética y varios síndromes genéticos raros, no tienen un vínculo mecanístico plausible y quedan en espera (Hold). El síndrome mielodisplásico (L2) y el mieloma indolente (L1) muestran evidencia de acondicionamiento de trasplante y merecerían una evaluación independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

