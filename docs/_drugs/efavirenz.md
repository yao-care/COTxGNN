---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: De Infección por VIH-1 a Infección por Virus de Inmunodeficiencia Simiana

## Resumen en Una Frase

Efavirenz (EFV) es un inhibidor no nucleósido de la transcriptasa inversa (INNTI), originalmente desarrollado para el tratamiento de la infección por VIH-1 en combinación con otros antirretrovirales.
El modelo TxGNN predice que podría ser efectivo para la **infección por virus de inmunodeficiencia simiana (SIV)**,
con **0 ensayos clínicos relevantes** y **16 publicaciones científicas** que respaldan esta dirección, principalmente en modelos animales con virus quimérico RT-SHIV. Sin embargo, esta predicción refleja un uso como herramienta de investigación preclínica, no una oportunidad de reposicionamiento clínico para pacientes humanos.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Infección por VIH-1 (inferida del contexto bibliográfico; sin registro formal en Colombia) |
| Nueva Indicación Predicha | Infección por virus de inmunodeficiencia simiana (SIV) |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Efavirenz actúa como inhibidor no nucleósido de la transcriptasa inversa (INNTI), uniéndose a un sitio alostérico de la enzima RT del VIH-1 e interrumpiendo la replicación viral. Esta especificidad hacia la RT del VIH-1 es el núcleo de su mecanismo de acción.

La conexión con el SIV no es directa: la transcriptasa inversa natural del SIV presenta diferencias estructurales significativas respecto a la del VIH-1 y no es susceptible a los INNTI. No obstante, el virus quimérico RT-SHIV (simian-human immunodeficiency virus) —que porta la región RT del VIH-1 insertada en un esqueleto de SIV— sí es susceptible a EFV. La totalidad de la literatura disponible describe el uso de EFV en macacos infectados con RT-SHIV para estudiar cinética viral, reservorios tisulares y emergencia de resistencia antirretroviral.

En consecuencia, la predicción de TxGNN captura una relación mecanística real entre EFV y la RT del VIH-1 expresada en estos modelos animales. Sin embargo, desde la perspectiva del reposicionamiento farmacológico, esta "nueva indicación" no constituye una oportunidad terapéutica clínica para humanos: es una aplicación establecida de EFV como componente de HAART en modelos de primates no humanos (herramienta de investigación biomédica básica).

---

## Evidencia de Ensayos Clínicos

El único ensayo recuperado (**NCT00863668**) fue retirado antes de iniciar (inscripción = 0), investiga el inhibidor de integrasa Raltegravir —no EFV— y no guarda relación con la infección por SIV. Se clasifica como error de asociación en base de datos (relevancia grado C) y se excluye del análisis.

**Actualmente no hay ensayos clínicos relevantes registrados para EFV en infección por SIV.**

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Estudio animal (modelo RT-SHIV primate) | Antimicrobial Agents Chemother | EFV demostró actividad antiviral significativa en macacos rhesus infectados con RT-SHIV; primera evaluación in vivo de INNTI en modelo quimérico SIV/HIV-1 RT |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Estudio animal | J Virology | EFV + lamivudina + tenofovir (HAART) suprimió carga viral plasmática en todos los macacos RT-SHIV evaluados; modelo primate para estudio de SIDA |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Estudio animal | PloS One | Caracterización de la cinética de decaimiento viral bifásico en macacos rhesus con RT-SHIV bajo HAART que incluye EFV; modelo para estudios de erradicación de VIH |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Virología molecular | J Virology | La diversidad genética del SIV/RT de HIV-1 persiste en macacos a pesar de monoterapia con EFV previa a ART combinada |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Investigación traslacional | J Virology | PCR alelo-específico ultrasensible detectó variantes resistentes a EFV preexistentes a baja frecuencia en modelo RT-SHIV |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Estudio animal | Retrovirology | Dinámica de subpoblaciones RT-SHIV en macacos tratados con EFV en monoterapia corta seguida de ART combinada continua |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Estudio animal | Antimicrobial Agents Chemother | HAART intensificada (4-5 fármacos incluyendo EFV) en macacos RT-SHIV: mayor supresión y cinética de decaimiento viral mejorada |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Imagen / traslacional | Antimicrobial Agents Chemother | Espectrometría de masas por imagen de 6 ARVs incluyendo EFV en bazo de primates no humanos con RT-SHIV; relación espacial con expresión viral y fibrosis |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antiviral Therapy | EFV inactivo contra SIV silvestre (mac251, B670) y HIV-2; activo exclusivamente contra cepas SHIV que portan RT de HIV-1 |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro | J Virology | Caracterización in vitro de RT-SHIV en macacos cola de cerdo para estudiar resistencia a NNRTIs incluyendo EFV; base para modelos in vivo |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha (infección por SIV) no representa una oportunidad de reposicionamiento clínico: refleja el uso bien establecido de EFV como componente de HAART en modelos de investigación con primates no humanos infectados con el virus quimérico RT-SHIV, cuya relevancia se limita al ámbito de la investigación biomédica básica sobre VIH. Adicionalmente, EFV no tiene registro sanitario en Colombia y no se dispone de datos de seguridad locales.

**Para avanzar se necesita:**
- Redefinir el objetivo: si el interés es reposicionamiento clínico humano, explorar indicaciones con mayor potencial traslacional (p. ej., actividad antitumoral reportada en algunos estudios, efectos neurológicos conocidos de EFV)
- Obtener datos de MOA completos desde DrugBank (DG002) para análisis mecanístico estructurado
- Consultar el prospecto del INVIMA o EMA/FDA para recuperar advertencias y contraindicaciones formales (DG001)
- Evaluar viabilidad de registro sanitario en Colombia si se identificara una indicación con evidencia L2 o superior
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

