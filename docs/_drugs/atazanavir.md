---
layout: default
title: Atazanavir
parent: Solo Predicción del Modelo (L5)
nav_order: 70
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Atazanavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: ATAZANAVIR+RITONAVIR"
monitor_inn: "Atazanavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Atazanavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Atazanavir: De ATAZANAVIR+RITONAVIR (VIH) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Atazanavir es un inhibidor de la proteasa del VIH-1, registrado en Colombia para su uso en combinación con ritonavir (tratamiento de la infección por VIH).
El modelo TxGNN predice que podría ser efectivo para **síndrome de inmunodeficiencia adquirida felina**, una enfermedad veterinaria, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ATAZANAVIR+RITONAVIR |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, atazanavir es un inhibidor de la proteasa del VIH-1, y su eficacia en la infección por VIH está establecida como parte de regímenes combinados con ritonavir.

El virus de inmunodeficiencia felina (FIV) es un lentivirus con una proteasa emparentada con la del VIH-1, por lo que existe una justificación mecanística teórica. Sin embargo, la proteasa del FIV difiere en especificidad de sustrato y sensibilidad a inhibidores, y no hay datos que respalden la actividad de atazanavir frente a ella.

El puntaje alto de TxGNN es solo una predicción computacional. Al ser una condición veterinaria, la relevancia clínica para humanos es mínima.

### Otras predicciones del modelo (contexto)

| Enfermedad predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Infección por virus de inmunodeficiencia símica (SIV) | 99.98% | L4 | Solo modelo animal indirecto (terapia HAART en macacos); no es un objetivo de reposicionamiento humano |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical | 99.98% | L5 | Sin vínculo mecanístico plausible; probable artefacto de la red |
| Hiperlipidemia familiar combinada (término obsoleto) | 99.82% | L5 | Los inhibidores de proteasa se asocian a alteraciones lipídicas; posible efecto en dirección opuesta |
| VIH congénito | 99.71% | L3 | Solapa con el uso original (VIH); evidencia observacional de seguridad en embarazo |
| Complejo relacionado con el SIDA | 99.71% | L3 | Solapa con el uso original; baja novedad |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal predicha.

## Evidencia de Literatura

Para la indicación principal (síndrome de inmunodeficiencia adquirida felina) no hay literatura relacionada disponible. Como referencia, la predicción de rango 2 (SIV) cuenta con una publicación indirecta, y las predicciones 5 y 6 (indicaciones muy cercanas al uso original) tienen estudios observacionales:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Estudio animal (primates no humanos) | J Infect Dis | En macacos infectados con SIV tratados con HAART, hubo menor replicación viral e inflamación en el SNC, pero persistió el ADN viral. No es específico de atazanavir |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohorte | Antivir Ther | La exposición a atazanavir durante el embarazo es efectiva, con o sin tenofovir (VIH congénito) |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohorte | JAMA Pediatr | Anomalías congénitas y exposición antirretroviral intrauterina en lactantes expuestos no infectados |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Diseño de cohorte | Front Immunol | Estudio PHACS SMARTT sobre seguridad de la exposición intrauterina a antirretrovirales |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Caso/no caso (farmacovigilancia) | Eur J Clin Pharmacol | Riesgo de anomalías congénitas tras exposición fetal a antirretrovirales en registros europeos |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohorte | J Acquir Immune Defic Syndr | Regímenes de TAR e incidencia de afecciones neurológicas definitorias de SIDA |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohorte | AIDS Rev | Factores de riesgo de eventos adversos gastrointestinales en pacientes con VIH tratados y no tratados |

Nota: la mayoría de estos estudios abordan antirretrovirales en general, no atazanavir específicamente, y no respaldan una indicación nueva distinta.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20066897 (cancelado) | VIRATAZ® TABLETAS | Tableta recubierta | ATAZANAVIR+RITONAVIR |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** insuficiencia hepática y enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, infección por hepatitis C (aguda y crónica), infección crónica por hepatitis B, hemofilia, hiperbilirrubinemia (incluida la hereditaria) y síndrome de Gilbert, nefrolitiasis, nefropatía aguda por uratos, bloqueo auriculoventricular y acidosis láctica.
- **Interacciones farmacológicas:** se identificaron 100 interacciones; entre las de nivel **Mayor** destacan famotidina, ranitidina, rabeprazol, omeprazol (reducción de acidez gástrica que puede afectar la absorción de atazanavir), loperamida, triamcinolona y budesonida. Entre las de nivel **Moderado** figuran acarbosa, hidrocortisona, albiglutida, alogliptina, metformina, pioglitazona, alosetrón, aprepitant, acetohexamida, hidróxido de aluminio, betametasona y carbonato de calcio.
- Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal predicha es una enfermedad veterinaria sin ensayos ni literatura (nivel L5), con relevancia clínica humana mínima. Además, las predicciones con algo de evidencia (VIH congénito, complejo relacionado con el SIDA) coinciden con el uso original del fármaco, por lo que no constituyen un reposicionamiento genuino. El único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA.
- Si se desea explorar la vía veterinaria, estudios de actividad de atazanavir frente a la proteasa del FIV.
- Para VIH congénito, una evaluación específica de atazanavir en embarazo, ya que la mayor parte de la evidencia es de antirretrovirales en general.
- Aclarar la situación regulatoria actual del producto en Colombia (registro cancelado).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

