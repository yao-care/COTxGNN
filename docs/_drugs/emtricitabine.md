---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Emtricitabina: De Infección por VIH-1 a Infección por Virus de Inmunodeficiencia Simiana

## Resumen en Una Frase

Emtricitabina (FTC) es un inhibidor nucleosídico de la transcriptasa inversa (INTI), componente esencial de la terapia antirretroviral combinada (cART) para el tratamiento de la infección por VIH-1 en humanos.
El modelo TxGNN predice que podría ser efectivo para la **Infección por Virus de Inmunodeficiencia Simiana (SIV)**, con **0 ensayos clínicos válidos en humanos** y **20 publicaciones en modelos de primates no humanos** que actualmente respaldan esta dirección.
Sin embargo, debe tenerse en cuenta que el SIV es un patógeno de primates no humanos utilizado como modelo experimental del VIH, no una indicación clínica humana convencional.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (terapia antirretroviral combinada) |
| Nueva Indicación Predicha | Infección por Virus de Inmunodeficiencia Simiana (SIV) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el sistema. Según la información conocida, emtricitabina es un análogo nucleosídico de la citidina que, tras su fosforilación intracelular a FTC-trifosfato, se incorpora como pseudosustrato en la cadena del ADN viral en crecimiento, causando terminación prematura de cadena. Su eficacia como antirretroviral de primera línea en infección por VIH-1 ha sido ampliamente validada en ensayos clínicos de Fase 3 en humanos.

El vínculo mecanístico con el SIV es biológicamente coherente: tanto el SIV como el VIH-1 pertenecen a la familia de los lentivirus de primates, y sus transcriptasas inversas comparten alta conservación estructural. Múltiples estudios en primates no humanos (macacos) han demostrado que FTC, solo o en combinación con tenofovir, inhibe eficazmente la replicación del SIV/SHIV, con protección documentada tanto en modelos de profilaxis pre-exposición (PrEP) como en modelos de tratamiento activo.

No obstante, existe una limitación fundamental para el reposicionamiento clínico: el SIV es esencialmente una enfermedad animal utilizada como modelo experimental del VIH en primates no humanos. No existe una indicación clínica humana de "infección por SIV", por lo que esta predicción refleja la solidez del modelo animal antes que una oportunidad de reposicionamiento farmacológico clínico convencional. La alta puntuación TxGNN (99.92%) refleja la proximidad biológica entre VIH y SIV en el grafo de conocimiento, no necesariamente una brecha terapéutica humana sin cubrir.

---

## Evidencia de Ensayos Clínicos

Los 2 registros recuperados de ClinicalTrials.gov corresponden a ensayos en infección por VIH humano — no en SIV — y ninguno es aplicable directamente a esta indicación (uno fue retirado sin inscripción; el otro estudia inmunomodulación en pacientes VIH). Ambos fueron clasificados como Grado C (mismatched) por el sistema de relevancia.

Actualmente no hay ensayos clínicos registrados para el tratamiento o prevención de la infección por SIV en humanos, lo cual es esperado dado que el SIV es una enfermedad de primates no humanos.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Estudio NHP controlado | J Infect Dis | TAF solo o combinado con FTC previene infección vaginal por SHIV en macacos; apoya uso de FTC como componente de PrEP |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Estudio NHP | J Infect Dis | FTC + TAF oral protege macacos contra infección rectal por SHIV (hasta 19 exposiciones semanales) |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Estudio NHP controlado | J Infect Dis | FTC/TDF oral previene infección vaginal por SHIV incluso con coinfección por Chlamydia y Trichomonas |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Estudio NHP | J Infect Dis | Gel vaginal con FTC/TFV brinda protección dual vaginal y rectal frente a SHIV en macacos |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Estudio NHP controlado | J Infect Dis | FTC/TDF intermitente mantiene eficacia profiláctica contra SHIV portador de mutación K65R (resistente a tenofovir) |
| [32128569](https://pubmed.ncbi.nlm.nih.gov/32128569/) | 2020 | Estudio NHP | J Infect Dis | Comparación cabotegravir LA vs. FTC/TDF oral en modelo de transmisión peneana de SHIV; ambos con alta eficacia |
| [22814162](https://pubmed.ncbi.nlm.nih.gov/22814162/) | 2012 | Estudio NHP | Jpn J Infect Dis | Doble dosis oral de FTC/TDF previene infección por SHIV altamente patogénico (KS661c) en macacos cynomolgus |
| [21632769](https://pubmed.ncbi.nlm.nih.gov/21632769/) | 2011 | Estudio NHP | J Virology | Truvada (FTC/TDF) intermitente protege contra SHIV-M184V (variante resistente a FTC) por vía rectal |
| [19656878](https://pubmed.ncbi.nlm.nih.gov/19656878/) | 2009 | Estudio NHP | J Virology | Gel tópico con TFV ± FTC otorga protección completa frente a desafíos vaginales repetidos con SHIV |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Estudio animal | J Virology | ART con FTC + tenofovir suprime SIVagm en monos verdes africanos; modela dinámica viral en hospederos naturales |

---

## Información de Mercado en Colombia

Emtricitabina no cuenta con registros sanitarios activos ante el INVIMA. El medicamento no está comercializado en el mercado colombiano en ninguna presentación.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente coherente — FTC inhibe la transcriptasa inversa tanto de VIH como de SIV por el mismo mecanismo — pero la infección por SIV es una enfermedad de primates no humanos sin correlato clínico humano directo; no existe una indicación médica humana que reposicionar, y el medicamento no está comercializado en Colombia.

**Para avanzar se necesita:**
- Clarificar el objetivo estratégico: ¿reposicionamiento en investigación veterinaria/preclínica o exploración de modelos de VIH en NHP?
- Obtener datos de MOA desde DrugBank (DG002) para completar el análisis mecanístico formal
- Evaluar la indicación de rango 2 (**síndrome de inmunodeficiencia adquirida felina / FAIDS**) como candidato veterinario clínicamente más accionable, dado que existe un estudio publicado en gatos domésticos con FTC (PMID 37112803)
- Si el objetivo es Colombia, iniciar trámite de registro ante INVIMA para emtricitabina, dado que el mercado local actualmente no cuenta con ningún producto aprobado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

