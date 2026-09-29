---
layout: default
title: Candesartan Cilexetil
parent: Solo Predicción del Modelo (L5)
nav_order: 109
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Candesartán cilexetilo: De Indicación Original No Especificada a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Candesartán cilexetilo es un antagonista del receptor de angiotensina II tipo 1 (ARA-II) comercializado en Colombia. Los registros sanitarios disponibles no detallan su indicación original.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica el texto "CANDESARTAN") |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, candesartán es un bloqueador del receptor AT1 de angiotensina II. Al bloquear este receptor reduce la vasoconstricción mediada por el sistema renina-angiotensina-aldosterona (SRAA), y mecanísticamente podría ser aplicable a la hipertensión renovascular.

La hipertensión renovascular maligna depende en gran medida del SRAA. Por eso el vínculo biológico es plausible. Las demás indicaciones predichas comparten el mismo puntaje o uno muy cercano (0.997). Esto sugiere que provienen de una vecindad similar en el grafo de conocimiento y no de evidencia independiente.

Este vínculo es teórico. No hay ensayos ni literatura que lo confirmen, y los datos de indicación original y de mecanismo de acción están incompletos. El puntaje alto de TxGNN es solo una predicción del modelo.

Otras indicaciones predichas (todas con nivel L5 y recomendación Hold):

| Rango | Indicación predicha | Puntaje | Observación |
|------|------|------|------|
| 2 | Enfermedad renal hipertensiva maligna | 99.68% | Vínculo plausible por daño vascular mediado por el SRAA; sin ensayos ni literatura |
| 3 | Hipertensión pulmonar por enfermedad pulmonar o hipoxia | 99.67% | Las publicaciones recuperadas son de biología general de la hipoxia y no evalúan candesartán ni ningún ARA-II |
| 4 | Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.67% | Categoría heterogénea; no permite establecer una justificación específica |
| 5 | Síndrome de Braddock | 99.56% | Sin vínculo mecanístico identificable; probable artefacto del grafo |

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
| 19995395 | CANDEPREX® 16 MG TABLETAS (MEGALABS COLOMBIA S.A.S) | Tableta (vía oral) | CANDESARTAN (sin descripción de indicación) |

Nota: los 5 registros listados en el Evidence Pack son idénticos (mismo número de registro y mismo producto). El total informado es de 20 registros sanitarios.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Del análisis de racionalidad (no del prospecto) se desprenden estos riesgos que deben evaluarse antes de cualquier propuesta:
- **Función renal**: los ARA-II pueden causar deterioro agudo de la función renal en estenosis bilateral de arteria renal o riñón único. Esto es especialmente relevante en hipertensión renovascular.
- **Hiperpotasemia**: requiere revisión específica en lesión renal grave.
- **Hipertensión pulmonar por enfermedad pulmonar**: los vasodilatadores pueden empeorar el acoplamiento ventilación-perfusión en pulmón hipóxico.

No se encontraron interacciones farmacológicas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las cinco indicaciones predichas tienen nivel de evidencia L5: no hay ensayos clínicos ni literatura pertinente, y el puntaje de 99.68% proviene solo del modelo. Además, falta el prospecto de INVIMA (brecha bloqueante para el tamizaje de seguridad) y el riesgo renal de los ARA-II exige evaluación específica.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), brecha bloqueante.
- Obtener el mecanismo de acción y las indicaciones originales desde DrugBank.
- Realizar una búsqueda dirigida de literatura sobre ARA-II o candesartán en hipertensión renovascular maligna y en enfermedad renal hipertensiva maligna.
- Buscar ensayos clínicos específicos de ARA-II en estas indicaciones.
- Definir un plan de seguridad renal (creatinina, potasio, estenosis de arteria renal) antes de considerar cualquier propuesta.
- Descartar la indicación de síndrome de Braddock, que probablemente es un artefacto del grafo, salvo que aparezca evidencia independiente.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Todo candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

