---
layout: default
title: Ciclesonide
parent: Solo Predicción del Modelo (L5)
nav_order: 156
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Ciclesonida: De Indicación Registrada (Ciclesonida inhalada) a Eccema Atópico

## Resumen en Una Frase

Ciclesonida es un corticosteroide inhalado (profármaco) que cuenta con registros sanitarios en Colombia, hoy cancelados, en solución para inhalación; su indicación aparece registrada solo con el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **eccema atópico**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es únicamente una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ciclesonida (el registro no detalla la indicación; la literatura la describe como asma persistente) |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ciclesonida es un corticosteroide inhalado que actúa como profármaco: las esterasas lo convierten en su metabolito activo, desisobutiril-ciclesonida, que se une al receptor de glucocorticoides (NR3C1). La afinidad del metabolito activo es muy superior a la del fármaco original (IC50 de 1,75 nM frente a 210 nM). Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción original, por lo que este análisis se basa en el conocimiento de clase.

El eccema atópico es una enfermedad inflamatoria de la piel con un fuerte componente de inflamación de tipo Th2. La supresión de la inflamación mediada por el receptor de glucocorticoides es mecanísticamente plausible, y es el mismo fundamento por el que se usan corticosteroides tópicos en esta enfermedad. Sin embargo, se trata de un argumento de clase y no de evidencia específica de ciclesonida.

Debe tenerse en cuenta que la entrada "dermatitis atópica" (3.º lugar de la predicción) es la misma enfermedad que "eccema atópico" con otro nombre. No constituye una corroboración independiente y no debe contarse como apoyo adicional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para eccema atópico.

*Otras predicciones del modelo con literatura (evidencia indirecta):*

| PMID | Año | Tipo | Revista | Indicación | Hallazgos Principales |
|------|-----|------|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Revisión (guía) | Basic & Clinical Pharmacology & Toxicology | Bronquitis | Guía finlandesa sobre diagnóstico y farmacoterapia de la EPOC estable; aporta contexto indirecto sobre corticosteroides inhalados como clase, no datos de eficacia de ciclesonida |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Reporte de caso | Contact Dermatitis | Dermatitis de contacto | Dermatitis alérgica sistémica por budesonida inhalada, con reactividad cruzada en pruebas de parche con ciclesonida; es una señal de seguridad, contraria a la dirección de reposicionamiento |

---

## Otras Predicciones del Modelo

| Posición | Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Sensibilización al metacrilato de 2-hidroxietilo (HEMA) | 99.76% | L5 | Alergia de contacto; el tratamiento principal es evitar el alérgeno, por lo que la necesidad clínica es poco clara |
| 4 | Bronquitis | 99.70% | L4 | Coherente con la acción antiinflamatoria de la vía aérea; solo evidencia indirecta |
| 5 | Dermatitis de contacto | 99.25% | L4 | La única publicación es una señal de seguridad (alergia), no de eficacia |
| 6 | Rasgos relacionados con asma (susceptibilidad) | 99.13% | L5 | Concepto de susceptibilidad genética, no una indicación tratable; el uso en asma ya corresponde a la indicación original |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20137070 | CICLOVENT® 160 MCG | Solución para inhalación | Ciclesonida | Cancelado |
| 20137073 | CICLOVENT® 80 MCG | Solución para inhalación | Ciclesonida | Cancelado |

Ambos registros pertenecen a CIPLA LTD y se encuentran cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** queratitis por herpes simple, insuficiencia suprarrenal, enfermedad de Addison, osteoporosis (incluida la posmenopáusica), enfermedades fúngicas, dermatofitosis, hipertensión ocular, glaucoma e infecciones parasitarias.
- **Señal de alergia:** existe un reporte de caso de dermatitis alérgica sistémica por budesonida inhalada con reactividad cruzada con ciclesonida en pruebas de parche.
- **Interacciones:** la consulta no encontró interacciones con otros fármacos; solo se registró su diana farmacológica, el receptor de glucocorticoides.
- **Contexto de clase:** la guía de EPOC citada indica que se debe verificar el riesgo de neumonía asociado a corticosteroides inhalados.

No se dispone de las advertencias y contraindicaciones del prospecto de INVIMA; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto (99.96%), pero no hay ensayos clínicos ni literatura para ciclesonida en eccema atópico (nivel L5). Además, los registros en Colombia están cancelados y no se cuenta con datos de seguridad del prospecto, lo que limita la viabilidad práctica.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción original desde DrugBank.
- Realizar una revisión de literatura específica de ciclesonida en eccema atópico y comparar con corticosteroides tópicos ya aprobados.
- Evaluar la compatibilidad de vía de administración: la forma disponible es inhalada y la indicación predicha es cutánea.
- Aclarar la situación regulatoria (registros cancelados) y la necesidad clínica frente a las alternativas existentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

