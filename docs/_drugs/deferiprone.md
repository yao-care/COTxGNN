---
layout: default
title: Deferiprone
parent: Evidencia Moderada (L3-L4)
nav_order: 201
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Deferiprone: nueva indicación predicha, Porfiria hepática (nivel de evidencia L4). Indicación original: DEFERIPRONA"
---

# Deferiprone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

# Deferiprona: De Indicación Original (Deferiprona) a Porfiria Hepática

## Resumen en Una Frase

Deferiprona es un quelante oral de hierro, registrado en Colombia bajo el producto IROFIN® 500 mg tabletas recubiertas; en el registro sanitario la indicación aparece únicamente como "DEFERIPRONA", sin más detalle.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**,
pero hasta ahora **no hay ensayos clínicos registrados** y solo se dispone de **2 publicaciones preclínicas** (modelos animales) que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DEFERIPRONA (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes compiladas. Según la información conocida, deferiprona es un quelante oral de hierro; su uso principal se relaciona con la sobrecarga de hierro, y mecanísticamente podría ser aplicable a enfermedades en las que el hierro agrava el daño.

En la porfiria cutánea tardía, el exceso de hierro hepático y el estrés oxidativo dependiente del hierro empeoran la uroporfiria e inhiben la enzima uroporfirinógeno descarboxilasa. Por ello, reducir el hierro es una estrategia terapéutica plausible (la flebotomía ya se usa con este fin). Un estudio en ratones Hfe-/- (PMID 17854053) mostró que la quelación con deferiprona o las dietas deficientes en hierro reducen la acumulación de uroporfirina.

Un estudio de 2020 (PMID 32678895) mostró que la quelación de hierro corrigió la anemia hemolítica y la fotosensibilidad en un modelo de porfiria eritropoyética congénita. Esta es una forma eritropoyética y no estrictamente hepática, por lo que la evidencia es indirecta. El mecanismo es plausible, pero la evidencia es solo preclínica y no hay ensayos en humanos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Estudio preclínico (modelo murino) | Hepatology | En ratones Hfe-/- con porfiria cutánea tarda inducida, la quelación con deferiprona y las dietas deficientes en hierro se compararon como métodos para reducir el hierro hepático y la acumulación de uroporfirina |
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Estudio preclínico (modelo animal) | Blood | La quelación de hierro corrigió la anemia hemolítica y la fotosensibilidad en porfiria eritropoyética congénita |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20218402 (cancelado) | IROFIN® 500 MG TABLETAS RECUBIERTAS | Tableta recubierta | DEFERIPRONA |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas** (se identificaron 100 interacciones; las 20 primeras listadas son de nivel moderado):
- **Antiácidos y sales de calcio, magnesio y aluminio**: carbonato, citrato, acetato, fosfato, gluconato y lactato de calcio; óxido, hidróxido, carbonato, cloruro, citrato, gluconato y sulfato de magnesio; hidróxido de aluminio; magaldrato.
- **Otros agentes**: hierro, caolín, attapulgita y sucralfato.

En general, estos productos pueden unirse a la deferiprona (por quelación de cationes) y reducir su absorción, por lo que conviene separar su administración. Esta recomendación es una inferencia farmacológica general, no proviene de los datos compilados.

No se dispone de datos de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo preclínica (L4), sin ensayos clínicos, y una de las dos publicaciones se refiere a una forma de porfiria distinta (eritropoyética). Además, el único registro sanitario en Colombia está cancelado, y no hay datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), un vacío de datos que bloquea el análisis de seguridad
- Complementar los datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Buscar evidencia clínica en humanos (series de casos o ensayos) en porfiria cutánea tardía
- Aclarar la situación regulatoria: no hay registro vigente en Colombia
- Diseñar un estudio exploratorio con monitoreo de seguridad hematológica, si se decide avanzar

**Otras predicciones del modelo (para referencia):**
- **Talasemia beta con otras manifestaciones** (99.03%, L4): la quelación de hierro en talasemia está bien establecida; es más un uso cercano a la indicación original que un reposicionamiento verdadero. Falta verificarlo con datos de ECA primarios.
- **Deficiencia de piruvato quinasa de glóbulos rojos** (99.15%, L5): la quelación podría ser un apoyo plausible ante la sobrecarga secundaria de hierro, sin evidencia en este conjunto de datos.
- Las demás predicciones (hipertensión portal no cirrótica familiar de inicio temprano, cirrosis asociada a cobre idiopática, síndrome hepatopulmonar, trombosis portal primitiva, esclerosis hepatoportal, piropoiquilocitosis hereditaria) no tienen vínculo mecanístico claro ni evidencia, por lo que se recomienda mantenerlas en espera (Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

