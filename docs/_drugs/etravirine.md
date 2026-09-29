---
layout: default
title: Etravirine
parent: Solo Predicción del Modelo (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirina: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Felina Adquirida

## Resumen en Una Frase

Etravirina es un inhibidor no nucleósido de la transcriptasa inversa (ITINN) del VIH-1, comercializado en Colombia como INTELENCE®. El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia felina adquirida**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción se basa solo en el modelo y probablemente refleja la cercanía del concepto "virus de inmunodeficiencia" en el grafo, no una farmacología real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro INVIMA solo consigna "ETRAVIRINA" (el nombre del principio activo, sin texto de indicación). Por su clase, se entiende como infección por VIH-1 |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia felina adquirida (FIV) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, etravirina es un ITINN que inhibe la transcriptasa inversa del VIH-1, y su uso en VIH-1 está establecido.

Mecanísticamente, la predicción es débil. La transcriptasa inversa del virus de inmunodeficiencia felina (FIV) se considera poco sensible a los ITINN. El modelo probablemente asignó el puntaje alto por compartir el concepto "virus de inmunodeficiencia", no por afinidad farmacológica demostrada.

Además, "síndrome de inmunodeficiencia felina adquirida" es un término de enfermedad animal, no una indicación clínica humana. Por eso no se ve una vía realista de reposicionamiento. La segunda predicción, la infección por el virus de inmunodeficiencia de simios (SIV), tiene el mismo puntaje y el mismo problema: SIVmac y VIH-2 son intrínsecamente resistentes a los ITINN.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065823 | INTELENCE® TABLETAS 200MG (JANSSEN CILAG S.A.) | Tableta (vía oral) | ETRAVIRINA (sin texto de indicación) |

Los 4 registros del paquete de datos corresponden al mismo número de registro sanitario y al mismo producto.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y el mecanismo argumenta en contra: la transcriptasa inversa de FIV y SIV es poco sensible a los ITINN. Además, la enfermedad predicha es un modelo animal, no una indicación clínica humana.

**Para avanzar se necesita:**
- Descartar esta predicción como candidata clínica, salvo que aparezca evidencia de actividad de etravirina contra la transcriptasa inversa de FIV.
- Completar los datos de mecanismo de acción (MOA) desde DrugBank.
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones, hoy sin datos.
- Completar el campo de indicaciones originales, que está vacío, para distinguir usos ya aprobados de reposicionamiento real. Las predicciones de rango 4 y 5 (complejo relacionado con el SIDA y VIH congénito, ambas L3) parecen ser usos ya aprobados en VIH y no reposicionamiento novedoso.
- Si se busca reposicionamiento real, revisar por separado el ensayo de Fase 2 en ataxia de Friedreich (NCT04273165), que no respalda ninguna de las predicciones de esta lista.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

