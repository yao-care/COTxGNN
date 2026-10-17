---
layout: default
title: Acetic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 24
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Acetic Acid: nueva indicación predicha, Trastorno post-bacteriano (post-bacterial disorder) (nivel de evidencia L5). Indicación original: Ácido acético"
monitor_inn: "acetic acid"
predicted_indications: ["post-bacterial disorder", "postinfectious vasculitis", "post-infectious syndrome", "Chagas cardiomyopathy", "infective urethral stricture", "infection-related hemolytic uremic syndrome", "drug-induced osteoporosis", "pityriasis simplex", "tinea corporis"]
---

# Acetic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Ácido acético: De ácido acético tópico (ducha vaginal) a Trastorno post-bacteriano

## Resumen en Una Frase

El ácido acético es un compuesto que, según el único registro sanitario colombiano disponible, se comercializó como solución tópica de uso vaginal (ducha vaginal con vinagre).
El modelo TxGNN predice que podría ser efectivo para **trastorno post-bacteriano**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
La predicción se apoya únicamente en el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ácido acético |
| Nueva Indicación Predicha | Trastorno post-bacteriano (post-bacterial disorder) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido acético tiene propiedades antibacterianas y antisépticas (acidificación del medio), pero no hay datos que expliquen su acción frente a un trastorno post-bacteriano.

La relación entre la indicación original (uso tópico antiséptico/acidificante) y la nueva indicación es especulativa. Un trastorno post-bacteriano se refiere a secuelas posteriores a una infección, y no existe un vínculo mecanístico documentado entre el ácido acético y ese tipo de secuelas.

Por lo tanto, la predicción debe considerarse una hipótesis generada por el modelo, sin respaldo clínico ni bibliográfico.

### Otras predicciones y hallazgo relevante

Entre las demás indicaciones predichas, **tinea corporis** (puntaje 99.25%) es la única con literatura relacionada y nivel de evidencia L4. Esa literatura es mayoritariamente histórica (décadas de 1940 y 1950, sobre tinea capitis y epidermofitosis del pie) o indirecta (modelos in vitro de onicomicosis), y no hay ensayos modernos controlados. Su plausibilidad se basa en la acidificación de la piel y la alteración de la membrana fúngica. Se considera una línea de investigación, no una recomendación.

Las demás predicciones (vasculitis postinfecciosa, síndrome postinfeccioso, cardiomiopatía de Chagas, estenosis uretral infecciosa, síndrome urémico hemolítico asociado a infección, osteoporosis inducida por fármacos y pitiriasis simple) tampoco cuentan con ensayos clínicos y carecen de un mecanismo plausible o bien documentado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (trastorno post-bacteriano).

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20019826 (cancelado) | DUCHA VAGINAL INTIMA AZUL - VINAGRE | Solución tópica | Ácido acético |

---

## Consideraciones de Seguridad

- **Señal de seguridad (literatura relacionada con tinea corporis)**: un reporte de casos describe quemaduras por remedios caseros con uso tópico no controlado de ácidos concentrados (PMID 37256034), lo que advierte sobre los riesgos de concentraciones inadecuadas.
- **Contraindicaciones según el grafo de conocimiento del modelo** (no provienen del prospecto): porfiria hereditaria, enfermedad del metabolismo de las porfirinas, porfiria, infección por herpes simple y herpes zóster geniculado.

No se encontraron interacciones farmacológicas registradas. Consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastorno post-bacteriano se basa únicamente en el puntaje del modelo, sin ensayos ni literatura, y el único registro sanitario en Colombia está cancelado. La indicación de tinea corporis podría explorarse como pregunta de investigación, pero su evidencia es histórica e indirecta.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente no disponible
- Obtener datos del mecanismo de acción desde DrugBank
- Realizar una revisión de literatura específica sobre ácido acético y secuelas post-bacterianas
- Si se desea explorar tinea corporis: estudios in vitro y ensayos controlados modernos con concentraciones y formulaciones definidas, y evaluación de seguridad cutánea
- Evaluar la compatibilidad de la vía de administración con la nueva indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

