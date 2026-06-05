---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 5
---

# Montelukast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Montelukast: De Asma a Bronquitis

## Resumen en Una Frase

Montelukast es un antagonista selectivo del receptor de cisteinil-leucotrieno (CysLT1), globalmente aprobado para el tratamiento del asma y la rinitis alérgica, aunque actualmente sin registro sanitario activo en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis** (incluyendo bronquiolitis viral, bronquitis obstructiva recurrente y bronquitis eosinofílica no asmática), con **23 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección.
La evidencia más sólida se concentra en el subtipo de bronquiolitis viral pediátrica y en la bronquitis obstructiva recurrente, donde la vía de los leucotrienos está fisiopatológicamente implicada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma y rinitis alérgica (aprobación global; sin registro activo en Colombia) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Montelukast actúa bloqueando el receptor CysLT1, lo que impide que las cisteinil-leucotrienas (LTC4, LTD4 y LTE4) ejerzan sus efectos inflamatorios sobre la vía aérea. Este mecanismo inhibe directamente la broncoconstricción mediada por leucotrienos, la hipersecreción mucosa y la infiltración eosinofílica, procesos centrales en varios tipos de bronquitis. En particular, la vía de los leucotrienos juega un papel clave en la remodelación de la vía aérea y en los episodios repetidos de sibilancias en la infancia, lo que explica por qué el modelo TxGNN conecta este fármaco con la bronquitis.

La bronquitis comparte un sustrato inflamatorio importante con el asma (indicación establecida de Montelukast), especialmente en sus presentaciones virales y eosinofílicas. En la bronquiolitis por virus respiratorio sincitial (VRS), se ha documentado un aumento de cisteinil-leucotrienas en el espacio aéreo de los lactantes, proporcionando una base bioquímica directa para el uso de este fármaco. De manera análoga, en la bronquitis eosinofílica no asmática (NAEB), el bloqueo de CysLT1 tiene soporte mecanístico explícito, con estudios publicados que demuestran reducción de la eosinofilia en esputo y mejoría de la puntuación de tos cuando Montelukast se añade al tratamiento con corticosteroides inhalados. Por el contrario, la evidencia mecanística es más débil para la bronquitis bacteriana aguda, donde predomina la inflamación neutrofílica.

Dado que Montelukast no tiene registro en Colombia, este escenario representa una oportunidad de reposicionamiento local a partir de evidencia global. Es importante destacar que la evidencia es más robusta para la población pediátrica (bronquiolitis viral recurrente, edad 1-7 años) que para adultos. La herramienta TxGNN reconoce la continuidad biológica entre asma y bronquitis eosinofílica/viral, lo cual es consistente con el concepto de "espectro atópico de la vía aérea".

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Fase 4 | Desconocido | 100 | RCT directo en niños de 1-7 años con bronquitis obstructiva recurrente; evalúa efectividad de Montelukast sódico en tratamiento y prevención de episodios. Estado desconocido, requiere seguimiento de resultados |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completado | 146 | Efecto de Montelukast en bronquiolitis aguda y sibilancias post-bronquiolitis viral en lactantes de 3-12 meses; alta relevancia para la indicación de bronquiolitis en la primera infancia |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Fase 3 | Completado | 1.125 | Gran ensayo multicéntrico doble ciego comparando dos dosis de MK-0476 vs. placebo en síntomas respiratorios por bronquiolitis inducida por VRS en niños de 3-24 meses |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completado | 141 | Ensayo doble ciego controlado con placebo de Montelukast diario en bronquiolitis viral; resultado primario: duración de la enfermedad aguda en lactantes con primer episodio de bronquiolitis |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Fase 4 | Desconocido | 63 | Montelukast adicionado a budesonida inhalada vs. dosis doble de budesonida en bronquitis eosinofílica no asmática (NAEB); objetivos: reducción de eosinofilia en vía aérea y puntuación VAS de tos |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Fase 4 | Completado | 49 | Utilidad del feNO para distinguir causas de tos crónica (incluyendo bronquitis); comparación de respuesta a Montelukast vs. prednisolona medida por contador de tos en 24 horas |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Fase 4 | Completado | 100 | Montelukast oral añadido al tratamiento estándar máximo en niños preescolares hospitalizados con cuadro obstructivo agudo; evalúa beneficio adicional sobre el manejo convencional |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Fase 4 | Completado | 30 | Montelukast para Síndrome de Bronquiolitis Obliterante (BOS) post-trasplante pulmonar; basado en eficacia previamente observada en BOS post-trasplante de médula ósea, con posible efecto sobre fibrosis progresiva |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Fase 2 | Completado | 36 | Régimen FAM (fluticasona + azitromicina + Montelukast) en BOS de nuevo inicio post-trasplante de células madre; punto final primario: falla de tratamiento definida como caída ≥10% en FEV1 |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completado | 51 | Montelukast en bronquiolitis aguda por VRS; evaluación de perfil de citocinas, progresión clínica y papel del aumento de leucotrienas en la fase aguda de la infección |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | Ensayo Clínico | Chinese Medical Journal | Montelukast + budesonida vs. budesonida sola en bronquitis eosinofílica no asmática: mejoría significativa en puntuación de tos, calidad de vida y reducción de eosinofilia en esputo; evidencia directa del beneficio del bloqueo CysLT1 en NAEB |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Revisión Sistemática | Pediatric Allergy Immunology | Revisión sistemática sobre eficacia de Montelukast para prevenir sibilancias post-bronquiolitis por VRS; señala que las cisteinil-leucotrienas son liberadas durante la infección por VRS y contribuyen a la patogenia de la inflamación de vía aérea posterior |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Revisión | Therapeutic Advances in Respiratory Disease | Revisión del potencial terapéutico de Montelukast en síndrome de bronquiolitis obliterante (BOS) post-trasplante; analiza mecanismos via TH-1/TH-2, NF-κB y TGF-β; resume la evidencia de ensayos clínicos disponibles |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Ensayo Fase 2 | Transplantation and Cellular Therapy | Ensayo prospectivo fase 2 multicéntrico de Montelukast en BOS post-trasplante de células hematopoyéticas; evalúa si el bloqueo de CysLT altera el declive de la función pulmonar e investiga la patogénesis del BOS |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Ensayo Fase 2 | Biology of Blood and Marrow Transplantation | Régimen FAM en BOS de nuevo inicio post-HCT: el 67% de los pacientes no presentó falla de tratamiento al año; hipótesis de que el Montelukast puede abortar la progresión temprana del BOS cuando se administra precozmente |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Estudio Clínico | Respiratory Research | Budesonida/formoterol + Montelukast + N-acetilcisteína en BOS post-HSCT; propuestos como alternativa a corticosteroides sistémicos con mayor perfil de seguridad y eficacia comparable |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Estudio Animal | J Cardiothoracic Surgery | Papel de LTB4 y Montelukast en bronquiolitis obliterante post-trasplante pulmonar en ratas; Montelukast redujo el rechazo crónico mediante inhibición de la vía del leucotrieno B4 y disminución de la fibrosis |
| [20442434](https://pubmed.ncbi.nlm.nih.gov/20442434/) | 2010 | Estudio Preclínico | Am J Respir Crit Care Med | Montelukast durante la infección primaria por VRS previene hiperrespuesta bronquial, inflamación eosinofílica e hipersecreción mucosa tras reinfección en modelo murino; proporciona base preclínica para uso en bronquiolitis viral |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | Estudio Piloto | Respiratory Medicine | Montelukast vs. dosis doble de budesonida en bronquitis eosinofílica no asmática: el régimen combinado sugiere efecto antiinflamatorio aditivo del bloqueo de leucotrienos sobre los corticosteroides inhalados |
| [25846070](https://pubmed.ncbi.nlm.nih.gov/25846070/) | 2016 | Estudio Clínico | World Journal of Pediatrics | Características de bronquiolitis por VRS con coinfección de Mycoplasma pneumoniae y terapia adicionada de Montelukast; los resultados sobre la eficacia del LTRA en este subgrupo complejo fueron no concluyentes |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa (advertencias, contraindicaciones e interacciones no disponibles en esta evaluación).

**Advertencia de relevancia crítica documentada en la literatura del Evidence Pack**: Múltiples publicaciones incluidas en este paquete (PMID 37758273, PMID 30905424, PMID 35608857, PMID 36948487, PMID 39836401) documentan la asociación entre Montelukast y eventos neuropsiquiátricos. En 2020, la FDA añadió una advertencia en caja negra (*Black Box Warning*) que incluye: agitación, agresión, ansiedad, depresión, desorientación, alucinaciones, insomnio, irritabilidad, pesadillas, sonambulismo y comportamiento suicida. Este riesgo es especialmente relevante para la indicación en bronquitis pediátrica, que representa la población de mayor interés en este contexto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La vía de los cisteinil-leucotrienos está directamente implicada en la fisiopatología de la bronquiolitis viral y la bronquitis eosinofílica, y existen múltiples ensayos clínicos completados — incluyendo un Fase 3 multicéntrico con 1.125 pacientes en bronquiolitis por VRS y estudios directos en bronquitis obstructiva recurrente — que justifican avanzar con precaución. La principal barrera no es la evidencia clínica, sino la ausencia de registro en Colombia y la necesidad de manejo riguroso del riesgo neuropsiquiátrico.

**Para avanzar se necesita:**
- Iniciar trámite de registro sanitario ante el INVIMA si se proyecta comercialización en Colombia
- Obtener el prospecto oficial actualizado (incluyendo la Black Box Warning de 2020) para completar la evaluación de seguridad formal
- Consultar la base de datos DrugBank para recuperar el mecanismo de acción detallado y las categorías de interacciones medicamentosas
- Definir con precisión la subpoblación objetivo: niños con bronquiolitis viral recurrente (1-7 años) vs. adultos con bronquitis eosinofílica no asmática, ya que el perfil de evidencia y el balance beneficio-riesgo difieren entre estos grupos
- Diseñar un protocolo activo de monitoreo de eventos neuropsiquiátricos para cualquier uso en población pediátrica, con educación a cuidadores sobre señales de alerta temprana
- Evaluar si la indicación de bronquitis califica como uso compasivo o extensión de etiqueta a partir de la evidencia de asma ya registrada globalmente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

