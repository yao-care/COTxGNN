---
layout: default
title: Empagliflozin
parent: Solo Predicción del Modelo (L5)
nav_order: 176
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

# Empagliflozina: De Diabetes Mellitus Tipo 2 a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

Empagliflozina es un inhibidor del cotransportador sodio-glucosa tipo 2 (SGLT2), utilizado originalmente para mejorar el control glucémico en adultos con diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la persona rígida clásico**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según la información farmacológica del expediente; el texto del registro INVIMA solo dice "EMPAGLIFLOZINA") |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el expediente. Según la información farmacológica disponible, empagliflozina actúa sobre los cotransportadores sodio-glucosa SGLT2 (principal) y SGLT1. Su eficacia en diabetes tipo 2 está comprobada, y también reduce el riesgo de muerte cardiovascular en pacientes con diabetes y enfermedad cardiovascular.

**No existe un vínculo mecanístico establecido** con el síndrome de la persona rígida. Esta enfermedad es típicamente autoinmune y afecta la neurotransmisión GABAérgica (a menudo con anticuerpos anti-GAD65). La inhibición de SGLT2 no aborda de forma evidente esa patología. El único respaldo es el puntaje alto del grafo de conocimiento de TxGNN, sin estudios que lo sustenten.

Las otras predicciones del modelo siguen el mismo patrón:
- **Síndrome de la extremidad rígida focal** (99.06%): es una variante focal del mismo espectro. El puntaje idéntico sugiere que refleja vecinos compartidos en el grafo y no evidencia independiente.
- **Opsismodisplasia** (99.03%): es una displasia esquelética rara asociada a mutaciones de INPPL1 (SHIP2), que modula la señalización de PI3K/Akt e insulina. Es una conexión hipotética y no verificada. Además es una condición pediátrica grave, por lo que cualquier investigación futura exigiría una evaluación de seguridad cuidadosa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 20 registros sanitarios en total. Las filas devueltas en el expediente son idénticas, así que se muestran una sola vez:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20061998 | JARDIANCE® 25 MG (Boehringer Ingelheim International GmbH) | Tableta recubierta | EMPAGLIFLOZINA (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5). No hay ensayos, literatura ni mecanismo plausible que conecte la inhibición de SGLT2 con el síndrome de la persona rígida. Sin datos de seguridad del prospecto local, no es posible avanzar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos bloqueante
- Obtener los datos del mecanismo de acción desde DrugBank
- Una revisión de literatura preclínica que justifique un vínculo entre SGLT2 y la fisiopatología autoinmune o GABAérgica
- Definir la indicación original con el texto completo del registro sanitario
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

