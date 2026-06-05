---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: De Infección por VIH-1 a Infección por Virus de Inmunodeficiencia Simiana

## Resumen en Una Frase

Ritonavir es un inhibidor de la proteasa del VIH-1, originalmente utilizado como componente clave de los esquemas de terapia antirretroviral de alta eficacia (HAART) para el tratamiento de la infección por VIH en humanos.
El modelo TxGNN predice que podría ser efectivo para la **Infección por Virus de Inmunodeficiencia Simiana (SIV)**,
con **0 ensayos clínicos registrados** pero **12 publicaciones científicas** que respaldan esta dirección, principalmente estudios en primates no humanos y ensayos in vitro que documentan actividad antiretroviral directa contra SIV.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Infección por VIH-1 (terapia antirretroviral) |
| Nueva Indicación Predicha | Infección por Virus de Inmunodeficiencia Simiana (SIV) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos. Sin embargo, según la información científica conocida, ritonavir actúa como inhibidor competitivo de la proteasa aspártica del VIH-1, enzima imprescindible para el procesamiento postraducional de las poliproteínas virales y la maduración de nuevas partículas infecciosas. Adicionalmente, es ampliamente empleado como potenciador farmacocinético (*booster*) gracias a su fuerte inhibición del CYP3A4, lo que eleva los niveles plasmáticos de otros antirretrovirales coadministrados.

El VIH y el SIV pertenecen ambos al género *Lentivirus* dentro de la familia *Retroviridae*, y sus proteasas comparten una estructura tridimensional y un sitio catalítico altamente conservados evolutivamente. Esta homología estructural constituye la base mecanística central de la predicción: si ritonavir inhibe eficazmente la proteasa del VIH-1, es esperable que también inhiba la proteasa del SIV. Los estudios in vitro han validado esta hipótesis de forma directa, demostrando que la IC₅₀ de ritonavir frente a SIVmac239 (13 ± 5 nM) es comparable a la obtenida para VIH-1 (25 ± 14 nM) (PMID 12709355).

En modelos animales con primates no humanos infectados por SIV, los esquemas HAART que incluyen ritonavir como booster de lopinavir han demostrado supresión virológica sostenida y reducción del reservorio viral (PMID 16973590, PMID 22737073, PMID 12951220). Es importante señalar, no obstante, que SIV es una enfermedad propia de primates no humanos y no representa una indicación clínica directa en pacientes humanos; su valor principal radica en su utilidad como modelo preclínico para el estudio de estrategias terapéuticas contra el VIH.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ritonavir en la indicación de infección por virus de inmunodeficiencia simiana (SIV).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudio NHP | Journal of Virology | Cuatro macacos cynomolgus con SIVmac251 recibieron terapia cuádruple antirretroviral por 7 días; se modeló la cinética de decaimiento viral y se compararon las dinámicas entre SIV y VIH-1 |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Estudio NHP longitudinal | mBio | Las infecciones lentivirales persisten en el cerebro pese a ART efectiva; evaluación en modelos NHP de SIV/SHIV y personas con VIH, con análisis del reservorio en corteza cerebral |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Ensayo NHP | PLoS ONE | Macacos rhesus con SIV tratados con cART combinada con el inhibidor HDAC suberonilida hidroxámico (SAHA); medición del impacto sobre el reservorio viral residual |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Ensayo NHP | PLoS Pathogens | Esquema ART altamente intensificado en macacos rhesus con SIVmac251 (viremia 10³–10⁷ copias/mL); supresión virológica sostenida y restricción del reservorio a largo plazo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudio NHP inmunológico | Journal of Virological Methods | HAART oral (AZT + 3TC + LPV/RTV) administrada a macacos con SHIV 89.6P durante 28 días; seguimiento de subpoblaciones linfocíticas CD8 en sangre periférica |
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | Estudio in vitro | Antimicrobial Agents and Chemotherapy | IC₅₀ de ritonavir frente a SIVmac239: 13 ± 5 nM vs. VIH-1: 25 ± 14 nM; actividad antiproteasas comparable entre SIV y VIH-1 en ensayo de infectividad focal |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Estudio in vitro comparativo | Antiviral Therapy | 17 antirretrovirales aprobados evaluados frente a VIH-2, SIVmac251, SIV B670 y SHIV; datos orientadores para tratamiento y profilaxis post-exposición con lentivirus no-VIH-1 |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Modelo NHP quimérico | Microbes and Infection | Construcción de virus quimérico SHIV-pr con gen de proteasa de VIH-1 insertado en genoma SIVmac; herramienta in vivo para evaluar inhibidores de proteasa en macacos rhesus |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Estudio mecanístico | Journal of Virology | La proteasa viral de VIH-1 procesa proteolíticamente la proteína Vif tanto in vivo como in vitro; evidencia del rol de la proteasa más allá del procesamiento de Gag/Pol |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | Estudio in vitro | Antiviral Chemistry & Chemotherapy | Actividad antiviral del derivado fluoroquinolónico K-12 frente a VIH-1 (incluidas cepas resistentes a ritonavir), VIH-2 y SIV; ritonavir usado como referencia de sensibilidad |

---

## Información de Mercado en Colombia

Ritonavir **no se encuentra comercializado en Colombia** según los datos regulatorios disponibles. No existen registros sanitarios activos ante el INVIMA para este medicamento.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La actividad de ritonavir frente a SIV está sustentada in vitro y en modelos de primates no humanos, con una base mecanística sólida derivada de la homología estructural de las proteasas lentivirales; sin embargo, SIV es una enfermedad propia de primates no humanos y no constituye una indicación clínica directa para uso en pacientes humanos, lo que limita la aplicabilidad traslacional inmediata de esta predicción.

**Para avanzar se necesita:**
- Definir el contexto de aplicación objetivo: investigación preclínica como modelo NHP para VIH, medicina veterinaria de primates, o fundamento para nuevas estrategias terapéuticas humanas anti-VIH
- Obtener datos completos del mecanismo de acción (MOA) y advertencias de seguridad del prospecto oficial (actualmente con brecha de datos)
- Gestionar registro sanitario ante el INVIMA si se requiere uso clínico o investigativo en Colombia
- Evaluar si existe potencial traslacional hacia una indicación humana derivada (p. ej., optimización de booster farmacocinético en cepas resistentes) que justifique escalar la evidencia a nivel clínico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

