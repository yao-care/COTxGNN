---
layout: default
title: Chlorpheniramine
parent: Evidencia Moderada (L3-L4)
nav_order: 153
evidence_level: L3
indication_count: 4
---

# Chlorpheniramine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **4** 
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

# Clorfeniramina: De Combinaciones para el Resfriado Común a Urticaria Alérgica

## Resumen en Una Frase

La clorfeniramina es un antihistamínico de primera generación, utilizado originalmente en productos combinados para el resfriado común y los síntomas gripales (con paracetamol, ibuprofeno, dextrometorfano y fenilefrina).
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**, pero no existen ensayos clínicos registrados y la literatura disponible consiste sobre todo en revisiones, reportes de caso y estudios de otros antihistamínicos, por lo que la evidencia es limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol, combinaciones excluyendo psicolépticos (combinaciones para el resfriado común) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, la clorfeniramina es un antagonista (agonista inverso) del receptor de histamina H1, de la familia de las alquilaminas, usado desde la década de 1950. La base de datos farmacológica la vincula con el receptor H1 (gen HRH1) y la describe como un fármaco para tratar síntomas de alergias.

En la urticaria alérgica, la liberación de histamina por los mastocitos produce roncha y eritema, por lo que el bloqueo H1 es mecanísticamente directo. Los antihistamínicos H1 son un tratamiento establecido para la urticaria. Por ello, esta predicción refleja un uso de clase ya conocido más que un reposicionamiento realmente novedoso.

La pregunta abierta es si la clorfeniramina ofrece alguna ventaja frente a los antihistamínicos de segunda generación, dada su carga sedante y anticolinérgica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Revisión | Curr Rev Clin Exp Pharmacol | Revisión integral de la clorfeniramina; describe usos en condiciones alérgicas, urticaria crónica, asma y otros |
| [1683523](https://pubmed.ncbi.nlm.nih.gov/1683523/) | 1991 | Revisión | Ann Allergy | Comparación de antihistamínicos H1; ventajas de los de segunda generación (menos sedación y actividad anticolinérgica) |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Revisión | Drugs | Cetirizina en rinitis alérgica, asma y urticaria crónica (otro fármaco) |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Revisión | Drugs | Loratadina tan eficaz como clorfeniramina y otros antihistamínicos en trastornos alérgicos |
| [14977391](https://pubmed.ncbi.nlm.nih.gov/14977391/) | 2004 | Revisión | Drugs | Uso de cetirizina en trastornos alérgicos (otro fármaco) |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohorte | Asian Pac J Allergy Immunol | Descripción de 142 niños tailandeses con urticaria |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Reporte de caso y revisión de farmacovigilancia | Medicine | Dos casos de anafilaxia inducida por clorfeniramina y revisión de base de datos de farmacovigilancia |
| [26240795](https://pubmed.ncbi.nlm.nih.gov/26240795/) | 2015 | Reporte de caso | Asia Pac Allergy | Anafilaxia por clorfeniramina diagnosticada con prueba de activación de basófilos |
| [21217928](https://pubmed.ncbi.nlm.nih.gov/21217928/) | 2011 | Reporte de caso | Allergy Asthma Immunol Res | Hipersensibilidad a clorfeniramina con intolerancia al ácido acetilsalicílico |
| [19348661](https://pubmed.ncbi.nlm.nih.gov/19348661/) | 2009 | Reporte de caso | J Dermatol | Urticaria inducida por múltiples antihistamínicos H1 |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19982950 | ZAS TABLETAS | Tableta | Paracetamol, combinaciones excluyendo psicolépticos (cancelado) |
| 20188459 | RESFRYGRYP NOCHE® | Gránulos | Preparaciones de otras combinaciones para el resfriado común (cancelado) |
| 20165041 | ADVIL® GRIPA MAX | Cápsula blanda | Ibuprofeno, dextrometorfano bromhidrato, fenilefrina clorhidrato, clorfeniramina maleato (cancelado) |

Los tres registros están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): hipertensión, insuficiencia hepática y enfermedad hepática, epilepsia, insomnio, EPOC, úlcera gástrica y péptica, gastritis, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, trombocitopenia, hipotiroidismo, enfermedad inflamatoria intestinal, trastornos psicóticos y mentales, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, bronquitis, trastorno hipotensivo, entre otras. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: solo consta la unión al receptor H1 (mecanismo farmacológico); no hay interacciones medicamentosas específicas documentadas.
- **Señales de la literatura**: casos de anafilaxia e hipersensibilidad inducidas por clorfeniramina (PMID 31852144, 26240795, 21217928). Además, su perfil sedante y anticolinérgico es relevante frente a los antihistamínicos de segunda generación.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Otras Predicciones Evaluadas

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Urticaria por frío | 99.13% | L3 | Pregunta de investigación. Un estudio doble ciego de 1977 (PMID 334082, 8 sujetos) comparó clorfeniramina, ciproheptadina y placebo; es pequeño y antiguo |
| Enfermedad de la cavidad nasal | 99.53% | L4 | Hold. Solo modelos animales (gato, perro, rata); el término es demasiado amplio y debe precisarse (p. ej., rinitis alérgica) |
| Laringofaringitis aguda | 99.50% | L5 | Hold. Solo predicción del modelo; sin literatura ni ensayos |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El bloqueo H1 es un mecanismo directo y establecido para la urticaria, pero no hay ensayos clínicos para esta indicación y la literatura es mayormente de revisiones y reportes de caso. Además, no existen registros sanitarios vigentes en Colombia y las guías actuales favorecen los antihistamínicos de segunda generación, por lo que no se identifica una ventaja clara.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial (INVIMA) para las advertencias y contraindicaciones.
- Completar los datos de mecanismo de acción desde DrugBank.
- Evidencia comparativa que demuestre alguna ventaja de la clorfeniramina frente a los antihistamínicos de segunda generación en urticaria.
- Evaluar la viabilidad regulatoria, dado que todos los registros están cancelados.
- Si se continúa con la rinitis alérgica, definir la condición con precisión antes de la evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

