---
layout: default
title: Imiquimod
parent: Solo Predicción del Modelo (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imiquimod: nueva indicación predicha, Neoplasia premaligna (nivel de evidencia L5). Indicación original: No especificada en el registro INVIMA (solo figura el nombre del prin…"
monitor_inn: "IMIQUIMOD"
predicted_indications: ["benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

# Imiquimod: De Indicación Original (no especificada en el registro) a Neoplasia Premaligna

## Resumen en Una Frase

Imiquimod es un inmunomodulador de uso tópico (crema) que en Colombia contó con registros sanitarios, hoy cancelados, aunque el registro no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia premaligna**, con **2 ensayos clínicos** y **9 publicaciones** que respaldan esta dirección.
La evidencia clínica es limitada: un ensayo de Fase 3 completado (20 pacientes) y otro terminado prematuramente con solo 9 participantes.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro INVIMA (solo figura el nombre del principio activo) |
| Nueva Indicación Predicha | Neoplasia premaligna |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 según la clasificación de los datos compilados; sin embargo, los dos ensayos de Fase 3 son muy pequeños (uno terminado con 9 participantes), por lo que la solidez real es menor |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el registro compilado. Según el conocimiento farmacológico establecido, imiquimod es un agonista del receptor tipo Toll 7 (TLR7) que activa localmente la inmunidad innata y adaptativa (interferón alfa, TNF-alfa, IL-12). Esta activación favorece la eliminación de células epiteliales displásicas.

Este mecanismo es coherente con su uso establecido en queratosis actínica, una lesión premaligna cutánea, y con su empleo fuera de indicación en neoplasias intraepiteliales (cervical, vulvar, anal) y en papulosis bowenoide. Por ello, la predicción de TxGNN para neoplasia premaligna resulta biológicamente plausible.

Cabe aclarar que este vínculo se apoya en la farmacología conocida de imiquimod y no en el campo de mecanismo de acción del registro, que está vacío.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Fase 3 | Completado | 20 | Estudio abierto de imiquimod crema 5% tres días por semana en queratosis actínicas de la cabeza; evalúa la duración del efecto. Diseño de un solo brazo y muestra pequeña. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | Ensayo aleatorizado de imiquimod tópico en neoplasia intraepitelial cervical de alto grado (CIN 2-3) como alternativa a la escisión. Terminado con solo 9 participantes, sin potencia para concluir sobre eficacia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revisión (Cochrane) | Cochrane Database Syst Rev | Intervenciones para la neoplasia intraepitelial del canal anal, asociada a VPH, especialmente en hombres VIH positivos que tienen sexo con hombres. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revisión (Cochrane) | Cochrane Database Syst Rev | Intervenciones médicas para la neoplasia intraepitelial vulvar de alto grado, con alta morbilidad y recurrencia tras la cirugía. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revisión | Int J Mol Sci | Tratamientos combinados con terapia fotodinámica para cáncer de piel no melanoma. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revisión | Skin Therapy Lett | Manejo actual de las queratosis actínicas, lesiones premalignas con potencial de progresar a carcinoma escamoso. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revisión | Semin Cutan Med Surg | Estrategias tópicas (fluorouracilo, diclofenaco, imiquimod, terapia fotodinámica) para cáncer de piel no melanoma y lesiones precursoras. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Reporte de caso | Int J STD AIDS | Tratamiento exitoso de neoplasia intraepitelial vulvar de alto grado con imiquimod 5% en una receptora de trasplante renal. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Reporte de caso | Int J STD AIDS | Resolución de papulosis bowenoide del pene con imiquimod 5%, bien tolerada. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclínico | Urol Oncol | Farmacocinética y farmacodinamia de agonistas TLR7 en modelo de rata; contexto de uso en lesiones (pre)malignas. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128548 (cancelado) | VIROSUPRIL® CREMA 3.75% | Crema tópica | IMIQUIMOD (el registro no detalla la indicación) |
| 19967737 (cancelado) | VIROSUPRIL® CREMA | Crema tópica | IMIQUIMOD (el registro no detalla la indicación) |

Ambos registros pertenecen a MEGALABS COLOMBIA S.A.S y están cancelados, por lo que actualmente no hay productos vigentes con imiquimod como único principio activo.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** respuesta fotoparoxística, enfermedad por fotosensibilidad, enfermedad autoinmune, enfermedad injerto contra huésped y quemadura solar.
- **Interacciones farmacológicas:** se identificaron 59 posibles interacciones, todas con nivel de gravedad no clasificado. Entre las primeras listadas figuran pantoprazol, morfina, omeprazol, lansoprazol, prednisona, simvastatina, loperamida, prednisolona, ácido acetilsalicílico, bupropión, budesonida, warfarina, clopidogrel e hidroxicloroquina.
- **Señales de la literatura:** se describió conversión maligna de papilomatosis oral florida durante el tratamiento con imiquimod, y casos aislados de eritema multiforme y liquen planopilar asociados a su uso tópico. Esto exige cautela, sobre todo en mucosas.

No se dispone de las advertencias del prospecto de INVIMA; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado en queratosis actínica y literatura que respalda el uso de imiquimod en lesiones premalignas, con un mecanismo plausible. Sin embargo, los ensayos son muy pequeños, el producto no tiene registro vigente en Colombia y faltan datos de seguridad del prospecto, por lo que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), lo cual es un requisito bloqueante para el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Definir la lesión premaligna específica (queratosis actínica, neoplasia intraepitelial cervical, vulvar, anal) y la población objetivo, dado que el término es muy amplio.
- Evaluar la vía regulatoria, ya que los registros actuales están cancelados.
- Establecer un plan de monitoreo de reacciones locales y de seguridad en mucosas, con atención a fotosensibilidad y enfermedades autoinmunes.

---

*Nota: otras predicciones de menor rango (neoplasia benigna de mucosa bucal, quiste odontogénico, entre otras) cuentan con evidencia más débil o nula y no se desarrollan en este informe.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

