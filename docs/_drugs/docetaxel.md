---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: De Taxano Antineoplásico a Carcinoma de Mama Femenino

## Resumen en Una Frase

Docetaxel (Taxotere) es un agente citotóxico de la clase de los taxanos, ampliamente utilizado en oncología mundial para el tratamiento de tumores sólidos; sin embargo, actualmente **no cuenta con ningún registro sanitario INVIMA en Colombia** (0 licencias activas).
El modelo TxGNN predice que podría ser efectivo para el **Carcinoma de Mama Femenino**, con **más de 30 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta indicación.
Dado que docetaxel ya es estándar global para esta patología pero carece de registro colombiano, esta evaluación constituye un análisis de viabilidad para su introducción formal al mercado nacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin aprobación en Colombia; globalmente indicado para cáncer de mama, pulmón, próstata y gástrico |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Docetaxel es un taxano de segunda generación que ejerce su acción antineoplásica uniéndose con alta afinidad a la subunidad β-tubulina de los microtúbulos, estabilizando el polímero e inhibiendo su despolimerización. Este mecanismo bloquea la progresión de la mitosis en la transición G2/M e induce la apoptosis celular. Si bien los datos formales de mecanismo de acción (MOA) no están disponibles en el sistema actual, la farmacología de docetaxel está extensamente documentada desde su primera revisión clínica en 1995 (PMID 7595719) y es una de las características mejor comprendidas en oncología.

El carcinoma de mama es una de las indicaciones más consolidadas para los taxanos en general y para docetaxel en particular. Las células tumorales mamarias, especialmente los subtipos HER2-positivo y triple negativo (TNBC), exhiben alta sensibilidad a los agentes que interfieren con la dinámica de los microtúbulos. Múltiples ensayos clínicos de Fase 3 —con miles de participantes cada uno— han confirmado el beneficio de docetaxel tanto en el contexto adyuvante (complementando regímenes de antraciclinas) como en el metastásico, constituyendo desde hace décadas uno de los pilares del tratamiento oncológico mamario global.

La predicción de TxGNN con un puntaje del 99.90% (rango 1259) es altamente concordante con la evidencia acumulada: la ausencia de docetaxel del mercado colombiano representa una brecha regulatoria —no una incertidumbre clínica— que limita el acceso de pacientes colombianas a un tratamiento oncológico esencial y de eficacia demostrada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Fase 3 | Completado | 150 | RCT multicéntrico comparando docetaxel semanal vs CMF en mujeres ≥65 años o no candidatas a antraciclinas con cáncer de mama de alto riesgo; evalúa docetaxel como alternativa eficaz en tratamiento adyuvante |
| [NCT00002544](https://clinicaltrials.gov/study/NCT00002544) | Fase 3 | Completado | 300 | RCT: mitoxantrone vs FAC como quimioterapia de primera línea en cáncer de mama metastásico con pronóstico desfavorable; establece marco de referencia para taxanos en este contexto |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Fase 3 | Completado | 2411 | RCT: AC preoperatorio vs AC seguido de docetaxel (pre o postoperatorio) en cáncer de mama operable estadios II-III; gran estudio que define el papel del docetaxel en el entorno neoadyuvante/adyuvante |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Fase 3 | Completado | 3270 | RCT: TC o AC-paclitaxel solos vs combinados con trastuzumab en cáncer de mama invasivo HER2-bajo; el ensayo más amplio que evalúa regímenes basados en docetaxel |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Fase 3 | Completado | 2611 | RCT abierto: AC→docetaxel vs AC→docetaxel+capecitabina en cáncer de mama de alto riesgo; confirma la eficacia del esquema basado en docetaxel y evalúa la adición de capecitabina |
| [NCT04066335](https://clinicaltrials.gov/study/NCT04066335) | N/A | Desconocido | 1498 | Estudio observacional de seguridad de Nanoxel M (docetaxel nanoparticulado); proporciona datos de seguridad en mundo real con gran muestra, relevante para formulaciones alternativas |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Fase 2 | Completado | 101 | RCT: carboplatino+docetaxel vs carboplatino+paclitaxel seguido de AC en cáncer de mama triple negativo estadios I-III; evalúa regímenes con platino en TNBC |
| [NCT00003565](https://clinicaltrials.gov/study/NCT00003565) | Fase 2 | Completado | 109 | Estudio farmacocinético poblacional en pacientes caucásicos y afroamericanos con tumores sólidos (incluye cáncer de mama); documenta diferencias de PK entre grupos étnicos, relevante para dosificación en poblaciones diversas |
| [NCT00379015](https://clinicaltrials.gov/study/NCT00379015) | Fase 2 | Completado | 38 | Neoadyuvante: epirrubicina/ciclofosfamida seguido de docetaxel+trastuzumab en cáncer de mama localmente avanzado HER2+; evalúa combinación de taxano con anticuerpo monoclonal anti-HER2 |
| [NCT03076372](https://clinicaltrials.gov/study/NCT03076372) | Fase 1 | Desconocido | 34 | MM-310 (formulación liposomal de profármaco de docetaxel dirigida al receptor EphA2) en tumores sólidos; evalúa una nueva formulación de docetaxel con mayor selectividad tumoral |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | ECA (Fase 3) | J Clin Oncol | ABC trials: TC×6 vs regímenes TaxAC (TAC, AC-T, AC-TX) como terapia adyuvante; TC no inferior en algunos subgrupos; confirma la eficacia de los esquemas con docetaxel frente a regímenes con antraciclinas |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Revisión narrativa | The Oncologist | Revisión de 10 años de experiencia clínica con paclitaxel y docetaxel en cáncer de mama; documenta beneficios en entorno metastásico, adyuvante y neoadyuvante, con docetaxel mostrando ventajas sobre paclitaxel en varios escenarios |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Revisión | J Clin Oncol | Primera revisión comprensiva del perfil preclínico y clínico de docetaxel (Taxotere); establece las bases de su uso oncológico incluyendo actividad en tumores sólidos |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Fase 2 | Cancer | Capecitabina+docetaxel+epirrubicina (TEX) como primera línea en cáncer de mama localmente avanzado/metastásico; demuestra actividad y manejabilidad de la triple combinación oral-IV |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug Ther Bull | Paclitaxel y docetaxel en cáncer de mama y ovárico; discute la extensión de licencias de docetaxel para cáncer de mama metastásico y los beneficios comparativos frente a paclitaxel |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Fase IIb (ECA) | J Clin Oncol | Doxorrubicina+docetaxel dosis-densa ± tamoxifeno como terapia preoperatoria en cáncer de mama primario operable; demuestra altas tasas de respuesta patológica con el esquema dosis-denso |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Fase 2 (dosis) | Tumori | Docetaxel+gemcitabina semanal en cáncer de mama metastásico resistente a antraciclinas; muestra que la administración semanal permite preservar la calidad de vida con toxicidad manejable |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Fase 2 | Breast Cancer (Tokyo) | Docetaxel+ciclofosfamida+trastuzumab (HER-TC) como neoadyuvante en cáncer de mama HER2+; evalúa régimen libre de antraciclinas con respuesta patológica completa como endpoint primario |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Fase 2 | Oncology | Combinación docetaxel/vinorelbina en cáncer de mama metastásico; establece actividad de ambos agentes como monofármacos con tasas de respuesta documentadas |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohorte retrospectiva | Anti-Cancer Drugs | Asociación entre quimioterapia adyuvante con docetaxel y linfedema relacionado con cáncer de mama; documenta la retención de líquidos como efecto adverso relevante a monitorear |

---

## Información de Mercado en Colombia

Docetaxel **no cuenta con ningún registro sanitario INVIMA activo** en Colombia. La búsqueda en la base de datos regulatoria no arrojó licencias registradas para este principio activo.

> Actualmente no existen registros sanitarios INVIMA para docetaxel en Colombia. Su uso en el territorio nacional, de existir, correspondería a importación bajo modalidades especiales o uso compasivo.

---

## Citotoxicidad

Docetaxel es un agente antineoplásico citotóxico de la familia de los taxanos. Se confirma su inclusión en esta sección por cumplir los criterios: clase taxano/quimioterapia citotóxica, indicación original en cáncer (tumores sólidos), y categoría de quimioterapia citotóxica convencional.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional — clase Taxano (taxoide semisintético); agente estabilizador de microtúbulos |
| Riesgo de Mielosupresión | **Alto** — la neutropenia es la toxicidad limitante de dosis; neutropenia grado 3-4 reportada en 65-85% de pacientes en esquemas cada 3 semanas. Se recomienda considerar profilaxis primaria con G-CSF en regímenes de dosis estándar o alta intensidad |
| Clasificación de Emetogenicidad | **Baja a moderada** (nivel 1 como agente único según clasificación MASCC/ESMO); el riesgo aumenta en combinación con agentes altamente emetogénicos como cisplatino o ciclofosfamida |
| Ítems de Monitoreo | Hemograma completo con diferencial antes de cada ciclo (ANC ≥1500/mm³ para administrar), función hepática (ALT, AST, bilirrubina, fosfatasa alcalina — reducción de dosis si elevadas), función renal, peso corporal y signos de retención de líquidos/edema, evaluación de neuropatía periférica (escala NCI-CTCAE) |
| Protección en Manejo | Requiere manejo obligatorio como fármaco citotóxico: preparación exclusiva en cabina de seguridad biológica clase II, uso de EPP completo (guantes dobles de nitrilo, bata impermeable de manga larga, protección ocular, mascarilla FFP2), transporte en contenedores sellados, gestión de residuos conforme a normativa de medicamentos peligrosos vigente en Colombia (Decreto 4741 de 2005 y resoluciones concordantes) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Docetaxel cuenta con el más alto nivel de evidencia disponible (L1) para su uso en carcinoma de mama femenino, respaldado por múltiples ensayos de Fase 3 completados con más de 2.000 pacientes cada uno, décadas de experiencia clínica global y una posición consolidada como estándar de tratamiento internacional; su ausencia del mercado colombiano (0 registros INVIMA) representa una brecha regulatoria —no una incertidumbre clínica— que justifica actuar con guardianes de calidad y proceso formal de registro.

**Para avanzar se necesita:**
- Obtener y procesar el prospecto oficial (FDA/EMA) para documentar advertencias clave, contraindicaciones, interacciones farmacológicas y guías de ajuste de dosis (datos actualmente marcados como [Data Gap])
- Compilar el dossier regulatorio completo para solicitud de registro INVIMA, incluyendo estudios pivotales de Fase 3, informe de farmacovigilancia y datos de bioequivalencia (si aplica formulación genérica)
- Definir plan de farmacovigilancia activa adaptado a la población colombiana, con foco en neutropenia febril, retención de líquidos y neuropatía periférica
- Evaluar cadena de suministro: requisitos de almacenamiento (temperatura controlada 2-25°C), preparación en unidad de farmacia oncológica certificada y disponibilidad de G-CSF para profilaxis
- Establecer protocolos institucionales de manejo de citotóxicos conforme a normativa colombiana vigente
- Revisar interacciones farmacológicas clínicamente relevantes con CYP3A4 (ketoconazol, eritromicina) antes del uso clínico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

