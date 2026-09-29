---
layout: default
title: Febuxostat
parent: Evidencia Moderada (L3-L4)
nav_order: 196
evidence_level: L4
indication_count: 3
---

# Febuxostat
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Febuxostat: De Hiperuricemia (Gota) a Hipouricemia Renal

## Resumen en Una Frase

Febuxostat es un inhibidor no purínico y selectivo de la xantina oxidasa, usado para reducir el ácido úrico en la hiperuricemia y la gota. El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**, con **1 ensayo clínico** (de relevancia dudosa) y **2 publicaciones** (una revisión narrativa y un reporte de caso). La evidencia es muy débil y la predicción es probablemente un artefacto del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia/gota (según la farmacología conocida del fármaco). El texto de indicación en los registros solo dice "FEBUXOSTAT" y no especifica ninguna indicación |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, febuxostat es un inhibidor no purínico y selectivo de la xantina oxidasa, y su eficacia para bajar el ácido úrico sérico está comprobada.

La hipouricemia renal ya es un estado de ácido úrico bajo, por lo que el puntaje tan alto (0.9999) probablemente refleja cercanía en el grafo de conocimiento (ambas condiciones giran en torno al metabolismo del urato) y no una coincidencia terapéutica real. La indicación original busca bajar el urato y esta condición ya lo tiene bajo.

La única justificación plausible es una hipótesis. Un reporte de caso (PMID 36754409) plantea que los inhibidores de la xantina oxidorreductasa podrían ayudar a prevenir la lesión renal aguda inducida por ejercicio, una complicación frecuente en la hipouricemia renal. El efecto actuaría sobre la carga urinaria de urato y no sobre el urato sérico. Ningún dato clínico respalda esta idea todavía.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado sobre el efecto del control del ácido úrico en la recurrencia de cálculos y la función renal en pacientes con litiasis e hiperuricemia |

Este ensayo no respalda la indicación predicha. El título del registro es solo el nombre de un departamento hospitalario (Urología, Hospital Central Xu-hui de Shanghái) y el resumen apunta a hiperuricemia con litiasis, no a hipouricemia renal. Su relevancia se clasificó como baja (C) y habría que revisar el registro original para confirmarla.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión narrativa | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) para el reumatólogo: causas y enfoque clínico. No evalúa febuxostat como tratamiento |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Reporte de caso | Internal Medicine | Futbolista japonés de 16 años con hipouricemia renal familiar (mutaciones en URAT1) y lesión renal aguda recurrente por ejercicio. La hidratación no la previno, y se propone el uso de inhibidores no purínicos de la xantina oxidorreductasa como profilaxis. El resultado no es visible en el resumen disponible |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20088755 | UREXIL® 80 MG TABLETAS RECUBIERTAS (Laboratorios Bussié S.A.) | Tableta recubierta (oral) | Sin indicación específica en el registro (solo figura "FEBUXOSTAT") |

El fármaco tiene 20 registros en total. Los detalles disponibles corresponden a este único registro, que aparece repetido en los datos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una revisión narrativa, un reporte de caso individual y un ensayo cuya relación con la indicación no se puede verificar. Además, bajar aún más el urato en una condición de urato bajo no tiene una lógica terapéutica clara, y el puntaje alto del modelo parece un artefacto del grafo.

**Para avanzar se necesita:**
- Revisar el registro completo de NCT04398251 para confirmar condición e intervención.
- Leer el texto completo del caso PMID 36754409 para saber si febuxostat se usó y con qué resultado.
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y los datos del mecanismo de acción.
- Definir si el objetivo sería la carga urinaria de urato y la prevención de lesión renal aguda por ejercicio, y en ese caso diseñar un estudio dirigido.
- Considerar las otras predicciones del mismo fármaco, que tienen una lógica mecanística más coherente pero también evidencia débil (nivel L4, solo reportes de caso): la deficiencia parcial de HPRT y el síndrome de Lesch-Nyhan. En este último el alopurinol es el estándar, y febuxostat solo sería alternativa en intolerantes, con uso pediátrico fuera de indicación y sin efecto sobre las manifestaciones neurológicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

