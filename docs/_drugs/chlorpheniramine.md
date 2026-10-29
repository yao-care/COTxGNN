---
layout: default
title: Chlorpheniramine
parent: Solo Predicción del Modelo (L5)
nav_order: 153
evidence_level: L5
indication_count: 1
monitor_inn: "Chlorpheniramine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-29
description: "Chlorpheniramine: nueva indicación predicha, enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: PARACETAMOL COMBINACIONES EXCLUYENDO SICOLEPTICOS"
---

# Chlorpheniramine
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

## Clorfeniramina: antagonista del receptor H1 de histamina → enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Clorfeniramina es un antihistamínico que bloquea el receptor H1 y se encuentra en productos combinados para el resfriado común.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal (nasal cavity disease)**,
pero hasta ahora no hay ensayos clínicos registrados y solo **8 publicaciones**, todas preclínicas o de fisiopatología, que se relacionan con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PARACETAMOL COMBINACIONES EXCLUYENDO SICOLEPTICOS; PREPARACIONES DE OTRAS COMBINACIONES PARA EL RESFRIADO COMÚN; IBUPROFENO. DEXTROMETORFANO BROMHIDRATO. FENILEFRINA CLORHIDRATO. CLORFENIRAMINA MALEATO |
| Nueva Indicación Predicha | enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0,9953 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Clorfeniramina actúa como antagonista del receptor H1 de histamina (gen HRH1). No se dispone de datos detallados sobre el mecanismo de acción en la información compilada, pero la farmacología conocida indica que el bloqueo H1 reduce la rinorrea, los estornudos, el picor y la permeabilidad vascular mediados por histamina en la mucosa nasal.

Este efecto es coherente con su presencia en productos combinados para el resfriado común y la rinitis alérgica. Mecanísticamente, por tanto, podría ser aplicable a enfermedades de la cavidad nasal.

Sin embargo, "enfermedad de la cavidad nasal" es un término amplio e inespecífico. Antes de cualquier evaluación conviene acotarlo a una condición definida, por ejemplo la rinitis alérgica. Además, la literatura disponible son modelos animales (gato, perro, rata) de congestión nasal y rinitis alérgica, y un estudio de fisiopatología; no aportan evidencia clínica sobre clorfeniramina en esta enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10582118](https://pubmed.ncbi.nlm.nih.gov/10582118/) | 1999 | Estudio animal preclínico | Am J Rhinol | El bloqueo combinado de receptores H1 (clorfeniramina) y H3 produjo descongestión nasal en un modelo felino de congestión |
| [10582116](https://pubmed.ncbi.nlm.nih.gov/10582116/) | 1999 | Estudio animal preclínico | Am J Rhinol | Caracterización de la resistencia y geometría nasal con rinometría de presión y acústica en un modelo felino de congestión nasal |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Estudio animal preclínico | Am J Rhinol | Modelo de congestión nasal alérgica en perros sensibilizados a ambrosía, medido por rinometría acústica |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Estudio animal preclínico | J Pharmacol Toxicol Methods | Caracterización farmacológica de un modelo canino crónico y no invasivo de congestión nasal |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Estudio animal preclínico | Am J Rhinol | Rinometría acústica en perros como modelo de congestión nasal inducida por el compuesto 48/80 |
| [10822083](https://pubmed.ncbi.nlm.nih.gov/10822083/) | 2000 | Estudio animal preclínico | Immunopharmacology | Nuevo modelo de rinitis alérgica en ratas y evaluación de antagonistas H1 |
| [1705288](https://pubmed.ncbi.nlm.nih.gov/1705288/) | 1990 | Estudio animal preclínico | J Pharmacobiodyn | Modelo de rinitis alérgica en rata Brown Norway y evaluación de fármacos antialérgicos |
| [2923378](https://pubmed.ncbi.nlm.nih.gov/2923378/) | 1989 | Fisiopatología | Am Rev Respir Dis | Origen de las proteínas en las secreciones nasales inducidas por histamina en sujetos atópicos y no atópicos |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19982950 | ZAS TABLETAS | Tableta | PARACETAMOL COMBINACIONES EXCLUYENDO SICOLEPTICOS |
| 20188459 | RESFRYGRYP NOCHE® | Gránulos | PREPARACIONES DE OTRAS COMBINACIONES PARA EL RESFRIADO COMÚN |
| 20165041 | ADVIL® GRIPA MAX | Cápsula blanda | IBUPROFENO. DEXTROMETORFANO BROMHIDRATO. FENILEFRINA CLORHIDRATO. CLORFENIRAMINA MALEATO |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en modelos animales y estudios de fisiopatología, sin ensayos clínicos ni estudios que evalúen clorfeniramina en humanos para esta enfermedad. Además, la indicación predicha es demasiado amplia para evaluarse tal cual.

**Para avanzar se necesita:**
- Acotar la indicación a una condición definida (por ejemplo, rinitis alérgica)
- Datos clínicos (ensayos o estudios observacionales) de clorfeniramina en la condición acotada
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto aprobado por INVIMA
- Verificación de la compatibilidad de vías de administración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

