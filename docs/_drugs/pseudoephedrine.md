---
layout: default
title: Pseudoephedrine
parent: Solo Predicción del Modelo (L5)
nav_order: 543
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Pseudoephedrine: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L4). Indicación original: Combinaciones de paracetamol excluyendo psicolépticos"
monitor_inn: "pseudoephedrine"
predicted_indications: ["nasal cavity disease", "allergic urticaria"]
---

# Pseudoephedrine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Pseudoefedrina: De Combinaciones Antigripales a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

La pseudoefedrina es un descongestionante simpaticomimético que, en Colombia, se registró en productos combinados (con paracetamol) para el tratamiento sintomático de cuadros gripales.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, pero **no hay ensayos clínicos registrados** y solo hay **7 publicaciones** (una revisión, un estudio farmacológico comparativo y varios modelos animales) que apoyan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones de paracetamol excluyendo psicolépticos |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 0.9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico general, la pseudoefedrina es un simpaticomimético indirecto: libera norepinefrina y estimula los receptores alfa-adrenérgicos de los vasos de la mucosa nasal, lo que produce vasoconstricción y reduce la inflamación de la mucosa. Es un mecanismo plausible y bien establecido para la congestión nasal.

La congestión nasal ya es el uso principal conocido de la pseudoefedrina y de sus combinaciones antigripales. Por ello, esta predicción se acerca más a una **confirmación de una indicación existente** que a un reposicionamiento genuino. El puntaje alto del modelo (0.9975) es coherente con esa farmacología.

Cabe señalar que el respaldo disponible es limitado: una revisión sobre rinitis no alérgica (2012), un estudio comparativo de descongestionantes orales y tópicos (fenilpropanolamina vs. d-pseudoefedrina, 2001) y varios modelos animales (perro y gato) de congestión nasal.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Revisión | Allergy Asthma Proc | Capítulo sobre rinitis no alérgica: síntomas de congestión, rinorrea y estornudos, con causas inflamatorias y no inflamatorias |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Estudio farmacológico comparativo | Am J Rhinol | Compara el efecto descongestionante oral y tópico de fenilpropanolamina y d-pseudoefedrina mediante rinometría acústica |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Modelo animal (gato) | Am J Rhinol Allergy | Loratadina y montelukast combinados producen descongestión; también se evaluó la d-pseudoefedrina con y sin desloratadina |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Modelo animal (perro) | Am J Rhinol | Modelo de congestión nasal alérgica en perros sensibilizados a ambrosía, medida con rinometría acústica |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Modelo animal (perro) | J Pharmacol Toxicol Methods | Caracterización farmacológica de un modelo crónico no invasivo de congestión nasal |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Modelo animal (perro) | Am J Rhinol | Rinometría acústica en perros como modelo para estudiar la congestión nasal |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Estudio animal | J Pharmacol Exp Ther | Agonistas α2c-adrenérgicos selectivos en modelos animales de congestión nasal |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20018638 (cancelado) | TYPIREC ANTIGRIPAL | Cápsula blanda | Paracetamol combinaciones excluyendo psicolépticos |
| 20013677 (cancelado) | ROSSFELL® CÁPSULAS | Cápsula dura | Pseudoefedrina combinaciones |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): hipertensión, insuficiencia hepática, epilepsia, EPOC, úlcera gástrica y péptica, enfermedad renal, pancreatitis, enfermedad hepática y de la vesícula biliar, insuficiencia cardíaca congestiva, hipotiroidismo, enfermedad inflamatoria intestinal, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, hipotensión, abuso de sustancias, trastornos de coagulación, rabdomiólisis, enfermedad coronaria y enfermedad cerebrovascular/accidente cerebrovascular.
- **Interacciones farmacológicas**: se identificaron 150 interacciones; las 20 primeras listadas son en su mayoría de nivel moderado, principalmente con antidiabéticos (acarbosa, acetohexamida, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina, ertugliflozina, exenatida, glimepirida, glipizida, gliburida, insulinas), además de dietilpropión (moderada) y ácido ascórbico (menor).

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (enfermedad de la cavidad nasal) es mecanísticamente plausible, pero corresponde en esencia a un uso ya conocido de la pseudoefedrina, no a un reposicionamiento nuevo. La evidencia es de nivel L4 (estudios farmacológicos y modelos animales, sin ensayos clínicos) y ambos registros sanitarios colombianos están cancelados. Las otras predicciones (laringofaringitis aguda, urticaria alérgica) están en nivel L5 y no tienen respaldo directo; en la urticaria la literatura trata de antihistamínicos, no de pseudoefedrina.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), una brecha que bloquea el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Aclarar el motivo de la cancelación de los registros sanitarios y la situación regulatoria vigente de la pseudoefedrina en Colombia.
- Definir si el objetivo es una indicación nueva o la confirmación de una existente, y buscar ensayos clínicos en humanos para la indicación nasal.
- Evaluar el perfil cardiovascular y de interacciones (hipertensión, diabetes, enfermedad coronaria) antes de cualquier uso ampliado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

