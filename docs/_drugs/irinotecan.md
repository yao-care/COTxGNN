---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 1
---

# Irinotecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# IRINOTECAN: De Cáncer Colorrectal a Carcinoma de Mama Femenino

## Resumen en Una Frase

Irinotecan es un agente quimioterapéutico de la clase camptotecina, ampliamente utilizado a nivel mundial para el tratamiento del cáncer colorrectal avanzado como parte de regímenes FOLFIRI y en combinación con terapias biológicas.
El modelo TxGNN predice que podría ser efectivo para el **Carcinoma de Mama Femenino**,
con **22 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Cáncer colorrectal avanzado |
| Nueva Indicación Predicha | Carcinoma de Mama Femenino |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Irinotecan es un profármaco que, una vez en el organismo, es convertido por las carboxilesterasas CES1/CES2 en su metabolito activo **SN-38**. SN-38 actúa estabilizando el complejo de corte ADN-Topoisomerasa I (*cleavable complex*), lo que genera roturas de doble cadena (DSB) al colisionar con la horquilla de replicación durante la fase S del ciclo celular, induciendo apoptosis en células de proliferación activa.

Las células del cáncer de mama —en especial el subtipo triple negativo (TNBC) y el HR+/HER2−— dependen intensamente de la Topoisomerasa I para sostener su rápida proliferación, lo que las hace biológicamente susceptibles al mecanismo de SN-38. Adicionalmente, la alta expresión de la proteína Trop-2 en la superficie tumoral del cáncer de mama ha permitido el desarrollo de conjugados anticuerpo-fármaco (ADC) que utilizan SN-38 como carga citotóxica, como el sacituzumab govitecan. Esta vía mecanística ya fue validada con la aprobación de la FDA para dos indicaciones de cáncer de mama: TNBC y HR+/HER2− metastásico.

Más allá de los ADC, el irinotecan libre cuenta con evidencia clínica directa de Fase 2 en cáncer de mama metastásico refractario (NCT00072852, n=134, completado), lo que respalda tanto la plausibilidad biológica como la viabilidad clínica de esta predicción del modelo TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Fase 2 | Completado | 134 | Irinotecan en dos esquemas de dosificación como agente único en mujeres con cáncer de mama metastásico refractario a antraciclinas, taxanos y capecitabina; evidencia directa del fármaco en esta indicación |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Fase 1/2 | Completado | 515 | Sacituzumab govitecan (ADC anti-Trop-2 con carga SN-38) en cáncer epitelial avanzado incluyendo mama; valida directamente la eficacia y seguridad del metabolito activo de irinotecan en cáncer de mama |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Fase 2 | Desconocido | 124 | Irinotecan en cáncer de mama avanzado/metastásico en tercera línea o posterior, en pacientes chinas refractarias a antraciclinas y taxanos; evalúa eficacia y seguridad |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Fase 1 | Completado | 41 | UCN-01 (inhibidor de Chk1) + irinotecan en tumores sólidos refractarios; desde 2007 reclutó exclusivamente cáncer de mama triple negativo |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Fase 1 | Completado | 12 | Irinotecan seguido de capecitabina en carcinoma de mama avanzado; establece dosis óptima y perfil de seguridad de la combinación secuencial |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Fase 2 | Desconocido | 180 | Navicixizumab en monoterapia o combinado con irinotecan en tumores sólidos avanzados; incluye cohorte específica C para TNBC |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Fase 1 | Completado | 45 | MM-398 (irinotecan nanoliposomal, Nal-IRI) para determinar biodistribución tumoral del fármaco y factibilidad de imagen como biomarcador predictivo |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Fase 1 | Completado | 21 | SNB-101 (formulación nanoparticular de SN-38, metabolito activo de irinotecan) en tumores sólidos avanzados; escalada de dosis con diseño ATD |
| [NCT04579224](https://clinicaltrials.gov/study/NCT04579224) | Fase 3 | Activo sin reclutamiento | 184 | Eribulin + gemcitabina vs. tratamiento estándar del médico (que puede incluir regímenes con irinotecan) en carcinoma urotelial metastásico; evidencia indirecta sobre rol de irinotecan como estándar |
| [NCT06769425](https://clinicaltrials.gov/study/NCT06769425) | Fase 1 | En reclutamiento | 157 | HS-10502 (inhibidor selectivo de PARP1) en combinación con agentes quimioterapéuticos en tumores sólidos avanzados; en evaluación |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | ECA Fase 3 | Journal of Clinical Oncology | TROPiCS-02: sacituzumab govitecan (payload SN-38) mejora significativamente la supervivencia libre de progresión vs. quimioterapia estándar en HR+/HER2− MBC endocrina-resistente |
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | ECA Fase 1/2 | New England Journal of Medicine | IMMU-132-01: sacituzumab govitecan en TNBC metastásico refractario; tasa de respuesta objetiva 33.3%, mediana de supervivencia libre de progresión 5.5 meses |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | ECA Fase 1/2 | Journal of Clinical Oncology | Sacituzumab govitecan en TNBC metastásico muy pretratado (mediana 7 líneas previas); ORR 30% y duración de respuesta 7.7 meses |
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Diseño Fase 3 | Future Oncology | Protocolo del estudio TROPiCS-02: fundamento del ADC anti-Trop-2/SN-38 en HR+/HER2− MBC y diseño del ensayo confirmatorio |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Fase 1 | Clinical Cancer Research | Primer ensayo en humanos de sacituzumab govitecan; actividad clínica documentada en cáncer de mama y múltiples tumores sólidos metastásicos |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | Revisión clínica | Cancer | Farmacocinética y seguridad de sacituzumab govitecan a 8-10 mg/kg en cánceres epiteliales avanzados; caracterización de SN-38 libre circulante |
| [26101915](https://pubmed.ncbi.nlm.nih.gov/26101915/) | 2015 | Traslacional | Oncotarget | Trop-2 como blanco terapéutico novel para ADCs; la alta razón fármaco:anticuerpo (DAR 7.6:1) de IMMU-132 no compromete la unión y maximiza la entrega de SN-38 |
| [32727805](https://pubmed.ncbi.nlm.nih.gov/32727805/) | 2020 | Estudio piloto | Anticancer Research | Régimen IRIS (irinotecan + S-1) en cáncer de mama avanzado/metastásico; evalúa eficacia y seguridad de irinotecan en combinación oral |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Revisión | Oncology | Fundamento del uso de mitomicina + irinotecan en cáncer de mama; sinergismo por upregulación de Topo I inducida por mitomicina, diana de SN-38 |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Revisión | Oncology | Actividad antitumoral amplia de irinotecan documentada en fases II/III incluyendo mama, linfoma, leucemia y cánceres ginecológicos; base del desarrollo del fármaco |

---

## Citotoxicidad

| Ítem | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (inhibidor de Topoisomerasa I, clase camptotecina; profármaco activado a SN-38) |
| Riesgo de Mielosupresión | Alto — la neutropenia grave (Grado 3-4) es la toxicidad hematológica limitante de dosis; puede requerir G-CSF profiláctico |
| Clasificación de Emetogenicidad | Moderada a alta (requiere profilaxis antiemética según esquema de dosificación y protocolo institucional) |
| Ítems de Monitoreo | Hemograma completo con diferencial (antes de cada ciclo); función hepática (ALT, AST, bilirrubinas); función renal (creatinina, depuración); electrolitos ante diarrea grave |
| Protección en Manejo | Debe seguir regulaciones de manejo de fármacos citotóxicos; precaución especial por síndrome colinérgico agudo (diarrea temprana, sudoración, cólicos) y diarrea tardía grave —ambas toxicidades características de irinotecan |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 2 completado que evalúa directamente irinotecan en cáncer de mama metastásico refractario (NCT00072852, n=134), junto con un segundo estudio de Fase 2 en población asiática (NCT03562390, n=124) y evidencia de alta calidad de Fase 3 que valida el metabolito activo SN-38 mediante sacituzumab govitecan en dos subtipos de cáncer de mama. La convergencia de evidencia clínica directa e indirecta justifica avanzar con precaución y un plan de monitoreo reforzado.

**Para avanzar se necesita:**
- Confirmar disponibilidad y registro de irinotecan ante INVIMA en Colombia
- Obtener datos formales de mecanismo de acción (MOA) de DrugBank para completar el análisis de red de reposicionamiento
- Acceder al prospecto oficial para caracterización completa de advertencias, contraindicaciones e interacciones farmacológicas
- Definir población objetivo en cáncer de mama (TNBC vs. HR+/HER2− vs. línea de tratamiento específica) antes de diseñar protocolo clínico
- Establecer plan de manejo de toxicidades específicas de irinotecan: neutropenia severa, diarrea tardía (Grado 3-4) y síndrome colinérgico agudo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

