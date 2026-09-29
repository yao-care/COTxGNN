---
layout: default
title: Glucagon
parent: Evidencia Moderada (L3-L4)
nav_order: 211
evidence_level: L4
indication_count: 1
---

# Glucagon
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Glucagón: De Indicación Registrada No Detallada a Síndrome del Intestino Irritable

## Resumen en Una Frase

El glucagón es una hormona peptídica comercializada en Colombia en forma inyectable. El registro sanitario solo indica el nombre del principio activo, sin describir la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome del intestino irritable (SII)**.
Hay **11 ensayos clínicos** y **20 publicaciones** asociados a esta búsqueda, pero **ninguno prueba glucagón en SII**. La evidencia disponible corresponde a agonistas del receptor GLP-1 (ROSE-010, liraglutida, GLP-1 nativo), que actúan sobre un receptor distinto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | GLUCAGON (el registro no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Síndrome del intestino irritable |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del glucagón en la base consultada. Por eso no fue posible contrastar el mecanismo con un registro curado.

El vínculo plausible es este: el glucagón suprime la motilidad gastrointestinal, y por eso se usa como antiespasmódico en estudios de imagen del tracto digestivo. Esa acción podría relacionarse con el dolor y la disfunción de la motilidad del SII. **Esta hipótesis proviene de farmacología general y no de los datos analizados.**

Las publicaciones y los ensayos disponibles apoyan el eje hormonal intestinal en el SII, pero mediante análogos de GLP-1. El glucagón y el GLP-1 derivan del mismo precursor (proglucagón) y actúan sobre receptores diferentes, así que esa evidencia no puede trasladarse directamente al glucagón. El puntaje de 0.992 es solo una predicción computacional.

## Evidencia de Ensayos Clínicos

Ningún ensayo evalúa glucagón. Se muestran los más relevantes de los 11 identificados; el resto son estudios dietéticos o de ciencia básica sin relación con glucagón ni con el tratamiento del SII.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Completado | 52 | Efecto de ROSE-010 (análogo de GLP-1) sobre la función motora gastrointestinal en mujeres con SII con estreñimiento. Es la evidencia clínica más cercana, pero no usa glucagón. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Completado | 12 | GLP-1 nativo frente a un análogo inhibe la motilidad antro-duodeno-yeyunal posprandial. Apoya el control hormonal de la motilidad, pero no es glucagón ni población con SII. |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Fase 2 | Terminado | 8 | Liraglutida frente a placebo en pacientes con reservorio ileal y alta frecuencia intestinal. Con solo 8 participantes carece de potencia, y es otra condición. |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completado | 66 | Ejercicio moderado continuo frente a intervalos de alta intensidad sobre disbiosis y GLP-1 en SII con obesidad y prediabetes. Es una intervención de estilo de vida. |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completado | 37 | Modo de acción del butirato en el colon humano. Estudio mecanístico sin glucagón. |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Activo, sin reclutar | 375 | Organoides de intestino delgado humano expuestos a antígenos nutricionales. Modelo de ciencia básica. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | ECA (análisis secundario) | Scand J Gastroenterol | ROSE-010 mostró alivio del dolor durante crisis de SII. Se buscó la subpoblación más adecuada para el tratamiento. |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | ECA (doble ciego, controlado con placebo) | Am J Physiol Gastrointest Liver Physiol | Efecto de ROSE-010 sobre la motilidad gastrointestinal en mujeres con SII con estreñimiento. Se evaluaron seguridad, farmacodinamia y farmacocinética. |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revisión sistemática y metaanálisis | Front Endocrinol | Mejoría del SII con agonistas del receptor GLP-1. GLP-1 y ROSE-010 inhiben el complejo motor migratorio y reducen la motilidad. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revisión | Exp Physiol | Papel de las células L y del GLP-1 en la fisiopatología del SII. |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Estudio clínico observacional | Clin Res Hepatol Gastroenterol | El GLP-1 sérico disminuido se correlaciona con el dolor abdominal en SII con estreñimiento. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohorte | Ann Gastroenterol | Patrones de prescripción y suspensión de agonistas GLP-1 en pacientes con SII. |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclínico (rata) | Neurogastroenterol Motil | Exendina-4 mejoró la disfunción gastrointestinal en el modelo de rata Wistar Kyoto de SII. |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclínico (rata) | Int J Mol Med | Papel del GLP-1 en la patogénesis de modelos experimentales de SII. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Revisión/concepto | Adv Exp Med Biol | GLP-1 en aerosol como alternativa para diabetes y SII. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Revisión | Expert Opin Investig Drugs | Nuevos fármacos en investigación para SII con estreñimiento. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 208565 | GLUCAGEN INYECTABLE (Novo Nordisk A/S) | Polvo liofilizado para reconstituir a solución inyectable | GLUCAGON (sin texto de indicación detallado) |

Los datos recibidos muestran cinco filas idénticas del registro 208565, que se presentan aquí como una sola. El total declarado es de 12 registros sanitarios.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún ensayo ni publicación evalúa glucagón en SII. La evidencia disponible es de análogos de GLP-1, que actúan sobre otro receptor, y el vínculo mecanístico es una inferencia. Además, faltan datos de seguridad del prospecto y de mecanismo de acción, por lo que la candidatura sigue siendo una pregunta de investigación (nivel L4).

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío bloqueante para el tamizaje de seguridad.
- Obtener el mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico.
- Aclarar la indicación aprobada en el registro 208565, que solo indica el nombre del principio activo.
- Buscar estudios con glucagón en motilidad intestinal o dolor abdominal funcional, o justificar por qué la evidencia de GLP-1 sería extrapolable.
- Evaluar la compatibilidad de la vía de administración, hoy solo disponible como inyectable.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

