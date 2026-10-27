---
layout: default
title: Albendazole
parent: Evidencia Alta (L1-L2)
nav_order: 32
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-14
description: "Albendazole: nueva indicación predicha, Equinococosis alveolar (nivel de evidencia L2). Indicación original: ALBENDAZOL"
monitor_inn: "Albendazole"
predicted_indications: ["alveolar echinococcosis", "coenurosis", "Cestode infectious disease"]
---

# Albendazole
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **3** 
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

## Albendazol: De Antiparasitario (ALBENDAZOL) a Equinococosis Alveolar
{: .text-alpha }

## Resumen en Una Frase

Albendazol es un antiparasitario del grupo de los benzimidazoles, registrado en Colombia con la indicación genérica "ALBENDAZOL" (sin detalle de la indicación aprobada).
El modelo TxGNN predice que podría ser efectivo para **equinococosis alveolar**,
con **3 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ALBENDAZOL (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Equinococosis alveolar |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 7 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Albendazol se une a la beta-tubulina del parásito e inhibe la polimerización de los microtúbulos. Esto altera la captación de glucosa y la integridad celular de las larvas de *Echinococcus multilocularis*. Es el mismo mecanismo antihelmíntico en el que se basa su uso establecido en la equinococosis quística.

La equinococosis alveolar y la quística son enfermedades causadas por larvas de cestodos del género *Echinococcus*. Albendazol ya es el tratamiento parasitostático estándar de la forma alveolar. Por eso, el puntaje alto del modelo es coherente con la práctica clínica actual y **no representa una señal de reposicionamiento novedosa**.

Hay una limitación importante: la literatura indica que, en la equinococosis alveolar, los benzimidazoles no parecen ser parasiticidas *in vivo*. Por ello, el tratamiento suele ser prolongado y se combina con cirugía cuando es posible.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Fase 2 | Completado | 194 | Albendazol en equinococosis alveolar en etapa temprana (Kirguistán). Es la evidencia directa más sólida del conjunto |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completado | 50 | Marcadores de viabilidad del parásito para el seguimiento de pacientes tratados con albendazol. No es un ensayo de eficacia |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Desconocido | 24 | ECA de albendazol adyuvante tras resección de quiste hidatídico pulmonar (forma quística, relevancia indirecta) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Revisión | Acta Tropica | Consenso de expertos para el diagnóstico y tratamiento de la equinococosis quística y alveolar |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Revisión | Clinical Microbiology Reviews | Avances del siglo XXI en genética, diagnóstico y tratamiento de la equinococosis |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Revisión | Tidsskr Nor Laegeforen | Resección quirúrgica combinada con tratamiento prolongado en la enfermedad alveolar |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revisión | World J Gastroenterol | Manejo actual de la equinococosis hepática; la cirugía es la base del tratamiento |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Revisión | Parasite | Albendazol y mebendazol como opciones actuales y búsqueda de alternativas |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Revisión | Acta Tropica | Ninguna opción no quirúrgica ha reemplazado aún a albendazol y mebendazol |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Estudio observacional | J Antimicrob Chemother | Comparación de mebendazol y albendazol a largo plazo en 35 pacientes con equinococosis alveolar |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Revisión | Parasitology | Albendazol no es parasiticida y puede causar efectos adversos graves; se propone reposicionar piroaridina |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclínico | Antimicrob Agents Chemother | Metabolismo y farmacología de formulaciones solubilizadas de albendazol en ratas con equinococosis alveolar |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Revisión | Chin J Schisto Control | Avances en el uso de albendazol para la equinococosis alveolar |

---

## Información de Mercado en Colombia

Los siete registros sanitarios están **cancelados**; actualmente no hay productos vigentes con albendazol en los datos compilados.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19973311 | Albendazol 200 mg tableta (Pentacoop) | Tableta | ALBENDAZOL |
| 20119849 | Albendazol 2% suspensión (Coopidrogas) | Suspensión oral | ALBENDAZOL |
| 29497 | Rotopar suspensión (Chalver) | Suspensión oral | ALBENDAZOL |
| 19929550 | Albendazol 200 mg (American Generics) | Tableta recubierta | ALBENDAZOL |
| 19928206 | Albendazol suspensión (American Generics) | Suspensión oral | ALBENDAZOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no son texto de prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, neutropenia, agranulocitosis, anemia (incluida la macrocítica), pancitopenia y anemia aplásica.
- **Interacciones farmacológicas:** se registraron 96 interacciones. Entre las de nivel moderado figuran aprepitant, cobicistat, deferasirox, yoduro I-123 e I-131, fostamatinib, alemtuzumab, amprenavir, anagrelida, apalutamida, bendamustina, bexaroteno, binimetinib, boceprevir y bosentán. Entre las de nivel menor figuran cimetidina, dexametasona, lidocaína y armodafinilo.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 2 completado (n=194) que prueba albendazol directamente en equinococosis alveolar temprana, además de abundante literatura que respalda su uso como tratamiento parasitostático estándar. La predicción coincide con la práctica clínica establecida y no constituye un reposicionamiento novedoso. Además, no hay productos vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones oficiales
- Completar los datos del mecanismo de acción desde DrugBank
- Verificar si existe algún producto con albendazol vigente en Colombia, o iniciar un nuevo registro
- Plan de monitoreo de hemograma y función hepática, por las contraindicaciones del grafo de conocimiento
- Revisar las interacciones farmacológicas relevantes antes de prescribir
- Confirmar la adecuación de la duración y la dosis del tratamiento prolongado, dado que el fármaco no es parasiticida en la forma alveolar

---

## Otras Indicaciones Predichas (Referencia)

- **Coenurosis** (puntaje 99.83%, nivel L1): los ensayos de Fase 3 son sobre neurocisticercosis, una enfermedad relacionada pero distinta, por lo que respaldan el efecto de clase y no la coenurosis directamente.
- **Enfermedad infecciosa por cestodos** (puntaje 99.74%, nivel L1): categoría general que incluye usos ya establecidos (hidatidosis y neurocisticercosis), por lo que refleja la práctica actual y no un reposicionamiento novedoso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

