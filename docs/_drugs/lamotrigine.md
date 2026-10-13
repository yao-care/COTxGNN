---
layout: default
title: Lamotrigine
parent: Solo Predicción del Modelo (L5)
nav_order: 376
evidence_level: L5
indication_count: 9
---

# Lamotrigine
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

# Lamotrigina: De Indicación Registrada (sin detalle) a Neuralgia del Trigémino

## Resumen en Una Frase

Lamotrigina es un anticonvulsivo bloqueador de canales de sodio; en Colombia su registro sanitario solo indica el nombre del principio activo, sin detallar la indicación.
El modelo TxGNN predice que podría ser efectivo para **neuralgia del trigémino** (segunda predicción de la lista), con **2 ensayos clínicos** y **18 publicaciones** que respaldan esta dirección.
La predicción con mayor puntaje, "neoplasia del nervio trigémino", no tiene respaldo real y se explica a continuación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LAMOTRIGINA (el registro no detalla la indicación; clínicamente se usa en epilepsia y trastorno bipolar) |
| Nueva Indicación Predicha | Neuralgia del trigémino (la predicción de rango 1, neoplasia del nervio trigémino, se descarta; ver nota) |
| Puntaje de Predicción TxGNN | 99.89% (neuralgia del trigémino); 99.97% (neoplasia del nervio trigémino) |
| Nivel de Evidencia | L2 (neuralgia del trigémino) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la predicción de rango 1:** la "neoplasia del nervio trigémino" obtuvo el puntaje más alto (99.97%), pero parece deberse a la cercanía en la red con la neuralgia del trigémino. No hay ensayos clínicos, y las dos publicaciones recuperadas tratan sobre neuralgia, no sobre tratamiento tumoral. Su nivel de evidencia es L5 y su recomendación es Hold. Por eso este informe se centra en la neuralgia del trigémino, que cuenta con evidencia real.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, lamotrigina bloquea los canales de sodio dependientes de voltaje de forma dependiente del uso y reduce la liberación de glutamato. La base de datos farmacológica consultada la asocia con el canal Nav1.2 (en rata) y la describe como anticonvulsivo para epilepsia y trastorno bipolar.

La neuralgia del trigémino se caracteriza por descargas ectópicas de alta frecuencia en las aferencias del nervio, a menudo por compresión vascular y desmielinización focal. Bloquear los canales de sodio y reducir el glutamato puede suprimir esas descargas. Es el mismo mecanismo general de la carbamazepina, tratamiento de primera línea.

La guía de la Academia Europea de Neurología (2019) incluida en la literatura recuperada reconoce a lamotrigina como opción adicional o de segunda línea. La evidencia controlada se limita a ensayos pequeños.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Fase 2/3 | Completado | 21 | Eficacia y seguridad de lamotrigina frente a carbamazepina en neuralgia del trigémino; muestra pequeña |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | No aplica | Completado | 20 | Estudio doble ciego, controlado con placebo, de lamotrigina añadida al tratamiento en neuralgia del trigémino (2003-2006) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guía | Eur J Neurol | Guía de la Academia Europea de Neurología para el manejo de la neuralgia del trigémino |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Revisión sistemática | Biomedicines | Revisión paraguas de fármacos para neuralgia del trigémino, con su eficacia y efectos adversos |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Revisión | Pract Neurol | Guía práctica: nuevos criterios diagnósticos y decisiones de tratamiento médico y quirúrgico |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Revisión | Mol Pain | Panorama desde la fisiopatología hasta los tratamientos farmacológicos |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revisión | Expert Rev Neurother | Actualización de farmacoterapia: carbamazepina y oxcarbazepina de elección; anticonvulsivos de tercera generación como alternativas |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Otro | No Shinkei Geka | Menciona lamotrigina entre los fármacos eficaces de uso fuera de indicación en Japón |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Otro | Drugs | Opciones farmacológicas actuales e innovadoras para neuralgia típica y atípica |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20067216 (cancelado) | LAMOTRIGINA 50MG (Tecnoquímicas S.A.) | Tableta dispersable | LAMOTRIGINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento (no provienen del prospecto):** se asocian con lamotrigina trastornos de ansiedad, trastorno neurótico, trastorno distímico, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica), pancitopenia, anemia aplásica idiopática, anemia aplásica y meningitis no infecciosa. Estas relaciones requieren confirmación con el prospecto.
- **Consideración adicional:** según la literatura recuperada, lamotrigina puede agravar las crisis mioclónicas en algunas epilepsias generalizadas.
- **Interacciones farmacológicas:** no se registraron interacciones con otros fármacos; solo una asociación farmacológica con el canal Nav1.2.

Para advertencias principales y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Para neuralgia del trigémino existe un ensayo completado de Fase 2/3 frente a carbamazepina y un ensayo controlado con placebo, ambos pequeños (n≈20), además de guías que la reconocen como opción de segunda línea. Esto corresponde a L2. El único registro sanitario local está cancelado y falta información de seguridad oficial, por lo que se recomienda avanzar con cautela.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto del registro INVIMA para obtener advertencias y contraindicaciones oficiales (brecha bloqueante para el tamizaje de seguridad).
- Completar los datos de mecanismo de acción desde DrugBank.
- Confirmar si existe un producto con registro vigente en Colombia, ya que el único registro está cancelado.
- Obtener evidencia controlada de mayor tamaño (ensayos con más pacientes) en neuralgia del trigémino.
- Plan de monitoreo hematológico y hepático, dadas las condiciones asociadas en el grafo de conocimiento.
- Descartar "neoplasia del nervio trigémino" y los síndromes de epilepsia refleja (nivel L3-L5; startle epilepsy, L3, tiene solo series de casos) como líneas prioritarias hasta contar con evidencia directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

