---
layout: default
title: Folic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 302
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Folic Acid: nueva indicación predicha, Enfermedad metabólica de la biotina (nivel de evidencia L5). Indicación original: Multivitaminas más hierro"
monitor_inn: "Folic acid"
predicted_indications: ["biotin metabolic disease"]
---

# Folic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Ácido fólico: De Multivitamínicos con Hierro a Enfermedad Metabólica de la Biotina
{: .text-alpha }

## Resumen en Una Frase

El ácido fólico (vitamina B9) se registró en Colombia como parte de un producto multivitamínico con hierro (P-NATAL®).
El modelo TxGNN predice que podría ser efectivo para la **enfermedad metabólica de la biotina**, pero no hay ensayos clínicos y solo se identificaron **20 publicaciones** de apoyo indirecto (en su mayoría revisiones generales sobre vitaminas).

<!-- review:begin co-lic-20261105-folic_acid-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El ácido fólico (vitamina B9) se registró en Colombia como parte de un producto multivitamínico con hierro (P-NATAL®), cuyo registro sanitario hoy está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-folic_acid-1 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas más hierro |
| Nueva Indicación Predicha | Enfermedad metabólica de la biotina |
| Puntaje de Predicción TxGNN | 0.9949 |
| Nivel de Evidencia | L5 (solo predicción del modelo; la literatura es indirecta y no evalúa esta indicación) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 11) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el ácido fólico es una vitamina hidrosoluble del complejo B que actúa como cofactor en el metabolismo de un carbono (síntesis de nucleótidos y metionina). Su uso en Colombia se limitó a un producto multivitamínico con hierro.

La biotina (vitamina B7) también es una vitamina hidrosoluble que actúa como cofactor en reacciones de carboxilación. Existe, por tanto, una conexión biológica general entre ambas: comparten la naturaleza de vitaminas del grupo B y rutas metabólicas cercanas.

Sin embargo, el ácido fólico no corrige los defectos de fondo de la enfermedad metabólica de la biotina (deficiencia de biotinidasa o de holocarboxilasa sintetasa), que se tratan con biotina farmacológica. El puntaje tan alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Esta predicción debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Todas las publicaciones identificadas son de apoyo indirecto: revisiones sobre vitaminas, diabetes, nutrición o estudios preclínicos; ninguna evalúa el ácido fólico en la enfermedad metabólica de la biotina. Se listan las más relevantes (prioridad a revisiones y metaanálisis):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Revisión | Handbook of Clinical Neurology | Trastornos que responden a vitaminas (cobalamina, folato, biotina, B1 y E); describe errores congénitos del metabolismo del folato y la cobalamina |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Revisión | Acta Vitaminologica et Enzymologica | Vitaminas en enfermedades metabólicas: malabsorción, errores del metabolismo y síndromes dependientes de vitaminas |
| [39828265](https://pubmed.ncbi.nlm.nih.gov/39828265/) | 2025 | Revisión paraguas / metaanálisis | Asia Pac J Clin Nutr | Efecto de vitaminas hidrosolubles sobre el control glucémico en diabetes tipo 2; no es específico de la enfermedad de la biotina |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Revisión | Int J Mol Sci | Deficiencia de vitamina B12 y sistema nervioso; menciona la relación entre B12, biotina y folato en reacciones bioquímicas |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Revisión | Cureus | Relación entre vitaminas y diabetes; niveles bajos de tiamina, piridoxina y biotina en personas con diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Revisión | Endocr Metab Immune Disord Drug Targets | Vitaminas y diabetes tipo 2, con hallazgos sobre vitaminas del grupo B |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Revisión | Clinics in Dermatology | Papel de las vitaminas B en el metabolismo celular y la síntesis de eritrocitos |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Revisión | Arch Biochem Biophys | La deficiencia de folato, B12, B6 y otros micronutrientes puede dañar el ADN; propone optimizar la ingesta |
| [38350491](https://pubmed.ncbi.nlm.nih.gov/38350491/) | 2025 | Observacional | Nutrition Reviews | Estado de micronutrientes en niños con desnutrición grave (evidencia indirecta) |
| [16183151](https://pubmed.ncbi.nlm.nih.gov/16183151/) | 2006 | Preclínico (ratas) | Int J Cardiol | El ácido fólico reduce la expresión de VCAM-1 en aorta de ratas con hiperhomocisteinemia |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20098323 | P-NATAL® | Cápsula blanda de gelatina con cubierta entérica | Multivitaminas más hierro |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN asocia al fármaco con varias condiciones de posible precaución, entre ellas enfermedad renal, diabetes mellitus, cetoacidosis diabética, hipercalcemia, nefrolitiasis, hiperparatiroidismo, hemocromatosis hereditaria, hemosiderosis, enfermedad de Wilson, anemia de células falciformes, anemia hemolítica, trastorno bipolar, enfermedad inflamatoria intestinal, colitis ulcerosa, úlcera péptica y sarcoidosis. Estas relaciones pueden reflejar componentes de productos combinados (por ejemplo, hierro, calcio o vitaminas) y no necesariamente el ácido fólico solo; deben verificarse.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total. Las únicas con nivel de gravedad definido son pancrelipasa (moderada) y sulfasalazina (menor). Otras con nivel no determinado incluyen calcitriol, pantoprazol, omeprazol, lansoprazol, metformina, glimepirida, acarbosa, mesalazina, sucralfato, prednisona, simvastatina y vancomicina, entre otras.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo TxGNN (aprendizaje profundo; puntaje alto, pero que puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica), sin ensayos clínicos y con literatura indirecta. Además, el tratamiento establecido de la enfermedad es la biotina, y el medicamento está comercializado en este país con al menos 11 licencias válidas.

<!-- review:begin co-lic-20261112-folic_acid-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "1 licencia válida" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): al menos 11 registros sanitarios vigentes (la lista de los datos está limitada a 20 registros). Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-folic_acid-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank) para evaluar un vínculo mecanístico real
- Advertencias y contraindicaciones del prospecto en INVIMA, imprescindibles antes de un tamizaje de seguridad
- Estudios que evalúen específicamente el ácido fólico en deficiencia de biotinidasa o de holocarboxilasa sintetasa
- Comparación frente al tratamiento estándar (biotina) para determinar si existe algún valor adicional
- Evaluación de la ruta de administración y de la vía regulatoria

<!-- review:begin co-lic-20261105-folic_acid-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluación de la ruta de administración y de la vía regulatoria, dado que no hay producto vigente en Colombia" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-folic_acid-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "cuyo registro sanitario hoy está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay producto vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 1 → al menos 11 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

