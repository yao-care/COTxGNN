---
layout: default
title: Darunavir
parent: Solo Predicción del Modelo (L5)
nav_order: 196
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Darunavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Combinaciones (ritonavir y darunavir)"
---

# Darunavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Darunavir: De Combinaciones con Ritonavir (VIH) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Darunavir es un inhibidor de la proteasa del VIH-1, registrado en Colombia en combinación con ritonavir.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica. Se trata de una indicación veterinaria, fuera del alcance habitual del reposicionamiento en humanos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones (ritonavir y darunavir) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, darunavir es un inhibidor de la proteasa del VIH-1, usado en combinación con ritonavir, y su eficacia en la infección por VIH está establecida. Mecanísticamente, podría ser aplicable a otros lentivirus relacionados.

El virus de inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH, por lo que un vínculo es plausible. Sin embargo, la proteasa del FIV difiere estructuralmente de la del VIH-1, y las diferencias en la especificidad de sustrato podrían reducir la unión del inhibidor. El puntaje alto (0.9997) es solo una predicción y probablemente refleja la cercanía con nodos relacionados con VIH en el grafo de conocimiento.

Además, es una indicación veterinaria, por lo que su valor para el reposicionamiento en humanos es limitado.

### Otras predicciones del modelo (para contexto)

| Rango | Enfermedad predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|---|---|---|---|---|
| 2 | Infección por virus de inmunodeficiencia simia (SIV) | 99.97% | L4 | Solo estudios preclínicos en macacos con regímenes combinados de cART; la contribución de darunavir no puede separarse. Su valor traslacional está en el VIH, que ya es la indicación original. |
| 3 | Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de sustancia blanca cortical | 99.97% | L5 | Sin vínculo mecanístico plausible; probable artefacto del grafo de conocimiento. |
| 4 | Hiperlipidemia combinada familiar (término obsoleto) | 99.19% | L5 | Los inhibidores de proteasa suelen causar dislipidemia; el efecto esperado podría ser opuesto al buscado. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (inmunodeficiencia adquirida felina).

Como referencia, para la segunda predicción (infección por SIV) se recuperaron las siguientes publicaciones preclínicas en macacos:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Estudio preclínico animal | PloS one | Terapia antirretroviral combinada supresora más el inhibidor de HDAC SAHA en macacos rhesus infectados con SIV, para estudiar reservorios virales |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Estudio preclínico animal | AIDS Res Hum Retroviruses | Comparación de regímenes inyectables coformulados de cART en macacos infectados con SIVmac239 |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Estudio preclínico animal | AIDS | Auranofina junto con cART restringe el reservorio viral en el modelo de SIDA en monos |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Estudio preclínico animal | PLoS Pathogens | Régimen antirretroviral muy intensificado que logra supresión viral prolongada y restricción del reservorio en macacos |

Estos estudios son indirectos: evalúan combinaciones de antirretrovirales y no se ha confirmado el papel específico de darunavir (se requeriría revisar el texto completo).

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20109284 | VIRONTAR N COMPRIMIDOS RECUBIERTOS | Tableta recubierta | Combinaciones (ritonavir y darunavir) | Cancelado |
| 20109025 | VIRONTAR | Comprimido | Darunavir + ritonavir | Cancelado |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, cirrosis hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, infección crónica por virus de hepatitis C, infección por virus de hepatitis C, infección crónica por virus de hepatitis B, hipertrigliceridemia y hemofilia (incluida la forma sintomática en portadoras).
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las principales:
  - **Mayor:** cisaprida.
  - **Moderadas:** antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, dapagliflozina, saxagliptina, clorpropamida, acetohexamida), corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida), aprepitant y claritromicina.

Se recomienda consultar el prospecto para advertencias y contraindicaciones oficiales, ya que no se dispuso de ellas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal carece de ensayos clínicos y literatura (nivel L5), corresponde a una indicación veterinaria y no tiene respaldo mecanístico sólido. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de darunavir (por ejemplo, desde DrugBank).
- Prospecto de INVIMA con advertencias y contraindicaciones.
- Evaluación de si la indicación veterinaria está dentro del alcance del programa; de lo contrario, priorizar indicaciones humanas.
- Estudios de afinidad de darunavir con la proteasa del FIV.
- Revisión de texto completo de los estudios en SIV para determinar la contribución de darunavir.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

