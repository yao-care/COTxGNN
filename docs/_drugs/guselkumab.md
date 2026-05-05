---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

---

# Guselkumab: De Psoriasis en Placa a Colitis Ulcerosa

## Resumen en Una Frase

Guselkumab (Tremfya®) es un anticuerpo monoclonal anti-IL-23p19 aprobado globalmente para el tratamiento de la psoriasis en placa moderada a grave y la artritis psoriásica activa, pero sin registro sanitario vigente en Colombia para ninguna indicación.
El modelo TxGNN predice que podría ser efectivo para **Colitis Ulcerosa**, respaldado por **19 ensayos clínicos activos** — incluyendo el estudio pivotal QUASAR de Fase 3 (publicado en *The Lancet*, 2025) — y **20 publicaciones científicas** que confirman su eficacia, incluyendo la aprobación de la FDA en 2024/2025.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis en placa moderada a grave (aprobación FDA/EMA vigente; sin registro INVIMA Colombia) |
| Nueva Indicación Predicha | Colitis Ulcerosa |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Guselkumab actúa uniéndose selectivamente a la subunidad p19 de la interleucina-23 (IL-23), bloqueando su interacción con el receptor IL-23R y suprimiendo la diferenciación de células Th17 y Th22. Este mecanismo fue validado originalmente en la piel, donde el eje IL-23/Th17 impulsa la hiperproliferación epidérmica y la inflamación crónica de la psoriasis. La misma vía opera en la mucosa intestinal de pacientes con colitis ulcerosa (CU): las células presentadoras de antígenos intestinales secretan IL-23 en exceso, activando células Th17 locales que producen IL-17A, IL-17F e IL-22, destruyendo la barrera epitelial e impulsando la infiltración de neutrófilos y el daño tisular crónico.

La ventaja farmacológica de guselkumab frente a ustekinumab (que bloquea la subunidad p40 compartida por IL-12 e IL-23) radica en que no interfiere con IL-12, mediador crítico de la inmunidad frente a infecciones intracelulares. Esta selectividad ofrece un perfil de seguridad teóricamente superior para el tratamiento crónico. Adicionalmente, guselkumab posee una característica dual única: puede unirse a CD64 (FcγRI) expresado en macrófagos del tejido mucoso, lo que podría conferir propiedades adicionales de modulación inflamatoria local en la pared intestinal — una distinción relevante frente a otros inhibidores de IL-23p19.

El programa QUASAR (Fase 2b en *Gastroenterology* 2023; Fase 3 en *The Lancet* 2025) validó de forma definitiva esta traslación mecanística: guselkumab demostró tasas de remisión clínica y cicatrización endoscópica significativamente superiores a placebo en pacientes con CU moderada a grave, tanto en inducción intravenosa como en mantenimiento subcutáneo. El estudio ASTRO (*Lancet Gastroenterology & Hepatology*, 2026) añadió la evidencia de inducción subcutánea. La aprobación de la FDA en 2024/2025 constituye la validación regulatoria definitiva de la predicción del modelo TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Fase 2b/3 | Activo (no reclutando) | 1064 | Estudio pivotal QUASAR: inducción IV + mantenimiento SC de guselkumab vs placebo en CU moderada a grave. Diseño biétápico de inducción/mantenimiento. Resultados de Fase 3 publicados en *The Lancet* 2025 como base de la aprobación FDA |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Fase 3 | Activo (no reclutando) | 418 | Evaluación de inducción subcutánea de guselkumab vs placebo en CU moderada a grave; diseño treat-through que evalúa remisión clínica al final de la inducción SC |
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Fase 2b | Activo (no reclutando) | 577 | Terapia combinada guselkumab + golimumab (anti-TNF) vs monoterapias en CU refractaria a terapias avanzadas previas; concepto innovador de combinación dual-biológica |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Fase 3 | Activo (no reclutando) | 112 | Eficacia y farmacocinética de guselkumab en CU pediátrica moderada a grave; endpoint primario de remisión al final del mantenimiento en respondedores a la inducción |
| [NCT06663332](https://clinicaltrials.gov/study/NCT06663332) | Fase 3 | Reclutando | 196 | Extensión pediátrica a largo plazo (basket trial): seguridad de guselkumab SC en Enfermedad de Crohn, CU y artritis psoriásica juvenil hasta 2031 |
| [NCT07302360](https://clinicaltrials.gov/study/NCT07302360) | N/A | Reclutando | 200 | Efectividad en práctica clínica real en pacientes bio-naïve con CU moderada a grave en China; complementa el perfil de eficacia en entornos fuera del ensayo clínico |
| [NCT07245394](https://clinicaltrials.gov/study/NCT07245394) | N/A | Reclutando | 200 | SHIFT-IBD: cambio a guselkumab en pacientes con EII (CD y CU) que fracasaron a ustekinumab; evalúa estrategia de secuenciación entre inhibidores de IL-23 |
| [NCT06408935](https://clinicaltrials.gov/study/NCT06408935) | Fase 3b | Reclutando | 112 | Cicatrización transmural en Enfermedad de Crohn evaluada por IRM (índice MaRIA) a semana 48; establece guselkumab como agente modificador de la enfermedad |
| [NCT07102368](https://clinicaltrials.gov/study/NCT07102368) | N/A | Reclutando | 400 | Evidencia del mundo real en CD y CU tratados con guselkumab: efectividad, calidad de vida, fatiga, productividad laboral y satisfacción con el tratamiento |
| [NCT06916390](https://clinicaltrials.gov/study/NCT06916390) | Fase 4 | No iniciado | 20 | Guselkumab en pouchitis (complicación inflamatoria post-colectomía en CU refractaria); exploración de indicación extendida en la CU quirúrgica |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | ECA Fase 3 | The Lancet | QUASAR Fase 3: guselkumab demostró remisión clínica y cicatrización endoscópica significativamente superiores a placebo en inducción y mantenimiento en CU moderada a grave |
| [41544637](https://pubmed.ncbi.nlm.nih.gov/41544637/) | 2026 | ECA Fase 3 | Lancet Gastroenterology & Hepatology | ASTRO: inducción subcutánea de guselkumab demostró eficacia y seguridad en CU moderada a grave (treat-through), simplificando la vía de administración frente al esquema IV estándar |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | ECA Fase 2b | Gastroenterology | QUASAR Fase 2b: guselkumab IV indujo tasas de remisión clínica y remisión endoscópica significativas en pacientes con fracaso a corticoides, inmunosupresores y/o terapias avanzadas previas |
| [40113101](https://pubmed.ncbi.nlm.nih.gov/40113101/) | 2025 | ECA Fase 3 | Gastroenterology | GRAVITI: guselkumab SC en inducción y mantenimiento de Enfermedad de Crohn moderada a grave; confirma la eficacia del mecanismo IL-23 a lo largo de todo el espectro de la EII |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Guía Clínica | Gastroenterology | Guía de práctica clínica viva AGA 2024 para CU moderada a grave: incluye recomendaciones para inhibidores de IL-23p19 incluyendo guselkumab con grado de evidencia alto |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Metaanálisis en red | Gastroenterology | Síntesis de evidencia AGA 2024: guselkumab figura entre los agentes con mayor eficacia comparativa para inducción de remisión en CU moderada a grave |
| [40407729](https://pubmed.ncbi.nlm.nih.gov/40407729/) | 2025 | Metaanálisis en red | Alimentary Pharmacology & Therapeutics | Comparativa de eficacia de terapias de mantenimiento en CU: guselkumab entre los agentes más efectivos para remisión sostenida, considerando diferencias en diseño de ECAs |
| [37069321](https://pubmed.ncbi.nlm.nih.gov/37069321/) | 2023 | Revisión | Nature Reviews Gastroenterology & Hepatology | Revisión exhaustiva del papel del eje IL-12/IL-23 en la homeostasis intestinal y la patogénesis de la EII; base mecanística del uso de inhibidores de p19 selectivos en CU y EC |
| [41324615](https://pubmed.ncbi.nlm.nih.gov/41324615/) | 2025 | Revisión experta | Expert Opinion on Biological Therapy | Evaluación del posicionamiento de guselkumab en CU: análisis del programa QUASAR, características diferenciales (doble acción IL-23/CD64) y perfil de seguridad a largo plazo |
| [40088885](https://pubmed.ncbi.nlm.nih.gov/40088885/) | 2025 | Editorial | Med (New York) | Análisis crítico del programa QUASAR: rapidez de respuesta sintomática, tasas de remisión objetiva, y áreas de incertidumbre que requieren evidencia del mundo real en subpoblaciones no representadas |

---

## Información de Mercado en Colombia

Guselkumab **no cuenta con registros sanitarios INVIMA** en Colombia para ninguna indicación. El medicamento se comercializa internacionalmente como **Tremfya®** (solución inyectable 100 mg/mL, vía subcutánea) con las siguientes aprobaciones vigentes de referencia:

- **FDA (EE. UU.):** Psoriasis en placa (2017), Artritis psoriásica (2020), Colitis ulcerosa moderada a grave (2024/2025)
- **EMA (Europa):** Psoriasis en placa y artritis psoriásica

La ausencia de registro INVIMA representa una oportunidad de entrada regulatoria utilizando el expediente de aprobación FDA/EMA como referencia, en el marco del procedimiento de reconocimiento de autoridades extranjeras de referencia vigente en Colombia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de acción de guselkumab (inhibición selectiva de IL-23p19) tiene validación clínica robusta en colitis ulcerosa, culminando en aprobación regulatoria FDA y respaldado por el programa QUASAR publicado en *The Lancet* (2025) y el ASTRO en *Lancet Gastroenterology & Hepatology* (2026). Múltiples metaanálisis en red y guías AGA respaldan su posición en el algoritmo terapéutico de la CU. La principal limitación operativa es la ausencia total de registro INVIMA en Colombia para cualquier indicación, lo que requiere un proceso regulatorio completo antes del acceso clínico.

**Para avanzar se necesita:**
- Iniciar el proceso de registro INVIMA para guselkumab, utilizando el dossier FDA/EMA como referencia regulatoria (psoriasis en placa como primera indicación, seguida de CU)
- Obtener y analizar el prospecto oficial (PI/RCP) para documentar advertencias, contraindicaciones e interacciones farmacológicas (actualmente identificadas como vacíos de datos DG001 y DG002)
- Completar el perfil de mecanismo de acción (DG002) consultando DrugBank API para el análisis completo del reposicionamiento
- Definir estrategia de acceso y precio: negociación con Janssen Colombia, análisis de cobertura en PBS y mecanismos No-PBS, e identificación de hospitales de alta complejidad como centros piloto
- Establecer criterios de selección de pacientes (fracaso a biológicos previos, índice Mayo, biomarcadores inflamatorios: PCR, calprotectina fecal)
- Monitorear el estudio SHIFT-IBD (NCT07245394) para datos de secuenciación post-ustekinumab, y el ASTRO (PMID 41544637) para la estrategia de inducción subcutánea — ambos relevantes para definir el posicionamiento en el algoritmo de tratamiento colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

