---
layout: default
title: Thimerosal
parent: Solo Predicción del Modelo (L5)
nav_order: 623
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Thimerosal: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: Tiomersal"
monitor_inn: "THIMEROSAL"
predicted_indications: ["hypotrichosis simplex of the scalp", "alopecia", "congenital hypotrichosis milia", "diffuse alopecia areata", "primary hereditary glaucoma", "open-angle glaucoma", "renal tubular acidosis", "postmenopausal osteoporosis", "potassium deficiency disease", "male infertility due to gonadal dysgenesis"]
---

# Thimerosal
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Tiomersal: De Antiséptico/Conservante Tópico a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Tiomersal (timerosal) es un compuesto organomercurial utilizado como antiséptico tópico y conservante; en Colombia contó con un registro sanitario para una solución tópica, hoy cancelado.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Se trata de una señal puramente computacional, sin plausibilidad biológica identificada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tiomersal (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el tiomersal es un antiséptico y conservante organomercurial (libera etilmercurio), cuyo uso se ha centrado en la antisepsia tópica y la conservación de productos como vacunas y algunos productos oftálmicos.

**Esta predicción no tiene un respaldo mecanístico sólido.** La hipotricosis es un trastorno genético del desarrollo del folículo piloso, y no se conoce ninguna relación farmacológica entre un compuesto de etilmercurio y dicho desarrollo. El puntaje alto de TxGNN (0.9999) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un efecto terapéutico demostrado.

Además, los compuestos de mercurio son tóxicos y pueden causar efectos dermatológicos adversos. Otras predicciones del modelo para este fármaco siguen el mismo patrón: alopecia, hipotricosis congénita con milia, alopecia areata difusa, glaucoma, acidosis tubular renal, osteoporosis posmenopáusica, déficit de potasio e infertilidad masculina por disgenesia gonadal. En todas se carece de evidencia y de plausibilidad biológica. En varias de ellas (acidosis tubular renal, infertilidad, alopecia) la toxicidad conocida del mercurio sugiere un posible perjuicio en lugar de un beneficio.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24342 | MERTHIOLATE INCOLORO (TINTURA) | Solución tópica | Tiomersal |

El único registro (fabricante: Tecnofar TQ S.A.S.) se encuentra **cancelado**; actualmente no hay productos vigentes con este principio activo.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.
- **Perfil toxicológico general**: aunque no se dispone del prospecto, el tiomersal es un sensibilizante de contacto conocido, y los compuestos de mercurio pueden provocar reacciones dermatológicas, toxicidad ocular y nefrotoxicidad. Estas preocupaciones van en contra de su uso en las indicaciones predichas.

Consultar el prospecto para información adicional de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, sin mecanismo plausible y con señales de toxicidad que contradicen el beneficio. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener los datos de mecanismo de acción desde DrugBank.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), pues su ausencia impide el análisis de seguridad inicial.
- Establecer una justificación biológica verosímil (estudios preclínicos o de mecanismo) antes de considerar cualquier evaluación clínica.
- Evaluar la compatibilidad de vía de administración y la relación de similitud con la indicación original, hoy pendientes.
- Revisar con prioridad la toxicidad del mercurio en las indicaciones predichas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

