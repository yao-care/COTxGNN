---
layout: default
title: Tropicamide
parent: Solo Predicción del Modelo (L5)
nav_order: 648
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tropicamida: De Combinaciones de Tropicamida (Oftalmología) a Síndrome de la Cola de Caballo

## Resumen en Una Frase

Tropicamida es un anticolinérgico de uso oftálmico tópico, registrado en Colombia en combinaciones de tropicamida y fenilefrina para dilatar la pupila (midriasis).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tropicamida en combinaciones (solución oftálmica) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la tropicamida es un antagonista muscarínico (anticolinérgico). Los datos farmacológicos la vinculan con los receptores muscarínicos M2, M3, M4 y M5, y se usa como midriático de acción corta para examinar el cristalino, el humor vítreo y la retina.

El síndrome de la cola de caballo se produce por la compresión de las raíces nerviosas y causa disfunción de vejiga, intestino y sensibilidad. Un anticolinérgico podría, en teoría, actuar sobre la hiperactividad del detrusor, pero no trata la causa de fondo, que requiere descompresión quirúrgica. El puntaje alto (0.995) probablemente refleja cercanía en el grafo de conocimiento por síntomas vesicales o intestinales neurogénicos compartidos, y no un efecto terapéutico demostrado.

Además, el fármaco solo está aprobado en forma oftálmica, con exposición sistémica mínima, por lo que no existe una vía de administración plausible para esta indicación.

### Otras predicciones del modelo (todas con evidencia L5 y decisión Hold)

| Posición | Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Vejiga neurogénica (término obsoleto en la ontología) | 99.13% | El antagonismo muscarínico es un mecanismo establecido (como oxibutinina o tolterodina), pero la tropicamida no tiene estudios para este uso y existen alternativas aprobadas y mejor estudiadas. |
| 3 | Síndrome del intestino irritable | 99.12% | Los antiespasmódicos antimuscarínicos se usan en este síndrome, pero los efectos anticolinérgicos (estreñimiento, boca seca, taquicardia) podrían empeorar los síntomas. |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los tres registros sanitarios están cancelados; no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20069775 | T-P OFTENO | Solución oftálmica | Tropicamida combinaciones | Cancelado |
| 20215215 | FOTORRETIN® Solución Oftálmica Estéril | Solución oftálmica | Fenilefrina combinaciones | Cancelado |
| 19950677 | FOTORRETIN® Solución Oftálmica | Solución oftálmica | Fenilefrina combinaciones | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la tropicamida con las siguientes enfermedades:
  - Glaucoma de ángulo abierto, glaucoma de ángulo cerrado e hipertensión ocular
  - Hipertensión y trastorno hipertensivo
  - Diabetes mellitus y cetoacidosis diabética
  - Paro cardíaco súbito, enfermedad de la conducción cardíaca, isquemia miocárdica y enfermedad arterial coronaria
  - Hipertiroidismo, enfermedad de Graves y tirotoxicosis
- **Interacciones farmacológicas:** la consulta se completó y reportó 4 registros, todos de farmacología de receptores (no interacciones con otros fármacos): unión a los receptores muscarínicos M2, M3, M4 y M5. No se identificaron interacciones con otros medicamentos.
- **Consideración adicional:** el uso sistémico implicaría los efectos adversos anticolinérgicos típicos (boca seca, estreñimiento, taquicardia), relevantes para varias de las condiciones listadas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo computacional (L5), sin ensayos clínicos ni literatura. Además, el fármaco solo existe en forma oftálmica, sin registros vigentes en Colombia, y no hay una vía de administración plausible para la indicación predicha, que requiere descompresión quirúrgica y no tratamiento anticolinérgico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a la API de DrugBank).
- Advertencias y contraindicaciones del prospecto en INVIMA (descargar y analizar el PDF).
- Evidencia preclínica o clínica que respalde un efecto sobre la función vesical o intestinal neurogénica.
- Una formulación sistémica con estudios farmacocinéticos y de seguridad, si se decidiera continuar.
- Comparación con alternativas ya aprobadas (oxibutinina, tolterodina) para las indicaciones de vejiga neurogénica y síndrome del intestino irritable.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

