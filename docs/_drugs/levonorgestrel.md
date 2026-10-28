---
layout: default
title: Levonorgestrel
parent: Evidencia Moderada (L3-L4)
nav_order: 401
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Levonorgestrel: nueva indicación predicha, Acné (nivel de evidencia L4). Indicación original: Levonorgestrel"
monitor_inn: "LEVONORGESTREL"
predicted_indications: ["acne (disease)", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "blunt duct adenosis of breast", "apocrine adenosis of breast"]
---

# Levonorgestrel
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

## Levonorgestrel: De Levonorgestrel (anticoncepción hormonal) a Acné
{: .text-alpha }

## Resumen en Una Frase

Levonorgestrel es un progestágeno sintético utilizado originalmente como anticonceptivo (sistema intrauterino y tableta de 0,75 mg), según los registros sanitarios colombianos.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero no hay ensayos clínicos registrados y la literatura disponible es indirecta: no demuestra un beneficio del levonorgestrel solo en el acné.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levonorgestrel (el registro no detalla la indicación; los productos son un sistema intrauterino y una tableta anticonceptiva) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el levonorgestrel es un progestágeno derivado de la 19-nortestosterona: inhibe la ovulación, modifica el moco cervical y el endometrio, y en el sistema intrauterino ejerce una fuerte acción antiproliferativa local sobre el endometrio.

La relación con el acné es débil y, en parte, contraria a lo esperado. El levonorgestrel conserva cierta actividad androgénica residual, lo cual es opuesto a lo que se busca en el acné. El beneficio dermatológico de los anticonceptivos combinados suele atribuirse al componente estrogénico y a progestágenos antiandrogénicos (por ejemplo, acetato de clormadinona). Los productos con levonorgestrel solo (sistema intrauterino, implante, píldora de progestágeno solo) no son tratamientos establecidos para el acné, y algunas publicaciones sugieren que podrían empeorarlo.

El puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento con los anticonceptivos hormonales, y no un efecto terapéutico directo. Por eso la predicción debe considerarse una pregunta de investigación y no una hipótesis respaldada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se recuperaron 20 publicaciones; la mayoría son revisiones generales sobre anticoncepción hormonal. Las más relevantes para el acné son:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | ECA (ensayo aleatorizado controlado con placebo) | J Am Acad Dermatol | Evalúa un anticonceptivo oral combinado de dosis baja (20 µg de etinilestradiol + 100 µg de levonorgestrel) en acné moderado; el efecto corresponde a la combinación con estrógeno, no al levonorgestrel solo |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Revisión | Drugs | Etinilestradiol/acetato de clormadinona fue significativamente más eficaz que etinilestradiol/levonorgestrel en acné papulopustular leve a moderado |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Revisión | Am J Clin Dermatol | Beneficios dermatológicos de etinilestradiol/clormadinona en acné, hirsutismo y seborrea por hiperandrogenismo |
| [30088446](https://pubmed.ncbi.nlm.nih.gov/30088446/) | 2018 | Revisión | Curr Drug Targets | Interacciones moleculares de distintos esteroides en la producción de sebo |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Revisión | Am J Med | Describe la androgenicidad de los progestágenos, incluidos los derivados de 19-carbonos usados en anticonceptivos |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Revisión | Semin Reprod Med | Sistemas intrauterinos liberadores de progestágeno: anticoncepción y reducción del sangrado menstrual |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Sistema intrauterino de levonorgestrel en hiperplasia endometrial (no relacionado con acné) |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Estudio clínico | Hum Reprod | Levonorgestrel intrauterino en endometriosis (no relacionado con acné) |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|-----|
| 20046501 | JAYDESS® | Implantes y sistemas intrauterinos e intraoculares | Levonorgestrel | Vigente |
| 20080147 | POSTCOID® 0.75 MG | Tableta | Levonorgestrel | Vigente |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): hipertensión, epilepsia, trastornos de ansiedad y neuróticos, distimia, porfirias, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, hipotiroidismo, lupus eritematoso sistémico, asma, trastornos de la coagulación sanguínea, hipertrigliceridemia, e hipercalcemia y trastornos del metabolismo del fósforo.
- **Interacciones farmacológicas**: se identificaron 100 interacciones, todas las mostradas de nivel moderado. Las principales corresponden a antidiabéticos (acarbosa, canagliflozina, dapagliflozina, ertugliflozina, exenatida, linagliptina, liraglutida, nateglinida y diversas insulinas), además de aprepitant, clotrimazol, fenilbutirato de glicerol y linaclotida.
- Los datos de advertencias y contraindicaciones del prospecto de INVIMA no están disponibles; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en literatura indirecta; no hay ensayos clínicos, y el perfil androgénico del levonorgestrel va en contra de un beneficio en acné. Además, no existen registros sanitarios vigentes en Colombia. Las otras cinco indicaciones predichas (síndrome de Worth, osteoporosis asociada al embarazo, vitreorretinopatía inflamatoria neovascular, adenosis de mama de conducto romo y adenosis apocrina de mama) tampoco tienen evidencia (nivel L5) ni un vínculo mecanístico plausible.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto de INVIMA.
- Revisión de la evidencia comparativa que muestre si el levonorgestrel solo mejora, no cambia o empeora el acné.
- Ensayos clínicos específicos, si se decide continuar, con atención a las contraindicaciones señaladas.
- Aclarar la situación regulatoria, dado que ambos registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

