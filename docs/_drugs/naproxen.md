---
layout: default
title: Naproxen
parent: Solo Predicción del Modelo (L5)
nav_order: 461
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Naproxeno: De Combinaciones con Tiocolchicósido/Naproxeno a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

Naproxeno es un antiinflamatorio no esteroideo (AINE) que en Colombia se registró bajo licencias de naproxeno solo y de productos asociados con tiocolchicósido, todas ellas hoy canceladas.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones de tiocolchicósido |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general, el naproxeno es un inhibidor no selectivo de las ciclooxigenasas COX-1 y COX-2 (PTGS1 y PTGS2), lo que reduce la síntesis de prostaglandinas. Su uso clínico conocido incluye artritis reumatoide, artrosis, espondilitis anquilosante, tendinitis, bursitis, gota aguda y dismenorrea primaria.

El síndrome de braquidactilia-sindactilia es una malformación congénita rara de las extremidades, de origen genético y del desarrollo. No se ha identificado una vía plausible que conecte la inhibición de prostaglandinas con su causa subyacente. En el mejor de los casos, un beneficio sería sintomático (dolor o inflamación) y no modificaría la enfermedad.

El puntaje alto (99.35%) refleja una predicción del modelo, probablemente por cercanía en la red del grafo de conocimiento, y no un mecanismo biológico validado. Debe tratarse como una hipótesis por contrastar, no como un hallazgo accionable. Las otras tres predicciones principales (síndrome de microftalmia colobomatosa-displasia rizomélica, displasia acromesomélica tipo Hunter-Thompson y síndrome de braquiolmia-amelogénesis imperfecta) son igualmente enfermedades genéticas raras, con puntajes de 99.2%, 99.2% y 99.1%, también sin evidencia de respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20240091 | MIDOL ® (cancelado) | Tableta recubierta | Combinaciones de tiocolchicósido |
| 20210473 | RELAFEN® Tabletas Recubiertas (cancelado) | Tableta recubierta | Tiocolchicósida |
| 20024731 | DURAFLEX ® 500MG (cancelado) | Cápsula blanda | Naproxeno |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** hipertensión, insuficiencia hepática y enfermedad hepática, enfermedad renal, insuficiencia cardíaca congestiva, enfermedad coronaria y aterosclerosis coronaria, infarto de miocardio y trombosis coronaria, accidente cerebrovascular y enfermedad cerebrovascular, infarto cerebral, trastornos de la coagulación, anemia (incluida la macrocítica) y hemoglobinopatías, epilepsia, diabetes mellitus y cetoacidosis diabética, osteoporosis (incluida la posmenopáusica), obesidad, hiperplasia prostática benigna, enfermedad de la vesícula biliar, piouréter y abuso/dependencia de sustancias.
- **Interacciones farmacológicas:** los datos compilados solo registran la farmacología sobre sus dianas humanas, COX-1 (PTGS1) y COX-2 (PTGS2); no hay interacciones con otros fármacos con nivel de gravedad definido.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre la inhibición de COX y una malformación congénita de origen genético. Además, todos los registros sanitarios del naproxeno en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Revisión de literatura que explore un vínculo biológico entre la vía de prostaglandinas y el síndrome
- Prospecto oficial de INVIMA con advertencias y contraindicaciones, para el análisis de seguridad
- Aclarar la situación regulatoria (registros cancelados) y la compatibilidad de vías de administración
- Considerar priorizar otras indicaciones con mayor plausibilidad biológica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

