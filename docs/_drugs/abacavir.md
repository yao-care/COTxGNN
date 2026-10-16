---
layout: default
title: Abacavir
parent: Evidencia Moderada (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Abacavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L4). Indicación original: Abacavir/zidovudina/lamivudina (combinación antirretroviral)"
monitor_inn: "ABACAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Abacavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Abacavir: De Terapia Antirretroviral (VIH) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Abacavir es un inhibidor nucleósido de la transcriptasa inversa, registrado en Colombia únicamente como parte de combinaciones antirretrovirales (abacavir/zidovudina/lamivudina y lamivudina/abacavir).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero actualmente no hay ensayos clínicos y solo **1 publicación** preclínica respalda esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Abacavir/zidovudina/lamivudina (combinación antirretroviral) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, abacavir es un inhibidor nucleósido de la transcriptasa inversa (INTI) que actúa sobre la transcriptasa inversa de lentivirus, y su eficacia en la infección por VIH ha sido comprobada en combinación con otros antirretrovirales.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus cuya transcriptasa inversa se asemeja a la del VIH-1, y el gato doméstico se utiliza como modelo animal de la infección por VIH. Por ello existe una justificación mecanística: varios inhibidores de la transcriptasa inversa activos contra el VIH también lo son contra el FIV.

Conviene tener cautela. El único respaldo es un estudio de 2002 sobre la combinación zidovudina, lamivudina y abacavir; no es posible separar la contribución individual de abacavir. El puntaje tan alto de TxGNN es una predicción computacional que probablemente refleja la relación conocida de clase antirretroviral. Además, es una indicación veterinaria y de valor limitado para el reposicionamiento en humanos.

### Otras predicciones del modelo

- **Infección por el virus de inmunodeficiencia simia (SIV)** (99.79%, nivel L4, Hold): respaldada solo por un estudio *in vitro* de 2004 sobre la susceptibilidad de VIH-2, SIV y SHIV (PMID [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/), *Antiviral Therapy*). Es un modelo animal de VIH y la indicación ya está cubierta por el uso establecido en VIH-1.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de la sustancia blanca cortical** (99.78%, nivel L5, Hold): sin ensayos ni literatura, y sin vínculo mecanístico sustentado en los datos disponibles.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Estudio preclínico de combinación (inferido del título; por verificar) | Antiviral Research | Efecto combinado de zidovudina, lamivudina y abacavir para suprimir la replicación del FIV *in vitro*. El FIV en el gato es un modelo animal del VIH, y varios inhibidores de la transcriptasa inversa activos contra el VIH también lo son contra el FIV. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20203375 (cancelado) | SELMIVIR® | Tableta recubierta | Abacavir/zidovudina/lamivudina |
| 20140104 (cancelado) | KAVIDUVIR® tableta recubierta | Tableta recubierta | Lamivudina y abacavir |

No hay registros vigentes actualmente en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo asociadas (grafo de conocimiento TxGNN, no texto de prospecto):** insuficiencia hepática, enfermedad hepática, hígado graso y esteatohepatitis no alcohólica; enfermedad renal; pancreatitis; enfermedad de la vesícula biliar; miopatías y enfermedades musculares (incluida parálisis periódica familiar, dermatomiositis y miositis); neutropenia, agranulocitosis y anemia (incluida la macrocítica); hipertrigliceridemia; trastornos de obesidad; acidosis láctica; piouréter.
- **Interacciones farmacológicas:** se identificaron 93 interacciones potenciales. Las de nivel moderado incluyen **naltrexona** y **orlistat**. Otras (nivel no clasificado) incluyen metformina, omeprazol, pantoprazol, lansoprazol, morfina, prednisona, hidrocortisona, vancomicina, anfotericina B, sulfasalazina, sucralfato, glimepirida, rosiglitazona, lactulosa, oxandrolona, nistatina, cloruro de potasio y vitamina A.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un estudio preclínico de combinación sin ensayos clínicos (nivel L4), la indicación predicha es veterinaria, y abacavir no tiene actualmente registros vigentes en Colombia. El alto puntaje de TxGNN refleja probablemente la relación de clase antirretroviral más que una oportunidad nueva de reposicionamiento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de abacavir (consulta a DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA (necesarias para el cribado de seguridad).
- Verificar el diseño y los resultados del estudio de 2002 y determinar la contribución individual de abacavir.
- Confirmar el interés real en una indicación veterinaria o, en su defecto, priorizar otras predicciones con mayor valor traslacional.
- Evaluar la situación regulatoria (registros cancelados) antes de cualquier desarrollo local.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

