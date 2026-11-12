---
layout: default
title: Lithium Carbonate
parent: Solo Predicción del Modelo (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Lithium Carbonate: nueva indicación predicha, Pseudoacondroplasia (nivel de evidencia L5). Indicación original: Litio"
monitor_inn: "Lithium carbonate"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
---

# Lithium Carbonate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Carbonato de Litio: De Litio (indicación registrada) a Pseudoacondroplasia
{: .text-alpha }

## Resumen en Una Frase

El modelo TxGNN predice que podría ser efectivo para **pseudoacondroplasia**, pero actualmente no hay **ningún ensayo clínico** ni **publicaciones** que respalden específicamente esta indicación; se trata de una predicción puramente computacional.

<!-- review:begin co-lic-20261105-lithium_carbonate-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El carbonato de litio contaba en Colombia con registros sanitarios para su uso como litio (la indicación aprobada se registra solo como "LITIO"). El modelo TxGNN predice que podría ser efectivo para **pseudoacondroplasia**, pero actualmente no hay **ningún ensayo clínico** ni **publicaciones** que respalden específicamente esta indicación; se trata de una predicción puramente computacional." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lithium_carbonate-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Litio (texto registrado en INVIMA, sin mayor detalle) |
| Nueva Indicación Predicha | Pseudoacondroplasia |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, el litio inhibe la enzima GSK-3β y modula la vía de señalización Wnt/β-catenina, que participa en la biología del condrocito y de la placa de crecimiento.

La pseudoacondroplasia es causada por mutaciones en el gen COMP, que provocan estrés del retículo endoplásmico y muerte de los condrocitos. El vínculo con el litio es **puramente especulativo**: no existe evidencia directa que relacione el fármaco con esta enfermedad. El puntaje alto de TxGNN (0.9998) es solo una predicción computacional y no sustituye la evidencia clínica.

Cabe señalar que otras predicciones del modelo (por ejemplo, displasia acromesomélica tipo Hunter-Thompson, braquiolmia o síndromes de displasia esquelética) comparten la misma debilidad: ninguna cuenta con ensayos clínicos, y para varias de ellas el riesgo teratogénico conocido del litio obliga a la cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para pseudoacondroplasia.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20018308 | ACTILITIO® TABLETAS 300 MG | Tableta | LITIO | Vigente |
| 20005911 | THERALITE® 300 MG | Tableta | LITIO | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento (no provienen del prospecto):** enfermedad renal, piouréter, trastorno cognitivo, hipotiroidismo, mixedema, hipotiroidismo congénito, psoriasis, parapsoriasis, paro cardíaco súbito, enfermedad de la conducción cardíaca y diabetes insípida (neurohipofisaria/central).
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total; entre las mostradas destacan las de nivel **mayor** con **bupropión** y **lorcaserina**. Hay numerosas interacciones de nivel moderado (por ejemplo, metformina, pioglitazona, acarbosa, canagliflozina, clorpropamida, famotidina, metronidazol, claritromicina, morfina, loperamida, mesalazina, balsalazida, citrato de potasio, albiglutida y alogliptina) y de nivel menor (doxiciclina, epinefrina y ácido acetilsalicílico).
- **Riesgo teratogénico:** el litio es una preocupación conocida en el embarazo, lo que limita su uso en trastornos del desarrollo.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo, sin ensayos clínicos ni literatura específica (nivel L5). Además, el mecanismo es especulativo, el perfil de seguridad del litio es exigente y no existen registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco y análisis del vínculo mecanístico con la pseudoacondroplasia
- Estudios preclínicos (modelos de condrocitos o de ratón con mutaciones en COMP) que respalden la hipótesis
- Revisión del prospecto de INVIMA para completar advertencias y contraindicaciones
- Evaluación del balance riesgo-beneficio, incluido el riesgo teratogénico y la toxicidad renal y tiroidea
- Aclarar la situación regulatoria

<!-- review:begin co-lic-20261105-lithium_carbonate-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria, dado que ambos registros están cancelados" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lithium_carbonate-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "dado que ambos registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "El carbonato de litio contaba en Colombia con registros sanitarios para su uso como litio (la indicación aprobada se registra solo como "LIT" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

