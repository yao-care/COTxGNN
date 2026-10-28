---
layout: default
title: Cefazolin
parent: Solo Predicción del Modelo (L5)
nav_order: 142
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Cefazolin: nueva indicación predicha, Otitis media infecciosa (nivel de evidencia L4). Indicación original: CEFAZOLINA"
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
---

# Cefazolin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Cefazolina: De Indicación Registrada No Especificada a Otitis Media Infecciosa
{: .text-alpha }

## Resumen en Una Frase

Cefazolina es una cefalosporina de primera generación, de uso parenteral, cuyo registro sanitario en Colombia no detalla una indicación específica (solo figura el nombre del producto).
El modelo TxGNN predice que podría ser efectiva para **otitis media infecciosa**, pero actualmente **no hay ensayos clínicos registrados** y solo **2 publicaciones** indirectas respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFAZOLINA (el registro sanitario no especifica una indicación clínica) |
| Nueva Indicación Predicha | Otitis media infecciosa |
| Puntaje de Predicción TxGNN | 0.9944 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, cefazolina es una cefalosporina de primera generación que inhibe la síntesis de la pared celular bacteriana y tiene actividad contra bacterias grampositivas, como estreptococos y *Staphylococcus aureus* sensible a meticilina.

Algunos de estos microorganismos participan en la otitis media bacteriana, lo que da un vínculo mecanístico plausible con la nueva indicación. Sin embargo, la cobertura frente a los patógenos más frecuentes de la otitis media (*H. influenzae*, *M. catarrhalis*) es limitada, y el fármaco solo se administra por vía parenteral, lo que reduce su utilidad práctica en una enfermedad que normalmente se trata con antibióticos orales.

La predicción también se extiende a otras formas de otitis media (crónica, supurativa, no supurativa, alérgica) y a bronquitis. Las formas no infecciosas (alérgica) o a menudo no bacterianas (no supurativa, bronquitis viral) tienen un respaldo biológico débil, y es probable que parte de la predicción refleje similitudes que el modelo TxGNN (aprendizaje profundo) aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Reporte de caso | Ann Otol Rhinol Laryngol | Terapia empírica con ceftazidima-cefazolina en síndrome de Gradenigo pediátrico (complicación de otitis media aguda); evidencia indirecta y no controlada |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisión | Clinical Pharmacy | Manejo del síndrome de Stevens-Johnson; menciona otitis media solo como contexto y no es relevante para esta indicación |

**Nota sobre indicaciones relacionadas:** la única comparación humana controlada es un estudio de 1982 en otitis media supurativa (cefmetazol vs. cefazolina, 172 pacientes evaluables, [6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/)), donde cefazolina fue el comparador y no el fármaco en estudio. El resto de la literatura corresponde a series veterinarias, estudios de sensibilidad bacteriana o estudios de otros fármacos.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20152146 (cancelado) | CEFAZOLINA 1 G | Polvo estéril para reconstituir a solución inyectable | CEFAZOLINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): enfermedad de la coagulación sanguínea, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y deficiencia congénita de protrombina.
- **Interacciones farmacológicas** (100 interacciones registradas; las de nivel moderado son las más relevantes): kanamicina, neomicina, estreptomicina (aminoglucósidos) y ácido picosulfúrico. Otras interacciones de nivel desconocido incluyen anfotericina B, ácido acetilsalicílico, amoxicilina, metformina y omeprazol, entre otras.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos clínicos, la literatura es antigua, indirecta o veterinaria, y el único producto registrado en Colombia está cancelado. Además, la limitada cobertura de los patógenos típicos de la otitis media y la vía exclusivamente parenteral restan valor práctico a la predicción.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar sistemáticamente la evidencia moderna sobre cefazolina en otitis media y sus complicaciones (por ejemplo, mastoiditis o síndrome de Gradenigo).
- Evaluar la compatibilidad de vías de administración y el valor frente a las alternativas orales estándar.
- Aclarar la situación regulatoria, dado que el único registro sanitario está cancelado.
- Considerar priorizar otras indicaciones con mayor plausibilidad biológica, ya que las formas alérgica y no supurativa carecen de respaldo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

