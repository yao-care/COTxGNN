---
layout: default
title: Levofloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacino: De Antibacteriano (indicación no especificada en el registro) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Levofloxacino es un antibiótico fluoroquinolónico que se comercializa en Colombia, entre otras formas, como solución oftálmica y como tabletas orales.
El modelo TxGNN predice que podría ser efectivo para la **queratoconjuntivitis epitelial punteada**, pero solo hay **0 ensayos clínicos** y **1 publicación** (un reporte de brote sin relación mecanística con el fármaco).
Por ahora es una predicción del modelo sin respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice «LEVOFLOXACINO») |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.92% (posición 979 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Levofloxacino inhibe la ADN girasa y la topoisomerasa IV bacterianas, y así detiene la replicación del ADN de las bacterias. Los datos de DrugBank no traen el mecanismo de acción detallado (`original_moa`). Lo anterior proviene del análisis mecanístico incluido en el paquete de evidencia.

**Este análisis no respalda un vínculo mecanístico** con la nueva indicación. La única publicación citada describe un brote de queratoconjuntivitis por **microsporidios**, y los microsporidios no son un blanco de las fluoroquinolonas. El puntaje de 0.999 es solo una predicción del grafo de conocimiento y no indica eficacia clínica. La similitud con la indicación original tampoco está evaluada todavía.

Existe una solución oftálmica de levofloxacino registrada en Colombia, pero la compatibilidad de vía de administración con esta indicación está pendiente de evaluar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Reporte de brote | American Journal of Ophthalmology | Brote de queratoconjuntivitis microsporidiana asociado a contaminación del agua de piscinas en Taiwán. No evalúa levofloxacino ni respalda su uso. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20134443 | LANDAX (Laboratorios Sophia S.A. de C.V.) | Solución oftálmica | LEVOFLOXACINO (el registro no detalla la indicación) |

Los datos de entrada repetían el mismo registro cinco veces, así que se muestra una sola fila. El total informado es de 20 registros. Además de la solución oftálmica, hay formas orales: tableta cubierta con película y tableta recubierta.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene nivel de evidencia L5: sin ensayos clínicos y con una única publicación que no guarda relación mecanística con el fármaco. Además, faltan datos de seguridad de INVIMA.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Obtener el mecanismo de acción desde DrugBank y confirmar las indicaciones originales aprobadas, porque el campo está vacío.
- Buscar ensayos y literatura específicos de levofloxacino en queratoconjuntivitis epitelial punteada.
- Evaluar la compatibilidad de vía de administración (por ejemplo, la solución oftálmica ya registrada).

**Nota:** dentro de las 10 predicciones del paquete, otras tienen más respaldo que esta. La **peste septicémica** (L3, Proceed with Guardrails) cuenta con estudios preclínicos en primates. Es probable que ya esté en la etiqueta del fármaco, por lo que quizá no sea un reposicionamiento real. La **gammapatía monoclonal** (L2, pregunta de investigación) se apoya en el ECA de fase 3 TEAMM, que estudió mieloma sintomático y no MGUS, así que no debe extrapolarse a MGUS asintomática.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

