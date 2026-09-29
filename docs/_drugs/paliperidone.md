---
layout: default
title: Paliperidone
parent: Solo Predicción del Modelo (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidona: De Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La paliperidona es un antipsicótico atípico, conocido por su uso en esquizofrenia. El registro sanitario colombiano solo repite el nombre del principio activo (“PALIPERIDONA”) y no describe la indicación.
El modelo TxGNN predice que podría ser efectiva para **distrofia retiniana con o sin anomalías extraoculares**, pero hay **0 ensayos clínicos** y las **15 publicaciones** recuperadas tratan de anomalías oculares en general. Ninguna menciona la paliperidona ni otro antipsicótico, así que no respaldan la predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia (conocimiento general del fármaco; el texto del registro solo dice “PALIPERIDONA”) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.92% (posición 982 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos de DrugBank no traen el mecanismo de acción, pero el análisis del paquete de evidencia describe la paliperidona como antagonista de los receptores de dopamina D2 y de serotonina 5-HT2A. Ese es el mecanismo que explica su efecto antipsicótico.

Ese mecanismo **no tiene un vínculo plausible** con la degeneración retiniana hereditaria, y nada en los datos conecta el fármaco con esta enfermedad. El puntaje alto (0.999) sale solo del grafo de conocimiento y no de estudios reales. Los artículos recuperados hablan de anomalías orbitarias, de músculos extraoculares y congénitas del ojo, y ninguno menciona la paliperidona.

Por tanto, esta predicción debe leerse como una señal computacional sin sustento biológico ni clínico por ahora.

## Evidencia de Literatura

Actualmente no hay ensayos clínicos relacionados registrados. La literatura recuperada es la siguiente (10 de 15; no hay ECA, y se priorizan revisiones sobre reportes de caso):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Seminars in Neurology | Enfoque sistemático para evaluar la diplopía; sin relación con paliperidona |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Revisión | Seminars in Ultrasound, CT, and MR | Infecciones orbitarias, con la sinusitis como causa más común |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klinische Monatsblätter für Augenheilkunde | Ptosis congénita: formas simples y complicadas, y su evaluación |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan Journal of Ophthalmology | Anomalías congénitas de la forma del cristalino |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Lesiones orbitarias pediátricas: diagnóstico diferencial y hallazgos de imagen |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Revisión | Progress in Retinal and Eye Research | Propioceptores de los músculos extraoculares y percepción espacial visual |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | Journal of Binocular Vision and Ocular Motility | Oftalmoplejía y trastornos congénitos de disinervación craneal |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Cohorte | Neuroradiology | Hallazgos neurorradiológicos y clínicos en oftalmoplejía |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Reporte de caso | American Journal of Ophthalmology | Dos casos de criptoftalmos unilateral |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Reporte de caso | Optometry and Vision Science | Divergencia sinérgica en fibrosis congénita de los músculos extraoculares |

Otras 5 publicaciones sin clasificar (sobre maculopatía con anomalías del disco óptico, CFEOM, MAB21L1, ácido retinoico y estructura de músculos extraoculares) tampoco mencionan la paliperidona.

## Información de Mercado en Colombia

Los cinco registros devueltos son filas idénticas del mismo registro sanitario; se muestra una sola vez. El total reportado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19983120 | INVEGA® Tabletas de Liberación Prolongada 6 mg (Janssen Cilag S.A.) | Tableta de liberación prolongada | Solo figura “PALIPERIDONA” (sin texto de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos, la literatura recuperada no menciona el fármaco y no se identifica ningún vínculo mecanístico plausible. Las demás predicciones (miopías, malformaciones cerebrales, trastornos metabólicos y neuropatías hereditarias) tampoco tienen evidencia. La única con datos reales es la **esquizofrenia resistente al tratamiento** (L3, 4 ensayos de Fase 4, incluido un estudio naturalista con 30 pacientes). Es una subpoblación de la indicación ya existente y no un reposicionamiento propiamente dicho. En las miopías, el antagonismo D2 iría además en dirección desfavorable.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y confirmar el texto de la indicación aprobada.
- Completar el mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica que conecte la señalización dopaminérgica o serotoninérgica con la degeneración retiniana hereditaria; sin ella, no seguir con esta indicación.
- Si se quiere una línea con evidencia real, evaluar la esquizofrenia resistente como pregunta de investigación comparativa, con la paliperidona palmitato de acción prolongada frente a la clozapina.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

