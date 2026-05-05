---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

El skill de txgnn-pipeline confirma el contexto del proyecto. Ahora procedo a generar el informe completo siguiendo las instrucciones del sistema.

---

# Bevacizumab: De Cáncer Colorrectal a Neoplasia de Epiglotis

## Resumen en Una Frase

Bevacizumab es un anticuerpo monoclonal anti-VEGF aprobado globalmente para el tratamiento de múltiples tumores sólidos (colorrectal, pulmón no microcítico, glioblastoma, ovario, entre otros), aunque actualmente no cuenta con registro INVIMA en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Neoplasia de Epiglotis (epiglottis neoplasm)**,
con **0 ensayos clínicos** y **0 publicaciones** que respalden específicamente esta indicación — la predicción se apoya exclusivamente en la estructura del grafo de conocimiento biológico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro INVIMA en Colombia (indicación global conocida: cáncer colorrectal, CPNM, glioblastoma, cáncer de ovario) |
| Nueva Indicación Predicha | Neoplasia de Epiglotis (epiglottis neoplasm) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Sin embargo, a partir de la información clínica y farmacológica disponible públicamente, bevacizumab es un anticuerpo monoclonal humanizado recombinante que se une selectivamente al factor de crecimiento endotelial vascular (VEGF-A), bloqueando su interacción con los receptores VEGFR-1 y VEGFR-2 en la superficie de las células endoteliales. Esto inhibe la neoangiogénesis tumoral, privando al tumor de su suministro de nutrientes y oxígeno, lo que reduce su capacidad de crecimiento y diseminación.

La relación entre la indicación original (tumores sólidos VEGF-dependientes) y la neoplasia de epiglotis se basa en la observación general de que los tumores de cabeza y cuello expresan VEGF en diversos grados. El modelo TxGNN infirió esta conexión a partir de la proximidad estructural en el grafo biológico: bevacizumab → inhibición de VEGF → tumores de cabeza y cuello → región epiglótica. Este razonamiento tiene cierta coherencia topológica, pero su aplicabilidad clínica real es cuestionable.

No obstante, las neoplasias de epiglotis son en su mayoría benignas (papilomas escamosos, fibromas, hemangiomas), con un grado de vascularización significativamente menor al de los tumores malignos para los que bevacizumab está aprobado. La dependencia de VEGF en estos tumores benignos sigue mecanismos distintos, y no existe ninguna evidencia clínica ni preclínica que respalde esta indicación específica. La predicción se sitúa en el nivel de mayor incertidumbre (L5).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Bevacizumab no cuenta con ningún registro sanitario INVIMA activo en Colombia. El fármaco no está comercializado en el mercado colombiano bajo ninguna presentación o nombre de marca registrado localmente.

---

## Citotoxicidad

Bevacizumab es un agente antineoplásico (anticuerpo monoclonal dirigido contra VEGF-A). Cumple con los criterios de inclusión en esta sección: indicación oncológica primaria y clasificación como agente biológico antitumoral.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — anticuerpo monoclonal antiangiogénico (clase anti-VEGF); no es citotóxico convencional |
| Riesgo de Mielosupresión | Bajo (bevacizumab no actúa directamente sobre células hematopoyéticas; el riesgo hematológico es mínimo como monoterapia) |
| Clasificación de Emetogenicidad | Baja (anticuerpo monoclonal; no asociado a náuseas/vómitos significativos como agente único) |
| Ítems de Monitoreo | Presión arterial (riesgo de hipertensión), proteinuria (relación proteína/creatinina en orina o tira reactiva antes de cada ciclo), función renal, vigilancia de eventos tromboembólicos arteriales y venosos, signos de perforación gastrointestinal y de cicatrización deficiente |
| Protección en Manejo | Seguir regulaciones estándar para medicamentos biológicos/anticuerpos monoclonales; no requiere las mismas medidas de protección que los citotóxicos convencionales (sin riesgo de exposición por inhalación o contacto dérmico en condiciones normales de preparación) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo TxGNN carece por completo de respaldo clínico o preclínico específico para neoplasia de epiglotis (L5: solo predicción del modelo, sin estudios reales). La biología de los tumores de epiglotis —predominantemente benignos y con baja dependencia de la vía VEGF— no justifica el desarrollo clínico en esta indicación con los datos actuales.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción (MOA) completo desde la API de DrugBank (DG002 pendiente de resolución)
- Revisar el perfil de seguridad completo desde la ficha técnica disponible en TFDA/EMA/FDA (DG001 pendiente de resolución)
- Verificar expresión de VEGF en tejido de neoplasias de epiglotis mediante estudios inmunohistoquímicos publicados
- Identificar subtipos histológicos que podrían tener componente vascular significativo (ej. hemangiomas epiglóticos)
- Evaluar si existe alguna serie de casos o modelo animal que permita generar hipótesis antes de considerar estudios clínicos
- Gestionar el registro INVIMA en Colombia si se decide avanzar en investigación clínica local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

