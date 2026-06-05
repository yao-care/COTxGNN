---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

El skill TxGNN no aporta guías específicas para redacción de informes. Procedo a generar el reporte directamente basado en el Evidence Pack y las instrucciones del sistema.

---

# Calcitriol: De Trastornos Óseos por Déficit de Vitamina D Activa a Raquitismo Hipofosfatémico Hereditario

## Resumen en Una Frase

Calcitriol (1,25-dihidroxivitamina D₃) es la forma biológicamente activa de la vitamina D, utilizado clínicamente para el manejo de hipocalcemia, hipoparatiroidismo y trastornos óseos por insuficiencia de vitamina D activa. El modelo TxGNN predice que podría ser efectivo para el **Raquitismo Hipofosfatémico Hereditario**, con **7 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Esta predicción tiene alta plausibilidad mecánica: en las formas hereditarias de raquitismo hipofosfatémico, el exceso de FGF23 suprime directamente la síntesis endógena de calcitriol, siendo la suplementación con este compuesto la base del tratamiento convencional durante más de cuatro décadas.

> **Nota sobre la predicción de mayor puntaje (Rango #1):** La indicación "obsolete vitamin D deficiency" (99.96%) registra 0 ensayos y 0 publicaciones por un artefacto del pipeline de datos: el término está marcado como "obsoleto" en la ontología de enfermedades, lo que impide el mapeo de evidencia. Se trata de un problema del pipeline, no de un vacío clínico real. El presente informe se centra en el **Rango #7 — Raquitismo Hipofosfatémico Hereditario**, que es la indicación con mayor nivel de evidencia clínica disponible (L2, "Proceed with Guardrails").

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicacion Original | No disponible en la base de datos (sin registro INVIMA); uso clínico establecido: hipocalcemia, hipoparatiroidismo, osteodistrofia renal |
| Nueva Indicacion Predicha | Raquitismo Hipofosfatémico Hereditario |
| Puntaje de Prediccion TxGNN | 99.28% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Numero de Registros Sanitarios | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales del mecanismo de acción en el dataset (DG002). Sin embargo, calcitriol es la forma hormonal activa de la vitamina D (1,25-dihidroxivitamina D₃), producida fisiológicamente por la enzima 1α-hidroxilasa en las células tubulares renales proximales. Su mecanismo central consiste en la unión al Receptor de Vitamina D (VDR) en tejidos diana, regulando la expresión génica que controla la absorción intestinal de calcio y fósforo, la reabsorción tubular renal de calcio, y la mineralización ósea. PTH es el principal inductor de la 1α-hidroxilasa renal, mientras que FGF23 la inhibe.

En el Raquitismo Hipofosfatémico Hereditario —cuya forma más prevalente es el Raquitismo Ligado al Cromosoma X (XLH), causado por mutaciones del gen *PHEX*— la fisiopatología conecta directamente con el calcitriol: la disfunción de PHEX desencadena hipersecreción de FGF23 en osteocitos y osteoblastos, el cual actúa sobre el riñón **suprimiendo la actividad de 1α-hidroxilasa** e inhibiendo la reabsorción de fosfato. El resultado es una doble deficiencia: hipofosfatemia crónica **y** niveles inapropiadamente bajos de calcitriol endógeno, lo que compromete la mineralización en placas de crecimiento y tejido óseo, generando raquitismo y osteomalacia.

La suplementación con calcitriol más fosfato oral fue el estándar de cuidado para XLH y otras formas hereditarias —ADHR (autosómica dominante), ARHR (autosómica recesiva), HHRH (hipercalciúrica)— durante más de cuatro décadas, con evidencia publicada desde 1980 en *The New England Journal of Medicine* y revisada en 2024 en *The Lancet*. Aunque el burosumab (anticuerpo monoclonal anti-FGF23) representa un avance terapéutico para XLH pediátrico específicamente, calcitriol mantiene relevancia clínica central en formas no-XLH donde el biológico no tiene indicación aprobada, y como alternativa de acceso en entornos con limitaciones de costo o disponibilidad.

---

## Evidencia de Ensayos Clínicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|--------|-------------|----------------------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Fase Temprana 1 | Activo (no reclutando) | 20 | **Monoterapia con calcitriol en XLH** (sin suplemento de fosfato): evalúa si calcitriol solo mejora fosfatemia y mineralización ósea en niños y adultos con XLH sin incrementar nefrocalcinosis durante 1 año de seguimiento con escalada de dosis |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Fase 4 | Desconocido | 100 | **Comparación alta vs baja dosis de vitamina D activa + fosfato neutro en niños con XLH**: objetivo establecer dosificación estandarizada por peso; documenta madurez clínica de la terapia convencional |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Fase 3 | Activo (no reclutando) | 27 | **ENERGY 3**: eficacia y seguridad de INZ-701 en deficiencia de ENPP1; calcitriol presumiblemente como parte del tratamiento de referencia o brazo comparador |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completado | 260 | **Estudio observacional FGF23** en hipofosfatemias hereditarias y adquiridas (n=260): por inhibición de FGF23 sobre 1α-hidroxilasa renal, provee base mecanística para el uso de calcitriol |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Desconocido | 150 | **FGF23, Klotho y esclerostina en formadores de cálculos renales**: relevancia indirecta para monitoreo de hipercalciuria como efecto adverso del calcitriol en XLH |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | No iniciado | 65 | **Medición de ATP por espectroscopía en diabetes fosfato/XLH**: estudio de biomarcadores sobre metabolismo energético tubular; no evalúa eficacia de calcitriol directamente |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Retirado | 0 | **Cinacalcet en raquitismo hipofosfatémico familiar**: retirado sin reclutamiento; el protocolo menciona calcitriol + fosfato como tratamiento estándar de base, confirmando su uso rutinario |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Revisión | Calcified Tissue Int | Diagnóstico y terapia de XLH (Böckmann & Haffner): calcitriol + fosfato como estándar convencional vs burosumab; actualización de protocolos de monitoreo |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Revisión | The Lancet | Revisión exhaustiva de XLH (Kamenický et al.): fisiopatología de FGF23, supresión directa de síntesis de calcitriol, opciones terapéuticas actuales |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Revisión | J Bone Miner Res | Raquitismo hipofosfatémico y talla baja (Davis et al.): presentación clínica, diagnóstico diferencial y estrategias terapéuticas con calcitriol |
| [38044258](https://pubmed.ncbi.nlm.nih.gov/38044258/) | 2024 | Revisión | Best Pract Res Clin Endocrinol Metab | Exceso hereditario de FGF-23 (Cherian & Paul): XLH, ADHR, ARHR y síndromes asociados; papel de calcitriol como terapia base en todas las formas |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Revisión | Horm Res Paediatrics | Historia del raquitismo y evolución de tratamientos (Miller & Imel): de ergocalciferol a calcitriol y análogos activos en diferentes formas de rickets |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohorte | J Endocrinol Invest | Crecimiento en altura desde nacimiento a adultez en raquitismo hipofosfatémico hereditario bajo tratamiento convencional con calcitriol y fosfato |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Revisión | Metabolism | Manejo de XLH en adultos (Lecoq et al.): calcitriol + fosfato para síntomas musculoesqueléticos y dentales; complicaciones a largo plazo incluyendo nefrocalcinosis |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Observacional | Pediatric Endocrinol Rev | Efecto del tratamiento temprano con calcitriol y fosfato sobre el crecimiento en 127 pacientes con XLH procedentes de 49 centros europeos |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Intervencionista | J Clin Invest | Curación de enfermedad ósea en XLH con fosforo y calcitriol a alta dosis (68 ng/kg/día): inducción y mantenimiento de remisión de osteomalacia resistente a terapia convencional |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Intervencionista | N Engl J Med | Comparación fosfato solo vs + ergocalciferol vs + calcitriol en raquitismo resistente a vitamina D (n=11 niños): calcitriol superior en aumentar absorción intestinal de fósforo y reducir requerimientos de fosfato |

---

## Información de Mercado en Colombia

Calcitriol **no cuenta con ningún registro sanitario activo ante INVIMA** según los datos disponibles (total de licencias: 0). Si bien el medicamento se comercializa ampliamente a nivel global bajo marcas como Rocaltrol® (Roche), Calcijex® y Decostriol®, la ausencia de registro en Colombia implica que cualquier utilización clínica requeriría importación bajo régimen especial (Decreto 481 de 2004) o solicitud de uso compasivo ante el INVIMA.

---

## Consideraciones de Seguridad

Consultar el prospecto del fabricante para información completa de advertencias y contraindicaciones, ya que los datos formales de seguridad no fueron recuperados en este Evidence Pack.

**Aspectos de seguridad clínicamente relevantes para esta indicación (conocimiento clínico establecido, no procedentes del dataset):**
- **Hipercalcemia e hipercalciuria**: Principal riesgo dosis-dependiente; requiere monitoreo periódico de calcio sérico y calciuria de 24 horas, especialmente durante ajuste de dosis
- **Nefrocalcinosis**: Complicación a largo plazo documentada en XLH bajo terapia convencional con calcitriol + fosfato; vigilar con ecografía renal semestral/anual
- **Hiperparatiroidismo secundario**: Puede desarrollarse con tratamiento prolongado; monitorear niveles de PTH

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Calcitriol en combinación con fosfato oral es una terapia consolidada para el raquitismo hipofosfatémico hereditario, respaldada por más de cuatro décadas de evidencia clínica, publicaciones en revistas de máximo impacto (*N Engl J Med* 1980, *The Lancet* 2024) y un ensayo de Fase 4 que documenta su uso maduro. La plausibilidad mecánica es directa y bien fundamentada en la fisiopatología del eje FGF23/1α-hidroxilasa. La ausencia de registro INVIMA en Colombia y la necesidad de monitoreo especializado para prevención de nefrocalcinosis e hipercalcemia justifican los guardarraíles de implementación.

**Para avanzar se necesita:**
- Tramitación de registro sanitario ante INVIMA o importación bajo régimen especial para acceso legal al medicamento en Colombia
- Protocolo de monitoreo clínico estructurado: calcio sérico y urinario (24 h), fósforo, función renal, PTH intacta y ecografía renal periódica (detección precoz de nefrocalcinosis)
- Evaluación por especialista en endocrinología pediátrica o nefrología para dosificación individualizada según peso, edad y forma genética de la enfermedad
- Recuperación de datos formales de MOA desde DrugBank (actualmente DG002 — High severity) para completar el análisis de seguridad del pipeline
- Revisión formal de interacciones farmacológicas prioritarias: tiazidas (potencian hipercalcemia), digoxina (hipercalcemia aumenta toxicidad), colestiramina (reduce absorción de calcitriol) y antiácidos con magnesio (hipermagnesemia en insuficiencia renal)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

