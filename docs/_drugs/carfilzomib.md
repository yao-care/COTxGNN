---
layout: default
title: Carfilzomib
parent: Solo Predicción del Modelo (L5)
nav_order: 114
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Carfilzomib: De Mieloma Múltiple a CMM7 (Subtipo de Melanoma)

## Resumen en Una Frase

Carfilzomib es un inhibidor del proteasoma que se comercializa en Colombia como KYPROLIS®. El registro sanitario no declara su indicación, pero en el uso clínico general se emplea contra el mieloma múltiple.
El modelo TxGNN predice que podría ser efectivo para **CMM7 (un subtipo de melanoma)**, con un puntaje alto (99.37%) pero **0 ensayos clínicos y 0 publicaciones** específicas para este subtipo.
Para el melanoma en general solo hay **5 publicaciones**, todas preclínicas o indirectas, y ningún ensayo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mieloma múltiple (según conocimiento general del fármaco). El texto de indicación del registro solo repite el nombre "CARFILZOMIB" |
| Nueva Indicación Predicha | CMM7 (subtipo de melanoma) |
| Puntaje de Predicción TxGNN | 99.37% |
| Nivel de Evidencia | L5 para CMM7. Para melanoma en general sería L4 (solo estudios preclínicos) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información conocida, carfilzomib es un inhibidor del proteasoma. Su eficacia en mieloma múltiple es conocida, y mecanísticamente podría ser aplicable al melanoma. Bloquear el proteasoma puede inducir apoptosis (muerte celular programada) en células tumorales.

El único respaldo experimental proviene de un estudio in vitro en células de melanoma murino B16-F1 (PMID 33671902). Allí, carfilzomib combinado con bortezomib aumentó la muerte celular apoptótica. Este resultado no demuestra eficacia ni seguridad en humanos.

La predicción para CMM7 se basa solo en la asociación general con melanoma, sin evidencia propia del subtipo. Las otras predicciones del modelo tienen limitaciones similares:
- **Melanoma leptomeníngeo pediátrico:** no se ha establecido que carfilzomib penetre el sistema nervioso central, lo que es una barrera adicional.
- **Melanoma uveal de células epitelioides:** biológicamente distinto del melanoma cutáneo, por lo que los datos preclínicos no pueden asumirse transferibles.
- **Melanoma vulvar:** no se recuperaron ensayos ni literatura para melanoma mucoso.

---

## Evidencia de Literatura

No hay literatura específica para CMM7. Las siguientes publicaciones corresponden a la predicción de **melanoma en general** (rango 5) y son todas preclínicas o indirectas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Preclínico (in vitro, línea celular murina) | Biology | Carfilzomib combinado con bortezomib aumentó la apoptosis en células de melanoma B16-F1, con activación de caspasas 3, 8, 9 y 12 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico (acoplamiento molecular) | J Biomol Struct Dyn | Reposicionamiento de fármacos clínicos contra dianas de quinasas en diez tipos de cáncer, incluido melanoma. Evidencia computacional, no clínica |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclínico (mecanístico) | Matrix Biol | Bortezomib y carfilzomib activan la vía NF-κB e inducen heparanasa en células de mieloma, lo que se asocia a un fenotipo tumoral más agresivo. No evalúa melanoma |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclínico (mecanístico, células humanas de melanoma) | Mol Cancer Res | El gen ZFAND2a regula la supervivencia celular en melanoma humano mediante la ligasa E3 cIAP2. Por el resumen disponible, no parece probar carfilzomib como terapia |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclínico (mecanístico) | Leukemia | Moléculas PROTAC dirigidas a proteínas BET son activas en modelos preclínicos de mieloma. No evalúa carfilzomib en melanoma |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20087826 | KYPROLIS® (AMGEN INC.) | Polvo liofilizado (para reconstituir a solución inyectable) | El texto registrado solo indica "CARFILZOMIB" |

Los cinco registros devueltos corresponden al mismo número sanitario, por lo que se muestra una sola fila. El total declarado es de 20 registros.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor del proteasoma) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto. En general se esperan hemograma y función hepática y renal |
| Protección en Manejo | Manejar como fármaco antineoplásico, según las regulaciones locales para fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La búsqueda de interacciones farmacológicas no arrojó resultados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto, pero no hay ensayos clínicos ni literatura específica para CMM7 (nivel L5). Para melanoma en general solo existen estudios preclínicos e indirectos (L4), y un resultado en células murinas no establece eficacia ni seguridad en humanos.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA, con advertencias y contraindicaciones, para poder hacer el tamizaje de seguridad. Este es el bloqueo principal.
- Completar el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Buscar evidencia específica del subtipo CMM7 y estudios en modelos de melanoma humano, in vitro e in vivo.
- Evaluar la penetración en el sistema nervioso central antes de considerar enfermedad leptomeníngea.
- Definir la compatibilidad de la vía de administración, que está pendiente. En Colombia solo se registra como polvo liofilizado inyectable.

Los resultados son solo para fines de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

