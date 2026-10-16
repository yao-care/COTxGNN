---
layout: default
title: Povidone
parent: Solo Predicción del Modelo (L5)
nav_order: 525
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Povidone: nueva indicación predicha, Eritrodermia ictiosiforme congénita (nivel de evidencia L5). Indicación original: Atorvastatina y ezetimibe"
---

# Povidone
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

# Povidona: De Atorvastatina y Ezetimibe a Eritrodermia Ictiosiforme Congénita

## Resumen en Una Frase

Povidona figura en el registro sanitario de Colombia dentro del producto COLMIBE® 40/10 tabletas (atorvastatina y ezetimibe), donde en realidad actúa como excipiente y no como principio activo. El modelo TxGNN predice que podría ser efectivo para **eritrodermia ictiosiforme congénita**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se apoya únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Atorvastatina y ezetimibe |
| Nueva Indicación Predicha | Eritrodermia ictiosiforme congénita |
| Puntaje de Predicción TxGNN | 99.11% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la povidona es un polímero sintético que se usa principalmente como excipiente y aglutinante; en su forma de povidona yodada se emplea como antiséptico tópico. La indicación original que consta en el registro (atorvastatina y ezetimibe) corresponde a un producto combinado en el que la povidona no es el principio activo.

No se pudo establecer un vínculo mecanístico validado entre la povidona y la eritrodermia ictiosiforme congénita. El único respaldo es el puntaje alto del grafo de conocimiento de TxGNN (0.991), que es una inferencia computacional sin corroboración clínica.

Una conexión posible, pero puramente especulativa, sería el efecto emoliente, formador de película y retenedor de humedad sobre piel hiperqueratósica. Ninguna evidencia recuperada respalda esta hipótesis, y además no actuaría sobre el defecto genético de fondo (mutaciones en genes como TGM1, ALOXE3, ALOX12B o NIPAL4, que afectan la barrera epidérmica y el metabolismo lipídico). La compatibilidad de vías de administración tampoco ha sido evaluada: el único producto registrado es oral (tableta).

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
| 20249624 (cancelado) | COLMIBE® 40/10 TABLETAS | Tableta | Atorvastatina y ezetimibe |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia respiratoria, disociación auriculoventricular, bloqueo auriculoventricular y bloqueo cardíaco (término obsoleto).

Para advertencias, contraindicaciones oficiales e interacciones farmacológicas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo, sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico validado. Además, la povidona consta en el registro como excipiente de un producto combinado cuyo único registro sanitario está cancelado.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), indispensable para el tamizaje de seguridad
- Consultar datos del mecanismo de acción en DrugBank
- Aclarar si la hipótesis se refiere a povidona como compuesto activo (p. ej., povidona yodada tópica) o como excipiente
- Realizar una búsqueda sistemática de literatura y ensayos sobre povidona en ictiosis
- Evaluar la compatibilidad de vías de administración (oral frente a tópica) con la nueva indicación
- Aportar estudios preclínicos o de mecanismo que justifiquen un vínculo biológico con las vías genéticas de la enfermedad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

