---
layout: default
title: Amiodarone
parent: Evidencia Moderada (L3-L4)
nav_order: 49
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
description: "Amiodarone: nueva indicación predicha, Catecholaminergic polymorphic ventricular tachycardia (nivel de evidencia L4). Indicación original: AMIODARONA"
---

# Amiodarone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Amiodarone: Catecholaminergic polymorphic ventricular tachycardia
{: .text-alpha }

## Resumen en Una Frase

Amiodarona es un antiarrítmico multicanal registrado en Colombia (Cordarone®, entre otros) cuya indicación aprobada figura en los registros únicamente como "AMIODARONA", sin detalle clínico adicional.
El modelo TxGNN predice que podría ser efectivo para **taquicardia ventricular polimórfica catecolaminérgica (CPVT)**, pero **no hay ensayos clínicos** y solo hay **9 publicaciones** (casos clínicos, series pequeñas y revisiones generales) que no respaldan específicamente el uso de amiodarona.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AMIODARONA |
| Nueva Indicación Predicha | Catecholaminergic polymorphic ventricular tachycardia |
| Puntaje de Predicción TxGNN | 0.9978 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | 4 (los 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, amiodarona es un bloqueador multicanal (potasio, sodio, calcio) con antagonismo beta-adrenérgico. En teoría, esto podría suprimir arritmias ventriculares desencadenadas por estímulo adrenérgico, que es el desencadenante característico de la CPVT.

Sin embargo, la CPVT se origina por una fuga de calcio mediada por mutaciones en RYR2 o CASQ2. El tratamiento de primera línea son los betabloqueadores junto con flecainida. La literatura recuperada consiste en casos clínicos, series pequeñas y revisiones generales, sin datos controlados que respalden específicamente a la amiodarona. El vínculo mecanístico es, por tanto, plausible pero débil.

**Otras indicaciones predichas (para contexto):** el modelo también generó otras predicciones con mayor respaldo o con evidencia nula:
- **Taquicardia ventricular** (puntaje 0.9964, nivel L1, Proceed with Guardrails): la evidencia es sólida (AVID, ALPS, PROCAMIO), pero es una indicación ya establecida clínicamente, más una confirmación que un reposicionamiento propiamente dicho.
- **Taquicardia ventricular incesante infantil** (0.9965, nivel L2): existe un ensayo aleatorizado doble ciego de amiodarona intravenosa en taquiarritmias incesantes pediátricas (PMID 16316969), aunque con población mixta.
- Artritis reumatoide, gota, tricotilomanía y otras (nivel L5): sin respaldo y sin vínculo mecanístico plausible.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para CPVT.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revisión sistemática | Life (Basel) | Características clínicas, hallazgos genéticos y desenlaces arrítmicos de pacientes con CPVT en China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte retrospectiva | Rev Cardiovasc Med | Características clínicas, base genética y costos sanitarios de la CPVT en una ciudad china |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento farmacológico de arritmias ventriculares |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Caso clínico | PACE | Flecainida suprime las tormentas inducidas por desfibrilador en CPVT (no es amiodarona) |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Caso clínico | Turk Pediatri Arsivi | Paro cardíaco súbito en un niño de 2 años con CPVT |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Caso clínico | Medicine | Diagnóstico tardío de CPVT con mutación RYR2 en un niño de 9 años |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Caso clínico | Front Cardiovasc Med | Resolución de CPVT con denervación simpática cardíaca derecha en un adolescente |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Caso clínico | BMJ Case Reports | Supervivencia de un niño con paro cardíaco extrahospitalario y dilema diagnóstico |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Caso clínico | Anesth Analg | Neonato con síndrome de QT largo y arritmias refractarias tratado con lidocaína, esmolol y amiodarona |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 52270 | CORDARONE® 200 MG TABLETA | Tableta | AMIODARONA | Vigente |
| 45892 | AMIODARONA 200MG TABLETA | Tableta | AMIODARONA | Vigente |
| 52271 | CORDARONE INYECTABLE | Solución inyectable | AMIODARONA | Vigente |
| 19992832 | AMIODARONA CLORHIDRATO 150 MG/3ML | Solución inyectable | AMIODARONA | Vigente |

Los cuatro registros están cancelados; no hay registros vigentes en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento TxGNN, no según el prospecto):** síndrome de QT largo (incluido el familiar), torsades de pointes, bloqueo auriculoventricular, síndrome del seno enfermo, enfermedad hepática y daño hepático inducido por fármacos, hipotiroidismo e hipertiroidismo (incluidos enfermedad de Graves y tirotoxicosis), enfermedad pulmonar intersticial, neumonía eosinofílica, neumonitis por hipersensibilidad, neuritis óptica y enfermedades del nervio óptico, neuropatía periférica, depósitos corneales, deficiencia de potasio y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas:** se identificaron **355 interacciones**. Entre las de nivel mayor figuran: cisaprida, claritromicina, dolasetrón, eliglustat, clotrimazol, dexametasona, hidrocortisona, agalsidasa beta y las formulaciones de anfotericina B. Entre las moderadas: famotidina, cimetidina, aprepitant, bisacodilo y budesonida.
- **Toxicidad documentada en la literatura:** toxicidad pulmonar, disfunción tiroidea, efectos hepáticos, prolongación del QT y efectos proarrítmicos y hemodinámicos.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para CPVT solo hay predicción del modelo y literatura de baja calidad (casos clínicos y series pequeñas), sin ensayos clínicos. La terapia de primera línea (betabloqueadores más flecainida) está bien establecida, y el perfil de toxicidad de la amiodarona y sus contraindicaciones (QT largo, bloqueo AV) hacen poco favorable el balance. Además, los cuatro registros colombianos están cancelados.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto en INVIMA para obtener advertencias y contraindicaciones oficiales.
- Obtener datos del mecanismo de acción desde DrugBank.
- Revisar estudios comparativos de amiodarona frente a betabloqueadores y flecainida en CPVT.
- Verificar la situación regulatoria actual: el medicamento está comercializado, con 4 registros vigentes en Colombia.
- Si se busca una alternativa con mayor respaldo, evaluar la indicación de **taquicardia ventricular** (L1, Proceed with Guardrails), considerando que ya es una indicación clínica establecida y requeriría barreras de seguridad: monitoreo tiroideo, hepático, pulmonar y del QT, además de revisión de interacciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

