---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Desogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Desogestrel: De Anticoncepción Oral a Amenorrea

## Resumen en Una Frase

Desogestrel es un progestágeno gonano de tercera generación utilizado como componente activo en anticonceptivos orales combinados (junto con etinilestradiol) y como píldora solo-progestágeno (POP 75 µg) para la prevención del embarazo. El modelo TxGNN predice que podría ser efectivo para la **Amenorrea**, con **2 ensayos clínicos** y **16 publicaciones** que actualmente respaldan esta dirección. Sin embargo, la relación es bidireccional y mecánisticamente compleja: el desogestrel en formulación combinada puede restaurar ciclos en amenorrea hipotalámica funcional, mientras que el desogestrel como POP puede inducir amenorrea en aproximadamente el 50% de las usuarias como efecto secundario.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoncepción oral (progestágeno de tercera generación) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde DrugBank. Según la información conocida, desogestrel es un profármaco que se metaboliza a **etonogestrel** (su forma biológicamente activa), con alta selectividad por el receptor de progesterona y baja actividad androgénica residual. En combinación con etinilestradiol (EE), actúa sobre el eje hipotalámico-hipofisario-gonadal suprimiendo la secreción de LH y FSH, inhibiendo la ovulación y regularizando el ciclo menstrual.

En el contexto de la **amenorrea hipotalámica funcional** (como la amenorrea del atleta o por bajo peso corporal), la terapia hormonal combinada que incluye EE + desogestrel puede restaurar la función menstrual al corregir el déficit estrogénico y normalizar el patrón de sangrado. Estudios en adolescentes (PMID 2956138) muestran que EE + desogestrel reduce los niveles de LH, FSH y andrógenos, restaurando ciclos en pacientes con oligomenorrea e hiperandrogenismo ovárico. El efecto antiandrogénico de desogestrel —mediado por el aumento de SHBG y la reducción de testosterona libre— también contribuye al restablecimiento del eje reproductivo.

No obstante, existe una **paradoja mecanística crítica**: el desogestrel administrado solo (POP 75 µg, como Cerazette) inhibe la ovulación en el ~97% de los ciclos y produce amenorrea en aproximadamente el 50% de las usuarias al suprimir el pico de LH sin aportar soporte estrogénico. El PMID 35261299 (2022) confirma esta alta tasa de amenorrea como desenlace del uso de desogestrel POP frente a drospirenona. Por tanto, la predicción de TxGNN puede estar capturando simultáneamente el potencial terapéutico de la formulación combinada y un efecto secundario bien documentado de la formulación POP, lo que requiere clarificación antes de avanzar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Fase 3 | Completado | 121 | Modulación por grasa corporal de la función reproductiva en atletas jóvenes; evalúa si el estrógeno transdérmico u oral mejora la densidad ósea y la arquitectura ósea en atletas con amenorrea y déficit estrogénico. OCP (con posible componente desogestrel) como una de las intervenciones. |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Fase 4 | Desconocido | 42 | Efectos de anticonceptivo oral combinado y anillo vaginal hormonal sobre parámetros hormonales, inflamatorios y metabólicos en mujeres con SOP durante 59 semanas; la regulación del ciclo menstrual y la amenorrea son desenlaces secundarios relevantes. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Observacional/ECA | Gynecological Endocrinology | Perfil de sangrado en mujeres con factores de riesgo cardiovascular usando drospirenona 4 mg versus desogestrel 75 µg; desogestrel POP asociado a mayor tasa de amenorrea y control de ciclo deficiente |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Revisión Sistemática (Cochrane) | Cochrane Database Syst Rev | 20 µg vs >20 µg EE en COC: evalúa control del ciclo y patrones de sangrado, incluyendo amenorrea, en formulaciones con desogestrel |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Revisión Sistemática (Cochrane) | Cochrane Database Syst Rev | Versión anterior del mismo Cochrane; resultados consistentes sobre control del ciclo menstrual en COC que contienen desogestrel |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Estudio Clínico | J Reproductive Medicine | Densidad mineral ósea en mujeres jóvenes con oligoamenorrea hipotalámica tratadas con anticonceptivos orales (incluyendo formulaciones con desogestrel); evalúa dosis de EE y pérdida ósea por amenorrea |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Estudio Clínico | Georgian Medical News | Tratamiento de trastornos menstruales de origen central (oligomenorrea y amenorrea) en 159 mujeres infértiles; la terapia hormonal muestra eficacia en restaurar ciclos frente al tratamiento estándar |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Estudio Clínico | Am J Obstet Gynecol | Perfil de tolerabilidad de desogestrel/EE; documenta beneficios no anticonceptivos como reducción de dismenorrea, endometriosis y regularización del ciclo menstrual |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Estudio Clínico | Br J Obstet Gynaecol | Comparación de dos formulaciones OCP con 150 µg desogestrel y 20 vs 30 µg EE (Mercilon vs Marvelon); evalúa control del ciclo incluyendo tasas de amenorrea como efecto secundario |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Estudio Farmacodinámico | Acta Obstet Gynecol Scand Suppl | Estudios farmacodinámicos de desogestrel solo y combinado con EE; evalúa androgenicidad comparada y efectos en SOP con amenorrea, estableciendo el perfil antiandrogénico de desogestrel |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Revisión | Obstet Gynecol Survey | Nueva era de la anticoncepción oral con desogestrel, norgestimate y gestodene: mecanismo de baja androgenicidad, efectos sobre el ciclo menstrual y relevancia para condiciones como amenorrea por hiperandrogenismo |
| [2956054](https://pubmed.ncbi.nlm.nih.gov/2956054/) | 1987 | Estudio Clínico | Contraception | Postergación del sangrado de privación en usuarias de COC (incluyendo desogestrel monofásico); relevante para comprender el manejo del patrón de sangrado y la inducción de amenorrea |

---

## Información de Mercado en Colombia

Actualmente no hay registros sanitarios de desogestrel en Colombia (INVIMA: 0 registros).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La relación entre desogestrel y amenorrea es mecánisticamente ambigua y bidireccional: como componente de anticonceptivo oral combinado (COC con EE) puede restaurar ciclos en amenorrea hipotalámica funcional, pero como POP 75 µg puede inducir amenorrea en el 50% de las usuarias como efecto secundario documentado. La evidencia disponible (nivel L3) corresponde principalmente a estudios observacionales y revisiones sobre el uso de desogestrel en anticoncepción, sin ensayos diseñados específicamente para tratar la amenorrea como indicación primaria. Adicionalmente, desogestrel no tiene registro en Colombia, lo que representa una barrera regulatoria de entrada.

**Para avanzar se necesita:**
- Clarificar la pregunta clínica: ¿se busca tratar amenorrea hipotalámica funcional con COC que incluya desogestrel, o gestionar la amenorrea inducida por POP como efecto secundario?
- Obtener datos completos del mecanismo de acción (MOA) desde DrugBank para respaldar la plausibilidad biológica
- Diseñar un estudio clínico prospectivo enfocado en amenorrea hipotalámica con formulación COC de desogestrel + EE
- Gestionar el registro sanitario en Colombia ante INVIMA antes de cualquier uso clínico
- Revisar las advertencias, contraindicaciones e interacciones farmacológicas completas mediante consulta al prospecto oficial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

