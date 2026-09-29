---
layout: default
title: Cefuroxime
parent: Solo Predicción del Modelo (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxima: De Antibiótico Cefalosporínico a Hiperamilasemia

## Resumen en Una Frase

Cefuroxima es una cefalosporina de segunda generación, un antibiótico usado para tratar infecciones bacterianas. El modelo TxGNN predice que podría ser efectiva para **hiperamilasemia** (amilasa elevada en sangre), pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. La evidencia se limita a la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo dice «CEFUROXIMA») |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, cefuroxima es una cefalosporina de segunda generación que inhibe la síntesis de la pared celular bacteriana. Su eficacia está comprobada en infecciones bacterianas, pero no hay una vía mecanística que la conecte con la hiperamilasemia.

La hiperamilasemia es una alteración de laboratorio, es decir, una elevación de la amilasa en sangre. No es una infección bacteriana, y un antibiótico no tiene un efecto esperado sobre ella. El análisis del paquete de evidencia no identificó ninguna justificación mecanística ni evidencia clínica, y concluye que la predicción carece de respaldo.

El puntaje alto del modelo (99.76%, posición 2530) no equivale a evidencia. Por sí solo no basta para sostener un reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20099285 | CEFUROXIMA AXETIL TABLETAS 500 MG (fabricante: Alkem Laboratories Ltd) | Tableta cubierta con película | CEFUROXIMA |

Los tres registros reportados comparten el mismo número (20099285) y los mismos datos, por lo que se muestran una sola vez. La única vía de administración registrada es la oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hiperamilasemia no tiene ensayos clínicos, literatura ni mecanismo plausible (nivel L5). Es probable que sea un artefacto del grafo de conocimiento y no hay base para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Consultar DrugBank para obtener el mecanismo de acción.
- Redirigir el esfuerzo a otras predicciones del mismo fármaco que sí tienen respaldo. La **infección del tracto urinario** (L3, Proceed with Guardrails) es un uso antibacteriano establecido más que un reposicionamiento, y debe seguir el antibiograma local y las guías de uso racional de antibióticos. La **otitis media supurativa** (L4) es solo una pregunta de investigación, sin ensayos clínicos de eficacia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

