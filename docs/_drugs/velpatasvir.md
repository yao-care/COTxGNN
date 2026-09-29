---
layout: default
title: Velpatasvir
parent: Solo Predicción del Modelo (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Velpatasvir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Velpatasvir: De Hepatitis C Crónica a Infección por el Virus de la Hepatitis B

## Resumen en Una Frase

Velpatasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C (VHC). En Colombia se comercializa combinado con sofosbuvir (Epclusa®).
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la hepatitis B (VHB)**, pero la evidencia real es muy débil. De **26 ensayos clínicos** y **20 publicaciones** asociados, ninguno demuestra eficacia contra el VHB: casi todos son sobre hepatitis C, y el único dato relacionado con VHB es una señal de seguridad (reactivación del VHB durante el tratamiento del VHC).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sofosbuvir + Velpatasvir (el registro no detalla el texto de la indicación; los ensayos y la literatura corresponden a hepatitis C crónica) |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 (solo mecanismo y señales indirectas; sin estudios de eficacia en VHB) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (todos corresponden al mismo registro, 20126648) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la información conocida, velpatasvir es un inhibidor de NS5A del VHC y se usa junto con sofosbuvir (inhibidor de la polimerasa NS5B) en una tableta de dosis fija. Su eficacia contra el VHC está bien documentada en múltiples ensayos de fase 2 y 3.

La relación con el VHB es débil. Ambos son virus que infectan el hígado y comparten proximidad en el grafo de conocimiento, pero el VHB no tiene una proteína equivalente a NS5A. Por eso no se identifica un vínculo antiviral directo plausible. El puntaje alto de TxGNN probablemente refleja esa cercanía entre virus hepatotrópicos, no una razón mecanística.

El único hallazgo clínico relacionado con VHB es de seguridad. Se han descrito casos de reactivación del VHB en pacientes coinfectados con VHC tratados con antivirales de acción directa, incluido un reporte con sofosbuvir/velpatasvir. Esto no respalda el uso de velpatasvir para tratar hepatitis B, sino que exige vigilancia.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 26 asociados. Solo el primero involucra pacientes con VHB, y lo hace como prevención de reactivación, no como tratamiento del VHB con velpatasvir.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | SOF/VEL por 12 semanas con tenofovir alafenamida (TAF) profiláctico en coinfección VHC/VHB, con o sin cirrosis compensada (China) |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completado | 33808 | Estudio de seguridad de antivirales de acción directa en hepatitis C; podría informar el riesgo de reactivación del VHB, sin evaluar tratamiento del VHB |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Fase 3 | Completado | 222 | ECA de SOF/VEL en hepatitis C de adquisición reciente, con o sin VIH; solo eficacia contra VHC |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Fase 3 | Completado | 102 | SOF/VEL ± ribavirina en hepatitis C con cirrosis descompensada |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Fase 3 | Completado | 268 | SOF/VEL con o sin ribavirina en hepatitis C con cirrosis Child-Pugh B |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Fase 2 | Completado | 379 | SOF + velpatasvir (GS-5816) en hepatitis C sin tratamiento previo; no es un ensayo de VHB |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Fase 4 | Completado | 228 | Velpatasvir genérico + sofosbuvir en coinfección VHC/VIH |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Fase 4 | Completado | 281 | ECA de ribavirina adyuvante con SOF/VEL/voxilaprevir en hepatitis C sin respuesta previa |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Fase 1 | Completado | 15 | Interacción farmacológica con anticonceptivo hormonal en voluntarios sanos; no evalúa VHB |
| [NCT03513393](https://clinicaltrials.gov/study/NCT03513393) | Fase 1 | Completado | 11 | Efecto de la cola (bebida ácida) sobre la absorción de velpatasvir en voluntarios tratados con omeprazol |

---

## Evidencia de Literatura

No hay ensayos aleatorizados sobre VHB. Se muestran las publicaciones más relacionadas con VHB, ordenadas por relevancia.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Rep | Reactivación del VHB, sostenida por una variante de escape del HBsAg, en un paciente anti-HBc positivo tratado con sofosbuvir/velpatasvir por hepatitis C |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Estudio observacional | J Virus Erad | Efectividad y seguridad de SOF/VEL en pacientes chinos con hepatitis C, incluidos subgrupos con coinfección VHC/VHB |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | No clasificado | J Viral Hepat | Estrategia simplificada de SOF/VEL en Myanmar; los pacientes coinfectados con VHB recibieron tenofovir de forma concurrente |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohorte | J Gastroenterol Hepatol | Eficacia y seguridad de SOF/VEL ± ribavirina en hepatitis C genotipo 3, incluyendo pacientes con coinfección |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revisión | World J Gastroenterol | Avances en hepatitis viral pediátrica; el tratamiento del VHB sigue lejos de ser curativo, mientras que el del VHC ya dispone de antivirales de acción directa |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Estudio retrospectivo | Klin Mikrobiol Infekc Lek | Evaluación de frecuencia, eficacia y tolerancia del tratamiento antiviral de hepatitis B y C en niños (Ostrava) |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Reporte de congreso | AIDS Rev | Resumen de novedades sobre hepatitis virales y antivirales pangenotípicos contra el VHC |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Estudio transversal | Ann Hepatol | Comparación global de precios de fármacos para hepatitis B y C; no aporta datos de eficacia |

---

## Información de Mercado en Colombia

Los 4 registros del paquete de evidencia son entradas idénticas del mismo registro sanitario, por lo que se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20126648 | EPCLUSA® (GILEAD SCIENCES IRELAND UC) | Tableta recubierta (vía oral) | Sofosbuvir + Velpatasvir |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. En el paquete de evidencia no hay advertencias, contraindicaciones ni interacciones registradas para este fármaco.

Como observación de la evidencia recopilada (no del prospecto):
- **Reactivación del VHB:** hay un reporte de caso de reactivación durante el tratamiento con sofosbuvir/velpatasvir en un paciente anti-HBc positivo. Antes de usar antivirales de acción directa, conviene tamizar por VHB en pacientes con hepatitis C.
- **Absorción de velpatasvir:** depende del pH. Un ensayo de fase 1 indica que los inhibidores de la bomba de protones como omeprazol reducen la absorción entre 26% y 56%.
- **Antirretrovirales:** en pacientes con VIH se describen interacciones con algunos esquemas, por ejemplo con efavirenz y regímenes potenciados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El puntaje de TxGNN es alto (99.87%), pero no hay ningún estudio que demuestre actividad de velpatasvir contra el VHB. Además, el VHB carece de un blanco equivalente a NS5A.
- Toda la evidencia disponible es sobre hepatitis C. La única señal relacionada con VHB es un riesgo de seguridad (reactivación), no un beneficio terapéutico.
- Las otras predicciones del modelo (hepatitis E, hepatitis A, VIH, entre otras) también quedan en Hold, con evidencia L4 o L5.

**Para avanzar se necesita:**
- Datos de actividad antiviral in vitro de velpatasvir frente al VHB (líneas celulares con replicación viral).
- Datos detallados del mecanismo de acción y análisis de la relación mecanística con el VHB.
- Prospecto de INVIMA (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Datos de reactivación del VHB con esta combinación y un protocolo de tamizaje y monitoreo (HBsAg, anti-HBc, ADN del VHB) en pacientes coinfectados.
- Seguimiento de los resultados de NCT04997564, el único ensayo con pacientes VHC/VHB.

---
*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

