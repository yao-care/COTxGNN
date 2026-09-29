---
layout: default
title: Palbociclib
parent: Solo Predicción del Modelo (L5)
nav_order: 312
evidence_level: L5
indication_count: 4
---

# Palbociclib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Palbociclib: De Cáncer de Mama HR+/HER2- a Hipertiroidismo

## Resumen en Una Frase

Palbociclib es un inhibidor de las quinasas dependientes de ciclina 4/6 (CDK4/6), usado en cáncer de mama avanzado con receptores hormonales positivos y HER2 negativo.
El modelo TxGNN predice que podría ser efectivo para **hipertiroidismo**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HR+/HER2- (el texto del registro INVIMA solo dice "PALBOCICLIB", sin describir la indicación; el dato proviene de la literatura del paquete de evidencia) |
| Nueva Indicación Predicha | Hipertiroidismo |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Palbociclib es un inhibidor de CDK4/6 que frena la proliferación celular, y su eficacia en cáncer de mama HR+/HER2- está establecida. Sin embargo, no existe un vínculo documentado entre esa inhibición y el hipertiroidismo.

El puntaje de 99.44% (posición 4681 en el ranking del modelo) proviene únicamente del grafo de conocimiento. No hay ensayos, estudios preclínicos ni reportes que expliquen por qué el modelo asocia el fármaco con esta enfermedad. Por eso no es posible afirmar que la predicción sea mecanísticamente razonable, solo que es una hipótesis del modelo aún sin sustento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20195984 | REAMPLA® 125 MG TABLETAS RECUBIERTAS (PFIZER S.A.S.) | Tableta cubierta con película | Solo figura el nombre del principio activo (PALBOCICLIB), sin texto de indicación |

Nota: los cinco registros devueltos corresponden al mismo registro sanitario y producto. El total reportado es de 20 registros.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de CDK4/6). Las categorías de DrugBank no se incluyeron en el paquete; la clasificación se basa en la literatura |
| Riesgo de Mielosupresión | Alto. La literatura describe la supresión de médula ósea como un evento adverso frecuente de los inhibidores de CDK4/6, y estudios preclínicos reportan mielosupresión con palbociclib |
| Clasificación de Emetogenicidad | Baja (los eventos gastrointestinales son comunes, pero el riesgo emetogénico es bajo). Consultar el prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal. Vigilar síntomas respiratorios por el riesgo de enfermedad pulmonar intersticial |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y las normas institucionales de manejo de medicamentos peligrosos |

## Consideraciones de Seguridad

Los datos de advertencias, contraindicaciones e interacciones del registro local no están disponibles. La literatura del paquete de evidencia describe estas señales de seguridad para los inhibidores de CDK4/6:

- **Eventos tromboembólicos**: estudios de farmacovigilancia y cohortes (PMID 36794339, 35300061, 39123221) los reportan como señal de seguridad. Este punto es relevante si se considera cualquier uso fuera de oncología.
- **Mielosupresión y toxicidad gastrointestinal**: eventos adversos frecuentes (PMID 37994878).
- **Enfermedad pulmonar intersticial**: evento menos común pero potencialmente grave (PMID 37994878).

Consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertiroidismo es de nivel L5: no hay ensayos, literatura ni mecanismo documentado, solo un puntaje del modelo. Además, el perfil de mielosupresión y la señal tromboembólica exigen una justificación sólida antes de plantear un uso fuera de oncología.

**Para avanzar se necesita:**
- Una revisión de literatura dirigida que busque un vínculo biológico entre CDK4/6 y el hipertiroidismo.
- Los datos de mecanismo de acción de DrugBank.
- El prospecto de INVIMA con advertencias y contraindicaciones.
- Una evaluación del balance riesgo-beneficio, dado que el hipertiroidismo tiene tratamientos establecidos y menos tóxicos.

Entre las demás predicciones del mismo paquete, la de **artritis reumatoide** (L4) tiene un sustento preclínico y un reporte de caso, por lo que sería una candidata mejor fundamentada para una pregunta de investigación. La predicción de enfermedad trombótica no está respaldada: la evidencia disponible apunta a un riesgo, no a un beneficio.

*Los resultados de este informe son solo para fines de investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

