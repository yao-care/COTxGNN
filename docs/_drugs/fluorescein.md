---
layout: default
title: Fluorescein
parent: Solo Predicción del Modelo (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Fluorescein: nueva indicación predicha, Angina de Prinzmetal (nivel de evidencia L5). Indicación original: Fluoresceína (uso diagnóstico)"
monitor_inn: "fluorescein"
predicted_indications: ["Prinzmetal angina", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "hemoglobinopathy", "heparin cofactor 2 deficiency", "thrombophilia", "hyperthyroidism", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Fluorescein
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Fluoresceína: De Agente de Diagnóstico (Fluoresceína) a Angina de Prinzmetal
{: .text-alpha }

## Resumen en Una Frase

La fluoresceína es un colorante fluorescente de uso diagnóstico, registrado en Colombia como solución inyectable bajo la indicación "fluoresceína".
El modelo TxGNN predice que podría ser efectivo para **Angina de Prinzmetal**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción del modelo TxGNN (aprendizaje profundo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fluoresceína (uso diagnóstico) |
| Nueva Indicación Predicha | Angina de Prinzmetal |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la fluoresceína es un colorante diagnóstico fluorescente, usado sobre todo en angiografía y tinción de la superficie ocular, y no un fármaco terapéutico.

El análisis de los datos compilados no identificó ningún vínculo mecanístico: la fluoresceína no tiene actividad vasodilatadora ni antiespasmódica vascular conocida, que sería lo esperable para tratar la angina vasoespástica. El puntaje alto de TxGNN (0.9981) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por tanto, esta predicción debe considerarse una hipótesis sin sustento mecanístico ni clínico. La similitud con la indicación original no pudo evaluarse.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Angina de Prinzmetal.

**Nota sobre otras predicciones.** Entre las otras nueve indicaciones predichas, tres tienen literatura recuperada (artritis reumatoide, hemoglobinopatía, trombofilia e hipertiroidismo; nivel L4). En todos los casos se trata de estudios sobre manifestaciones oculares de esas enfermedades, donde la fluoresceína aparece como herramienta diagnóstica (angiografía o tinción), no como tratamiento. Es evidencia indirecta y no constituye una señal de reposicionamiento. Las demás predicciones (deficiencia de antitrombina tipo 2, exceso de factor 5, deficiencia de cofactor 2 de heparina, deleción parcial del brazo corto del cromosoma 16 y beta-talasemia) no tienen evidencia alguna (L5). Todas se mantienen en Hold.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20008605 | FLUORESCEINA SODICA 10%. | Solución inyectable | Fluoresceína |
| 19933781 | BIO-GLOSOLUCION | Solución inyectable | Fluoresceína |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en las consultas realizadas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para Angina de Prinzmetal se basa solo en el modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-fluorescein-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para Angina de Prinzmetal se basa solo en el modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible. Además, el producto no tiene registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-fluorescein-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank)
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para cualquier evaluación de seguridad
- Un fundamento farmacológico o preclínico que justifique un uso terapéutico de la fluoresceína, hoy inexistente
- Evaluar la compatibilidad de vía de administración (actualmente solo existe solución inyectable) y la situación regulatoria, dado que el medicamento está comercializado en este país con 2 licencias válidas de 2

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el producto no tiene registros sanitarios vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

