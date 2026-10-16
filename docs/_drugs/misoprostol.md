---
layout: default
title: Misoprostol
parent: Evidencia Moderada (L3-L4)
nav_order: 450
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Misoprostol: nueva indicación predicha, Amenorrea (nivel de evidencia L4). Indicación original: Misoprostol"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Misoprostol: De Indicación Original (Misoprostol, según registro INVIMA) a Amenorrea

## Resumen en Una Frase

Misoprostol es un análogo de la prostaglandina E1, registrado en Colombia en tabletas de 200 mcg; el registro sanitario disponible no detalla la indicación aprobada más allá del nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero no hay **ensayos clínicos** registrados y las **7 publicaciones** recuperadas tratan sobre terminación del embarazo, sangrado uterino anormal y una complicación del embarazo, no sobre el tratamiento de la amenorrea.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Misoprostol (el registro no especifica una indicación clínica) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin comercialización vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según la información conocida, misoprostol es un análogo de la prostaglandina E1 que induce contracciones uterinas y maduración cervical. Su uso establecido en la evacuación uterina (aborto retenido, aborto médico temprano combinado con mifepristona) se relaciona con la amenorrea propia del embarazo, no con el tratamiento de la amenorrea como trastorno primario.

La literatura recuperada trata sobre terminación del embarazo, sangrado uterino anormal y una complicación hepática del embarazo, por lo que el vínculo con la amenorrea es indirecto. En esos estudios, la amenorrea aparece como criterio de inclusión (por ejemplo, embarazos de ≤35 días de amenorrea) y no como la condición tratada.

El puntaje alto de TxGNN (99.64%) probablemente refleja la cercanía en la red de conocimiento con condiciones del sistema reproductivo, y no un efecto terapéutico demostrado. Mecanísticamente, misoprostol podría usarse para inducir sangrado por privación o evacuar productos retenidos en amenorreas secundarias de causa gestacional, pero esto no cuenta con respaldo directo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECA | Reproductive Sciences | 744 mujeres con embarazo ultratemprano (amenorrea ≤35 días): mifepristona en dosis baja con misoprostol autoadministrado para aborto médico; se evaluó eficacia, seguridad y aceptabilidad |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECA (dosis-respuesta) | Reproductive Sciences | 2500 mujeres con embarazo ultratemprano; mifepristona de 150 a 50 mg seguida de 200 µg de misoprostol oral; criterio principal: aborto completo sin cirugía |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Estudio clínico/cohorte | Human Reproduction | Mifepristona en dosis baja con misoprostol antes de la menstruación esperada para prevenir embarazos no deseados |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Estudio clínico prospectivo | J Obstet Gynaecol Res | Seguridad y eficacia de mifepristona en dosis baja con misoprostol autoadministrado para terminar embarazo temprano |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisión | BMJ | Manejo médico del aborto retenido y del embarazo anembrionario |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Can | Ablación endometrial en el manejo del sangrado uterino anormal |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Reporte de caso | Cureus | Hígado graso agudo del embarazo; la amenorrea aparece solo como síntoma de presentación |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189624 (cancelado) | MISO-CARE 200 MCG TABLETA | Tableta (oral) | MISOPROSTOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia misoprostol con las siguientes condiciones:
  - Cardiovasculares: hipertensión, insuficiencia cardíaca congestiva, infarto de miocardio, trombosis coronaria, accidente cerebrovascular, infarto cerebral, trastornos cerebrovasculares y enfermedad cardiovascular en general.
  - Hepáticas y digestivas: insuficiencia hepática, enfermedad hepática, lesión hepática inducida por fármacos, enfermedad de la vesícula biliar, enfermedad inflamatoria intestinal y úlcera péptica activa.
  - Hematológicas: trastornos de la coagulación, hemoglobinopatías y anemia (incluida la macrocítica).
  - Otras: asma (intrínseco y alérgico), abuso o dependencia de sustancias y meningitis no infecciosa.
- **Interacciones farmacológicas** (se consultaron 100 interacciones; se listan las principales):
  - **Mayor**: dinoprostona (tópica).
  - **Moderada**: óxido de magnesio, hidróxido de magnesio, carbonato de magnesio, magaldrato y quinapril.
  - **Menor**: citrato de sodio, hidróxido de aluminio, carbonato de calcio, bicarbonato de sodio y naproxeno.
  - Los antiácidos con magnesio son los más frecuentes en la lista.
- **Riesgo teratogénico**: misoprostol se asocia con malformaciones congénitas tras exposición intrauterina. Esto es especialmente relevante en cualquier uso en mujeres en edad fértil con amenorrea, donde debe descartarse el embarazo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es principalmente computacional: no hay ensayos clínicos y la literatura recuperada no estudia misoprostol como tratamiento de la amenorrea. Además, el único registro sanitario en Colombia está cancelado y hay preocupaciones de seguridad, incluida la teratogenicidad.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para conocer advertencias y contraindicaciones oficiales.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la literatura para identificar estudios que evalúen misoprostol específicamente como tratamiento de la amenorrea.
- Evaluar la viabilidad regulatoria, dado que no hay registro vigente en Colombia.
- Definir un plan de seguridad que contemple la exclusión del embarazo y los riesgos cardiovasculares y hepáticos señalados.

---

**Nota sobre la segunda predicción (coartación atípica de la aorta):** el puntaje de TxGNN es 99.30%, pero no hay ensayos ni literatura (nivel L5) y no se identifica un mecanismo plausible. La coartación es una anomalía estructural de tratamiento quirúrgico o por cateterismo. La asociación probablemente se debe al uso de alprostadil (PGE1), un fármaco distinto, para mantener el conducto arterioso. Se recomienda **Hold**.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

