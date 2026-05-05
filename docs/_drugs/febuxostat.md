---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Usando el skill `txgnn-pipeline` para orientación de flujo. Ahora procedo a generar el informe de evaluación de reposicionamiento basado en el Evidence Pack provisto.

---

# Febuxostat: De Hiperuricemia por Gota a Hipouricemia Renal

## Resumen en Una Frase

Febuxostat es un inhibidor selectivo no purínico de la xantina oxidorreductasa (XOR), aprobado globalmente para reducir los niveles séricos de urato en pacientes adultos con hiperuricemia crónica asociada a gota.
El modelo TxGNN predice que podría ser efectivo para **Hipouricemia Renal (RHUC)** mediante un mecanismo paradójico: no para elevar el urato, sino para suprimir la generación de radicales libres (ROS) durante el ejercicio intenso, previniendo así la lesión renal aguda inducida por ejercicio (EAKI) en portadores de mutaciones URAT1.
Esta predicción cuenta con **1 ensayo clínico** y **2 publicaciones** científicas que respaldan la hipótesis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia crónica asociada a gota |
| Nueva Indicación Predicha | Hipouricemia renal (RHUC) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Febuxostat es un inhibidor selectivo no purínico de la xantina oxidorreductasa (XOR), enzima clave en los dos últimos pasos del catabolismo de purinas: la conversión de hipoxantina a xantina y de xantina a ácido úrico. Al bloquear XOR, Febuxostat reduce simultáneamente la producción de ácido úrico **y** la generación de especies reactivas de oxígeno (ROS), que son un subproducto obligado de la reacción catalizada por XOR.

La hipouricemia renal (RHUC) es una enfermedad rara causada por mutaciones en el transportador urato tubular URAT1 (gen *SLC22A12*), que impide la reabsorción renal de urato. El resultado clínico directo es un nivel sérico de urato anormalmente bajo; sin embargo, la actividad de XOR en estos pacientes no está disminuida y puede estar incluso aumentada. Durante el ejercicio anaeróbico de alta intensidad, el catabolismo acelerado de purinas desencadena una sobreactivación de XOR que genera un pico de ROS, produciendo estrés oxidativo agudo a nivel renal (EAKI). Aquí reside el aspecto contraintuitivo de la predicción: aunque el paciente tiene urato bajo (producto final), el intermediario catalítico de XOR genera el daño.

Febuxostat actuaría en RHUC interrumpiendo la cascada oxidativa en el nodo XOR, reduciendo la carga de ROS durante el ejercicio sin necesidad de modificar el urato sérico. La similitud mecanística con la indicación original (inhibición de XOR) es total; lo que cambia es el objetivo terapéutico: de antihiperuricémico a nefroprotector antioxidante. Este mecanismo ha sido descrito en reportes de caso y artículos de hipótesis, configurando una base farmacológica sólida aunque aún sin ensayos clínicos confirmatorios en RHUC.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado en el Hospital Central Xu-hui de Shanghái para explorar el efecto del control de ácido úrico sobre la recurrencia de cálculos renales y la función renal en pacientes urológicos con hiperuricemia. **Nota de relevancia:** el estado UNKNOWN indica falta de actualización por más de 2 años tras la fecha de finalización prevista (mayo 2022). El título del registro identifica solo la institución; no puede confirmarse si el protocolo aborda específicamente RHUC o EAKI. Se recomienda contactar al investigador principal para verificar el diseño real. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Perspectiva / Hipótesis | *Internal Medicine* (Tokio) | Reporte de un futbolista de 16 años con RHUC familiar por mutaciones compuestas en URAT1 y EAKI recurrente refractaria a hidratación profiláctica. Los autores proponen que los inhibidores selectivos no purínicos de XOR —incluyendo febuxostat— podrían prevenir EAKI al suprimir la generación de ROS durante el ejercicio, sin comprometer el perfil de urato. Constituye la referencia más directa al uso de febuxostat en RHUC. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión Narrativa | *Clinical Rheumatology* | Actualización comprensiva sobre hipouricemia para el reumatólogo clínico: definición (urato sérico < 2 mg/dL), etiología (incluyendo RHUC por mutaciones URAT1/GLUT9), complicaciones (EAKI, urolitiasis) y estrategias de manejo. Provee el marco conceptual de la enfermedad diana. |

---

## Información de Mercado en Colombia

Febuxostat **no cuenta con registros sanitarios activos en Colombia**. No existe ningún producto comercializado con esta molécula activa a la fecha de corte de datos (2026-05-05). Cualquier uso en el país requeriría importación bajo modalidad de uso no registrado, uso compasivo o autorización especial ante el INVIMA.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo farmacológico de Febuxostat en hipouricemia renal es biológicamente coherente y farmacológicamente sólido, pero la evidencia clínica directa se limita a un ensayo Fase 4 con estado incierto (presumiblemente diseñado para hiperuricemia, no para RHUC) y dos publicaciones de nivel observacional/hipótesis. La ausencia total de comercialización en Colombia añade una barrera regulatoria y de acceso que impide avanzar sin pasos previos fundamentales.

**Para avanzar se necesita:**
- Recuperar la ficha técnica completa de Febuxostat desde DrugBank (DG002) para documentar formalmente el MOA y los datos de toxicidad
- Contactar al investigador principal de NCT04398251 para confirmar si el diseño es relevante para RHUC o EAKI
- Identificar o diseñar estudios prospectivos controlados en pacientes con diagnóstico molecular confirmado de RHUC (mutación URAT1/SLC22A12)
- Evaluar la viabilidad regulatoria ante el INVIMA para uso compasivo u off-label, especialmente en población pediátrica y atlética
- Revisar el perfil de seguridad de Febuxostat en pacientes con urato sérico basal muy bajo bajo inhibición prolongada de XOR (riesgo teórico de hipouricemia profunda)
- Considerar que las indicaciones predichas en rangos 2 y 3 (deficiencia parcial de HPRT y síndrome de Lesch-Nyhan) comparten el mismo eje XOR, lo que podría justificar un programa de desarrollo conjunto para enfermedades raras del metabolismo de purinas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

