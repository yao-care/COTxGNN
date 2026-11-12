---
layout: default
title: Calcitriol
parent: Solo Predicción del Modelo (L5)
nav_order: 128
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
description: "Calcitriol: nueva indicación predicha, Deficiencia de vitamina D (término obsoleto) (nivel de evidencia L5). Indicación original: No detallada"
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Calcitriol: De una Indicación No Detallada en el Registro a Deficiencia de Vitamina D (término obsoleto)
{: .text-alpha }

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D. En Colombia sus registros sanitarios solo indican "Calcitriol" como indicación, sin detallar para qué enfermedad se aprobó.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de vitamina D (término obsoleto)**, pero **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada (el registro solo indica "Calcitriol") |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, calcitriol es la forma activa de la vitamina D, por lo que existe un vínculo biológico plausible con la deficiencia de vitamina D.

Sin embargo, el término de la enfermedad está marcado como **obsoleto**, es decir, es una entrada de ontología en desuso. El puntaje alto probablemente refleja un artefacto de nomenclatura y no una indicación nueva y accionable. No se aportaron ensayos ni literatura que lo respalden.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-calcitriol-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los dos registros sanitarios están **cancelados**; no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-calcitriol-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19934690 | Calcitriol 0.25 mcg cápsula blanda (COLMED LTDA) | Cápsula blanda | Calcitriol |
| 19942545 | Calcitriol 0.5 mcg (COLMED LTDA) | Cápsula blanda | Calcitriol |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): enfermedad renal, piouréter, sarcoidosis, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, susceptibilidad a nefrolitiasis por SLC26A1, nefrolitiasis, nefropatía aguda por uratos, hiperfosfatemia, hipervitaminosis y arteriosclerosis obliterante.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las principales:
  - **Mayores**: colecalciferol, burosumab y calcifediol.
  - **Moderadas**: fosfenitoína, hidroclorotiazida, amobarbital, butalbital, butabarbital, carbamazepina, calcipotriol tópico, hidróxido de aluminio, tiazidas y similares (bendroflumetiazida, benztiazida, clorotiazida, clortalidona), resinas de unión a ácidos biliares (colestiramina, colesevelam, colestipol) y glucósidos digitálicos (digitoxina, digoxina).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya solo en el modelo (L5), sin ensayos ni literatura, y corresponde a un término de enfermedad obsoleto.

<!-- review:begin co-lic-20261105-calcitriol-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción principal se apoya solo en el modelo (L5), sin ensayos ni literatura, y corresponde a un término de enfermedad obsoleto. Además, los dos registros sanitarios en Colombia están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-calcitriol-2 -->

**Para avanzar se necesita:**
- Reemplazar el término obsoleto por la entidad vigente y verificar si la predicción aporta una indicación distinta de las ya conocidas.
- Obtener el mecanismo de acción detallado y las advertencias y contraindicaciones del prospecto en INVIMA.
- Evaluar la reactivación o nueva solicitud de registro.

<!-- review:begin co-lic-20261105-calcitriol-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la reactivación o nueva solicitud de registro, dado que no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-calcitriol-3 -->

**Nota sobre otras predicciones del mismo fármaco:**
Entre las demás predicciones, la **hipofosfatemia raquítica hereditaria** (puntaje 0.9928) tiene el mayor respaldo: nivel L3 y recomendación *Proceed with Guardrails*. Cuenta con 2 ensayos clínicos: uno de Fase temprana 1, completado, con 16 participantes, sobre calcitriol en monoterapia en hipofosfatemia ligada al X; y uno de Fase 4, de estado desconocido, con 100 participantes, que compara dosis de vitamina D activa más fosfato. También cuenta con múltiples revisiones que describen calcitriol más fosfato como tratamiento estándar. Requiere vigilar hipercalciuria, nefrocalcinosis e hiperparatiroidismo. La **acidosis tubular renal** tiene nivel L4, con evidencia solo fisiológica y de casos, sin evidencia de que calcitriol trate la acidosis en sí.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los dos registros sanitarios están **cancelados**; no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, los dos registros sanitarios en Colombia están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay productos vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

