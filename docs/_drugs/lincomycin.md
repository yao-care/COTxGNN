---
layout: default
title: Lincomycin
parent: Solo Predicción del Modelo (L5)
nav_order: 404
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
monitor_inn: "lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
description: "Lincomycin: nueva indicación predicha, Hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). Indicación original: LINCOMICINA"
---

# Lincomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Lincomycin: Hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Lincomicina es un antibiótico de la clase de las lincosamidas, registrado en Colombia en presentación inyectable (el texto de indicación del registro solo dice "LINCOMICINA", sin detallar la enfermedad).
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LINCOMICINA |
| Nueva Indicación Predicha | Hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9914 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la lincomicina es un antibiótico lincosamida que inhibe la síntesis de proteínas bacterianas al unirse a la subunidad ribosomal 50S.

La hiperamilasemia es un hallazgo de laboratorio (elevación de amilasa en sangre), asociado con frecuencia a pancreatitis, enfermedad de las glándulas salivales o insuficiencia renal. No es un proceso bacteriano, por lo que **no se identifica un vínculo mecanístico plausible** entre la acción antibacteriana de la lincomicina y esta condición.

El puntaje alto de TxGNN (0.9914) proviene únicamente de una predicción computacional del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Sin respaldo clínico ni bibliográfico, la relación podría reflejar ruido de asociación o eventos adversos y no un potencial terapéutico real.

Las otras dos predicciones evaluadas tampoco muestran respaldo: el síndrome de hiperviscosidad policlonal (0.9914) y la analbuminemia congénita (0.9906) carecen de ensayos, literatura y mecanismo plausible. La analbuminemia congénita es un defecto genético de la síntesis de albúmina que un antibacteriano no puede corregir.

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
| 20134615 | LINCOMICINA INYECCION 600 MG/2ML (Caplin Point Laboratories Colombia S.A.S.) | Solución inyectable | LINCOMICINA | Vigente |
| 40743 | LINCOCIN® 600 MG/ 2 ML SOLUCION INYECTABLE (Pfizer S.A.S.) | Solución inyectable | LINCOMICINA | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, colitis y enfermedades del sistema digestivo e intestinales en general.
- **Interacciones farmacológicas:** se identificaron 21 interacciones. Las de nivel **moderado** son con balsalazida, ácido picosulfúrico, attapulgita, caolín, eritromicina y etinilestradiol. Otras 15 interacciones (clotrimazol, cimetidina, morfina, metformina, omeprazol, lactulosa, triamcinolona, simvastatina, ranitidina, warfarina, lidocaína, cetirizina, montelukast, salmeterol, entre otras) tienen gravedad no clasificada.

Consultar el prospecto para información adicional de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un mecanismo farmacológico plausible. Además, las predicciones alternativas (hiperviscosidad policlonal y analbuminemia congénita) tienen el mismo problema.

<!-- review:begin co-lic-20261105-lincomycin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros sanitarios vigentes en Colombia, y las predicciones alternativas (hiperviscosidad policlonal y analbuminemia congénita) tienen el mismo problema." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lincomycin-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank para evaluar si existe algún vínculo biológico real.
- Revisión de literatura que descarte que la señal provenga de eventos adversos o ruido de asociación (por ejemplo, elevación de amilasa como hallazgo secundario).
- Prospecto oficial de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad.
- Aclarar la situación regulatoria.

<!-- review:begin co-lic-20261105-lincomycin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria, dado que ambos registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lincomycin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "no hay registros sanitarios vigentes en Colombia, y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que ambos registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

