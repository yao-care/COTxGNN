---
layout: default
title: Doravirine
parent: Solo Predicción del Modelo (L5)
nav_order: 165
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirina: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Doravirina es un inhibidor no nucleósido de la transcriptasa inversa (ITINN) desarrollado contra el VIH-1. En Colombia se comercializa como parte de una combinación fija con lamivudina y tenofovir disoproxilo.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro. El texto solo lista los componentes (lamivudina, tenofovir disoproxilo y doravirina). Por el mecanismo conocido, corresponde a la infección por VIH-1 |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, la doravirina es un ITINN. Se une a un bolsillo alostérico de la transcriptasa inversa del VIH-1 y bloquea la replicación viral.

El virus de inmunodeficiencia felina (VIF) es un lentivirus, como el VIH, y por eso el grafo de conocimiento lo coloca cerca. Sin embargo, es un pariente lejano. Los ITINN se unen a un bolsillo específico del VIH-1, por lo que no se espera actividad contra la transcriptasa inversa del VIF sin datos in vitro.

El puntaje alto (0.999) probablemente refleja la cercanía en el grafo entre lentivirus e inmunodeficiencias, no un mecanismo validado. La predicción debe tratarse como una hipótesis sin respaldo experimental.

Otras predicciones del modelo (ver Conclusión) tampoco cuentan con evidencia directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 8 registros sanitarios corresponden a un mismo producto. La tabla muestra una sola entrada para evitar repeticiones.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20160000 | DELSTRIGO® Tabletas Recubiertas (Merck Sharp & Dohme LLC) | Tableta recubierta (vía oral) | Lamivudina, tenofovir disoproxilo y doravirina |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal es solo del modelo (L5). No hay ensayos ni publicaciones, y el mecanismo sugiere que los ITINN no deberían actuar sobre el VIF. Además, la indicación es veterinaria, ajena al uso humano aprobado en Colombia.

Las otras dos predicciones tampoco son viables con la información actual:
- **Infección por virus de inmunodeficiencia de simio (L4):** el único artículo recuperado (PMID 31658118) trata de islatravir en VIH-1, no de doravirina en VIS. Los ITINN suelen ser inactivos contra VIH-2 y los linajes SIVmac. Está en Hold.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical (L5):** no hay vínculo plausible, probablemente es un artefacto del embedding. Está en Hold.

**Para avanzar se necesita:**
- Datos in vitro de actividad de doravirina contra la transcriptasa inversa del VIF (y del VIS, si se quisiera explorar esa línea)
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA
- Definir si el interés es realmente veterinario, ya que el registro colombiano es de uso humano

*Este resultado es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

