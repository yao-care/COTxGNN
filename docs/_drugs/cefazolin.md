---
layout: default
title: Cefazolin
parent: Evidencia Moderada (L3-L4)
nav_order: 116
evidence_level: L4
indication_count: 8
---

# Cefazolin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Cefazolina: De Infecciones Bacterianas (indicación original no especificada en el registro) a Otitis Media Infecciosa

## Resumen en Una Frase

La cefazolina es una cefalosporina de primera generación, un antibiótico inyectable que se usa contra infecciones bacterianas. El modelo TxGNN predice que podría ser efectiva para la **otitis media infecciosa**. Actualmente la respaldan **1 ensayo clínico** (sin confirmar que evalúe cefazolina) y **3 publicaciones** indirectas, por lo que la evidencia es débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada. El registro INVIMA solo dice «CEFAZOLINA» |
| Nueva Indicación Predicha | Otitis media infecciosa |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (todos corresponden al mismo número de registro, 20152146) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente. Según la farmacología general, la cefazolina es una cefalosporina de primera generación que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina. Por eso es biológicamente plausible que actúe sobre infecciones bacterianas del oído.

La otitis media aguda suele ser bacteriana, y la cefazolina cubre bien estafilococos sensibles a meticilina y estreptococos. Sin embargo, tiene actividad limitada contra *Haemophilus influenzae* y *Moraxella catarrhalis*, que son los patógenos principales de la otitis media. Además, solo existe en forma parenteral, así que en la práctica se limitaría a enfermedad grave o complicada.

El puntaje alto de TxGNN refleja cercanía en el grafo de conocimiento (fármaco antibacteriano y enfermedad infecciosa). No demuestra eficacia clínica. La relación con la indicación original no pudo evaluarse, porque el registro local no detalla la indicación aprobada.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Fase 2 | Terminado | 520 | Compara un tratamiento antibiótico corto (5 días) con uno estándar (10 días) en niños de 6 a 23 meses con otitis media aguda. No se confirma que el fármaco evaluado sea cefazolina (relevancia baja, grado C) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Revisión | Southern Medical Journal | Las cefalosporinas son útiles en infecciones pediátricas por cocos grampositivos, especialmente en alergia a la penicilina |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisión | Clinical Pharmacy | Caso y revisión de síndrome de Stevens-Johnson en una niña tratada por otitis media con otros betalactámicos. No evalúa la eficacia de la cefazolina |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Serie/reporte de casos | Ann Otol Rhinol Laryngol | Terapia empírica ceftazidima-cefazolina en síndrome de Gradenigo pediátrico, una complicación rara de la otitis media aguda |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20152146 | CEFAZOLINA 1 G | Polvo estéril para reconstituir a solución inyectable | «CEFAZOLINA» (sin indicación detallada en el registro) |

El fabricante es FARMALOGICA S.A. Los cuatro registros del paquete de evidencia repiten el mismo número, producto y forma farmacéutica.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia directa es casi inexistente: el único ensayo no está confirmado como de cefazolina y la literatura es indirecta (revisiones antiguas y un reporte de casos). Además, la cefazolina tiene cobertura limitada de los patógenos típicos de la otitis media y solo se administra por vía parenteral. El puntaje TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Verificar en ClinicalTrials.gov el brazo de intervención del NCT01511107 para saber si incluye cefazolina.
- Obtener las advertencias y contraindicaciones del prospecto INVIMA, que faltan actualmente.
- Consultar los datos del mecanismo de acción en DrugBank.
- Comparar la cefazolina con los antibióticos de primera línea de las guías (por ejemplo amoxicilina-clavulanato o ceftriaxona), y definir si tendría un nicho en enfermedad grave o complicada por vía parenteral.
- Aclarar la indicación original aprobada en el registro colombiano, hoy registrada solo como «CEFAZOLINA».
- Tener en cuenta que las otras predicciones (bronquitis, otitis media crónica y supurativa, otosalpingitis, otitis media no supurativa y alérgica) tienen evidencia igual o más débil.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

