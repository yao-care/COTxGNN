---
layout: default
title: Velpatasvir
parent: Evidencia Moderada (L3-L4)
nav_order: 655
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Velpatasvir: nueva indicación predicha, Infección por virus de la hepatitis B (nivel de evidencia L4). Indicación original: Sofosbuvir + velpatasvir"
monitor_inn: "VELPATASVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Velpatasvir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Velpatasvir: De Hepatitis C (Sofosbuvir + Velpatasvir) a Infección por Virus de la Hepatitis B

## Resumen en Una Frase

Velpatasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C, utilizado originalmente en la combinación sofosbuvir + velpatasvir para tratar la hepatitis C crónica.
El modelo TxGNN predice que podría ser efectivo para **infección por virus de la hepatitis B**, pero los **5 ensayos clínicos** y **20 publicaciones** asociados se refieren a la hepatitis C, y ninguno demuestra eficacia contra el virus de la hepatitis B.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sofosbuvir + velpatasvir (combinación aprobada en el registro INVIMA; el texto no detalla la enfermedad) |
| Nueva Indicación Predicha | Infección por virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, velpatasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C (VHC) y se usa junto con sofosbuvir, un inhibidor de la polimerasa NS5B, en un régimen pangenotípico de una tableta diaria.

La relación entre ambas indicaciones es débil. Las dos son hepatitis virales, pero el virus de la hepatitis B (VHB) se replica con una maquinaria distinta (transcriptasa inversa/polimerasa) y no tiene un blanco equivalente a NS5A. El puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento entre enfermedades de "hepatitis viral" y no una base mecanística real.

Los estudios recuperados tratan el VHC. El VHB aparece solo como riesgo de reactivación en pacientes coinfectados tratados con antivirales de acción directa (por ejemplo, PMID 31542053), lo cual es un problema de seguridad y no una prueba de eficacia. En el ensayo NCT04997564, el efecto anti-VHB proviene del tenofovir alafenamida (TAF) administrado de forma profiláctica, no de velpatasvir.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | SOF/VEL 12 semanas con TAF profiláctico en coinfección VHC/VHB; aborda la prevención de reactivación del VHB, no el tratamiento del VHB con velpatasvir |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Fase 4 | Desconocido | 25 | Cambio de régimen antirretroviral y tratamiento con SOF/VEL en coinfección VIH-VHC; la actividad anti-VHB proviene de TAF |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Fase 2 | Completado | 40 | Régimen sin interferón (ledipasvir o velpatasvir con sofosbuvir) en linfomas B indolentes asociados al VHC |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Completado | 803 | Proyecto demostrativo de tratamiento simplificado del VHC en Myanmar |
| [NCT07560046](https://clinicaltrials.gov/study/NCT07560046) | Fase 4 | Aún sin reclutar | 1280 | Ensayo aleatorizado por conglomerados de pruebas y tratamiento del VHC en el punto de atención |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Cohorte (ensayo de un solo brazo) | Lancet Gastroenterol Hepatol | Seguridad y eficacia de SOF/VEL en VHC en Ruanda |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohorte | J Clin Exp Hepatol | Sustituciones de resistencia y predictores de fracaso con antivirales de acción directa |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revisión | Eur J Gen Pract | Diagnóstico y tratamiento de la hepatitis C crónica |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revisión | World J Gastroenterol | Manejo de la hepatitis viral pediátrica; el tratamiento del VHB está lejos de ser curativo |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Rep | Reactivación del VHB durante el tratamiento con SOF/VEL para VHC |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Estudio observacional | J Viral Hepat | Estrategia simplificada contra el VHC en Myanmar; los coinfectados con VHB recibieron tenofovir de forma concurrente |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Estudio de vida real | J Virus Erad | Efectividad y seguridad de SOF/VEL en pacientes chinos, incluida coinfección VHC/VHB |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohorte | J Gastroenterol Hepatol | SOF/VEL en VHC genotipo 3 en condiciones reales |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisión | Clin Pharmacokinet | Consideraciones farmacocinéticas y farmacodinámicas del tratamiento del VHC |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Estudio retrospectivo | Klin Mikrobiol Infekc Lek | Tratamiento antiviral de hepatitis B y C en niños en Ostrava |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20126648 (cancelado) | EPCLUSA® | Tableta recubierta | Sofosbuvir + velpatasvir |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 57 interacciones. Entre las principales:
  - **Mayores**: dexametasona y los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol), que pueden reducir la absorción de velpatasvir al disminuir la acidez gástrica.
  - **Moderadas**: antiácidos (hidróxido de aluminio, carbonato de calcio, magaldrato, compuestos de magnesio), antagonistas H2 (cimetidina, famotidina, nizatidina) y naldemedina.
  - **Menores**: fidaxomicina, naloxegol y prucaloprida.
- **Riesgo de reactivación del VHB**: la literatura describe reactivación en pacientes con antecedente de VHB tratados con antivirales de acción directa contra el VHC. Es una consideración clave si se usara en poblaciones con VHB.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Velpatasvir actúa sobre NS5A del VHC y no tiene actividad conocida contra el VHB. El puntaje alto de TxGNN refleja cercanía en la red de conocimiento, y la evidencia disponible se limita a la hepatitis C, sin datos de eficacia contra el VHB. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de velpatasvir, y estudios preclínicos in vitro que evalúen su actividad frente al VHB.
- Información de seguridad completa (advertencias y contraindicaciones) del prospecto de INVIMA.
- Aclarar el estado regulatorio local, dado que el registro está cancelado.
- Los demás candidatos (hepatitis E, hepatitis A, VIH, fiebres hemorrágicas virales y otros) no cuentan con base mecanística ni evidencia directa; se recomienda mantenerlos en espera.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

