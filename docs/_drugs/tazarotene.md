---
layout: default
title: Tazarotene
parent: Solo Predicción del Modelo (L5)
nav_order: 607
evidence_level: L5
indication_count: 3
---

# Tazarotene
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

# Tazaroteno: De Tazaroteno (indicación sin detallar en el registro) a Dermatitis Seborreica

## Resumen en Una Frase

Tazaroteno es un retinoide de uso tópico, registrado en Colombia como gel tópico, cuyo texto de indicación en el registro sanitario únicamente menciona el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **dermatitis seborreica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tazaroteno (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, el tazaroteno es un retinoide tópico (profármaco convertido en ácido tazaroténico) que se une a los receptores del ácido retinoico (RAR-α, RAR-β y RAR-γ), con mayor afinidad por RAR-β. Su uso clínico documentado incluye acné, psoriasis en placas, reducción de arrugas y pigmentación, y en la UE tiene designación huérfana para ictiosis congénitas.

Mecanísticamente, el tazaroteno normaliza la diferenciación de los queratinocitos y reduce la hiperproliferación epidérmica y la inflamación. Estos efectos son plausiblemente relevantes para la descamación y la inflamación de la dermatitis seborreica, otra enfermedad cutánea con alteración de la epidermis.

Es importante señalar que este vínculo es solo predictivo: no hay ensayos ni literatura en los datos compilados que lo respalden. Además, la irritación cutánea propia de los retinoides podría empeorar una condición que ya implica alteración de la barrera cutánea.

### Otras predicciones del modelo

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|------|------|------|------|
| Queratosis seborreica | 99.51% | L4 | Pregunta de investigación |
| Queratosis folicular invertida vulvar | 99.38% | L5 | Hold |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para dermatitis seborreica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para dermatitis seborreica.

Como referencia, para la segunda predicción (queratosis seborreica) existen dos publicaciones que ofrecen solo contexto indirecto:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/) | 2023 | Revisión sistemática | J Dermatol Treat | Evalúa eficacia y seguridad de tratamientos tópicos para queratosis seborreicas (26 reportes incluidos). No se puede confirmar a partir de los datos que el tazaroteno haya sido evaluado |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Estudio clínico comparativo | Int J Dermatol | Compara crioterapia estándar con calcipotrieno, tazaroteno e imiquimod tópicos en queratosis seborreicas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19978012 | TAZAT® GEL 0.05 % (cancelado) | Gel tópico | TAZAROTENO |
| 19977434 | TAZAT® GEL (cancelado) | Gel tópico | TAZAROTENO |

Ambos registros pertenecen a PERCOS S.A. y se encuentran cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según prospecto)**: respuesta fotoparoxística, enfermedad por fotosensibilidad y quemadura solar.
- **Interacciones farmacológicas**: no se identificaron interacciones con otros fármacos. Los datos corresponden a la farmacología de unión a los receptores del ácido retinoico (RAR-α, RAR-β, RAR-γ).
- **Consideraciones adicionales de las predicciones**: el tazaroteno es un retinoide teratogénico, por lo que el embarazo requiere evaluación cuidadosa. La irritación cutánea o de mucosas (por ejemplo, en zona vulvar) también debe considerarse.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para dermatitis seborreica tiene un puntaje alto del modelo, pero carece de ensayos clínicos y literatura que la respalden (nivel L5). Además, el producto no tiene registros vigentes en Colombia y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto desde INVIMA (brecha bloqueante para el tamizaje de seguridad)
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura específica sobre tazaroteno en dermatitis seborreica y, de ser posible, estudios exploratorios
- Evaluar la compatibilidad de vía de administración y la tolerabilidad cutánea (irritación y fotosensibilidad)
- Aclarar la situación regulatoria, dado que todos los registros están cancelados
- Priorizar, como pregunta de investigación, la predicción de queratosis seborreicas (nivel L4), revisando si los estudios existentes realmente evaluaron tazaroteno
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

