---
layout: default
title: Tapentadol
parent: Solo Predicción del Modelo (L5)
nav_order: 606
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tapentadol: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: Tapentadol"
---

# Tapentadol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tapentadol: De Tapentadol (indicación no detallada en el registro) a Trastorno de Migraña

## Resumen en Una Frase

Tapentadol es un analgésico opioide de acción central, comercializado en Colombia como PALEXIS® RETARD en tabletas de liberación prolongada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero **no hay ensayos clínicos** y solo **2 publicaciones** (asociadas a una predicción secundaria) que no demuestran eficacia.
La predicción se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tapentadol (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, tapentadol es un agonista del receptor opioide mu y un inhibidor de la recaptación de noradrenalina. Su eficacia se ha establecido en dolor, y mecanísticamente podría relacionarse con la migraña mediante la modulación central del dolor.

Sin embargo, este vínculo es solo teórico. Los opioides generalmente **no se recomiendan** para la migraña por el riesgo de cefalea por sobreuso de medicación, cronificación y su menor eficacia frente a triptanes, gepantes y AINE. El puntaje alto de TxGNN (0.997) es una predicción computacional que no cuenta con respaldo clínico.

Las otras predicciones del modelo (migraña con aura del tronco encefálico y susceptibilidad a migraña con o sin aura) siguen el mismo razonamiento. La última es un fenotipo de susceptibilidad genética, no una indicación tratable, por lo que probablemente es un artefacto del mapeo de ontologías. En la migraña con aura del tronco encefálico, las características neurológicas del aura hacen que un mecanismo puramente analgésico sea aún menos adecuado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la predicción principal (trastorno de migraña) no hay literatura disponible. Las únicas publicaciones identificadas corresponden a la predicción "susceptibilidad a migraña con o sin aura" y **no evalúan la eficacia de tapentadol en migraña**:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Revisión | Expert Opin Pharmacother | Analiza si los AINE y el paracetamol pueden sustituir a los opioides en dolor agudo, ante la crisis de sobredosis de opioides |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cohorte | Drug Healthc Patient Saf | Uso concomitante de opioides con triptanes o antidepresivos serotoninérgicos; señala que los opioides no se recomiendan para la migraña y advierte del riesgo de síndrome serotoninérgico |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20049944 | PALEXIS® RETARD 100 MG (cancelado) | Tableta de liberación prolongada | TAPENTADOL |
| 20049941 | PALEXIS® RETARD 150 MG (cancelado) | Tableta de liberación prolongada | TAPENTADOL |

Ambos registros, de GRÜNENTHAL GMBH, están cancelados, por lo que actualmente no hay productos vigentes con este principio activo en los datos compilados.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 120 interacciones en total. Entre las de nivel **Mayor** destacan:
  - Bupropión
  - Morfina
  - Lorcaserina
  - Dietilpropión
  - Dolasetrón
  - Palonosetrón
  - Fentermina

  También hay interacciones de nivel **Moderado** con epinefrina, hiosciamina, atropina, glicopirronio, diciclomina, trospio, naloxona, dronabinol, nabilona y eluxadolina, entre otros.
- **Contexto en migraña**: la literatura señala riesgo de síndrome serotoninérgico al combinar opioides con triptanes o antidepresivos serotoninérgicos (ISRS/IRSN), fármacos de uso frecuente en pacientes con migraña. Además, existe riesgo de cefalea por sobreuso de medicación y de abuso/dependencia.

Consultar el prospecto para información sobre advertencias y contraindicaciones, ya que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni estudios de eficacia. Los opioides no están recomendados para la migraña y existen alternativas establecidas. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA (advertencias y contraindicaciones), una brecha de datos bloqueante para el tamizaje de seguridad.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Evidencia clínica o preclínica que respalde un beneficio de tapentadol en migraña frente a los tratamientos estándar.
- Evaluar el riesgo de cefalea por sobreuso de medicación, dependencia e interacciones serotoninérgicas.
- Definir si existe interés en un producto con registro vigente en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

