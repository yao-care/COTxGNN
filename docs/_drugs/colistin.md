---
layout: default
title: Colistin
parent: Solo Predicción del Modelo (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Colistin: nueva indicación predicha, Vasculitis postinfecciosa (nivel de evidencia L5). Indicación original: Hidrocortisona y antiinfecciosos (gotas óticas)"
monitor_inn: "colistin"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "infective urethral stricture", "paratyphoid fever", "sinusitis", "chronic rhinosinusitis", "chronic ethmoidal sinusitis"]
---

# Colistin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Colistina: De Otitis/Infecciones Bacterianas (Hidrocortisona y Antiinfecciosos) a Vasculitis Postinfecciosa

## Resumen en Una Frase

Colistina es un antibiótico polimixina, registrado en Colombia en gotas óticas (combinadas con hidrocortisona y antiinfecciosos) y en polvo inyectable, usado contra bacterias Gram negativas.
El modelo TxGNN predice que podría ser efectivo para **vasculitis postinfecciosa** (puntaje de 99.91%), pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Las indicaciones con algo de literatura indirecta son la sinusitis y la rinosinusitis crónica, aunque sin ensayos controlados.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hidrocortisona y antiinfecciosos (gotas óticas); colistina (inyectable) |
| Nueva Indicación Predicha | Vasculitis postinfecciosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la colistina es una polimixina que altera la membrana externa de las bacterias Gram negativas al unirse al lipopolisacárido. Su eficacia en infecciones por Gram negativos (incluida *Pseudomonas aeruginosa*) está establecida.

La vasculitis postinfecciosa es una condición inmunomediada que aparece después de una infección. La colistina no tiene un mecanismo reconocido frente a la inflamación vascular inmunológica, por lo que la predicción parece reflejar la cercanía en el grafo de conocimiento entre términos de enfermedades infecciosas y el fármaco, más que una base biológica específica.

Entre las otras predicciones, las más plausibles son la **sinusitis** y la **rinosinusitis crónica** (puntajes de 99.25% y 99.22%), especialmente en fibrosis quística, donde *P. aeruginosa* y su biofilm son dianas reconocidas y la vía tópica o nasal podría limitar la toxicidad sistémica. Aun así, la evidencia es indirecta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para vasculitis postinfecciosa ni para las demás indicaciones predichas.

---

## Evidencia de Literatura

Para vasculitis postinfecciosa, actualmente no hay literatura relacionada disponible. La literatura más cercana corresponde a la sinusitis (predicción de rango 8), que se presenta como contexto:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Revisión | Eur Arch Otorhinolaryngol | Opciones terapéuticas para la rinosinusitis crónica en fibrosis quística, de difícil tratamiento y con recurrencias frecuentes |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | Estudio farmacocinético | J Antimicrob Chemother | Absorción sistémica de tobramicina y colistina (como colistimetato) administradas por vía nasal en fibrosis quística, como indicador de seguridad |
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | Reporte de caso | Int J Hematol | Tratamiento exitoso con colistina intravenosa de sinusitis, celulitis orbitaria y neumonía por *P. aeruginosa* multirresistente en un paciente con leucemia mieloide aguda |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | Cohorte (indirecta) | Int Forum Allergy Rhinol | La cirugía de senos mejora calidad de vida e infecciones pulmonares en discinesia ciliar primaria |
| [24315789](https://pubmed.ncbi.nlm.nih.gov/24315789/) | 2014 | In vitro | Int J Antimicrob Agents | El efecto bactericida de la colistina sobre *P. aeruginosa* planctónica no depende de la formación de radicales hidroxilo |
| [33155505](https://pubmed.ncbi.nlm.nih.gov/33155505/) | 2021 | Preclínico | Acta Otolaryngol | Sellador de fibrina autólogo con antibióticos como método de administración tópica tras cirugía de senos |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | In vitro | Pharmaceutics | Ceragenins con ivacaftor previenen biofilm de bacterias causantes de rinosinusitis |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20018421 | OIDOLYT GOTAS OTICAS | Suspensión ótica | Hidrocortisona y antiinfecciosos (cancelado) |
| 20148396 | COLIJECT® 150 MG / VIAL | Polvo liofilizado para reconstituir a solución inyectable | Colistina (cancelado) |
| 20033548 | FIXAMICIN® GOTAS OTICAS | Suspensión ótica | Hidrocortisona y antiinfecciosos (cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): enfermedad renal, piouréter, infección por herpes simple, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, miastenia gravis (incluida la de inicio en adulto), enfermedad de la unión neuromuscular, herpes zóster geniculado y miringitis bullosa hemorrágica.
- **Preocupaciones adicionales** señaladas en el análisis de las predicciones: la nefrotoxicidad de la colistina es relevante en enfermedades con daño renal, como el síndrome urémico hemolítico asociado a infección.

Para advertencias e interacciones farmacológicas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (vasculitis postinfecciosa) tiene solo respaldo computacional (L5), sin ensayos ni literatura, y no existe un mecanismo plausible. Además, no hay registros sanitarios vigentes en Colombia. Las indicaciones de sinusitis y rinosinusitis crónica (L4) podrían tratarse como preguntas de investigación, pero con evidencia solo indirecta.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones), que actualmente no están disponibles
- Verificar la situación regulatoria, dado que los 3 registros están cancelados
- Para sinusitis o rinosinusitis crónica: un estudio prospectivo de administración tópica o nasal que evalúe eficacia y seguridad
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original, hoy pendientes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

