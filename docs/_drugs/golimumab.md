---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 5
---

# Golimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Golimumab: De Artritis Reumatoide a Vasculitis Reumatoide

## Resumen en Una Frase

Golimumab (Simponi®) es un anticuerpo monoclonal humano anti-TNF-α aprobado globalmente para el tratamiento de artritis reumatoide, artritis psoriásica y espondiloartritis axial, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Vasculitis Reumatoide**, con **3 ensayos clínicos** y **6 publicaciones** que actualmente respaldan esta dirección, aunque ninguno de estos estudios aborda la indicación de forma directa.
La evidencia disponible es de nivel L3 —predominantemente observacional e indirecta— lo que sitúa esta indicación como una pregunta de investigación que requiere datos clínicos específicos antes de avanzar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (aprobación global; sin registro en Colombia) |
| Nueva Indicación Predicha | Vasculitis Reumatoide |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por Qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción desde el registro local, ya que golimumab no cuenta con registro sanitario en Colombia. Sin embargo, la literatura contenida en este Evidence Pack es consistente: golimumab es un anticuerpo monoclonal IgG1κ completamente humano que neutraliza directamente el factor de necrosis tumoral alfa (TNF-α), la citocina proinflamatoria central en la patogenia de la artritis reumatoide (RA), la artritis psoriásica y la espondiloartritis axial. Su aprobación en EE. UU. data de abril de 2009 (PMID 20065639).

La vasculitis reumatoide (RV) es una complicación sistémica grave de la RA de larga evolución y seropositiva, en la que el mismo mecanismo inflamatorio mediado por TNF-α que destruye las articulaciones también afecta los vasos sanguíneos de pequeño y mediano calibre. Dado que golimumab actúa precisamente sobre TNF-α —citocina presente tanto en la sinovitis de la RA como en la inflamación de la pared vascular en RV— existe una base mecanística plausible. De hecho, el reporte (PMID 29075910) señala que la introducción de los biológicos anti-TNF ha reducido la incidencia de vasculitis reumatoide en pacientes con RA seropositiva, lo que constituye evidencia epidemiológica indirecta de impacto.

No obstante, la relación no es libre de complejidad: un caso documentado (PMID 22999907) describe el desarrollo paradójico de arteritis de Takayasu —otra vasculitis de grandes vasos— bajo terapia anti-TNF, lo que alerta sobre fenómenos inmunes inesperados. Este hallazgo no invalida la hipótesis, pero exige cautela y monitoreo cuidadoso. El uso exitoso de golimumab en uveítis por enfermedad de Behçet (PMID 23252659), otra condición de naturaleza vasculítica, aporta un concepto de prueba conceptual indirecto para otras vasculitis autoinmunes.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio observacional multinacional de tocilizumab en RA con respuesta inadecuada a DMARDs o a un biológico previo; población puede incluir pacientes con manifestaciones extraarticulares como RV; datos de manejo de RA en contexto de escalada terapéutica |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750,000 | Gran estudio epidemiológico que cuantifica el riesgo de nuevas enfermedades inflamatorias mediadas inmunológicamente (IMIDs) en pacientes tratados con biológicos e inmunosupresores; vasculitis puede estar capturada como resultado secundario |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | No iniciado | 80 | Evaluación del manejo perioperatorio de inmunosupresores en pacientes reumatológicos sometidos a artroplastia total de hombro; sin relación directa con vasculitis reumatoide como indicación terapéutica |

> ⚠️ **Nota**: Ninguno de los tres ensayos estudia directamente la vasculitis reumatoide como indicación terapéutica de golimumab. La ausencia de ensayos clínicos específicos para RV es el principal limitante de la evidencia en esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Reporte de caso | Rheumatology International | Paciente con RA tratada con golimumab que desarrolló pioderma gangrenoso y artritis piógena en sepsis grave; el artículo menciona explícitamente que los biológicos anti-TNF han atenuado la incidencia de vasculitis reumatoide en RA seropositiva |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Cohorte comparativa | Int J Molecular Sciences | Meta-análisis en red de 36 ECAs que compara dosis estándar, altas y bajas de 5 inhibidores de TNF (incluyendo golimumab) en destrucción articular radiográfica en RA; resultados similares entre originales y biosimilares |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Reporte de caso | Ocular Immunol Inflamm | Uveítis refractaria por enfermedad de Behçet —condición de naturaleza vasculítica— tratada exitosamente con golimumab; constitye concepto de prueba para el uso de golimumab en enfermedades vasculíticas autoinmunes |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Reporte de caso | Joint Bone Spine | Dos casos de arteritis de Takayasu que se manifestaron durante terapia anti-TNF; alerta sobre vasculitis paradójica como evento adverso infrecuente, con implicaciones de seguridad para el uso de anti-TNF en vasculitis |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Revisión | BMC Medicine | Revisión actualizada de terapias biológicas en enfermedades reumatológicas autoinmunes; cubre mecanismos de acción, eficacia y limitaciones de inhibidores de TNF incluyendo golimumab |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Estudio de cohorte | Semin Arthritis Rheum | Frecuencia de enfermedad renal terminal en RA y sus causas —incluyendo nefropatía por vasculitis—; contextualiza la carga de complicaciones sistémicas de RA en el que RV puede jugar un rol |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> ⚠️ **Señal de alerta específica para esta indicación**: La literatura (PMID 22999907) documenta casos de vasculitis paradójica (arteritis de Takayasu) durante terapia anti-TNF. Aunque es infrecuente, este fenómeno debe considerarse en el monitoreo clínico si se utiliza golimumab en contexto de vasculitis reumatoide.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La base mecanística es plausible —TNF-α es central en la patogenia de ambas condiciones (RA y RV)— y los biológicos anti-TNF han reducido epidemiológicamente la incidencia de vasculitis reumatoide, pero no existe ningún ensayo clínico que evalúe golimumab directamente en RV como indicación, la evidencia disponible es exclusivamente indirecta u observacional (L3), y el perfil de seguridad específico en esta condición incluye una señal de vasculitis paradójica que requiere estudio prospectivo.

**Para avanzar se necesita:**
- Diseño y ejecución de un estudio observacional o ensayo piloto específico en pacientes con vasculitis reumatoide confirmada tratados con golimumab
- Obtención del registro sanitario en Colombia (INVIMA) y descarga del prospecto oficial para llenar los vacíos de seguridad (advertencias, contraindicaciones)
- Análisis sistemático del perfil de eventos adversos vasculíticos paradójicos bajo anti-TNF en series más amplias
- Confirmación del mecanismo de acción formal vía consulta a DrugBank API (Data Gap DG002 pendiente)
- Evaluación comparativa con otros anti-TNF (adalimumab, etanercept) que tienen mayor historial publicado en manifestaciones extraarticulares de RA, para contextualizar la posición de golimumab en este espacio terapéutico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

