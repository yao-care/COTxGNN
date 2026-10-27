---
layout: default
title: Propofol
parent: Solo Predicción del Modelo (L5)
nav_order: 539
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Propofol: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: Propofol"
monitor_inn: "PROPOFOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Prinzmetal angina", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Propofol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Propofol: De Indicación Original (Anestésico General) a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Propofol es un anestésico intravenoso general que actúa sobre los receptores GABA-A, registrado en Colombia en emulsión inyectable.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**,
con **3 ensayos clínicos** y **19 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Propofol (el registro INVIMA solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L1 (a verificar, ver nota abajo) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Propofol es un modulador alostérico positivo del receptor GABA-A. Los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción, pero la farmacología conocida del fármaco permite plantear la siguiente hipótesis: al reforzar la inhibición GABAérgica, podría reducir la hiperexcitabilidad cortical y trigeminovascular.

Existe además respaldo preclínico: el hemisuccinato de propofol suprime la depresión cortical propagada (PMID 22390898), considerada el correlato neural del aura migrañosa y un posible desencadenante del dolor. Esto ofrece una base plausible para un efecto abortivo en migraña refractaria.

La relación entre la indicación original (anestesia/sedación) y la nueva es de uso a dosis subanestésicas en entornos monitorizados (urgencias o sedación procedimental), no de extensión de la indicación original. Se trata de una dosis y un contexto de uso distintos.

**Nota sobre el nivel de evidencia:** el nivel L1 se asignó con base en el listado de un ensayo de Fase 2/3 y en la existencia de una comparación con placebo en adultos en urgencias (PMID 33070469). Los datos disponibles no incluyen resultados, por lo que L1 debe verificarse con los resultados publicados. Si el ensayo pivotal se considera solo de Fase 2 o con poder insuficiente, el nivel debería bajar a L2.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Fase 2/3 | Completado | 74 | Propofol a dosis bajas como terapia abortiva de migraña pediátrica en urgencias; directamente relacionado con la indicación |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | N/A | Completado | 40 | Infusión de propofol a dosis bajas como tratamiento abortivo de migraña en pediatría; evalúa eficacia, límites seguros de dosis y duración del efecto |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | N/A | Terminado | 12 | Propofol a dosis bajas en migraña refractaria grave en urgencias; terminado anticipadamente, con conclusiones limitadas |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33070469](https://pubmed.ncbi.nlm.nih.gov/33070469/) | 2021 | ECA | Emerg Med Australas | Propofol vs. placebo en adultos con migraña aguda en urgencias; el desenlace primario fue la resolución de la cefalea a la hora |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | ECA | J Emerg Med | Propofol a dosis bajas en migraña pediátrica; dosis subanestésicas con perfil de efectos secundarios favorable y posible menor estancia |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | ECA piloto | Emerg Med Australas | Propofol a dosis de sedación procedimental vs. tratamiento estándar en el manejo inicial de la migraña en urgencias |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | ECA | Arch Acad Emerg Med | Propofol + granisetrón vs. propofol + metoclopramida en el manejo de síntomas de migraña aguda |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | ECA | Arch Acad Emerg Med | Sumatriptán/placebo vs. sumatriptán/propofol en migraña aguda |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revisión sistemática | Acad Emerg Med | Seguridad y eficacia de propofol en migraña aguda en urgencias; evidencia limitada |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revisión sistemática/metaanálisis | Headache | Comparación de agentes parenterales para reducir recaídas tras migraña aguda grave |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Revisión sistemática | Headache | Tratamientos agudos de migraña pediátrica en urgencias |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía | Headache | Actualización 2025 de la guía de la American Headache Society sobre tratamientos parenterales de la migraña aguda en urgencias |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Revisión/serie de casos | Expert Rev Neurother | Perfil del propofol a dosis subanestésicas en migraña refractaria |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20007502 (cancelado) | SPIVA® MCT - LCT | Emulsión inyectable | PROPOFOL |
| 20017881 (cancelado) | PROPOFOL 1% MCT | Emulsión inyectable | PROPOFOL |

Ambos registros están cancelados, por lo que actualmente no hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según la base de conocimiento (no según prospecto):** el grafo de conocimiento asocia propofol con epilepsia, trastornos hipotensivos, insuficiencia respiratoria, arteriosclerosis intracraneal, trastornos hereditarios del metabolismo lipídico e hiperlipidemia familiar.
- **Riesgos clínicos relevantes:** sedación, depresión respiratoria e hipotensión; el uso debe limitarse a entornos monitorizados (urgencias o procedimentales).
- **Señal cardiovascular:** reportes de caso describen espasmo coronario inducido por anestesia y angina vasoespástica revelada durante la anestesia con propofol.
- **Interacciones farmacológicas (100 registradas; se muestran las principales):**
  - Moderadas: morfina (incluida liposomal), opio, ondansetrón, granisetrón, dolasetrón, claritromicina, levofloxacino, cisaprida, famotidina, loperamida, bisacodilo, aceite de ricino, glicerina, lactitol, lactulosa, citrato de magnesio, hidróxido de magnesio y aceite mineral.
  - Leve: metronidazol.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo completado de Fase 2/3 y varios ECA publicados en migraña aguda (adultos y pediátrica) que respaldan la dirección, además de una base mecanística plausible. Sin embargo, no se dispone de resultados cuantitativos en los datos compilados, la evidencia es heterogénea y los dos registros colombianos están cancelados.

**Para avanzar se necesita:**
- Verificar el nivel L1 con los resultados publicados de los ensayos (NCT01604785 y PMID 33070469); si no se confirma, bajar a L2.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones oficiales.
- Documentar el mecanismo de acción desde DrugBank.
- Definir un protocolo de uso limitado a entornos monitorizados, con vigilancia de sedación, función respiratoria y presión arterial.
- Evaluar la disponibilidad de un producto con registro vigente en Colombia.

---

### Otras indicaciones predichas (de menor prioridad)

| Indicación | Puntaje TxGNN | Nivel | Recomendación | Comentario |
|------|------|------|------|------|
| Migraña con aura del tronco encefálico | 99.58% | L3 | Pregunta de investigación | Sin ensayos específicos; evidencia extrapolada de migraña general y respaldo preclínico sobre depresión cortical propagada |
| Angina de Prinzmetal | 99.23% | L4 | Hold | Solo reportes de caso de espasmo coronario durante anestesia; señal de seguridad, no terapéutica |
| Síndrome nefrogénico de antidiuresis inapropiada | 99.20% | L5 | Hold | Sin ensayos ni literatura; no se identifica vía mecanística plausible |
| Síndrome de Tourette | 99.03% | L4 | Hold | Solo estudios de sedación durante cirugía de estimulación cerebral profunda; no evalúan eficacia terapéutica |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

