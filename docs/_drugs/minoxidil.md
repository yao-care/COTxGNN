---
layout: default
title: Minoxidil
parent: Evidencia Moderada (L3-L4)
nav_order: 448
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Minoxidil: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L4). Indicación original: Minoxidil"
monitor_inn: "MINOXIDIL"
predicted_indications: ["congenital hypotrichosis milia", "pulmonary arterial hypertension", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "primary hereditary glaucoma", "pulmonary arterial hypertension associated with schistosomiasis", "pulmonary arterial hypertension associated with chronic hemolytic anemia"]
---

# Minoxidil
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

# Minoxidil: De Minoxidil (sin indicación detallada en el registro) a Hipotricosis simple del cuero cabelludo

## Resumen en Una Frase

Minoxidil es un fármaco con registros sanitarios en Colombia en formas tópicas (loción, solución, aerosol) y oral (tableta). El texto de indicación del registro solo repite el nombre del principio activo. En la práctica clínica se conoce como antihipertensivo vasodilatador y como tratamiento del cabello.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, con **0 ensayos clínicos** y **3 publicaciones** (series o reportes de caso) que respaldan esta dirección de forma limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Minoxidil (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 7 (0 vigentes, 7 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según la información conocida, minoxidil actúa como abridor de canales de potasio (a través de su metabolito sulfato), lo que prolonga la fase anágena del folículo piloso y aumenta el tamaño de los folículos miniaturizados. Esto es mecanísticamente plausible en trastornos hereditarios del crecimiento del cabello.

La hipotricosis simple del cuero cabelludo es una enfermedad genética rara, autosómica dominante, asociada a variantes en el gen CDSN. Hoy no existe un tratamiento definitivo. Como minoxidil ya se usa en otras formas de pérdida de cabello, es razonable que el modelo lo proponga para esta condición.

Sin embargo, la evidencia disponible son reportes de caso en los que minoxidil se combinó con factores de crecimiento, extractos botánicos o plasma rico en plaquetas (PRP). Por eso no es posible separar el efecto del minoxidil del de las demás intervenciones.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Reporte/serie de casos | Dermatologic Therapy | Tratamiento de hipotricosis simple hereditaria del cuero cabelludo con minoxidil oral y factores de crecimiento |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Reporte de caso | J Dermatol Treat | Paciente de 14 años tratada con inyección de PRP combinada con minoxidil tópico al 2% |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Reporte de caso | Frontiers in Genetics | Caso familiar de un niño de 8 años con mutación en CDSN, tratado con extractos botánicos y minoxidil |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128461 | MINO FOAM® 5% | Aerosol | Minoxidil |
| 20236308 | MINOXIDIL 5% LOCIÓN | Loción | Minoxidil |
| 19948594 | VAXDIL® TABLETAS 10MG | Tableta | Minoxidil |
| 20267073 | MINOXIDIL 5% SOLUCIÓN TÓPICA | Solución tópica | Minoxidil |
| 19903008 | PILOGAN® ULTRA 5% | Solución tópica | Minoxidil |

Los 7 registros están cancelados; aquí se muestran los 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): hipotensión ortostática, atrofia multisistémica, síndrome de taquicardia postural ortostática, enfermedad renal, accidente cerebrovascular y trastornos cerebrovasculares, infarto de miocardio, enfermedad cardiovascular y cardíaca, feocromocitoma y paraganglioma simpático, derrame pericárdico, taponamiento cardíaco y pericarditis, hemoglobinopatías, y dermatosis del cuero cabelludo.
- **Interacciones farmacológicas** (se identificaron 100 en total; principales de nivel moderado): corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), bupropión, morfina, opio, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), dronabinol, nabilona y sapropterina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje muy alto, pero solo se apoya en tres reportes de caso con terapias combinadas y sin ensayos registrados. Además, los 7 registros sanitarios colombianos están cancelados y no se dispone de información de seguridad de prospecto.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios que aíslen el efecto del minoxidil (series más grandes o ensayos controlados).
- Aclarar la situación regulatoria, dado que no hay registros vigentes en Colombia.
- Evaluar la seguridad en población pediátrica, dado que los casos reportados incluyen niños y adolescentes, y tener en cuenta las contraindicaciones cardiovasculares señaladas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

