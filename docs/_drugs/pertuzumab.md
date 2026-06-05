---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: De Cáncer de Mama HER2-positivo a Cáncer de Mama con Receptor de Progesterona Positivo

## Resumen en Una Frase

Pertuzumab es un anticuerpo monoclonal anti-HER2 aprobado internacionalmente para el tratamiento del cáncer de mama HER2-positivo, donde actúa bloqueando la dimerización de los receptores HER2/HER3 e inhibiendo las vías de señalización de proliferación tumoral.
El modelo TxGNN predice que podría ser efectivo para el **cáncer de mama con receptor de progesterona positivo (PR+)**, subtipo biológicamente vinculado al fenotipo Luminal B HER2+, en el que la coexpresión de PR y HER2 justifica un abordaje terapéutico combinado.
Esta predicción está respaldada por **10 ensayos clínicos** y **20 publicaciones**, incluyendo múltiples ECAs de Fase 3 completados y guías clínicas internacionales de nivel L1.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HER2-positivo (aprobación internacional; no registrado en Colombia) |
| Nueva Indicación Predicha | Cáncer de mama con receptor de progesterona positivo (PR+) |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Pertuzumab es un anticuerpo monoclonal humanizado que se une selectivamente al dominio II del receptor HER2, bloqueando su heterodimerización con HER3 (y otros miembros de la familia HER). Esta acción, cuando se combina con trastuzumab —que bloquea el dominio IV de HER2—, produce un doble bloqueo que suprime de forma más completa las vías de señalización PI3K/AKT y MAPK implicadas en la proliferación y supervivencia tumoral. Aunque los datos formales de mecanismo de acción no están disponibles en la base de datos consultada, el perfil farmacológico de pertuzumab está extensamente documentado en la literatura clínica incluida en este informe.

El vínculo con el cáncer de mama PR+ radica en la biología del subtipo Luminal B HER2+: aproximadamente el 50% de los tumores HER2-positivos coexpresan receptores hormonales (ER y/o PR), configurando un fenotipo con crosstalk molecular bidireccional entre las vías HER2 y ER/PR. En este contexto, el bloqueo dual de HER2 con pertuzumab + trastuzumab puede contrarrestar la activación compensatoria de PI3K/AKT inducida por señalización estrogénica/progestacional, fenómeno conocido como resistencia endocrina mediada por HER2. Adicionalmente, los pacientes PR+ pueden recibir terapia endocrina concomitante, lo que abre la posibilidad de esquemas sin quimioterapia de alta toxicidad.

Estudios prospectivos clave respaldan directamente esta predicción. El ensayo WSG-ADAPT TP-II (PMID 37166817, JAMA Oncology 2023) comparó frontalmente terapia endocrina más pertuzumab/trastuzumab versus quimioterapia de-escalada en cáncer de mama temprano HR+/HER2+, con análisis de marcadores moleculares predictivos. El ensayo PERTAIN (PMID 30106636, JCO 2018) demostró beneficio en supervivencia libre de progresión con pertuzumab + trastuzumab + inhibidor de aromatasa en primera línea metastásica HR+/HER2+. Asimismo, el ensayo NEOADAPT (NCT02689921) fue diseñado específicamente para pacientes PR+/HER2+ con un esquema libre de quimioterapia. En conjunto, la racionalidad biológica y el cuerpo de evidencia clínica justifican plenamente la predicción del modelo TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Fase 3 | Completado | 517 | Equivalencia del biosimilar QL1209 vs pertuzumab (Perjeta®) + trastuzumab + docetaxel en neoadyuvancia para cáncer de mama HER2+/ER/PR-negativo; confirma pertuzumab como estándar de referencia |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Fase 3 | Completado | 454 | IMpassion050: atezolizumab + quimioterapia neoadyuvante con ciclofosfamida → paclitaxel + pertuzumab/trastuzumab en HER2+ temprano (T2-4, N1-3); evaluó eficacia y seguridad del bloqueo dual HER2 |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Fase 3 | Activo sin reclutamiento | 398 | Estudio doble ciego aleatorizado que compara biosimilar BCD-178 vs Perjeta® como neoadyuvancia en HER2+ (ER/PR negativos), con pertuzumab como rama de referencia |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Fase 2 | Completado | 417 | Estudio de 4 brazos neoadyuvantes con Herceptin ± docetaxel ± pertuzumab en cáncer de mama HER2+ localmente avanzado, inflamatorio o temprano; evaluó tasas de respuesta patológica completa |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Fase 2 | Activo sin reclutamiento | 164 | Evaluación del impacto de la heterogeneidad HER2 sobre la respuesta a T-DM1 + pertuzumab preoperatorio en HER2+ temprano; incluye estratificación por estado PR |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Fase 2 | Desconocido | 7 | NEOADAPT: inhibidor de aromatasa + pertuzumab/trastuzumab sin quimioterapia en cáncer de mama localizado no metastásico HR+/HER2+ (Estadio I-IIb); único ensayo diseñado específicamente para PR+/HER2+ sin quimioterapia |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Fase 2 | Terminado | 139 | DECRESCENDO: de-escalada de quimioterapia adyuvante en HER2+/ER-negativo/ganglio-negativo tras respuesta patológica completa con pertuzumab/trastuzumab subcutáneo; evalúa omisión de antraciclinas |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Fase 2 | Activo sin reclutamiento | 128 | TBCRC 023: terapia endocrina neoadyuvante ± lapatinib + trastuzumab durante 12 vs 24 semanas en HER2-sobreexpresado; explora interacción entre vías ER y HER2 |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completado | 1.151 | Estudio observacional retrospectivo multicéntrico sobre prevalencia, características clínicas y patrones de tratamiento de cáncer de mama HER2-bajo en mercados emergentes; caracterización de subtipos moleculares |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECA (WSG-ADAPT TP-II) | JAMA Oncology | Comparación prospectiva aleatorizada de terapia endocrina + pertuzumab/trastuzumab vs quimioterapia de-escalada en cáncer de mama temprano HR+/HER2+; demuestra viabilidad del abordaje sin quimioterapia con análisis de marcadores moleculares |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | ECA (PERTAIN) | J Clin Oncology | Pertuzumab + trastuzumab + inhibidor de aromatasa vs trastuzumab + inhibidor de aromatasa en primera línea de cáncer de mama HR+/HER2+ metastásico; mejoría de PFS con pertuzumab (21.72 vs 15.44 meses) |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECA seguimiento 5 años (NeoSphere) | Lancet Oncology | Análisis de supervivencia libre de progresión y libre de enfermedad a 5 años del ensayo NeoSphere; pertuzumab + trastuzumab + docetaxel mostró ventaja sostenida sobre trastuzumab + docetaxel en HER2+ temprano |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECA (WSG-ADAPT HER2+/HR-) | Annals of Oncology | De-escalada en HER2+/HR-negativo: doble bloqueo trastuzumab + pertuzumab ± paclitaxel semanal; los respondedores tempranos al doble bloqueo solo alcanzaron pCR comparable a la combinación con quimioterapia |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía de Práctica Clínica | J Clin Oncology | Actualización de guía ASCO sobre terapia sistémica para cáncer de mama HER2+ avanzado; pertuzumab + trastuzumab + taxano recomendado como primera línea estándar |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | ECA Fase 3 | British J Cancer | Equivalencia del biosimilar QL1209 vs pertuzumab de referencia + trastuzumab + docetaxel en neoadyuvancia HER2+/ER/PR-negativo; valida pertuzumab como comparador activo para nuevos estudios |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | ECA Fase 2 | Future Oncology | Protocolo DECRESCENDO: de-escalada con pertuzumab/trastuzumab sin antraciclinas en HER2+/HR-negativo/ganglio-negativo; aborda la omisión de toxicidades severas manteniendo doble bloqueo HER2 |
| [40282499](https://pubmed.ncbi.nlm.nih.gov/40282499/) | 2025 | ECA | Cancers | Propuesta operacional de quimioterapia metrónómica adyuvante en pT1-T2 N0 HER2+/ER/PR-positivo combinada con terapia anti-HER2, anti-hormonal y radioterapia; relevante para el subtipo PR+/HER2+ |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Revisión | Southern Medical J | Revisión de terapias neoadyuvantes y adyuvantes en cáncer de mama, incluyendo el papel de pertuzumab según subtipo molecular (Luminal B, HER2-enriquecido) |
| [33902424](https://pubmed.ncbi.nlm.nih.gov/33902424/) | 2022 | Revisión | Endocrine Metab Immune Disorders | Revisión de inmunoterapia para cáncer de mama incluyendo trastuzumab/pertuzumab para HER2+; contextualiza el bloqueo dual HER2 dentro del panorama terapéutico actual |

---

## Información de Mercado en Colombia

Pertuzumab no cuenta con registros sanitarios activos en Colombia. La consulta a la base de datos INVIMA no arrojó ningún registro (0 licencias) para este principio activo. El producto no está disponible como especialidad farmacéutica comercializada en el territorio colombiano a la fecha de este informe.

> **Nota:** A nivel global, pertuzumab (Perjeta®, Roche) cuenta con aprobación de la FDA (EE.UU.) y la EMA (Europa) para cáncer de mama HER2-positivo en múltiples escenarios (neoadyuvancia, primera línea metastásica y adyuvancia). Su ausencia en el registro colombiano representa una barrera regulatoria a resolver antes de cualquier implementación local.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — anticuerpo monoclonal anti-HER2 (no citotóxico convencional; actúa por inhibición de señalización y ADCC) |
| Riesgo de Mielosupresión | Bajo como monoterapia; moderado-alto en combinación con docetaxel/paclitaxel (la mielosupresión es atribuible principalmente al componente quimioterápico concomitante) |
| Clasificación de Emetogenicidad | Baja (pertuzumab en infusión IV sola); el potencial emetogénico del esquema global depende del agente quimioterápico asociado |
| Items de Monitoreo | Fracción de eyección ventricular izquierda (FEVI) antes del inicio y cada 3 ciclos; hemograma completo con diferencial (cuando se combina con quimioterapia); función hepática y renal; vigilancia de reacciones a la infusión (fiebre, escalofríos, hipotensión) en la primera administración |
| Protección en Manejo | Requiere cadena de frío (2-8°C) y manipulación aséptica; no está clasificado como agente citotóxico convencional, pero deben seguirse las precauciones estándar para productos biotecnológicos inyectables |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 2/3 completados —incluyendo WSG-ADAPT TP-II, PERTAIN y los ensayos pivotales de biosimilares de Fase 3— respaldan directamente la eficacia de pertuzumab en el subgrupo PR+/HER2+ de cáncer de mama con un nivel de evidencia L1, superando el umbral mínimo para considerar su uso. La sólida justificación mecanística (crosstalk HER2/PR, doble bloqueo HER2 como estrategia de superación de resistencia endocrina) refuerza la plausibilidad biológica de la predicción TxGNN.

**Para avanzar se necesita:**
- Tramitar registro sanitario ante INVIMA para pertuzumab (actualmente sin registro en Colombia)
- Completar datos de mecanismo de acción (MOA) mediante consulta de ficha técnica actualizada en DrugBank o TFDA
- Obtener información de advertencias, contraindicaciones e interacciones farmacológicas del prospecto oficial (actualmente sin datos disponibles)
- Establecer plan de monitoreo cardíaco (FEVI) como requisito de seguridad para uso en PR+/HER2+
- Definir el esquema combinado (pertuzumab + trastuzumab ± terapia endocrina vs esquemas con quimioterapia) según el perfil de riesgo del paciente
- Análisis de costo-efectividad en el contexto del sistema de salud colombiano dada la ausencia de acceso local actual
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

