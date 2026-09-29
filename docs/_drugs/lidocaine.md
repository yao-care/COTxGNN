---
layout: default
title: Lidocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaína: De Lidocaína en Combinaciones a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La lidocaína es un anestésico local, usado para anestesia local y regional y para el alivio del dolor. En Colombia está registrada en combinaciones, por ejemplo supositorios. El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punteada**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Además, el uso tópico repetido en el ojo puede dañar el epitelio corneal.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LIDOCAINA COMBINACIONES |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según los datos farmacológicos incluidos, la lidocaína bloquea canales de sodio dependientes de voltaje (Nav1.2, Nav1.4, Nav1.5, Nav1.7 y Nav1.8). Por eso podría aliviar el dolor de la superficie ocular.

Este mecanismo explica, como mucho, un alivio **sintomático** del dolor. No explica un efecto sobre la enfermedad de fondo. La queratoconjuntivitis epitelial punteada es un daño del epitelio de la córnea y la conjuntiva, y anestesiar la superficie no lo repara.

Además, el uso tópico repetido de lidocaína es conocido por retrasar la cicatrización del epitelio corneal y puede causar toxicidad epitelial. Por eso esta predicción se interpreta mejor como una **posible contraindicación de seguridad** que como una razón terapéutica. El puntaje alto del modelo no basta para justificar una investigación clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 227028 | PROCTO - GLYVENOL® SUPOSITORIOS (HALEON COLOMBIA S.A.S.) | Supositorio | Lidocaína combinaciones |

Nota: la información recibida trae 5 filas, todas del mismo registro 227028, y aquí se muestra una sola vez. El total reportado es de 20 registros. También hay formas tópicas (ungüento y crema) entre las formas farmacéuticas, pero ninguna es oftálmica.

## Consideraciones de Seguridad

- **Riesgo ocular específico**: el uso tópico repetido sobre la superficie ocular puede alterar la cicatrización del epitelio corneal y causar toxicidad epitelial.
- **Interacciones farmacológicas**: la consulta devolvió solo datos de farmacología (dianas de canales de sodio), no interacciones entre medicamentos. No hay datos de interacciones que reportar.

Para las demás advertencias y contraindicaciones, consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y el mecanismo conocido apunta a un posible daño epitelial en lugar de un beneficio. No hay razón científica actual para avanzar con esta indicación.

**Para avanzar se necesita:**
- Prospecto de INVIMA con advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad)
- Datos del mecanismo de acción desde DrugBank
- Evaluación de seguridad de la lidocaína sobre el epitelio corneal, incluyendo el uso repetido
- Evidencia preclínica o clínica directa en queratoconjuntivitis epitelial punteada; sin ella, conviene descartar esta indicación

Entre las otras predicciones, solo la **conjuntivitis atópica** (nivel L4) tiene un mecanismo plausible y comprobable. Se basa en la señalización entre nervios sensitivos y células caliciformes, y se clasifica como pregunta de investigación. No hay ensayos de eficacia directos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

