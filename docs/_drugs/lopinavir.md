---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir: De Infección por VIH a Infección por Virus de Inmunodeficiencia Simia

## Resumen en Una Frase

Lopinavir es un inhibidor de proteasa del VIH-1, utilizado típicamente en combinación con ritonavir (Lopinavir/Ritonavir) para el tratamiento de la infección por VIH en humanos.
El modelo TxGNN predice que podría ser efectivo para la **Infección por Virus de Inmunodeficiencia Simia (SIV)**,
con **0 ensayos clínicos** y **3 publicaciones** en modelos de primates no humanos que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (sin registro activo en Colombia) |
| Nueva Indicación Predicha | Infección por Virus de Inmunodeficiencia Simia |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Lopinavir en el sistema de información. Según la información conocida, Lopinavir es un inhibidor de la proteasa del VIH-1 que actúa bloqueando su sitio activo, impidiendo la maduración de nuevas partículas virales infecciosas. Se administra siempre potenciado con ritonavir para mejorar su farmacocinética.

La conexión entre la indicación original (VIH-1) y la nueva indicación predicha (infección por SIV) se basa en la homología estructural entre las proteasas del VIH-1 y del SIV: ambos virus pertenecen al género *Lentivirus* y comparten similitudes en el sitio catalítico de la proteasa, lo que haría teóricamente posible una inhibición cruzada. Los tres estudios identificados en la literatura utilizan regímenes HAART que incluyen Lopinavir/Ritonavir en macacos infectados con SIV o SHIV, observando reducción rápida de la carga viral.

Sin embargo, existe una limitación fundamental que condiciona el valor de esta predicción: la infección por SIV afecta exclusivamente a primates no humanos. No representa una indicación clínica en humanos, sino un modelo animal de investigación del VIH. Por tanto, este hallazgo tiene relevancia como validación preclínica del mecanismo de inhibición de proteasa, pero **no constituye una oportunidad de reposicionamiento para uso humano en sentido estricto**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudio Animal (PNH) | Journal of Virology | Cuatro macacos cinomolgos infectados con SIVmac251 recibieron terapia antirretroviral cuádruple (incluyendo Lopinavir) durante 7 días; se observó rápida disminución viral, comparable a la dinámica descrita en infección por VIH-1 en humanos |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Investigación Básica / Animal | Microbes and Infection | Construcción de SHIV con gen de proteasa derivado del VIH-1; el crecimiento viral fue completamente bloqueado por inhibidor de proteasa in vitro; inoculación en macacos rhesus produjo viremia débil pero persistente |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudio Animal (PNH) | Journal of Virological Methods | HAART oral con AZT + 3TC + Lopinavir/Ritonavir administrado durante 28 días en macacos rhesus infectados crónicamente con SHIV(89.6P); se evaluó el impacto sobre el subconjunto CD8 en sangre periférica |

---

## Información de Mercado en Colombia

Lopinavir no cuenta con registros sanitarios activos ante el INVIMA. El medicamento no está comercializado en Colombia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La infección por SIV es una enfermedad exclusiva de primates no humanos sin aplicación clínica directa en humanos; si bien la homología estructural entre las proteasas del VIH y del SIV aporta plausibilidad biológica, el contexto de los estudios disponibles (modelos animales de investigación básica) no configura una indicación reposicionable para uso humano.

**Para avanzar se necesita:**
- Obtener datos completos del mecanismo de acción (MOA) de Lopinavir mediante consulta a la API de DrugBank
- Gestionar el registro sanitario ante el INVIMA si se contempla la comercialización en Colombia
- Evaluar las indicaciones humanas de mayor rango predichas por TxGNN con evidencia clínica directa (p. ej., otras enfermedades infecciosas virales o indicaciones no virales)
- En caso de interés investigativo preclínico, definir si los hallazgos en modelos SIV son trasladables a estrategias antivirales de amplio espectro
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

