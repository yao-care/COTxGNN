---
layout: default
title: Benzocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 100
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
description: "Benzocaine: nueva indicación predicha, Conjuntivitis papilar (nivel de evidencia L5). Indicación original: Benzocaína"
monitor_inn: "Benzocaine"
predicted_indications: ["papillary conjunctivitis"]
---

# Benzocaine
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

## Benzocaína: De Anestésico Local (Benzocaína) a Conjuntivitis Papilar
{: .text-alpha }

## Resumen en Una Frase

Benzocaína es un anestésico local de tipo éster, registrado en Colombia como principio activo único y en combinación para uso bucal.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**,
pero **no hay ensayos clínicos ni publicaciones** que respalden actualmente esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Benzocaína (el registro sanitario no detalla una indicación en texto) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 0.9938 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 13 de 16) |
| Número de Registros Sanitarios | 16 (vigentes: 13) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, benzocaína es un anestésico local de tipo éster que bloquea los canales de sodio dependientes de voltaje, lo que reduce la transmisión del dolor. En Colombia se registró en soluciones y tabletas de uso bucal.

En teoría, este bloqueo podría aliviar la molestia de la superficie ocular. Sin embargo, sería solo un alivio sintomático y no una modificación de la enfermedad. La conjuntivitis papilar se origina principalmente por irritación alérgica o mecánica (uso de lentes de contacto, prótesis oculares, suturas expuestas), por lo que el vínculo terapéutico directo con el bloqueo de canales de sodio es débil.

Además, los anestésicos tópicos tienen un riesgo conocido de toxicidad corneal con el uso repetido, lo que va en contra de una aplicación ocular crónica. El puntaje alto del modelo debe interpretarse con cautela, dado que no existe evidencia clínica que lo acompañe.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19939513 | NORAVER P TABLETAS DE DISOLUCIÓN BUCAL | TABLETA BUCAL | CETILPIRIDINO CLORURO + COMBINACION | Vigente |
| 20049882 | OTIFIX® SOLUCION OTICA | SOLUCION OTICA | COMBINACIONES | Vigente |
| 20067385 | BUCOSEPTOL N | TABLETA BUCAL | BENZOCAINA | Vigente |
| 20161662 | NORAVER MF | TABLETA BUCAL | CETILPIRIDINO CLORURO + COMBINACION | Vigente |
| 20188546 | ISEPTIC® GARGANTA | TABLETA MASTICABLE | CETILPIRIDINO CLORURO + COMBINACION | Vigente |

Se muestran 5 de 16 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Posibles contraindicaciones según el grafo de conocimiento del modelo** (no provienen del prospecto; deben verificarse): insuficiencia hepática, enfermedad hepática, encefalopatía hepática, enfermedad renal, epilepsia, porfiria, trombocitopenia, neutropenia, agranulocitosis, diabetes mellitus y cetoacidosis diabética, trastornos de la coagulación, hipercalcemia, hiperparatiroidismo, gastritis, sarcoidosis, herpes simple, trastornos de ansiedad y abuso de sustancias, entre otros.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para obtener la información de seguridad oficial (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones, con un vínculo mecanístico débil y un riesgo conocido de toxicidad corneal con anestésicos tópicos.

<!-- review:begin co-lic-20261105-benzocaine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones, con un vínculo mecanístico débil y un riesgo conocido de toxicidad corneal con anestésicos tópicos. Además, los dos registros sanitarios en Colombia están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-benzocaine-1 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de literatura sobre anestésicos tópicos en conjuntivitis papilar y su seguridad corneal.
- Evaluar la compatibilidad de la vía de administración (los productos registrados son de uso bucal, no oftálmico).
- Valorar si existe un beneficio clínico real frente a los tratamientos actuales (antihistamínicos, estabilizadores de mastocitos, retiro del factor irritante).

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, los dos registros sanitarios en Colombia están cancelados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

