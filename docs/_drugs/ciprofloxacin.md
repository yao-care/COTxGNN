---
layout: default
title: Ciprofloxacin
parent: Evidencia Moderada (L3-L4)
nav_order: 159
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Ciprofloxacin: nueva indicación predicha, Esclerodermia difusa (nivel de evidencia L4). Indicación original: Ciprofloxacina"
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
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

# Ciprofloxacino: De Ciprofloxacina (indicación no detallada en el registro) a Esclerodermia Difusa

## Resumen en Una Frase

El ciprofloxacino es un antibiótico fluoroquinolona; en los registros sanitarios colombianos figura únicamente con el nombre del principio activo ("CIPROFLOXACINA"), sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, con **0 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección, ambas de evidencia preliminar o indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ciprofloxacina (el registro no detalla la indicación; se trata de un antibiótico) |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el ciprofloxacino es una fluoroquinolona que inhibe enzimas bacterianas (ADN girasa y topoisomerasa IV), y su eficacia antibacteriana está bien establecida. Mecanísticamente, su posible aplicación a la esclerodermia no es evidente y requiere confirmación.

Existen dos líneas de razonamiento. La primera es un posible efecto antifibrótico directo: una publicación de 2010 evaluó el ciprofloxacino oral en la piel de pacientes con esclerodermia mediante un ensayo aleatorizado, doble ciego y controlado, aunque los datos son preliminares. La segunda es indirecta: un estudio de 1995 describe sobrecrecimiento bacteriano del intestino delgado en pacientes con esclerosis sistémica, lo que justificaría el uso de un antibiótico en la afectación gastrointestinal, pero no tratamiento de la enfermedad de fondo.

El puntaje del modelo es muy alto, pero no está respaldado por evidencia clínica sólida. Debe interpretarse como una hipótesis para investigar, no como una indicación demostrada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Ensayo clínico aleatorizado, doble ciego (según el resumen disponible) | The Journal of Dermatology | Evalúa si el ciprofloxacino oral reduce la gravedad de la esclerodermia y su utilidad como antifibrótico en la piel; los resultados no están disponibles en el resumen y la evidencia es preliminar |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Estudio observacional/diagnóstico | British Journal of Rheumatology | 24 pacientes con esclerosis sistémica y síntomas de malabsorción evaluados por sobrecrecimiento bacteriano del intestino delgado; respalda el uso de antibióticos de forma indirecta |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20026284 | Ciprofloxacina 100 mg/10 ml solución inyectable (Laboratorios Ryan de Colombia) | Solución inyectable | Ciprofloxacina (cancelado) |
| 20104186 | Ciprofloxacino 100 mg/10 ml (Laboratorios Medifarma) | Solución inyectable | Ciprofloxacina (cancelado) |
| 20083338 | Ciriax® (Megalabs Colombia) | Solución inyectable | Ciprofloxacina (cancelado) |
| 20013311 | Ciprofloxacina 200 mg/100 ml (Laboratorios Medifarma) | Solución inyectable | Ciprofloxacina (cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no el prospecto):** síndrome de QT largo (incluido el familiar), torsades de pointes, epilepsia, enfermedad renal, deficiencia de potasio, tendinitis y otros trastornos tendinosos (bursitis aquílea, espolón calcáneo, periartritis, exostosis), neuropatía periférica y enfermedades del sistema nervioso periférico, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, miastenia gravis y enfermedades de la unión neuromuscular.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las de nivel **mayor** figuran los corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona) y el bupropión. Entre las de nivel **moderado** se encuentran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, albiglutida), famotidina, loperamida, alosetrón, aprepitant, ácido acetilsalicílico, balsalazida, bisacodilo, fosfato de calcio y budesonida.

Nota: la combinación con corticosteroides es relevante porque ambos aumentan el riesgo de lesión tendinosa, y los pacientes con esclerodermia suelen recibir corticosteroides. Consultar el prospecto para advertencias y contraindicaciones oficiales, ya que no se dispone de ellas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un puntaje alto del modelo, pero la evidencia real es limitada (un estudio preliminar y un estudio observacional indirecto, sin ensayos registrados). Además, no hay registros sanitarios vigentes en Colombia y los datos de seguridad oficiales no están disponibles.

**Para avanzar se necesita:**
- Revisar el texto completo y los resultados del ensayo aleatorizado de 2010 y buscar estudios confirmatorios.
- Obtener el prospecto en INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico con la fibrosis.
- Evaluar los riesgos de seguridad relevantes en esclerodermia (tendinopatía, interacción con corticosteroides, prolongación del QT).
- Definir la situación regulatoria (nuevo registro o reactivación), dado que todos los registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

