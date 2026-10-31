---
layout: default
title: Estriol
parent: Evidencia Moderada (L3-L4)
nav_order: 264
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-31
description: "Estriol: nueva indicación predicha, Amenorrea (nivel de evidencia L3). Indicación original: ESTRIOL"
monitor_inn: "ESTRIOL"
predicted_indications: ["amenorrhea (disease)"]
---

# Estriol
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

## Estriol: De Estriol (indicación registrada sin especificar) a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Estriol es un estrógeno natural débil, registrado en Colombia en óvulos vaginales cuyos registros sanitarios hoy figuran cancelados; la indicación aprobada solo aparece como "ESTRIOL", sin detalle clínico.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, con **0 ensayos clínicos** y **6 publicaciones** relacionadas, de las cuales solo dos aportan evidencia directa (una revisión de 2023 y un estudio de cohorte de 2012).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ESTRIOL (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0.9918 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el estriol es un agonista débil de los receptores de estrógeno alfa (ESR1) y beta (ESR2), y se comercializa desde hace décadas en Europa y Asia para los sofocos de la menopausia posmenopáusica.

La amenorrea hipotalámica funcional (AHF) se caracteriza por una secreción alterada y pulsátil de GnRH, lo que reduce LH y FSH y produce un estado de hipoestrogenismo. Un estrógeno en dosis bajas podría actuar como modulador neuroendocrino: restablecer la retroalimentación sobre el eje hipotálamo-hipófisis, normalizar parcialmente la secreción de LH y compensar los efectos de la deficiencia de estrógenos (por ejemplo, la pérdida ósea).

Esta hipótesis se apoya en un estudio de 2012 sobre la administración de estriol y la secreción de LH en mujeres con AHF, y en una revisión de 2023 sobre estrógenos en dosis bajas como moduladores neuroendocrinos. Sin embargo, la evidencia es mecanística y de pequeña escala: no demuestra recuperación de la menstruación ni de la ovulación. El puntaje de 0.9918 proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; es solo una predicción computacional, no evidencia clínica.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Cohorte | Fertility and Sterility | Evalúa el efecto de la administración de estriol sobre el eje hipotálamo-hipófisis y la secreción de gonadotropinas en mujeres con AHF; modula la secreción de LH |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Revisión | Biomedicines | Estrógenos en dosis bajas como moduladores neuroendocrinos en la AHF y posible activación de mecanismos de retroalimentación positiva |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Serie de casos | Am J Obstet Gynecol | Manifestaciones ginecológicas y endocrinas prolongadas tras acetato de medroxiprogesterona durante el embarazo (relevancia indirecta) |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | Ensayo clínico | J Obstet Gynaecol Br Commonw | Gonadotropinas humanas en amenorrea secundaria idiopática (no evalúa estriol) |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Revisión | J Clin Endocrinol Metab | Mecanismo de acción de compuestos antiovulatorios (relevancia indirecta) |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | Revisión | Die Medizinische Welt | Valor clínico del radioinmunoanálisis de LH, FSH, progesterona, estrona, estradiol y estriol (relevancia indirecta) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20007729 | ESTEINE® óvulo vaginal de liberación sostenida (vigente) | Óvulo | ESTRIOL |
| 55341 | OVESTIN® óvulos vaginales (vigente) | Óvulo | ESTRIOL |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología**: el estriol actúa sobre el receptor de estrógeno alfa (ESR1) y el receptor de estrógeno beta (ESR2). No se registraron interacciones con otros fármacos con nivel de gravedad definido.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a un estudio de cohorte pequeño y una revisión sobre mecanismos, sin ensayos clínicos registrados ni resultados de recuperación de menstruación u ovulación. Además, los dos registros sanitarios en Colombia están cancelados y faltan datos de seguridad, por lo que no es posible avanzar con garantías.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío crítico que bloquea la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Ensayos clínicos controlados que evalúen desenlaces clínicos (retorno de la menstruación, ovulación, densidad ósea) en AHF.
- Aclarar la situación regulatoria: reactivación de registros o nueva solicitud, así como la compatibilidad de la vía de administración (vaginal) con el uso propuesto.
- Evaluar la relación con la indicación original, que no está especificada en el registro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

