---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levonorgestrel: De Anticoncepción a Acné

## Resumen en Una Frase

Levonorgestrel es un progestágeno sintético de alta potencia, ampliamente utilizado como anticonceptivo hormonal en formulaciones orales combinadas, dispositivos intrauterinos (DIU) e implantes subdérmicos.
El modelo TxGNN predice que podría ser efectivo para **Acné (enfermedad)**, con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
La relación es biológicamente plausible pero de direccionalidad dual: el efecto sobre el acné depende críticamente de la formulación y la vía de administración.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoncepción hormonal (progestágeno en DIU, implante y anticonceptivos orales combinados) |
| Nueva Indicación Predicha | Acné (enfermedad) |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No registrado en INVIMA |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según información farmacológica bien establecida, levonorgestrel es un progestágeno derivado de la 19-nortestosterona con actividad androgénica intrínseca relativamente alta en comparación con progestinas de nueva generación como desogestrel, norgestimato o drospirenona. Esta actividad androgénica es la clave para entender su relación con el acné.

El acné es una enfermedad multifactorial en la que los andrógenos estimulan la producción de sebo en la glándula pilosebácea, creando el entorno propicio para la proliferación de *Cutibacterium acnes*. En formulaciones orales combinadas de baja dosis (levonorgestrel + etinilestradiol), el componente estrogénico eleva la globulina transportadora de hormonas sexuales (SHBG), reduciendo la testosterona libre biodisponible; el efecto neto puede mejorar el acné androgénico a pesar de la actividad androgénica intrínseca del progestágeno. Estudios clínicos directos confirman que la combinación EE 20 µg / LNG 100 µg mejora marcadores bioquímicos de androgenicidad y lesiones acneicas (PMID 12196750).

Sin embargo, la relación es estrictamente dependiente de la formulación y la vía de administración. Las formulaciones de solo progestágeno (DIU LNG, implante subdérmico) o dosis altas pueden exacerbar el acné por efecto androgénico directo con exposición sistémica baja en estrógenos. Comparado con progestinas antiandrogénicas como drospirenona o acetato de clormadinona, el levonorgestrel no es el progestágeno de elección para acné, pero los datos clínicos muestran eficacia real de las combinaciones EE/LNG de baja dosis en este contexto.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Fase 2 | Completado | 100 | Ensayo aleatorizado doble ciego controlado con placebo evaluando implante subdérmico de gestrinone para dolor pélvico; metodología más rigurosa del conjunto de datos (RCT multicéntrico) |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completado | 101,498 | Cohorte prospectiva controlada comparando NOMAC-E2 vs ACO con LNG en más de 100,000 usuarias; provee la base epidemiológica de referencia sobre efectos cutáneos de progestinas en anticonceptivos combinados |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completado | 131 | Anticonceptivos orales continuos combinados con doxiciclina (antibiótico de primera línea para acné); el diseño indica evaluación de manejo del acné en usuarias de ACO con LNG, con datos de seguridad en ese contexto |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminado | 44 | LNG-IUS para prevención de cáncer endometrial; documenta acné como efecto adverso de progestinas orales sistémicas frente a LNG intrauterino local; terminado anticipadamente con muestra pequeña |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Fase 2 | Desconocido | 60 | Tratamiento conservador de hiperplasia endometrial atípica con Mirena (LNG-IUS) vs megestrol en mujeres que desean fertilidad; estado desconocido limita su utilidad |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | ECA | J Am Acad Dermatology | ACO de baja dosis (EE 20 µg + LNG 100 µg) mejoró marcadores bioquímicos de androgenicidad en acné moderado; evidencia directa más relevante de este conjunto para la indicación predicha |
| [10717776](https://pubmed.ncbi.nlm.nih.gov/10717776/) | 1999 | ECA | Contraception | Estudio multicéntrico aleatorizado abierto comparando EE 20 µg + LNG vs EE 20 µg + otra progestina; evaluación de perfiles androgénicos bioquímicos y resultados clínicos incluyendo acné |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Revisión | Drugs | EE/acetato de clormadinona demostró eficacia significativamente superior a EE/LNG 0.03/0.15 mg en acné papulopustular leve a moderado; posiciona a LNG como comparador activo pero inferior en indicación dermatológica |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Revisión | J Women's Health | Drospirenona vs medroxiprogesterona acetato, LNG y progesterona micronizada; LNG carece de propiedades antiandrogénicas y antimineralocorticoides que reducirían acné vulgaris e hirsutismo |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Revisión | Am J Clin Dermatol | Trastornos de la unidad pilosebácea (acné, hirsutismo, seborrea, alopecia femenina de patrón); revisa ACO antiandrogénicos frente a progestinas androgénicas como LNG; contexto clínico dermatológico completo |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Revisión Mecanística | Am J Medicine | Base estructural de la androgenicidad de progestinas; LNG (serie 19-nortestosterona/androstano) tiene actividad androgénica intrínseca significativa; fundamento mecanístico para los efectos cutáneos |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Estudio Clínico Controlado | Human Reproduction | LNG-IUS mejora síntomas de endometriosis con efectos sistémicos mínimos comparado con progestágenos orales; relevante para comparar exposición cutánea según vía de administración |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Revisión | Semin Reprod Med | LNG-IUS: acción antiproliferativa endometrial local con niveles séricos de LNG bajos; provee contexto farmacocinético para diferenciar efectos cutáneos entre formulaciones sistémicas y locales |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Revisión Sistemática Cochrane | Cochrane Database Syst Rev | LNG-IUS para hiperplasia endometrial; revisión sistemática de alta calidad sobre eficacia de LNG intrauterino; referencia para diferenciar perfiles de eficacia según vía |
| [11091988](https://pubmed.ncbi.nlm.nih.gov/11091988/) | 2000 | Revisión | Obstet Gynecol Clin North Am | Implantes anticonceptivos con levonorgestrel (Norplant); mecanismos de acción incluyendo inhibición de ovulación y efectos sistémicos; base para entender exposición androgénica crónica en implantes |

---

## Información de Mercado en Colombia

Levonorgestrel no cuenta con registros sanitarios vigentes ante el INVIMA. La consulta a la base de datos regulatoria no arrojó ninguna licencia activa para este principio activo en Colombia, lo que representa una barrera regulatoria primaria antes de cualquier desarrollo de indicación adicional en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe evidencia clínica directa de calidad moderada-alta (incluyendo un ECA publicado en JAAD, PMID 12196750, y datos comparativos en más de 100,000 usuarias) que demuestra que la combinación de baja dosis EE/LNG mejora el acné androgénico mediante reducción de testosterona libre; sin embargo, la eficacia es formulation-dependent y el fármaco no está registrado en Colombia, lo que condiciona todo el desarrollo posterior.

**Para avanzar se necesita:**
- **Registro sanitario ante INVIMA**: ausencia total de licencias en Colombia; se requiere análisis de viabilidad regulatoria completo como paso previo obligatorio
- **Especificación de la formulación objetivo**: solo la combinación oral EE/LNG de baja dosis tiene evidencia directa en acné; las formulaciones de solo progestágeno (DIU, implante) tienen perfil de riesgo opuesto para piel
- **Datos de mecanismo de acción (MOA) completos**: cuantificar la actividad androgénica relativa vs efecto de SHBG según dosis y formulación específica
- **Información de seguridad completa**: advertencias, contraindicaciones y perfil de interacciones farmacológicas conforme a normativa colombiana
- **Análisis comparativo vs progestinas antiandrogénicas**: definir ventaja diferencial de LNG frente a drospirenona o norgestimato para acné, dada la evidencia de inferioridad relativa ya documentada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

