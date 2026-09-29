---
layout: default
title: Ciprofibrate
parent: Solo Predicción del Modelo (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Ciprofibrate
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

# Ciprofibrato: De Dislipidemia a Hiperlipoproteinemia

## Resumen en Una Frase

Ciprofibrato es un fibrato (agonista de PPAR-alfa) que se comercializa en Colombia como tabletas de 100 mg, y se usa para tratar dislipidemia, en particular hipertrigliceridemia e hiperlipidemia mixta.
El modelo TxGNN predice que podría ser efectivo para **hiperlipoproteinemia**, con **0 ensayos clínicos registrados** y **19 publicaciones** que respaldan esta dirección.
Esta predicción coincide en la práctica con el uso ya conocido del fármaco, por lo que no constituye un reposicionamiento genuino.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CIPROFIBRATO (el registro sanitario solo indica el nombre del principio activo; según la farmacología, dislipidemia/hipertrigliceridemia) |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 (según el Evidence Pack: estudios clínicos controlados en la literatura, sin ensayos registrados) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la farmacología de la clase, el ciprofibrato es un agonista del receptor PPAR-alfa (gen *PPARA*). Aumenta la actividad de la lipoproteína lipasa, reduce la apoC-III y disminuye la producción hepática de triglicéridos en VLDL. Como resultado baja los triglicéridos y desplaza el LDL hacia partículas más grandes y menos aterogénicas.

La hiperlipoproteinemia es, en la práctica, el uso ya conocido del fármaco. Las guías de la literatura lo describen como eficaz en hipercolesterolemia tipo IIa, hiperlipidemia combinada tipo IIb e hipertrigliceridemia tipo IV. Por eso la predicción de TxGNN es coherente, pero refleja una indicación existente y no una nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8831920](https://pubmed.ncbi.nlm.nih.gov/8831920/) | 1996 | Revisión de eficacia y seguridad | Atherosclerosis | Ciprofibrato 100 mg/día es eficaz en hiperlipoproteinemias tipos IIa, IIb y IV; en unos 3000 pacientes con tipo IIa redujo colesterol total, triglicéridos, apoB y LDL |
| [9015467](https://pubmed.ncbi.nlm.nih.gov/9015467/) | 1996 | Ensayo comparativo abierto | Postgrad Med J | 174 pacientes con hiperlipidemia tipo II; ciprofibrato 100 mg vs bezafibrato de liberación sostenida 400 mg durante 8 semanas |
| [3994783](https://pubmed.ncbi.nlm.nih.gov/3994783/) | 1985 | Ensayo doble ciego comparativo | Atherosclerosis | Ciprofibrato 100 mg/día vs fenofibrato 300 mg/día durante 3 meses; ambos redujeron colesterol total, LDL, VLDL y apoB, y aumentaron HDL y apoA |
| [2289217](https://pubmed.ncbi.nlm.nih.gov/2289217/) | 1990 | Estudio multicéntrico | Clin Ther | 127 pacientes con hiperlipidemia primaria tipos II y IV; 100 mg/día durante 12 semanas con reducción significativa de colesterol, LDL, triglicéridos y apoB, y aumento de HDL |
| [11048518](https://pubmed.ncbi.nlm.nih.gov/11048518/) | 2000 | Estudio clínico multicéntrico | Vnitrni Lekarstvi | 633 pacientes con hiperlipoproteinemia combinada; en 3 meses el colesterol bajó 13%, los triglicéridos más de 41% y el HDL subió 15% |
| [6951582](https://pubmed.ncbi.nlm.nih.gov/6951582/) | 1982 | Estudio dosis-respuesta | Atherosclerosis | 50 pacientes con dosis de 50, 100 y 200 mg/día; el mayor efecto fue con 200 mg, sin efectos adversos subjetivos |
| [12915663](https://pubmed.ncbi.nlm.nih.gov/12915663/) | 2003 | Estudio clínico mecanístico | J Clin Endocrinol Metab | 10 pacientes con tipo IIb; el VLDL-1 bajó 40% y el VLDL-2 25%, con mejor salida de colesterol mediada por HDL |
| [17414592](https://pubmed.ncbi.nlm.nih.gov/17414592/) | 2007 | Estudio clínico | Am J Ther | En dislipidemia tipo IV de Fredrickson, disminuyó el colesterol no-HDL y los triglicéridos, y aumentó el HDL |
| [9364979](https://pubmed.ncbi.nlm.nih.gov/9364979/) | 1997 | Estudio clínico comparativo | Thromb Haemost | Efecto de gemfibrozil y ciprofibrato sobre t-PA, PAI-1 y fibrinógeno en pacientes hiperlipidémicos |
| [3318453](https://pubmed.ncbi.nlm.nih.gov/3318453/) | 1987 | Revisión | Am J Med | Revisión del efecto de los derivados del ácido fíbrico (bezafibrato, ciprofibrato, fenofibrato) sobre lípidos y lipoproteínas |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19986691 | CIPROFIBRATO 100 MG TABLETAS (Laboratorios La Santé S.A.) | Tableta | CIPROFIBRATO (el texto de indicación registrado solo contiene el nombre del principio activo) |

Nota: el Evidence Pack informa 20 registros, pero los cinco listados comparten el mismo número de registro sanitario y los mismos datos, por lo que se muestran una sola vez.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones fármaco-fármaco específicas registradas. La consulta solo devolvió su diana farmacológica (PPAR-alfa). Una revisión sobre los fibratos (PMID 7809177) señala que pueden interactuar con otros medicamentos por su alta unión a proteínas plasmáticas, cambios en la cinética de la vitamina K y la inducción del citocromo P450. Requieren especial atención las estatinas y los anticoagulantes.
- **Riesgos de la clase (medidas de precaución)**: vigilar miopatía, con riesgo de rabdomiólisis en combinación estatina-fibrato (control de CK), y elevación de enzimas hepáticas. Los fibratos son proliferadores de peroxisomas en roedores, con una señal conocida de hepatocarcinogenicidad en ese modelo. Esto aconseja prudencia, aunque no se ha demostrado relevancia en humanos.
- **Perfil biliar**: hay estudios sobre cambios en los lípidos biliares con fibratos, con posible mayor riesgo de litiasis en algunos derivados (PMID 6421601, 3318452).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen numerosos estudios clínicos publicados, incluidos ensayos comparativos y un estudio doble ciego, que muestran la eficacia lipídica del ciprofibrato. Sin embargo, la evidencia es antigua y no hay ensayos registrados. Además, la indicación coincide con su uso ya conocido, así que se trata de una confirmación y no de un hallazgo de reposicionamiento.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones (es un dato bloqueante para el tamizaje de seguridad).
- Confirmar el mecanismo de acción en DrugBank.
- Aclarar la indicación aprobada exacta en los registros sanitarios, porque el texto actual solo dice "CIPROFIBRATO".
- Definir un plan de monitoreo (CK, enzimas hepáticas, interacciones con estatinas y anticoagulantes).
- Otras predicciones del modelo (hiperlipidemia, hiperlipidemia familiar combinada) muestran evidencia similar. Las predicciones sin respaldo clínico (por ejemplo, formas raras de hipercolesterolemia o fibroma de próstata) deben mantenerse en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

