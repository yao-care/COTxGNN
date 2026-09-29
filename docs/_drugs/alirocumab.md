---
layout: default
title: Alirocumab
parent: Solo Predicción del Modelo (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: De Indicación No Registrada (Inhibidor de PCSK9) a Ictiosis Ligada al X sin Deficiencia de Esteroide Sulfatasa

## Resumen en Una Frase

Alirocumab es un anticuerpo monoclonal que neutraliza PCSK9 y reduce el colesterol LDL. Los datos recibidos no traen una indicación original explícita.
El modelo TxGNN predice que podría ser efectivo para **ictiosis ligada al X sin deficiencia de esteroide sulfatasa**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible. El único texto registrado en las licencias es "ALIROCUMAB" (el nombre del principio activo, no una indicación) |
| Nueva Indicación Predicha | Ictiosis ligada al X sin deficiencia de esteroide sulfatasa |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo del fármaco. Según la información conocida, alirocumab es un anticuerpo que neutraliza PCSK9. Con ello aumenta el reciclaje del receptor de LDL en el hígado y reduce el colesterol LDL.

**No se identificó un vínculo mecanístico plausible** con la nueva indicación. La ictiosis ligada al X se relaciona con la esteroide sulfatasa y con la acumulación de sulfato de colesterol en la piel. Esa vía no depende del eje PCSK9/receptor de LDL.

El puntaje alto de TxGNN (0.994) proviene únicamente de la predicción del grafo de conocimiento. No está respaldado por estudios clínicos ni por literatura, así que debe leerse como una hipótesis sin sustento y no como una señal de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20117604 | PRALUENT® 75MG/ML SOLUCIÓN INYECTABLE (Sanofi-Aventis de Colombia S.A.) | Solución inyectable | Solo figura "ALIROCUMAB"; el texto de la indicación no está detallado |

Las cinco entradas devueltas corresponden al mismo registro 20117604, por eso se muestra una sola fila. El total informado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos, literatura ni un mecanismo plausible (L5). El puntaje alto de TxGNN no compensa esa falta de sustento.

**Para avanzar se necesita:**
- Una hipótesis biológica nueva que conecte PCSK9 o el metabolismo del colesterol con la ictiosis ligada al X. Sin ella no se justifica seguir con este candidato.
- Confirmar la indicación original aprobada en INVIMA, ya que el registro solo muestra el nombre del fármaco.
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones) y completar el mecanismo de acción desde DrugBank.

**Nota sobre otros candidatos del mismo paquete:** hay predicciones con más respaldo que la principal.
- *Enfermedad del proceso catabólico del colesterol* (rank 5, L3, "Research Question"): un ensayo de Fase 3 completado con inhibición de PCSK9 (NCT03207945, n=118) y varias revisiones. La evidencia es solo a nivel de clase y no confirma que el fármaco usado fuera alirocumab. Además, podría coincidir con el uso ya aprobado y no ser un reposicionamiento real.
- *Xantomatosis* (rank 3, L4, "Research Question"): plausible de forma indirecta, por reducción del colesterol LDL. Los dos reportes de caso recuperados no muestran que se haya evaluado alirocumab.
- *Defecto de síntesis de colesterol con trastorno del desarrollo sexual 46,XY* (rank 6): en principio está mecanísticamente contraindicado, porque reducir el colesterol LDL podría ser perjudicial.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

