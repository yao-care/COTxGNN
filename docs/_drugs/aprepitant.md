---
layout: default
title: Aprepitant
parent: Solo Predicción del Modelo (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: De Indicación Original no Detallada en el Registro a Síndrome Nefrogénico de Antidiuresis Inapropiada (NSIAD)

## Resumen en Una Frase

Aprepitant es un antagonista del receptor NK1 comercializado en Colombia como EMEND®. El registro sanitario consultado no detalla su indicación original, solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, con un puntaje muy alto (99.97%).
Sin embargo, hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una señal del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "APREPITANT") |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada (NSIAD) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información disponible, aprepitant es un antagonista del receptor de neurocinina 1 (NK1), es decir, bloquea la señal de la sustancia P.

El NSIAD se debe a mutaciones que activan de forma excesiva el receptor V2 de la vasopresina (AVPR2). Esto hace que el riñón retenga agua aunque la hormona antidiurética no esté elevada. Aprepitant no actúa sobre el receptor V2 ni sobre el manejo renal del agua.

**Conclusión de la evaluación:** no se identificó un vínculo mecanístico entre la indicación original y la nueva. El puntaje alto del modelo no tiene respaldo en mecanismo, ensayos ni literatura, y debe leerse como un posible artefacto del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19945183 | EMEND® 80 MG/125 MG (MERCK SHARP & DOHME LLC) | Cápsula dura | APREPITANT |

El mismo registro aparece repetido cinco veces en los datos recibidos. Aquí se muestra una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco en los datos recibidos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos, literatura ni mecanismo plausible que respalde el uso de aprepitant en NSIAD. La predicción del modelo es la única evidencia (nivel L5).

**Para avanzar se necesita:**
- Descargar el prospecto de INVIMA para completar la información de advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Obtener el mecanismo de acción desde DrugBank para respaldar el análisis mecanístico.
- Revisar las otras nueve predicciones del modelo. Todas tienen nivel L5 y también quedan en Hold. La más plausible biológicamente es la **hemorragia subaracnoidea** (rank 9). Los modelos preclínicos de lesión cerebral sugieren que los antagonistas NK1 podrían reducir la inflamación neurogénica y el edema, pero no se recuperó ningún ensayo ni publicación. Sigue siendo solo una pregunta de investigación.

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

