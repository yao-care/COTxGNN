---
layout: default
title: Gemfibrozil
parent: Evidencia Moderada (L3-L4)
nav_order: 312
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Gemfibrozil: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L4). Indicación original: GEMFIBROZIL"
monitor_inn: "gemfibrozil"
predicted_indications: ["rheumatoid arthritis", "multiple endocrine neoplasia", "HIV infectious disease", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "methemoglobinemia, alpha type", "sclerosing cholangitis", "methemoglobin reductase deficiency"]
---

# Gemfibrozil
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

# Gemfibrozilo: De Dislipidemia a Artritis Reumatoide

## Resumen en Una Frase

Gemfibrozilo es un fibrato (agonista de PPAR-alfa) registrado en Colombia bajo el nombre del principio activo, utilizado originalmente como hipolipemiante. El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero **no hay ensayos clínicos** y solo **4 publicaciones** indirectas o preclínicas respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | GEMFIBROZIL (el registro sanitario no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, gemfibrozilo es un agonista de PPAR-alfa de la clase de los fibratos, y su eficacia en la regulación de lípidos (reducción de triglicéridos y aumento de HDL) está bien establecida.

La relación con la artritis reumatoide es indirecta. La activación de PPAR tiene efectos antiinflamatorios e inmunomoduladores, incluida la modulación de respuestas de linfocitos T y de la producción de citocinas, lo que es plausible en una artritis autoinmune. Sin embargo, la indicación original (trastornos lipídicos) y la artritis reumatoide son enfermedades muy distintas, y el vínculo se apoya únicamente en el mecanismo.

El respaldo disponible es limitado: un estudio preclínico con bezafibrato (un agonista pan-PPAR, no gemfibrozilo) en artritis experimental, y un estudio de 2019 en ratas que combina gemfibrozilo con una dosis reducida de esteroide. El diseño y la solidez de este último no pueden confirmarse solo con el título.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclínico (modelo en rata; diseño no verificado) | Modern Rheumatology | Gemfibrozilo combinado con una dosis reducida de esteroide en artritis inducida por adyuvante en ratas; evalúa si logra un control similar al de la dosis completa de esteroide |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclínico (fibrato relacionado) | International Immunopharmacology | Bezafibrato, agonista pan-PPAR, atenuó la artritis reumatoide experimental mediante modulación de vías inflamatorias dependientes de PPAR, con énfasis en PPAR-γ |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclínico (mecanístico) | Journal of Immunology | Estudio sobre la regulación de Foxp3 en linfocitos T reguladores por óxido nítrico; relevancia indirecta para autoinmunidad |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Revisión | American Journal of Clinical Dermatology | Revisión sobre eritema palmar y sus causas fisiológicas y sistémicas; relación indirecta con el tema |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 36269 (cancelado) | GEMFIBROZILO 600MG TABLETAS | Tableta recubierta | GEMFIBROZIL |
| 22877 (cancelado) | LOPID® TABLETAS 600MG | Tableta recubierta | GEMFIBROZIL |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, colelitiasis, colecistolitiasis, coledocolitiasis, colangitis biliar primaria, trombocitopenia, anemia (incluida la macrocítica), leucopenia, insuficiencia renal y síndrome de Reynolds.
- **Interacciones farmacológicas**: se registraron 129 interacciones. Entre las de nivel **mayor** figuran:
  - Estatinas: rosuvastatina y simvastatina
  - Antidiabéticos: pioglitazona y repaglinida
  - Antidiarreicos: eluxadolina y loperamida

  También hay interacciones de nivel moderado con insulinas, nateglinida, rosiglitazona, clorpropamida, tolazamida, rifaximina y ácido quenodesoxicólico.

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de artritis reumatoide solo cuenta con respaldo preclínico y mecanístico, sin ensayos clínicos ni estudios en humanos. Además, los dos registros sanitarios en Colombia están cancelados y existe un perfil amplio de interacciones y contraindicaciones.

**Para avanzar se necesita:**
- Estudios preclínicos que confirmen la eficacia de gemfibrozilo específicamente (no solo de otros fibratos) en modelos de artritis
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales)
- Evaluación del riesgo de interacciones, en particular con estatinas y antidiabéticos, en pacientes con artritis reumatoide
- Resolver la situación regulatoria, ya que no hay registro sanitario vigente en Colombia

---

### Nota sobre otras indicaciones predichas

Los datos compilados muestran candidatos con más respaldo que artritis reumatoide, ambos con nivel de evidencia **L2** y recomendación de pregunta de investigación:

- **Infección por VIH (nivel L2):** el uso sería el manejo de la dislipidemia asociada a antirretrovirales, no el tratamiento de la infección. Incluye un ensayo aleatorizado doble ciego (PMID 12409741) en hipertrigliceridemia asociada a inhibidores de proteasa y un estudio de metformina o gemfibrozilo en lipodistrofia (PMID 14640387). Hay un ensayo clínico de Fase 1 completado (NCT00039663), solo de relevancia indirecta. Requiere atención por las interacciones con estatinas y antirretrovirales.
- **Hipoalfalipoproteinemia (nivel L2):** hay varios ensayos cruzados pequeños y antiguos con gemfibrozilo frente a lovastatina o niacina (PMID 2810673, 10716466, 8267492), centrados en parámetros lipídicos. Esta indicación es cercana a su uso lipídico actual.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

