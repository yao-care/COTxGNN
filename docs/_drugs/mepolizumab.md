---
layout: default
title: Mepolizumab
parent: Evidencia Moderada (L3-L4)
nav_order: 274
evidence_level: L4
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Mepolizumab: De Indicación No Registrada a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Mepolizumab es un anticuerpo monoclonal anti-IL-5 que reduce los eosinófilos y se comercializa en Colombia como NUCALA®. Los registros disponibles no especifican su indicación original.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**,
pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** (un reporte de caso), por lo que la evidencia es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el campo de indicación solo repite el nombre del principio activo) |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99.66% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Mepolizumab es un anticuerpo anti-IL-5 que bloquea esta vía y reduce los eosinófilos. El único respaldo es un reporte de caso: un paciente con un síndrome inmune hipereosinofílico resistente a esteroides mejoró con mepolizumab, junto con una mejoría de una microangiopatía trombótica mixta. Esto sugiere una posible contribución de los eosinófilos a algunas citopenias inmunes.

Sin embargo, el vínculo es indirecto. La trombocitopenia inmune se debe sobre todo a la destrucción de plaquetas mediada por autoanticuerpos y a una producción plaquetaria deficiente. Las vías de IL-5 y eosinófilos no se consideran centrales en este mecanismo. El título del reporte de caso está truncado, así que no se puede confirmar que la trombocitopenia haya sido un desenlace documentado.

El puntaje TxGNN de 0.997 es solo una predicción computacional y no equivale a evidencia clínica. Las otras cuatro predicciones del modelo (trastorno de liberación plaquetaria, enfermedad de von Willebrand tipo plaquetario, trombocitopenia autoinmune y trombastenia de Glanzmann) tienen aún menos respaldo. La mayoría parecen artefactos del grafo de conocimiento, por compartir vecinos de trastornos plaquetarios o hemorrágicos.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Reporte de caso | Blood Cells Mol Dis | Un síndrome inmune hipereosinofílico resistente a esteroides se resolvió con mepolizumab, con mejoría concomitante de una microangiopatía trombótica mixta (asociada a síndrome hemolítico urémico atípico) |

## Información de Mercado en Colombia

Los 5 registros listados en los datos corresponden al mismo número sanitario y al mismo producto, por lo que se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20188045 | NUCALA® 100MG/ML SOLUCIÓN INYECTABLE (GlaxoSmithKline Colombia S.A.) | Solución inyectable | No detallada (el registro solo indica "Mepolizumab") |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación es un reporte de caso sobre un síndrome hipereosinofílico, no sobre trombocitopenia inmune. El mecanismo de la trombocitopenia inmune (autoanticuerpos) no se relaciona claramente con la vía IL-5/eosinófilos, por lo que la predicción debe tratarse como una pregunta de investigación.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad)
- Confirmar la indicación aprobada y el mecanismo de acción del fármaco en DrugBank e INVIMA
- Revisar el texto completo del reporte de caso (PMID 28648630) para verificar si la trombocitopenia fue un desenlace documentado
- Buscar estudios que relacionen los eosinófilos o la IL-5 con la trombocitopenia inmune
- Evaluar si existen ensayos clínicos en otros registros, como ICTRP, antes de reconsiderar la decisión

*Este informe es solo una referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

