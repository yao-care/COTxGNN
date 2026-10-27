---
layout: default
title: Tadalafil
parent: Solo Predicción del Modelo (L5)
nav_order: 601
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Tadalafil: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto de indicación solo indica \"T"
---

# Tadalafil
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

## Tadalafilo: De Indicación No Especificada a Hipertricosis Universal Congénita tipo Ambras
{: .text-alpha }

## Resumen en Una Frase

Tadalafilo es un inhibidor de la fosfodiesterasa tipo 5 (PDE5) que cuenta con registros sanitarios en Colombia, aunque el texto de indicación registrado solo menciona el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo indica "TADALAFIL") |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tadalafilo es un inhibidor de PDE5 que aumenta el GMP cíclico (cGMP) y produce vasodilatación. Esta clase de fármacos se utiliza en disfunción eréctil e hipertensión arterial pulmonar, aunque la indicación aprobada en los registros colombianos no está detallada.

La relación con la nueva indicación es débil. La hipertricosis tipo Ambras es un trastorno congénito del crecimiento del vello, asociado a reordenamientos genómicos que producen un efecto de posición sobre el locus TRPS1. Una conexión indirecta podría pasar por cambios en el flujo sanguíneo folicular o en la señalización de cGMP, pero esto es especulativo y no está establecido.

La predicción de TxGNN parece derivarse únicamente de similitudes en el grafo de conocimiento, sin respaldo clínico ni bibliográfico. Además, existe una posible alerta de dirección del efecto: vasodilatadores como el minoxidil inducen hipertricosis como efecto adverso, lo que sugiere que el fármaco podría, en el mejor de los casos, no ser útil y, en el peor, agravar el problema.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

Entre las otras predicciones, solo la migraña con aura de tronco encefálico (puesto 8) tiene una publicación: un reporte de caso de 2006 (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*) que describe aura migrañosa típica sin cefalea asociada a tadalafilo. Es una señal de evento adverso, no de beneficio terapéutico.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20007296 | CIALIS® 5 MG | Tableta recubierta | TADALAFIL | Cancelado |
| 20065415 | IRTAL® 5 MG tabletas recubiertas | Tableta recubierta | TADALAFIL | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, epilepsia, estenosis aórtica y enfermedades de la válvula aórtica, trastornos hipotensivos, trastornos de la coagulación, síndrome coronario agudo, infarto de miocardio, accidente cerebrovascular y trastornos cerebrovasculares, anemia falciforme y otras hemoglobinopatías, mieloma de células plasmáticas, leucemia, priapismo, enfermedad de Peyronie, pérdida de audición, y miocardiopatía hipertrófica (incluida la familiar).
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Entre las principales de nivel moderado figuran aprepitant, dexametasona, claritromicina, cimetidina, miconazol, clotrimazol, lorcaserina y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina). También se registran interacciones de nivel menor (papaverina) y de nivel desconocido (pantoprazol, glimepirida, doxiciclina, morfina, metformina, omeprazol).
- **Señales de la predicción**: los vasodilatadores se asocian a hipertricosis como efecto adverso, y tadalafilo se ha asociado a aura migrañosa en un reporte de caso.

No se dispone de las advertencias del prospecto; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos ni literatura, con un mecanismo especulativo y posible dirección de efecto contraria. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar las advertencias y contraindicaciones.
- Consultar el mecanismo de acción en DrugBank para analizar el vínculo mecanístico.
- Aclarar la indicación aprobada original, ya que el registro solo muestra el nombre del principio activo.
- Realizar estudios preclínicos que respalden un vínculo entre PDE5/cGMP y el crecimiento del vello en este trastorno.
- Evaluar el estado regulatorio (registros cancelados) y la compatibilidad de vías de administración.
- Considerar otras predicciones con mayor plausibilidad, como la cardiopatía kifoescoliótica (por la hipertensión pulmonar asociada), aunque también carece de evidencia directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

