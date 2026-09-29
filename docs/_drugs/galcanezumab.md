---
layout: default
title: Galcanezumab
parent: Solo Predicción del Modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# Galcanezumab: De Migraña y Cefalea en Racimos a Deficiencia de Cofactor II de la Heparina

## Resumen en Una Frase

Galcanezumab es un anticuerpo monoclonal contra el péptido relacionado con el gen de la calcitonina (CGRP), comercializado como EMGALITY para la migraña y la cefalea en racimos.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de cofactor II de la heparina**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, y no se identificó un vínculo mecanístico plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto del registro solo repite «GALCANEZUMAB»). Según el análisis mecanístico: migraña y cefalea en racimos |
| Nueva Indicación Predicha | Deficiencia de cofactor II de la heparina |
| Puntaje de Predicción TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, galcanezumab es un anticuerpo monoclonal que neutraliza el CGRP, una molécula vasodilatadora implicada en la inflamación neurogénica del sistema trigeminovascular. Su eficacia se ha establecido en migraña y cefalea en racimos.

La deficiencia de cofactor II de la heparina es la pérdida hereditaria de una serpina que inhibe la trombina. El bloqueo del CGRP no reemplaza ni aumenta esta proteína, ni actúa sobre la cascada de coagulación. **Por eso no se identificó un vínculo mecanístico plausible.**

El puntaje alto (0.995) probablemente refleja un artefacto del grafo de conocimiento y no una señal biológica real. Las otras dos predicciones principales tienen el mismo problema:

- **Deficiencia de antitrombina tipo 2** (99.41%)
- **Exceso de factor V con trombosis espontánea** (99.41%)

Ambas son trastornos de la coagulación, sin ensayos, sin literatura y sin relación mecanística con la inhibición del CGRP.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se reportan 20 registros sanitarios. Las 5 entradas detalladas en el paquete corresponden al mismo registro, que se muestra una sola vez:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155001 | EMGALITY (Eli Lilly and Company) | Solución inyectable | GALCANEZUMAB (el registro no detalla la indicación) |

**Nota:** los metadatos del paquete indican como fuente `tfda` y un identificador de candidato `TW-`, lo que sugiere origen taiwanés. Conviene verificar que estos registros correspondan realmente a INVIMA (Colombia).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura (nivel L5), y no existe un vínculo mecanístico plausible entre el bloqueo del CGRP y las deficiencias de proteínas anticoagulantes. El CGRP es vasodilatador, por lo que su bloqueo exigiría una revisión de seguridad vascular y trombótica antes de cualquier uso en pacientes con tendencia a la trombosis.

**Para avanzar se necesita:**
- Verificar el origen regulatorio (INVIMA vs. TFDA) y obtener el prospecto con advertencias y contraindicaciones
- Completar los datos de mecanismo de acción desde DrugBank
- Revisar la seguridad vascular y trombótica de la inhibición del CGRP
- Evidencia preclínica o de mecanismo que justifique la predicción, antes de considerar cualquier estudio clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

