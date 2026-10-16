---
layout: default
title: Ketamine
parent: Solo Predicción del Modelo (L5)
nav_order: 365
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Ketamine: nueva indicación predicha, Trastorno de cefalea (headache disorder) (nivel de evidencia L5). Indicación original: KETAMINA"
---

# Ketamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Ketamina: De Uso Anestésico/Inyectable (KETAMINA I.V.) a Trastorno de Cefalea

## Resumen en Una Frase

Ketamina está registrada en Colombia como solución inyectable (KETAMINA I.V.), y el registro sanitario no detalla una indicación más allá del nombre del producto.
El modelo TxGNN predice que podría ser efectiva para **trastorno de cefalea**,
con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque la evidencia directa es de tamaño pequeño.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | KETAMINA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Trastorno de cefalea (headache disorder) |
| Puntaje de Predicción TxGNN | 99.33% |
| Nivel de Evidencia | L1 (condicionado: ver nota en la conclusión) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología conocida, la ketamina es un antagonista del receptor NMDA de glutamato. Este razonamiento se infiere del conocimiento farmacológico general y no del registro proporcionado.

La sensibilización central y la señalización glutamatérgica contribuyen a la migraña, la cefalea en racimos y el dolor de cabeza crónico. El bloqueo de los receptores NMDA podría atenuar la depresión cortical propagada, la transmisión nociceptiva trigeminovascular y el fenómeno de "wind-up" (amplificación progresiva del dolor). Esto ofrece un mecanismo plausible para un efecto analgésico en los trastornos de cefalea.

La indicación original registrada es poco específica, por lo que la relación con la nueva indicación se apoya sobre todo en el mecanismo y en la evidencia clínica. El puntaje TxGNN (0.993) es solo una predicción computacional y no constituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Fase 3 | Completado | 80 | Ensayo THINK: ketamina intranasal en dosis subdisociativa frente a tratamiento estándar en cefalea aguda en urgencias |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Fase 3 | Reclutando | 56 | Ketamina IV de dosis alta (1 mg/kg/h durante 6 h) frente a placebo en cefalea diaria crónica (KetHead); sin resultados aún |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Fase 4 | Completado | 54 | Ketamina en dosis baja frente a proclorperazina para cefalea en urgencias |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completado | 34 | Ketamina subdisociativa frente a placebo en migraña aguda en urgencias |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Fase 4 | Completado | 93 | Infusión única de ketamina con sulfato de magnesio en cefalea en racimos crónica refractaria |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Fase 4 | Desconocido | 60 | Ketamina frente a ketorolaco en cefalea tensional aguda |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Fase 1/2 | Completado | 23 | Prueba de concepto de espray intranasal de ketamina en cefalea en racimos crónica |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Fase 4 | Completado | 5 | Ketamina oral + aspirina frente a rimegepant en cefalea aguda; muestra muy pequeña |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Completado | 300 | Estudio PACE de analgésicos; relevancia indirecta para cefalea |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía | Headache | Actualización 2025 de la guía de la American Headache Society sobre farmacoterapia parenteral para migraña aguda en urgencias |
| [34703891](https://pubmed.ncbi.nlm.nih.gov/34703891/) | 2021 | Revisión sistemática | J Dent Anesth Pain Med | Eficacia de ketamina en migraña y otras cefaleas primarias frente a placebo y otras intervenciones |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Cohorte retrospectiva | Front Neurol | Infusiones de lidocaína y ketamina en trastornos de cefalea: eficacia, duración y seguridad |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Revisión sistemática y metaanálisis | J Neurol | Tratamiento preventivo de la cefalea en racimos crónica refractaria |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Revisión | Drugs | Tratamiento farmacológico de la cefalea en racimos (ataques agudos y profilaxis) |
| [34894295](https://pubmed.ncbi.nlm.nih.gov/34894295/) | 2021 | Revisión | Curr Pain Headache Rep | Ketamina, lidocaína y otras terapias IV para migraña crónica refractaria |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revisión | Expert Rev Neurother | Farmacoterapia de la neuralgia del trigémino; ketamina como posible coadyuvante |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Revisión | Curr Neurol Neurosci Rep | Manejo de cefalea pediátrica en urgencias y hospitalización |

Nota: el conjunto de literatura incluye además estudios sobre ketamina en depresión y otros usos, que no respaldan directamente la indicación de cefalea y no se listan aquí.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49510 (cancelado) | KETAMINA I.V. | Solución inyectable | KETAMINA |

Fabricante: FEPARVI S.A.S. Actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia la ketamina con contraindicación en: hipertensión arterial, hipertensión ocular, hipertensión intracraneal y pseudotumor cerebral; accidente cerebrovascular, enfermedad cerebrovascular e infarto cerebral; infarto de miocardio, isquemia miocárdica, trombosis coronaria y enfermedad arterial coronaria; insuficiencia respiratoria; tirotoxicosis, hipertiroidismo y enfermedad de Graves; delirio; abuso o dependencia de sustancias; y hemoglobinopatías.
- **Interacciones farmacológicas**: se identificaron 111 interacciones. Entre las de nivel moderado figuran morfina (incluida la liposomal), difenoxilato, opio, dronabinol, nabilona, metoclopramida, sibutramina, fentermina, efedrina, fenfluramina, isometepteno y epinefrina tópica. Otras con nivel no clasificado: atropina, anfotericina B, famotidina, omeprazol, cloruro de potasio, ondansetrón y ácido ursodesoxicólico. Predominan combinaciones con depresores del SNC y con agentes simpaticomiméticos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto, ya que no se dispone de esa información en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos clínicos directamente relacionados con cefalea (incluido un ensayo de Fase 3 completado y otro de Fase 3 en curso), junto con revisiones sistemáticas, pero las muestras son pequeñas y no se dispone de resultados. El nivel L1 asignado por el sistema es optimista: solo hay un ECA de Fase 3 completado (n=80) y sus resultados no se han verificado, por lo que el nivel real podría ser menor hasta confirmarlos. Además, el único registro sanitario en Colombia está cancelado, y el perfil de contraindicaciones cardiovasculares y cerebrovasculares exige cautela.

**Para avanzar se necesita:**
- Revisar los resultados publicados de THINK (NCT03081416) y de los demás ensayos completados, y esperar los de KetHead (NCT05306899).
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Confirmar el mecanismo de acción con DrugBank.
- Definir la vía de administración requerida (intravenosa vs. intranasal) y su disponibilidad en Colombia, dado que no hay registro vigente.
- Establecer criterios de exclusión y monitoreo cardiovascular y de presión arterial, y evaluar el riesgo de abuso por ser sustancia controlada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

