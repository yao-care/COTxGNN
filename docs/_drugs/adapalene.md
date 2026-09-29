---
layout: default
title: Adapalene
parent: Solo Predicción del Modelo (L5)
nav_order: 27
evidence_level: L5
indication_count: 1
---

# Adapalene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Adapaleno: De Acné a Zinc Plasmático Elevado

## Resumen en Una Frase

Adapaleno es un retinoide tópico de tercera generación (agonista de RAR-beta/gamma), comercializado para el acné.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**,
pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné (según el análisis de referencia; el registro sanitario solo dice «ADAPALENE») |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, el adapaleno es un retinoide tópico de tercera generación que actúa sobre los receptores RAR-beta y RAR-gamma, y su uso establecido es el acné.

No se ha demostrado un vínculo mecanístico con la nueva indicación. La única conexión especulativa es la interacción entre la vitamina A y el zinc: el zinc se necesita para sintetizar la proteína de unión al retinol y para el metabolismo de los retinoides. Sin embargo, el adapaleno tópico tiene absorción sistémica mínima, por lo que un efecto sobre el zinc plasmático es poco plausible sin más datos.

Además, el zinc plasmático elevado es un hallazgo de laboratorio, no una enfermedad con un tratamiento farmacológico establecido. Por eso esta predicción podría ser un artefacto del grafo de conocimiento y no una señal biológica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

El registro sanitario 208651 aparece repetido cinco veces en los datos; se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 208651 | DIFFERIN® GEL (GALDERMA S.A) | Gel tópico | ADAPALENE (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje alto del modelo (nivel L5), sin ensayos ni literatura. Además, no hay un mecanismo plausible: la absorción sistémica del adapaleno tópico es mínima y el zinc elevado es un hallazgo de laboratorio, no una enfermedad tratable.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA y extraer advertencias y contraindicaciones.
- Completar el mecanismo de acción desde DrugBank.
- Revisar si hay literatura sobre retinoides y homeostasis del zinc.
- Confirmar que «zinc plasmático elevado» sea un objetivo terapéutico válido.
- Evaluar la compatibilidad de vía de administración (tópica frente a sistémica), hoy pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

