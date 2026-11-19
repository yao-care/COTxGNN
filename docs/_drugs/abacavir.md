---
layout: default
title: Abacavir
parent: Solo Predicción del Modelo (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
monitor_inn: "ABACAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-20
description: "Abacavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) (nivel de evidencia L5). Indicación original: ABACAVIR/ZIDOVUDINA/LAMIV…"
---

# Abacavir
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

## Abacavir: inhibidor nucleosídico de la transcriptasa inversa → síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumen en Una Frase

Abacavir es un inhibidor nucleosídico de la transcriptasa inversa (INTI) de uso antirretroviral.
El modelo TxGNN predice que podría ser efectivo para la **síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)**,
pero la evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** preclínica, que evaluó una combinación de fármacos y no abacavir de forma aislada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ABACAVIR/ZIDOVUDINA/LAMIVUDINA; LAMIVUDINA Y ABACAVIR |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 0.9979 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 7) |
| Número de Registros Sanitarios | 7 (vigentes: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para abacavir and lamivudine (combinación que contiene Abacavir) (traducción no oficial): «Abacavir y lamivudina es un agente antirretroviral con actividad contra el VIH-1.» Texto original en inglés: "Abacavir and lamivudine is an antiretroviral agent with activity against HIV-1." ([DailyMed: abacavir and lamivudine prescribing information, Laurus Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12e80eb-906c-4932-bb03-b4060ba1d31c), versión del 2026-09-18; consultado el 2026-11-19). Según la información conocida, abacavir pertenece a la clase de los inhibidores nucleosídicos de la transcriptasa inversa, que actúan sobre la enzima que los retrovirus necesitan para copiar su material genético.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus cuya transcriptasa inversa guarda relación con la del VIH-1. Por eso existe una justificación mecanística plausible. El puntaje alto del modelo (0.9979) es una predicción computacional y probablemente refleja la cercanía de esta clase de antirretrovirales con los virus de este grupo.

Hay una limitación importante: el único estudio disponible (2002) evaluó la combinación de zidovudina, lamivudina y abacavir sobre la replicación del FIV in vitro. No es posible separar la contribución individual de abacavir, y el resumen disponible está truncado. Por ello, el estudio no basta para sostener un nivel de evidencia superior a L5 con los datos actuales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Estudio preclínico de combinación (inferido del título) | Antiviral Research | Evalúa el efecto combinado de zidovudina, lamivudina y abacavir para suprimir la replicación del FIV in vitro; el FIV se usa como modelo animal del VIH. No permite aislar el aporte de abacavir. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20203375 | SELMIVIR® | Tableta recubierta | Abacavir/zidovudina/lamivudina |
| 20140104 | KAVIDUVIR® tableta recubierta | Tableta recubierta | Lamivudina y abacavir |

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo registradas en la base de conocimiento del modelo (no provienen del prospecto)**: insuficiencia hepática, enfermedad hepática, hígado graso, esteatohepatitis no alcohólica, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, miopatía, miositis, dermatomiositis, neutropenia, agranulocitosis, anemia, hipertrigliceridemia, obesidad y acidosis láctica.
- **Interacciones Farmacológicas**: se identificaron 93 interacciones potenciales. Las de nivel moderado son naltrexona y orlistat. Otras interacciones, de gravedad no clasificada, incluyen metformina, omeprazol, pantoprazol, lansoprazol, prednisona, hidrocortisona, morfina, vancomicina, anfotericina B y sulfasalazina, entre otras.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un estudio preclínico in vitro de una combinación de fármacos, sin ensayos clínicos y sin evidencia que aísle el efecto de abacavir. Por ello, el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios que evalúen abacavir de forma individual frente al FIV, in vitro e in vivo.
- Confirmar el diseño y los resultados del estudio de 2002 mediante el texto completo.
- Datos del mecanismo de acción y del prospecto aprobado (advertencias y contraindicaciones).
- Definir si existe interés veterinario real, dado que la indicación corresponde a una enfermedad felina y no humana.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: abacavir and lamivudine prescribing information, Laurus Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12e80eb-906c-4932-bb03-b4060ba1d31c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

