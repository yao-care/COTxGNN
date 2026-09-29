---
layout: default
title: Palonosetron
parent: Solo Predicción del Modelo (L5)
nav_order: 315
evidence_level: L5
indication_count: 5
---

# Palonosetron
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Palonosetrón: De Indicación Original No Detallada a Trastorno de Migraña

## Resumen en Una Frase

Palonosetrón es un antagonista del receptor 5-HT3 comercializado en Colombia como solución inyectable. El registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero **no hay ensayos clínicos** y solo existe **1 publicación**, un reporte de caso que describe al fármaco como **inductor** de cefalea de tipo migrañoso, es decir, en sentido contrario a la predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada (el registro solo repite el nombre "PALONOSETRON") |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L4 (según el Evidence Pack; la única evidencia es un reporte de caso en dirección opuesta) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambos con el mismo número de registro, 20156752) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Palonosetrón pertenece a la clase de los antagonistas del receptor 5-HT3 y está registrado en Colombia como solución inyectable de 250 mcg/5 mL. El registro no indica la indicación aprobada, así que no es posible construir un vínculo mecanístico sólido con la migraña a partir de los datos disponibles.

Además, la señal clínica disponible apunta en contra de la predicción. El único reporte de caso (PMID 21132477) describe cefalea de tipo migrañoso **inducida** por palonosetrón. La cefalea es un efecto adverso conocido de esta clase de fármacos. Por eso, el puntaje alto (0.997) probablemente refleja una asociación en el grafo de conocimiento y no una señal terapéutica real.

Las otras cuatro predicciones del modelo tampoco tienen respaldo:
- **Migraña con aura de tronco encefálico:** sin ensayos ni literatura, y probablemente se explica por su cercanía en el grafo con la migraña.
- **Susceptibilidad a migraña con o sin aura:** la literatura recuperada trata de genética de la epilepsia y no examina palonosetrón.
- **Atrofodermia vermiculada y uleritema ofriógenes:** son dermatosis foliculares raras sin vínculo plausible con el antagonismo 5-HT3.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Reporte de caso | Canadian Journal of Anaesthesia | Describe cefalea de tipo migrañoso inducida por palonosetrón. Sugiere que el fármaco puede desencadenar el cuadro, no tratarlo. El registro no incluye resumen; el hallazgo se toma del título. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20156752 | PALONOSETRON 250.0 MCG /5 ML SOLUCION INYECTABLE (HB Human Bioscience S.A.S.) | Solución inyectable | PALONOSETRON (sin detalle de indicación) |

Nota: los dos registros del Evidence Pack son idénticos y comparten el mismo número de registro, por eso se muestran una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay advertencias, contraindicaciones ni interacciones farmacológicas registradas en el Evidence Pack.

Como dato de contexto, la cefalea es un efecto adverso conocido de los antagonistas 5-HT3. Esto es relevante si se evalúa el fármaco en pacientes con migraña.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos, y la única publicación específica del fármaco sugiere que palonosetrón puede provocar cefalea de tipo migrañoso. El puntaje alto de TxGNN parece un artefacto del grafo de conocimiento y no una señal terapéutica.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias, contraindicaciones e indicación aprobada), un vacío que hoy bloquea el tamizaje de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Buscar evidencia directa sobre antagonistas 5-HT3 en migraña (ensayos, revisiones sistemáticas y datos de farmacovigilancia sobre cefalea).
- Reevaluar solo si aparece evidencia de beneficio. De lo contrario, descartar la indicación, junto con las otras cuatro predicciones sin sustento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

