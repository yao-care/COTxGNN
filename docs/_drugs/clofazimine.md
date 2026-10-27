---
layout: default
title: Clofazimine
parent: Solo Predicción del Modelo (L5)
nav_order: 169
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Clofazimine: nueva indicación predicha, Neumocistosis (nivel de evidencia L5). Indicación original: CLOFAZIMINA"
monitor_inn: "Clofazimine"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
---

# Clofazimine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Clofazimina: De Indicación Original (Clofazimina) a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

Clofazimina es un fármaco antimicobacteriano (de la clase de las riminofenazinas) que en Colombia se registró bajo la denominación "CLOFAZIMINA"; en la literatura se utiliza dentro de esquemas combinados para la lepra y la tuberculosis resistente.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero **no hay ensayos clínicos** y la literatura recuperada no evalúa el fármaco contra *Pneumocystis*.
La predicción se apoya únicamente en el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLOFAZIMINA (el registro sanitario no detalla una indicación en texto) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en los datos compilados para este informe. Según la información conocida, la clofazimina es una riminofenazina antimicobacteriana, con actividad de alteración de membranas y ciclo redox, y se emplea junto con otros antibacterianos en la terapia multifármaco de la lepra y en esquemas para tuberculosis resistente.

La relación con la nueva indicación es débil. *Pneumocystis* es un hongo, y no se reconoce actividad de la clofazimina contra este organismo. No se identificó un vínculo mecanístico directo. El puntaje del modelo es alto (0.999), pero no está respaldado por datos clínicos ni preclínicos.

La literatura recuperada menciona la neumocistosis solo como infección oportunista concurrente en pacientes con sida (por ejemplo, un ensayo de profilaxis contra el complejo *Mycobacterium avium* y un reporte de caso de coinfección). En ninguno de ellos la neumocistosis es el objetivo del tratamiento con clofazimina. Por ello, la predicción debe considerarse especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Ensayo clínico aleatorizado, abierto | The Journal of Infectious Diseases | 110 pacientes con VIH evaluaron clofazimina (50 mg) como profilaxis de infección diseminada por el complejo *M. avium*. No trata *Pneumocystis*; la neumocistosis previa fue solo criterio de inclusión. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Reporte de caso | Infection | Paciente con sida con enfermedad pulmonar por *M. kansasii* y neumonía por *P. carinii*; recuperó con isoniazida, etambutol, clofazimina, ciprofloxacino y, tras la neumonía, trimetoprima-sulfametoxazol. La mejoría de la neumocistosis se atribuye al antimicrobiano específico, no a la clofazimina. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Revisión | PI Perspective | Actualización general sobre infecciones oportunistas; sin resumen disponible ni datos específicos de clofazimina en neumocistosis. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20274960 (cancelado) | CLOFZIMIN® 100 MG | Tableta recubierta | CLOFAZIMINA |

---

## Citotoxicidad

No corresponde: la clofazimina es un antimicobacteriano, no un fármaco antineoplásico, por lo que esta sección no aplica.

---

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones según el grafo de conocimiento del modelo (no provienen del prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, enfermedades diarreicas, úlcera péptica activa, enfermedades del sistema digestivo e intestinales, infarto esplénico, enfermedad del bazo e hiperesplenismo.
- **Interacciones y farmacología:** solo se identificó una asociación de tipo farmacológico con la proteína ZC3H14 (dedo de zinc tipo CCCH 14); no corresponde a una interacción con otro medicamento y no tiene nivel de gravedad asignado. Se reportó además actividad antiviral *in vitro* contra SARS-CoV-2 (CE50 0.31 µM) y MERS-CoV (CE50 1.48 µM), sin relevancia directa para esta predicción.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto, pero no hay ensayos clínicos, ni estudios preclínicos, ni vínculo mecanístico plausible con *Pneumocystis*; la literatura solo menciona la neumocistosis como infección concurrente. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia *in vitro* o en modelos animales de actividad contra *Pneumocystis*.
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Aclarar la situación regulatoria en Colombia (registro cancelado) y la disponibilidad del fármaco.
- Valorar otras predicciones del modelo con más soporte: la malaria presenta evidencia indirecta (un estudio *in vitro* con análogos de clofazimina, nivel L4), aunque también carece de datos clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

