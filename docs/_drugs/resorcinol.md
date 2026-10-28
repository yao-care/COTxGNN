---
layout: default
title: Resorcinol
parent: Solo Predicción del Modelo (L5)
nav_order: 555
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Resorcinol: nueva indicación predicha, Acné queloide (nivel de evidencia L5). Indicación original: Ácido salicílico, ácido benzoico, resorcinol (combinación)"
monitor_inn: "RESORCINOL"
predicted_indications: ["acne keloid", "amyopathic dermatomyositis", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial"]
---

# Resorcinol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Resorcinol: De Combinaciones Tópicas (Ácido Salicílico, Ácido Benzoico, Resorcinol) a Acné Queloide
{: .text-alpha }

## Resumen en Una Frase

Resorcinol es un agente tópico queratolítico y antiséptico, registrado en Colombia únicamente como parte de soluciones tópicas combinadas (con ácido salicílico y ácido benzoico), cuyos registros sanitarios hoy están cancelados.
El modelo TxGNN predice que podría ser efectivo para **acné queloide**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ácido salicílico, ácido benzoico, resorcinol (combinación) |
| Nueva Indicación Predicha | Acné queloide |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, resorcinol es un queratolítico y antiséptico tópico que se usa en productos para acné y dermatitis seborreica, y en Colombia se registró en soluciones tópicas combinadas.

La relación con la nueva indicación es plausible: el acné queloide es una enfermedad folicular e inflamatoria de la piel, y la acción queratolítica y antimicrobiana de resorcinol podría actuar sobre las lesiones foliculares. De las seis indicaciones predichas, esta es la más verosímil desde el punto de vista biológico.

Sin embargo, el puntaje de 0.9983 es solo una predicción computacional. No hay ensayos ni literatura que la validen, y la falta de datos del mecanismo limita el análisis. Las otras cinco predicciones (dermatomiositis amiopática, dermatomiositis neonatal, enfermedad pulmonar intersticial infantil asociada a enfermedad del tejido conectivo, acrodermatitis crónica atrófica e hidroa vacciniforme familiar) carecen de un vínculo mecanístico claro o creíble.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los dos registros sanitarios están cancelados; no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20052715 | Querafar® Solución Tópica | Solución tópica | Ácido salicílico, ácido benzoico, resorcinol (vigente) |
| 19977478 | Mesalit Solución Tópica | Solución tópica | Varias combinaciones (vigente) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento de TxGNN (PrimeKG) asocia resorcinol con las siguientes enfermedades, entre otras:
  - Metahemoglobinemia (incluida la debida a deficiencia de metahemoglobina reductasa) y sulfohemoglobinemia
  - Deficiencia de G6PD
  - Enfermedad renal
  - Diabetes mellitus y cetoacidosis diabética
  - Epilepsia
  - Enfermedades cardiovasculares: paro cardíaco súbito, enfermedad del sistema de conducción cardíaco, enfermedad vascular periférica, claudicación intermitente y enfermedad arterial periférica
  - Insuficiencia respiratoria
  - Dermatitis, dermatitis seborreica, foliculitis y exantema
  - Verrugas comunes e infección anogenital por VPH
  - Otras: piouréter, enfermedad por depósito de glucógeno, cistinuria, galactosemia y deficiencia de piruvato deshidrogenasa E3
- **Población neonatal y pediátrica:** resorcinol puede absorberse por la piel y tiene riesgos de toxicidad sistémica en lactantes, como metahemoglobinemia y efectos tiroideos. Esto es especialmente relevante para las indicaciones pediátricas predichas.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay productos vigentes con resorcinol en Colombia. Aunque el acné queloide es la indicación más plausible, falta validación y hay señales de seguridad que deben aclararse.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA para advertencias y contraindicaciones oficiales (brecha bloqueante para el tamizaje de seguridad)
- Obtener datos del mecanismo de acción desde DrugBank
- Revisar la literatura sobre resorcinol tópico en acné queloide y trastornos foliculares afines
- Evaluar la absorción sistémica y la seguridad, sobre todo en poblaciones pediátricas, y las contraindicaciones del grafo de conocimiento (G6PD, metahemoglobinemia, enfermedad renal)
- Confirmar la situación regulatoria y la viabilidad de una nueva formulación, dado que los registros actuales están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

