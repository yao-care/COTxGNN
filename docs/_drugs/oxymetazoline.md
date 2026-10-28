---
layout: default
title: Oxymetazoline
parent: Solo Predicción del Modelo (L5)
nav_order: 491
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Oxymetazoline: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L3). Indicación original: Oximetazolina"
monitor_inn: "oxymetazoline"
predicted_indications: ["nasal cavity disease", "headache disorder"]
---

# Oxymetazoline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Oxymetazolina: De Descongestionante Nasal a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

Oxymetazolina es un simpaticomimético de uso tópico, originalmente registrado en Colombia como solución nasal (y una presentación oftálmica) bajo el nombre de principio activo "oximetazolina".
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, con **0 ensayos clínicos** y **5 publicaciones** de apoyo limitado, en su mayoría indirecto.
Esta indicación se solapa con el uso descongestionante ya establecido, por lo que es más un hallazgo cercano a la indicación actual que un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Oximetazolina (el registro sanitario no detalla una indicación más específica) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 5) |
| Número de Registros Sanitarios | 5 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, la oximetazolina es un agonista adrenérgico directo (receptores alfa-1 y alfa-2) que produce vasoconstricción de la mucosa, lo que reduce la congestión y el edema. Los datos farmacológicos compilados también muestran afinidad por los receptores adrenérgicos α1A, α1B, α1D, α2A, α2B y α2C, así como por los receptores serotoninérgicos 5-HT1B, 5-HT1D y 5-HT2C.

La enfermedad de la cavidad nasal engloba cuadros con congestión o edema de la mucosa, que son justamente el objetivo del uso descongestionante ya conocido del fármaco. El puntaje tan alto del modelo (0.9996) es coherente con ese uso establecido.

Por ello, la coherencia mecanística es sólida, pero la predicción no aporta una indicación realmente nueva: es una extensión cercana a la indicación existente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Estudio clínico | Annals of the New York Academy of Sciences | Efecto del resfriado común sobre la función olfatoria en 36 sujetos, con medidas psicofísicas y rinometría acústica |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Cohorte/Observacional | Journal of Plastic Surgery and Hand Surgery | Permeabilidad nasal por rinometría acústica en niños de 4 a 8 años con fisura labiopalatina reparada frente a controles |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Estudio en animales | Annals of Otology, Rhinology, and Laryngology | Efecto de gotas nasales de oximetazolina sobre la defensa tisular local en sinusitis aguda experimental en conejos (14 animales) |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Reporte de caso | Global Pediatric Health | Rinoscleroma en un niño de 9 años, con obstrucción nasal como presentación |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Serie de casos/Procedimiento | American Journal of Rhinology & Allergy | Tratamiento con coblación de telangiectasias nasales en telangiectasia hemorrágica hereditaria |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 21491 | NASIVIN® INFANTIL | Solución nasal | Oximetazolina |
| 20018967 | OXIMETAZOLINA HCI 0.025% SOLUCIÓN NASAL | Solución nasal | Oximetazolina |
| 20191379 | ACICLER® SOLUCIÓN NASAL 0.05% | Solución nasal | Oximetazolina |
| 19928879 | CLARIVIS | Solución oftálmica | Oximetazolina |
| 35490 | AFRIN® SOLUCIÓN NASAL ADULTOS 0.05% | Solución nasal | Oximetazolina |

Los cinco registros figuran como cancelados.

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento, no el prospecto):**
  - Cardiovasculares: hipertensión, enfermedad cardíaca, enfermedad cardiovascular, enfermedad arterial coronaria, arteriosclerosis y aterosclerosis.
  - Metabólicas y endocrinas: diabetes mellitus, cetoacidosis diabética, hipertiroidismo, enfermedad de Graves y tirotoxicosis.
  - Oculares: glaucoma de ángulo cerrado, infecciones oculares, conjuntivitis, trastornos de la visión y ceguera.
  - Urológicas: hiperplasia prostática benigna.
- **Interacciones farmacológicas:** la consulta se completó con 9 registros, que corresponden a interacciones farmacológicas con dianas (receptores adrenérgicos α1 y α2 y receptores serotoninérgicos 5-HT1B, 5-HT1D y 5-HT2C), no a interacciones con otros medicamentos. No se identificaron fármacos específicos que interactúen.

No se dispone del prospecto con advertencias y contraindicaciones oficiales; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente coherente, pero coincide con el uso descongestionante ya establecido, por lo que no representa un reposicionamiento novedoso. Además, no hay ensayos clínicos, la literatura es mayormente indirecta o preclínica, y los cinco registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Aclarar el estado regulatorio: motivo de la cancelación de los registros y si existe algún producto vigente.
- Obtener el prospecto con advertencias y contraindicaciones oficiales (hoy es una brecha bloqueante para el análisis de seguridad).
- Confirmar los datos del mecanismo de acción en DrugBank.
- Definir con precisión qué condiciones de la cavidad nasal serían el objetivo y si aportan algo más allá de la indicación actual.
- Considerar el riesgo de las contraindicaciones identificadas (cardiovasculares, metabólicas y oculares) en el diseño de cualquier estudio.

---

### Otras indicaciones predichas (referencia)

- **Trastorno de cefalea** (TxGNN 0.9904, L4, pregunta de investigación): la evidencia principal es un estudio de tetracaína intranasal 3% más oximetazolina 0.05% en estado migrañoso (PMID 31919839), donde no se puede separar el aporte de la oximetazolina; el resto de la literatura es indirecta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

