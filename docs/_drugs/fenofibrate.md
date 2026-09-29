---
layout: default
title: Fenofibrate
parent: Evidencia Moderada (L3-L4)
nav_order: 197
evidence_level: L4
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Fenofibrato: De Reducción de Colesterol y Triglicéridos a Hipercolesterolemia Familiar Homocigota

## Resumen en Una Frase

El fenofibrato se usa para reducir los niveles de colesterol y triglicéridos en sangre, y en Colombia se comercializa combinado con pravastatina. El modelo TxGNN predice que podría ser efectivo para la **hipercolesterolemia familiar homocigota**.
Esta predicción cuenta con **1 ensayo clínico** (que evalúa otro fármaco, alirocumab, y no fenofibrato) y **10 publicaciones** generales de apoyo, por lo que la evidencia directa es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro. El texto registrado solo indica la composición: "pravastatina y fenofibrato" |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información farmacológica disponible, el fenofibrato es un agonista del receptor PPARα (la actividad reside en su metabolito activo). Reduce sobre todo los triglicéridos y eleva el colesterol HDL, con un efecto moderado y variable sobre el colesterol LDL. El fenofibrato se prescribe con frecuencia en combinación fija con una estatina, y en Colombia figura en un producto con pravastatina.

La hipercolesterolemia familiar homocigota se debe a la ausencia o el defecto grave de la función del receptor de LDL. Por eso, un beneficio sobre el LDL-C con un fármaco que actúa vía PPARα es biológicamente débil. El eje que domina esta enfermedad (receptor de LDL y PCSK9) no es el blanco del fenofibrato.

El puntaje TxGNN es muy alto (0.999), pero refleja la cercanía en el grafo entre nodos de trastornos lipídicos, no evidencia específica del fenofibrato. Un papel plausible sería limitado, por ejemplo como complemento ante hipertrigliceridemia residual, y siempre junto a la terapia de primera línea.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Estudio abierto de alirocumab (75 o 150 mg cada 2 semanas) sobre el LDL-C en niños y adolescentes de 8 a 17 años con HoFH. El fenofibrato no es la intervención, por lo que no aporta evidencia directa |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Estudio clínico | Pharmacol Res Commun | 22 pacientes con hiperlipoproteinemia tipo II tratados con fenofibrato 300 mg/día: colesterol total −22% y LDL −24%. Un paciente con HoFH mostró la mayor caída, pero es un caso único |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Revisión | Indian Heart J | Fármacos hipolipemiantes no estatínicos. La indicación más definida del fenofibrato en monoterapia es la triglicéridos en ayunas >500 mg/dl |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Revisión | Intern Med J | Trasplante hepático en HoFH ante terapias hipolipemiantes emergentes. No evalúa fenofibrato |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Estudio farmacocinético de interacciones | Pharmacotherapy | Efecto de lomitapida (aprobada para HoFH) sobre la farmacocinética de varios hipolipemiantes, entre ellos fenofibrato |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Sin clasificar | Ann N Y Acad Sci | Tratamiento farmacológico y quirúrgico de la dislipidemia en niños. Menciona fenofibrato entre los fármacos que redujeron lipoproteínas aterogénicas, sobre todo en hipercolesterolemia familiar |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Sin clasificar | Curr Atheroscler Rep | Manejo de la dislipidemia en el embarazo. Contexto general |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía | Endocr Pract | Guías de la AACE/ACE para el manejo de la dislipidemia y la prevención cardiovascular |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Revisión | Indian Heart J | LDL-C, estatinas e inhibidores de PCSK9. No trata específicamente el fenofibrato |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Sin clasificar | Pharmacotherapy | Ezetimiba como inhibidor selectivo de la absorción de colesterol. No trata el fenofibrato |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Revisión | Drugs | Farmacología y potencial terapéutico de atorvastatina en hiperlipidemias. No trata el fenofibrato |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20114242 | PRAVAFEN® CAPSULAS (ALTADIS FARMACEUTICA S.A.S.) | Cápsula dura | Pravastatina y fenofibrato (solo se registra la composición) |

Nota: el paquete de evidencia contiene 5 entradas idénticas de este mismo registro. Se muestran como una sola fila. El total informado es de 20 registros sanitarios.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias y contraindicaciones del prospecto de INVIMA aún no están disponibles.

Las dos entradas de "interacciones" del paquete no son interacciones entre fármacos. Corresponden a dianas farmacológicas del fenofibrato (PPARα y la proteína de unión a ácidos grasos 1), por lo que no permiten evaluar el riesgo de interacciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico con fenofibrato en HoFH: el único ensayo vinculado evalúa alirocumab, y la literatura es general. El mecanismo del fármaco (PPARα) no actúa sobre el defecto central de la enfermedad (el receptor de LDL). El puntaje alto de TxGNN refleja proximidad en el grafo, no evidencia propia del fármaco.

**Para avanzar se necesita:**
- Estudios de fenofibrato específicos en HoFH (más allá del caso único de 1984), idealmente como complemento de la terapia estándar
- Prospecto de INVIMA para advertencias y contraindicaciones, hoy sin datos
- Datos del mecanismo de acción desde DrugBank
- Confirmar el texto de indicación aprobada, hoy limitado a la composición del producto combinado
- Como referencia, la misma fuente muestra una señal más sólida para hiperlipoproteinemia (nivel L1, con varios ensayos de Fase 3). Sin embargo, coincide con el uso ya establecido del fármaco y no es un reposicionamiento novedoso
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

