---
layout: default
title: Dexibuprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexibuprofen: nueva indicación predicha, Espondilitis anquilosante (nivel de evidencia L5). Indicación original: Ibuprofeno combinaciones"
monitor_inn: "dexibuprofen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome"]
---

# Dexibuprofen
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

# Dexibuprofeno: De Ibuprofeno en Combinaciones a Espondilitis Anquilosante

## Resumen en Una Frase

Dexibuprofeno es el enantiómero activo S(+) del ibuprofeno, registrado en Colombia bajo la categoría "Ibuprofeno combinaciones". El modelo TxGNN predice que podría ser efectivo para **espondilitis anquilosante**, la indicación con mayor sustento entre las candidatas evaluadas, aunque con **0 ensayos clínicos** y solo **3 publicaciones** de revisión de carácter indirecto.

> Nota: la predicción con mayor puntaje TxGNN es el síndrome de braquidactilia-sindactilia (99,87%), pero carece de cualquier evidencia y de plausibilidad mecanística. Se presenta como indicación principal la espondilitis anquilosante (puntaje 99,70%) porque es la única con literatura relacionada y un fundamento farmacológico verosímil. Las demás candidatas se resumen más abajo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ibuprofeno combinaciones |
| Nueva Indicación Predicha | Espondilitis anquilosante (candidata priorizada); la de mayor puntaje es el síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99,70% (espondilitis anquilosante); 99,87% (síndrome de braquidactilia-sindactilia) |
| Nivel de Evidencia | L4 (espondilitis anquilosante); L5 para la mayoría de las demás |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold (con la espondilitis anquilosante como pregunta de investigación) |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, dexibuprofeno es el enantiómero S(+) del ibuprofeno y pertenece a la clase de los antiinflamatorios no esteroideos (AINE), que inhiben la ciclooxigenasa (COX) y reducen la síntesis de prostaglandinas, con efecto analgésico y antiinflamatorio.

En el caso de la espondilitis anquilosante, los AINE son tratamiento de primera línea según las guías para aliviar el dolor y la rigidez. Como dexibuprofeno es la forma activa del ibuprofeno, cabría esperar un efecto similar a dosis menores. Sin embargo, la literatura disponible son revisiones generales sobre dexibuprofeno y sobre sistemas de liberación de AINE en artritis, no estudios específicos en espondilitis anquilosante. La evidencia es, por tanto, indirecta, y el beneficio sería sintomático, no modificador de la enfermedad.

Para el resto de las candidatas (síndromes de malformación congénita, displasias esqueléticas genéticas, síndrome WHIM, etc.), no se identifica un vínculo mecanístico plausible: la inhibición de COX no actúa sobre defectos genéticos o del desarrollo. Sus altos puntajes (entre 99,7% y 99,9%) parecen reflejar artefactos de la topología del grafo más que una base biológica. La miosclerosis y la pseudoacondroplasia podrían, como mucho, tener un alivio sintomático del dolor, sin respaldo de evidencia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11771569](https://pubmed.ncbi.nlm.nih.gov/11771569/) | 2001 | Revisión | Clinical Rheumatology | Panorama de datos clínicos de dexibuprofeno: 8 ensayos con 1463 pacientes (varios doble ciego frente a placebo, ibuprofeno racémico y diclofenaco), estudios de farmacovigilancia y un metaanálisis de tolerabilidad |
| [9013382](https://pubmed.ncbi.nlm.nih.gov/9013382/) | 1996 | Revisión | Journal of Clinical Pharmacology | Reevaluación de estudios doble ciego aleatorizados de dexibuprofeno en síndrome lumbar, artritis reumatoide, esguince de tobillo, gonartrosis, espondilitis anquilosante y coxartrosis activada |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Revisión | Critical Reviews in Therapeutic Drug Carrier Systems | Microencapsulación como sistema de liberación de AINE en artritis, incluida la espondilitis anquilosante (no específico de dexibuprofeno) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20057197 (cancelado) | TAFLAX® FEM TABLETAS RECUBIERTAS | Tableta recubierta | Ibuprofeno combinaciones |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas en las consultas realizadas. Como referencia de clase, los AINE conllevan riesgos gastrointestinales, cardiovasculares y renales, que deben verificarse en el prospecto vigente.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las candidatas se basan únicamente en predicción computacional, sin ensayos clínicos. La espondilitis anquilosante (L4) tiene un fundamento plausible a nivel de clase, pero la evidencia es indirecta, el beneficio sería solo sintomático y el único registro sanitario en Colombia está cancelado. Las demás candidatas (L5) carecen de vínculo mecanístico y no deben avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de dexibuprofeno (consulta a DrugBank)
- Prospecto del INVIMA con advertencias y contraindicaciones (bloqueante para el cribado de seguridad)
- Revisión de estudios específicos de dexibuprofeno en espondilitis anquilosante, y comparación frente a AINE ya disponibles
- Verificación de la viabilidad comercial, dado que no hay registros vigentes en Colombia
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original (pendientes)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

