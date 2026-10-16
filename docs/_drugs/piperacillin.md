---
layout: default
title: Piperacillin
parent: Solo Predicción del Modelo (L5)
nav_order: 516
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Piperacillin: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: Piperacilina e inhibidor enzimático"
monitor_inn: "piperacillin"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "osteoarthritis susceptibility", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "WHIM syndrome"]
---

# Piperacillin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Piperacilina: De Antibiótico con Inhibidor Enzimático a Artritis Reumatoide

## Resumen en Una Frase

Piperacilina es un antibiótico betalactámico que en Colombia se registró en combinación con un inhibidor enzimático (piperacilina e inhibidor enzimático) para el tratamiento de infecciones bacterianas.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero **no hay ensayos clínicos** y las **15 publicaciones** recuperadas son en su mayoría reportes de caso donde la artritis reumatoide aparece solo como enfermedad concomitante, por lo que no respaldan realmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Piperacilina e inhibidor enzimático |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, piperacilina es una penicilina de espectro amplio (betalactámico) que inhibe la síntesis de la pared celular bacteriana. Su eficacia está establecida en infecciones bacterianas, no en enfermedades autoinmunes.

El análisis de la relación entre la indicación original y la nueva **no encuentra un vínculo mecanístico creíble**. Piperacilina no tiene actividad antiinflamatoria ni inmunomoduladora conocida relevante para la artritis reumatoide. El puntaje alto de TxGNN (0,999) parece ser un artefacto del grafo de conocimiento y no una señal biológica.

La literatura recuperada menciona la artritis reumatoide solo como comorbilidad en pacientes que recibieron piperacilina/tazobactam por infecciones o eventos adversos (por ejemplo, pancitopenia por metotrexato en pacientes con AR). Esto no constituye evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes. Todas son reportes de caso, cohortes o revisiones en las que la artritis reumatoide es un contexto clínico y no el objetivo del tratamiento con piperacilina.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohorte (modelo predictivo) | Br J Clin Pharmacol | Modelo para predecir eosinofilia inducida por ampicilina/sulbactam o piperacilina/tazobactam |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohorte | Ann Transl Med | Prevalencia y características de la lesión hepática inducida por antibióticos |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Reporte de caso | Proc (Baylor Univ Med Cent) | Pancitopenia por metotrexato en dosis bajas en paciente con AR, tratada con leucovorina |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Reporte de caso | Cureus | Pancitopenia por metotrexato en dosis bajas en AR |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Reporte de caso | Orthopadie (Heidelberg) | Infección por *Haemophilus influenzae* en prótesis de rodilla en paciente con AR tratada con piperacilina/tazobactam por neumonía |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Reporte de caso | Front Immunol | Erisipela ampollosa atípica por *E. coli* en paciente inmunosuprimida con AR de 20 años |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Reporte de caso/Revisión | BMC Infect Dis | Choque séptico por *Edwardsiella tarda* resistente |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Reporte de caso | Cureus | Derrames pleurales recurrentes en paciente con AR en remisión durante nueve años |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Reporte de caso | BMJ Case Rep | Pericarditis purulenta en paciente con AR tratada con etanercept; se inició piperacilina-tazobactam empírica |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Reporte de caso | Med J Aust | Pancitopenia tras sobredosis accidental de metotrexato en AR |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20089767 (cancelado) | AUROTAZ-P 4.5 G | Polvo estéril para reconstituir a solución inyectable | Piperacilina e inhibidor enzimático |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: se identificaron 81 interacciones en total. Las principales por nivel de gravedad:
- **Mayor**: vancomicina.
- **Moderada**: doxiciclina, tetraciclina, minociclina, kanamicina, estreptomicina y picosulfato.
- **Menor**: claritromicina.

Para el resto de las interacciones listadas el nivel de gravedad no está definido.

Se debe consultar el prospecto para advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5): no hay ensayos clínicos ni estudios que evalúen piperacilina como tratamiento de la artritis reumatoide, y no existe un vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado. Las otras ocho indicaciones predichas también carecen de respaldo mecanístico y de evidencia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una justificación biológica verosímil para la artritis reumatoide.
- Estudios preclínicos que muestren un efecto inmunomodulador o antiinflamatorio.
- Revisar el prospecto aprobado por INVIMA para completar advertencias y contraindicaciones.
- Aclarar la situación regulatoria, dado que el único registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

