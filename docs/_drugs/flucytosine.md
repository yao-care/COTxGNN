---
layout: default
title: Flucytosine
parent: Solo Predicción del Modelo (L5)
nav_order: 290
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Flucytosine: nueva indicación predicha, Enfermedad ósea de Paget (nivel de evidencia L5). Indicación original: FLUCITOSINA"
monitor_inn: "flucytosine"
drugbank_id: DB01099
predicted_indications: ["bone Paget disease"]
---

# Flucytosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Flucitosina: De Indicación Original (FLUCITOSINA) a Enfermedad Ósea de Paget
{: .text-alpha }

## Resumen en Una Frase

Flucitosina es un antimicótico.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad ósea de Paget**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

<!-- review:begin co-lic-20261105-flucytosine-4 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Flucitosina es un antimicótico que en Colombia contaba con un registro sanitario (ANCOTOSIN®) cuya indicación aprobada figura únicamente como "FLUCITOSINA"." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-flucytosine-4 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FLUCITOSINA (el texto del registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Enfermedad ósea de Paget |
| Puntaje de Predicción TxGNN | 0.9904 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Clinical Pharmacology» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Flucytosine (traducción no oficial): «La flucitosina es captada por los organismos fúngicos a través de la enzima citosina permeasa. Dentro de la célula fúngica, la enzima citosina desaminasa convierte rápidamente la flucitosina en fluorouracilo. El fluorouracilo ejerce su actividad antifúngica mediante su conversión posterior en varios metabolitos activos, que inhiben la síntesis de proteínas al incorporarse de forma falsa al ARN fúngico o interfieren con la biosíntesis del ADN fúngico mediante la inhibición de la enzima timidilato sintetasa.» Texto original en inglés: "Flucytosine is taken up by fungal organisms via the enzyme cytosine permease. Inside the fungal cell, flucytosine is rapidly converted to fluorouracil by the enzyme cytosine deaminase. Fluorouracil exerts its antifungal activity through the subsequent conversion into several active metabolites, which inhibit protein synthesis by being falsely incorporated into fungal RNA or interfere with the biosynthesis of fungal DNA through the inhibition of the enzyme thymidylate synthetase." ([DailyMed: Ancobon (flucytosine) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aea0df00-a88c-4a16-abcf-750f3ff2004e), versión del 2022-02-02; consultado el 2026-11-19). Según la información conocida, la flucitosina es un profármaco antimicótico: la citosina desaminasa fúngica la convierte en 5-fluorouracilo, que inhibe la síntesis de ADN y ARN del hongo. Su eficacia se asocia a infecciones fúngicas, no a enfermedades óseas.

La enfermedad ósea de Paget se caracteriza por una actividad osteoclástica desregulada y un recambio óseo aumentado, con factores genéticos como variantes de SQSTM1. Nada en los datos disponibles conecta la flucitosina con estas vías. No se identificó un vínculo mecanístico establecido entre la indicación original y la nueva.

Cualquier justificación posible (por ejemplo, efectos de metabolitos tipo 5-FU sobre células en proliferación) sería especulativa. El puntaje alto de TxGNN (0.9904) es una predicción derivada del modelo y no está respaldado por evidencia clínica ni bibliográfica.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20135088 | ANCOTOSIN® | CAPSULA DURA | FLUCITOSINA | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

El fabricante es Global Service Pharmaceutical S.A.S.

<!-- review:begin co-lic-20261105-flucytosine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El fabricante es Global Service Pharmaceutical S.A.S. No hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-flucytosine-2 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia la flucitosina con contraindicación en:
  - Enfermedad renal y piouréter
  - Enfermedad hepática y enfermedad de la vesícula biliar
  - Trombocitopenia, leucopenia, agranulocitosis y neutropenia (incluidas diversas formas congénitas, constitucionales e idiopáticas del adulto)
  - Anemia aplásica (adquirida y otras formas)
  - Hematopoyesis cíclica
  - Deficiencia de potasio
- **Interacciones farmacológicas**: se registraron 85 interacciones, de las cuales se muestran 20. Casi todas son de nivel moderado:
  - Anfotericina B (incluidas las formulaciones lipídicas, de sulfato de colesterilo y liposomal)
  - Aminoglucósidos y otros antibióticos: vancomicina, kanamicina, neomicina, estreptomicina, polimixina B, bacitracina
  - Mesalazina, balsalazida, olsalazina y sulfasalazina
  - Deferasirox, pentamidina, ibuprofeno, yobenguano (I-131) y cloruro de estroncio Sr-89
  - **Deferiprona**: interacción de nivel **mayor**, la de mayor gravedad en la lista mostrada.

Las advertencias principales y contraindicaciones del prospecto de INVIMA no están disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible con la enfermedad ósea de Paget. Además, el perfil de seguridad sugiere riesgos hematológicos, renales y hepáticos relevantes.

<!-- review:begin co-lic-20261105-flucytosine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario local está cancelado y el perfil de seguridad sugiere riesgos hematológicos, renales y hepáticos relevantes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-flucytosine-3 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), ya que su ausencia bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y ensayos que relacionen la flucitosina o el 5-FU con la enfermedad ósea de Paget.
- Evaluar estudios preclínicos que respalden un posible mecanismo antes de reconsiderar la candidatura.

<!-- review:begin co-lic-20261031-flucytosine-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Evaluar estudios preclínicos que respalden un posible mecanismo antes de reconsiderar la candidatura. / Aclarar la indicación clínica real del producto y su situación regulatoria (registro cancelado) si se contempla uso en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-flucytosine-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la indicación clínica real del producto y su situación regulatoria (registro cancelado) si se contempla uso en Colombia" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "No hay registros vigentes en Colombia" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario local está cancelado y" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "que en Colombia contaba con un registro sanitario (ANCOTOSIN®) cuya indicación aprobada figura únicamente como "FLUCITOSINA"" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ancobon (flucytosine) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aea0df00-a88c-4a16-abcf-750f3ff2004e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

