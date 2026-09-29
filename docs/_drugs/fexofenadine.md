---
layout: default
title: Fexofenadine
parent: Solo Predicción del Modelo (L5)
nav_order: 198
evidence_level: L5
indication_count: 1
---

# Fexofenadine
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

# Fexofenadina: De Alergias Estacionales a Conjuntivitis por Rosácea

## Resumen en Una Frase

La fexofenadina es un antihistamínico oral que se usa para aliviar los síntomas de las alergias estacionales y otras condiciones dependientes de la histamina.
El modelo TxGNN predice que podría ser efectiva para **conjuntivitis por rosácea** (rosácea ocular).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Alergias estacionales y condiciones dependientes de la histamina (el registro sanitario solo indica "Fexofenadina", sin detalle de indicación) |
| Nueva Indicación Predicha | Conjuntivitis por rosácea |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en el paquete de evidencia. Según la información farmacológica conocida, la fexofenadina es un antagonista selectivo del receptor de histamina H1 (gen *HRH1*) con acción periférica. Su utilidad en alergias estacionales está bien establecida.

Una posible conexión, no verificada, es que la rosácea ocular tiene un componente inflamatorio y quizás de tipo alérgico. Bloquear el receptor H1 podría aliviar la picazón y el enrojecimiento.

Sin embargo, el mecanismo es débil. La patología central de la rosácea ocular (disfunción de las glándulas de Meibomio, activación inmune innata, *Demodex* y desregulación vascular) no depende principalmente de la histamina. Este vínculo se infiere de la farmacología general y no proviene de una ruta en el grafo de conocimiento. El puntaje alto del modelo no equivale a evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los cinco registros del listado corresponden al mismo número de registro sanitario (20235810) y se presentan una sola vez. El total reportado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20235810 | NASOFREE® (PROCAPS S.A.) | Tableta recubierta | Fexofenadina (sin texto de indicación detallado) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las advertencias y contraindicaciones del prospecto de INVIMA aún no se han incorporado. La consulta de interacciones devolvió solo la entrada farmacológica del receptor H1 (objetivo del fármaco), sin interacciones con otros medicamentos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo propuesto es débil para la rosácea ocular. Faltan también los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad
- Obtener el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico
- Buscar estudios preclínicos o clínicos de antihistamínicos en rosácea ocular o conjuntivitis inflamatoria
- Evaluar la compatibilidad de vía de administración (la presentación local es solo oral; una indicación ocular podría requerir otra vía)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

