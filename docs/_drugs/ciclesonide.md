---
layout: default
title: Ciclesonide
parent: Solo Predicción del Modelo (L5)
nav_order: 125
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Ciclesonida: De Asma Persistente a Eccema Atópico

## Resumen en Una Frase

Ciclesonida es un glucocorticoide inhalado (profármaco), utilizado originalmente para tratar enfermedades inflamatorias y obstructivas de las vías respiratorias, como el asma persistente.
El modelo TxGNN predice que podría ser efectivo para **eccema atópico**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción del modelo sin estudios reales.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma persistente (según datos farmacológicos; el registro sanitario solo indica "Ciclesonida" sin texto de indicación) |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ciclesonida es un profármaco: se activa a desisobutirilciclesonida, que se une al receptor de glucocorticoides (NR3C1). La forma activa tiene mucha más afinidad por el receptor que el profármaco (IC50 de 1.75 nM frente a 210 nM; Ki de 0.31 nM frente a 37 nM). No se dispone de un texto detallado del mecanismo de acción en el registro del fármaco, pero esta información farmacológica es coherente con su acción antiinflamatoria.

Tanto el asma como el eccema atópico son enfermedades inflamatorias crónicas de tipo alérgico, y los glucocorticoides se usan de forma habitual contra la inflamación en ambas. Por eso el mecanismo es biológicamente plausible para la inflamación de la piel atópica.

Sin embargo, el respaldo actual es solo el puntaje alto del modelo (0.9996). No hay estudios de ciclesonida en piel, y las formas registradas en Colombia son únicamente para inhalación. La compatibilidad de vía de administración y la similitud con la indicación original aún no se han evaluado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20137070 | CICLOVENT® 160 MCG | Solución para inhalación | Solo figura el principio activo (Ciclesonida), sin texto de indicación |
| 20137073 | CICLOVENT® 80 MCG | Solución para inhalación | Solo figura el principio activo (Ciclesonida), sin texto de indicación |

Los datos contienen 8 registros en total. La lista recibida repite varias veces el registro 20137070, por lo que aquí se muestran solo los dos números distintos. El fabricante es CIPLA LTD.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones con otros medicamentos en los datos. El único registro es de farmacología: ciclesonida actúa como ligando del receptor de glucocorticoides.
- **Señal de seguridad de la clase**: existe un reporte de caso (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), *Contact Dermatitis*, 2012) de dermatitis alérgica sistémica por budesonida inhalada, con reactividad cruzada en pruebas epicutáneas con ciclesonida. No es evidencia de eficacia, sino una advertencia sobre posible hipersensibilidad cruzada entre corticoides.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones sobre ciclesonida en eccema atópico. Además, el único producto comercializado es una solución para inhalación, sin vía compatible con uso cutáneo.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad
- Confirmar la indicación aprobada en la etiqueta, ya que el registro solo muestra el nombre del principio activo
- Evaluar la compatibilidad de vía de administración (inhalada frente a la vía requerida para la piel)
- Buscar literatura y ensayos específicos de ciclesonida en dermatitis atópica
- Unificar "atopic eczema" y "dermatitis, atopic", que son el mismo concepto con distinta etiqueta
- Completar los datos del mecanismo de acción desde DrugBank
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

