---
layout: default
title: Empagliflozin
parent: Solo Predicción del Modelo (L5)
nav_order: 249
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

# Empagliflozina: De Indicación Registrada (Empagliflozina) a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

Empagliflozina es un inhibidor del cotransportador sodio-glucosa (SGLT), conocido comercialmente como Jardiance®, utilizado originalmente en el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la persona rígida clásico**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de un resultado computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Empagliflozina (el registro sanitario solo indica el nombre del principio activo, sin texto detallado de indicación) |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, empagliflozina es un inhibidor del cotransportador sodio-glucosa tipo 2 (SGLT2, con actividad también sobre SGLT1), que reduce la reabsorción renal de glucosa. Su eficacia está comprobada en diabetes tipo 2 y en la reducción del riesgo de muerte cardiovascular en pacientes con diabetes y enfermedad cardiovascular.

El síndrome de la persona rígida es un trastorno neurológico autoinmune, típicamente asociado a anticuerpos anti-GAD65, que altera la señalización inhibitoria GABAérgica. **No se ha establecido un vínculo mecanístico claro** con la inhibición de SGLT2. Cualquier conexión posible (efectos antiinflamatorios o metabólicos, o la superposición autoinmune con la diabetes tipo 1) es especulativa.

El puntaje elevado (0.991) es una predicción computacional sin respaldo clínico ni bibliográfico, y la falta de datos de mecanismo de acción limita aún más la evaluación.

### Otras predicciones del modelo

| Posición | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Observación |
|------|------|------|------|------|
| 2 | Síndrome de extremidad rígida focal | 99.06% | L5 | Variante rara del espectro de la persona rígida; el puntaje idéntico sugiere que proviene de la representación compartida de la enfermedad en el grafo de conocimiento, no de evidencia independiente |
| 3 | Opsismodisplasia | 99.03% | L5 | Displasia esquelética rara por mutaciones en INPPL1 (deficiencia de SHIP2); existe una conexión tenue con la señalización de insulina, pero sin efecto demostrado de empagliflozina |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20061998 | JARDIANCE® 25 MG | Tableta recubierta | Empagliflozina | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / dianas farmacológicas**: la consulta se completó y reportó 2 dianas farmacológicas de empagliflozina (no interacciones con otros medicamentos): el cotransportador sodio-glucosa 1 (SLC5A1) y el cotransportador sodio-glucosa 2 (SLC5A2).

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo computacional (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible. Además, el producto no tiene registro sanitario vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank) para evaluar un posible vínculo con la vía GABAérgica o autoinmune
- Revisión de la literatura preclínica y clínica sobre SGLT2 y trastornos autoinmunes neurológicos
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para el tamizaje de seguridad
- Verificar la situación regulatoria actual de empagliflozina en Colombia (el único registro está cancelado)
- Evidencia preclínica o de mecanismo que justifique avanzar de L5 a L4
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

