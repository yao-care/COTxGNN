---
layout: default
title: Haloperidol
parent: Solo Predicción del Modelo (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: De Indicación Original No Especificada a Trastorno Congénito de Glicosilación con Fucosilación Defectuosa

## Resumen en Una Frase

Haloperidol es un antipsicótico comercializado en Colombia. Los registros sanitarios consultados no describen su indicación original, solo figura el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **trastorno congénito de glicosilación con fucosilación defectuosa**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se basa solo en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto registrado es solo «HALOPERIDOL») |
| Nueva Indicación Predicha | Trastorno congénito de glicosilación con fucosilación defectuosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información recibida. Por farmacología general, haloperidol es un antagonista de los receptores de dopamina D2 de alta afinidad. Este mecanismo explica su uso en trastornos psicóticos y maníacos, pero no está documentado en este conjunto de datos.

No se identificó ningún vínculo mecanístico entre haloperidol y los trastornos congénitos de glicosilación con fucosilación defectuosa. Estos son trastornos metabólicos hereditarios, y el bloqueo dopaminérgico no tiene una relación conocida con la vía de fucosilación de proteínas.

Por lo tanto, esta predicción se apoya únicamente en la posición del puntaje dentro del grafo de conocimiento de TxGNN (puesto 1092). No hay ensayos, literatura ni razonamiento mecanístico que la sustenten. Debe tratarse como una hipótesis sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 20 registros sanitarios en total. Se muestran los registros únicos de la muestra recibida (formas orales, incluidas tabletas, y solución inyectable):

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19929092 | HALOPERIDOL SOLUCION INYECTABLE (FEPARVI LTDA) | Solución inyectable | No detallada (solo figura «HALOPERIDOL») |
| 19999331 | HALOPERIDOL SOLUCION ORAL 2 MG / ML (ACTIFARMA S.A.) | Solución oral | No detallada (solo figura «HALOPERIDOL») |
| 20118490 | APRACAL GOTAS (LABORATORIOS SIEGFRIED S.A.S.) | Solución oral | No detallada (solo figura «HALOPERIDOL») |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de mayor puntaje es solo del modelo (nivel L5), sin ensayos, literatura ni vínculo mecanístico plausible. No hay base para avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística que conecte el antagonismo D2 (u otro mecanismo de haloperidol) con la vía de fucosilación
- Estudios preclínicos que respalden la hipótesis
- El mecanismo de acción desde DrugBank y las advertencias y contraindicaciones del prospecto de INVIMA
- Confirmar la indicación original en los registros, porque el texto actual solo dice «HALOPERIDOL»

**Nota sobre otra predicción del mismo análisis:** la décima predicción, *trastorno afectivo bipolar maníaco* (puntaje 99.83%), sí tiene respaldo sólido: nivel L1, con varios ensayos de Fase 3 completados que incluyen haloperidol como comparador (p. ej., NCT00253162, NCT00253149, NCT00129220) y una revisión sistemática con metaanálisis en red (PMID 34642461). Sin embargo, la manía aguda es un uso ya establecido, por lo que no es un reposicionamiento genuino. Si se evalúa, requeriría vigilar síntomas extrapiramidales, prolongación del QT, discinesia tardía y exposición antenatal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

