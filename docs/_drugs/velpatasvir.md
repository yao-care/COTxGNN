---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: De Hepatitis C Viral Crónica a Infección por Virus de Hepatitis B

## Resumen en Una Frase

Velpatasvir es un inhibidor altamente selectivo de la proteína NS5A del virus de la hepatitis C (VHC), aprobado internacionalmente como componente de las combinaciones sofosbuvir/velpatasvir (Epclusa®) y sofosbuvir/velpatasvir/voxilaprevir (Vosevi®) para el tratamiento de la hepatitis C crónica de todos los genotipos.
El modelo TxGNN predice que podría ser efectivo para la **Infección por Virus de Hepatitis B (VHB)**, con **26 ensayos clínicos** y **20 publicaciones** identificadas; sin embargo, la totalidad de esta evidencia corresponde a estudios dirigidos al VHC, sin ningún dato de eficacia directa contra el VHB.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis C viral crónica (contexto clínico; sin registro en Colombia) |
| Nueva Indicación Predicha | Infección por Virus de Hepatitis B |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Velpatasvir es un inhibidor de segunda generación de la proteína NS5A del VHC, un componente estructural esencial del complejo de replicación viral. Al bloquear esta proteína, velpatasvir impide la formación del complejo replicativo y la ensamblaje de nuevas partículas virales. Combinado con sofosbuvir (inhibidor de NS5B), logra tasas de respuesta virológica sostenida superiores al 95% en todos los genotipos del VHC, lo que lo convierte en uno de los antivirales de acción directa más eficaces disponibles.

La base mecanística para su aplicación en la infección por VHB es, sin embargo, extremadamente débil. El VHB pertenece a la familia Hepadnaviridae y replica su ADN circular parcialmente bicatenario mediante transcripción inversa — un mecanismo completamente distinto al del VHC, que es un virus ARN monocatenario de sentido positivo. El genoma del VHB no codifica ninguna proteína homóloga al NS5A del VHC ni posee un dominio de unión equivalente sobre el cual velpatasvir pueda ejercer su acción inhibidora. No existe ninguna base estructural o funcional conocida para la actividad antiviral cruzada.

La revisión de los 26 ensayos clínicos y 20 publicaciones identificados confirma esta limitación de forma contundente: todos los estudios tienen el VHC como indicación primaria. El VHB aparece únicamente en dos contextos: (1) como comorbilidad en pacientes con coinfección VHC/VHB que reciben profilaxis con tenofovir para prevenir la reactivación del VHB durante el tratamiento del VHC, y (2) como señal de seguridad en forma de reactivación del VHB tras el inicio de antivirales de acción directa para VHC. La predicción de TxGNN probablemente refleja la proximidad semántica entre los nodos "hepatitis B" y "hepatitis C" en el grafo de conocimiento biomédico, no un vínculo terapéutico real.

---

## Evidencia de Ensayos Clínicos

De los 26 ensayos identificados, ninguno evalúa la eficacia de velpatasvir contra el VHB como objetivo terapéutico primario. Se presentan los más relevantes en el contexto de coinfección o monitoreo de VHB:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | SOF/VEL + profilaxis con TAF en pacientes con coinfección VHC/VHB de genotipos 1-6; diseño orientado a prevenir reactivación del VHB, no a tratar el VHB directamente |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completado | 33.808 | Gran estudio observacional de seguridad de antivirales de acción directa (n=33.808); monitorea la reactivación del VHB como evento adverso durante el tratamiento del VHC, no como diana de eficacia |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Fase 4 | Completado | 281 | SOF/VEL/VOX + ribavirina en retratamiento de VHC crónico sin respuesta previa; población puede incluir coinfectados con VHB, pero el punto primario es la RVS del VHC |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Fase 3 | Completado | 222 | Tratamiento de infección reciente por VHC con SOF/VEL en usuarios de drogas inyectables y coinfectados con VIH; sin datos de VHB |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Fase 1 | Completado | 15 | Interacción farmacocinética de SOF/VEL/VOX con anticonceptivos hormonales; población con VHC, sin relación con VHB |

> ⚠️ **Advertencia metodológica**: La totalidad de los 26 ensayos identificados fue diseñada para el tratamiento del VHC. El VHB no figura como hipótesis de eficacia en ninguno de ellos.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Reports | Reactivación del VHB sostenida por mutante de escape inmune del HBsAg en paciente anti-HBc positivo durante tratamiento con SOF/VEL para VHC; representa una señal de seguridad, no de eficacia antiVHB |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Cohorte real | J Virus Eradication | Efectividad de SOF/VEL en pacientes chinos con VHC, incluyendo subgrupo con coinfección VHC/VHB; los datos de VHB se limitan al monitoreo de reactivación |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Cohorte real | Lancet Gastroenterol Hepatol | SOF/VEL para VHC genotipo 4 naïve en Ruanda (SHARED-3); SVR12 elevada; sin datos de VHB |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Ensayo brazo único | Lancet Gastroenterol Hepatol | SOF/VEL/VOX para retratamiento de VHC GT4 con falla previa a DAA en Ruanda; sin datos de VHB |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohorte real | J Gastroenterol Hepatol | SOF/VEL en cohorte real de VHC genotipo 3 con cirrosis y coinfección; el VHB aparece como comorbilidad, sin análisis de eficacia antiVHB |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Estudio descriptivo | Cureus | Eficacia de SOF/VEL en pacientes con VHC e insuficiencia renal crónica; sin datos de VHB |
| [32405174](https://pubmed.ncbi.nlm.nih.gov/32405174/) | 2020 | Cohorte clínica | J Clin Exp Hepatol | SOF/VEL en enfermedad renal terminal y trasplante renal con VHC; sin datos de VHB |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Cohorte clínica | J Viral Hepatitis | Resultados de tratamiento simplificado con SOF/VEL para VHC en Myanmar; pacientes coinfectados con VHB tratados concurrentemente con tenofovir, no con velpatasvir |

---

## Información de Mercado en Colombia

Velpatasvir no cuenta con ningún registro sanitario vigente ante el INVIMA. No se encuentran presentaciones comercializadas en Colombia bajo esta sustancia activa, ni como producto único ni como parte de combinaciones a dosis fijas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Velpatasvir carece de base mecanística para actuar sobre el VHB: su diana específica (NS5A) no tiene homólogo en el genoma del VHB. Los 26 ensayos clínicos y 20 publicaciones identificadas corresponden íntegramente a estudios del VHC, donde el VHB aparece únicamente como señal de seguridad (riesgo de reactivación) o como comorbilidad que requiere manejo paralelo con antivirales específicos (tenofovir/entecavir). No existe ningún dato de eficacia antiviral directa de velpatasvir frente al VHB.

**Para avanzar se necesita:**
- Datos de actividad in vitro de velpatasvir frente al VHB (modelos HepG2.2.15 u otros sistemas de replicación del VHB)
- Datos completos del mecanismo de acción (MOA) desde DrugBank para evaluar posibles efectos pleiotrópicos no relacionados con NS5A
- Estudios de estructura comparada entre NS5A del VHC y proteínas equivalentes del ciclo replicativo del VHB (proteína core, polimerasa viral) para descartar o confirmar actividad cruzada residual
- Análisis regulatorio de INVIMA si se contempla en el futuro el registro de velpatasvir en Colombia para su indicación aprobada (VHC)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

