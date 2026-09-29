---
layout: default
title: Levocetirizine
parent: Solo Predicción del Modelo (L5)
nav_order: 256
evidence_level: L5
indication_count: 3
---

# Levocetirizine
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

# Levocetirizina: De Antihistamínico H1 (indicación no detallada en el registro) a Artritis Reumatoide

## Resumen en Una Frase

Levocetirizina es un antihistamínico de segunda generación que bloquea el receptor H1. Está comercializado en Colombia, pero el texto de indicación de sus registros sanitarios solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, aunque actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro (el texto registrado es solo "Levocetirizina") |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 5 (2 números de registro distintos) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, levocetirizina es un antagonista del receptor H1 de histamina de segunda generación. Su uso está establecido en cuadros alérgicos, pero los registros locales no detallan la indicación aprobada.

Existe una razón biológica indirecta para la predicción. La histamina y los mastocitos se han relacionado con la inflamación de la membrana sinovial, y ese sería el puente hacia la artritis reumatoide. Sin embargo, este vínculo es especulativo. No hay mecanismo verificado, ni ensayos, ni publicaciones que lo sustenten.

El puntaje de 99.73% proviene solo de un cálculo del modelo y no equivale a evidencia clínica. Antes de cualquier paso adicional se necesita una revisión bibliográfica dirigida, por ejemplo sobre antihistamínicos H1 en artritis inflamatoria.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 5 registros corresponden a 2 números de registro sanitario distintos. El registro 20232631 aparece repetido 4 veces con datos idénticos, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20126402 | RIZIN® TABLETAS (SAGPHARMA LTDA) | Tableta recubierta | Levocetirizina (sin detalle de indicación) |
| 20232631 | Levocetirizina diclorhidrato 5 mg tabletas recubiertas (GIMED S.A.S.) | Tableta recubierta | Levocetirizina (sin detalle de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero es solo computacional (nivel L5, etapa S0). No hay ensayos, literatura ni mecanismo verificado que la respalden. El vínculo con la artritis reumatoide es apenas plausible de forma indirecta, y por ahora es una pregunta de investigación.

Las otras dos predicciones del modelo (síndrome de microftalmia colobomatosa con displasia rizomélica y síndrome de braquidactilia-sindactilia) no tienen un vínculo mecanístico plausible. Su puntaje alto probablemente es un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Revisión bibliográfica dirigida sobre antihistamínicos H1 en artritis reumatoide e inflamación sinovial.
- Datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Descarga y análisis del prospecto de INVIMA (advertencias y contraindicaciones), que es un bloqueo para el tamizaje de seguridad.
- Confirmar la indicación aprobada en los registros sanitarios colombianos.
- Evaluar la compatibilidad de la vía de administración (oral) con la nueva indicación.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

