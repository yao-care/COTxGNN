---
layout: default
title: Cobicistat
parent: Solo Predicción del Modelo (L5)
nav_order: 176
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cobicistat: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Darunavir y cobicistat"
---

# Cobicistat
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

# Cobicistat: De Combinación Darunavir/Cobicistat (VIH) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Cobicistat es un potenciador farmacocinético que se usaba en la combinación darunavir/cobicistat, indicada en Colombia como parte del tratamiento antirretroviral.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Darunavir y cobicistat |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, cobicistat es un inhibidor de CYP3A basado en el mecanismo, utilizado como potenciador farmacocinético de inhibidores de la proteasa del VIH-1 (como darunavir) y de inhibidores de la integrasa (como elvitegravir). No tiene actividad antiviral intrínseca.

El puntaje alto (0.999) probablemente refleja la cercanía en la red de conocimiento con nodos de VIH y lentivirus, a través de sus combinaciones antirretrovirales aprobadas, y no un efecto directo sobre el virus de inmunodeficiencia felina (FIV). Cualquier beneficio dependería de administrarlo junto con un antiviral activo contra el FIV, y no hay datos que demuestren que dicha combinación funcione en gatos.

Cabe señalar que las otras dos predicciones del modelo tienen un puntaje igualmente alto pero poca solidez. La infección por el virus de inmunodeficiencia simia (SIV) es un modelo cercano del VIH, por lo que sería plausible solo como potenciador en regímenes combinados y en investigación preclínica o veterinaria. El trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de la sustancia blanca cortical no tiene un vínculo mecanístico identificable y probablemente es un artefacto de la conectividad del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20104155 (cancelado) | PREZCOBIX® tabletas recubiertas (Janssen Cilag S.A.) | Tableta recubierta | Darunavir y cobicistat |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones. Entre las de nivel **mayor** figuran loperamida, triamcinolona, cisaprida y budesonida. Entre las de nivel **moderado** figuran hidrocortisona, aprepitant, betametasona, clotrimazol, dexametasona, fenfluramina, metoclopramida, repaglinida y claritromicina. Prucalopride tiene nivel **menor**. Muchas de estas interacciones son coherentes con la inhibición de CYP3A.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y cobicistat carece de actividad antiviral propia. Además, el único registro sanitario en Colombia está cancelado y existen numerosas interacciones farmacológicas.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA
- Estudios preclínicos o veterinarios que evalúen cobicistat como potenciador de un antiviral activo contra el FIV
- Evaluación de la compatibilidad de vía de administración y similitud con la indicación original (aún pendientes)
- Aclarar la relevancia clínica y regulatoria de una indicación veterinaria frente al uso humano en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

