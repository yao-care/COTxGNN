---
layout: default
title: Thimerosal
parent: Solo Predicción del Modelo (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Tiomersal: De Antiséptico Tópico a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

El tiomersal es un compuesto organomercurial que se usa como antiséptico tópico y conservante. El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, así que la predicción se basa solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TIOMERSAL (el registro sanitario solo indica el nombre del principio activo, no una indicación clínica detallada) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el tiomersal es un antiséptico y conservante organomercurial, y no tiene ninguna actividad conocida sobre el crecimiento del cabello.

En este caso, la predicción **no parece razonable desde el punto de vista biológico**. El puntaje alto (0.9999) proviene de la cercanía del fármaco con nodos de enfermedades del cabello en el grafo de conocimiento, no de una relación terapéutica demostrada. Además, los organomercuriales de uso tópico pueden causar dermatitis de contacto, lo contrario de lo que necesitaría un tratamiento para la pérdida de cabello.

Las otras nueve predicciones principales del modelo tampoco tienen respaldo:
- **Alopecia, hipotricosis congénita con milia y alopecia areata difusa:** no hay mecanismo inmunomodulador ni estudios. El tiomersal es un sensibilizante de contacto conocido.
- **Glaucoma primario hereditario y de ángulo abierto:** no hay mecanismo plausible, y los conservantes oftálmicos están asociados a daño de la superficie ocular.
- **Acidosis tubular renal y deficiencia de potasio:** probablemente reflejan asociaciones de toxicidad, ya que el mercurio es nefrotóxico y favorece la pérdida renal de potasio.
- **Osteoporosis posmenopáusica e infertilidad masculina por disgenesia gonadal:** no hay efecto conocido sobre el hueso ni evidencia de beneficio. Los compuestos de mercurio se asocian con toxicidad reproductiva.

Todas tienen nivel de evidencia L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24342 | MERTHIOLATE INCOLORO (TINTURA) | Solución tópica | TIOMERSAL |

Nota: los datos reportan 7 registros en total, pero las entradas disponibles corresponden todas al mismo registro sanitario (24342, fabricante TECNOFAR TQ S.A.S), por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones que respalden la predicción (nivel L5), y el perfil conocido del tiomersal (sensibilización cutánea y toxicidad del mercurio) va en contra de su uso en hipotricosis o alopecia.

**Para avanzar se necesita:**
- Mecanismo de acción documentado (por ejemplo, desde DrugBank) y un vínculo mecanístico plausible con el crecimiento del cabello.
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias antes de cualquier evaluación de seguridad.
- Estudios preclínicos o clínicos que muestren un beneficio, y un análisis de la compatibilidad de vía de administración (actualmente pendiente).
- Una evaluación de riesgo-beneficio frente a la toxicidad por mercurio. Mientras no exista evidencia de eficacia, no se recomienda continuar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

