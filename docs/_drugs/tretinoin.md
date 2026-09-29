---
layout: default
title: Tretinoin
parent: Solo Predicción del Modelo (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoína: De Combinaciones de Tretinoína (texto de registro) a Nodulosis Reumatoide

## Resumen en Una Frase

Tretinoína (ácido retinoico all-trans) es un retinoide que en Colombia se comercializa en formulaciones tópicas. El registro sanitario solo indica "TETRINOINA COMBINACIONES", sin una indicación descriptiva.
El modelo TxGNN predice que podría ser efectiva para **nodulosis reumatoide**, pero actualmente no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta predicción. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tetrinoína combinaciones (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Nodulosis reumatoide |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Sí se conocen sus dianas farmacológicas: los receptores del ácido retinoico (RARα, RARβ y RARγ), PPARβ/δ, RORβ, TR4 (NR2C2) y TLX (NR2E1). A través de estos receptores, la señalización del ácido retinoico modula la diferenciación de las células T y la inflamación.

Esa es la única base mecanística plausible para relacionar la tretinoína con una enfermedad inflamatoria reumática. Sin embargo, no se encontró ningún vínculo específico de la tretinoína con la nodulosis reumatoide. La similitud con la indicación original está pendiente de evaluar, porque el registro colombiano no describe una indicación clínica concreta.

El puntaje alto de TxGNN (99.84%) refleja la predicción del modelo, no evidencia real. Las siguientes predicciones (artritis idiopática juvenil, poliartritis crónica juvenil, entre otras) están en el mismo grupo de enfermedades inflamatorias articulares. Varias son sinónimos entre sí y no aportan evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 20 registros corresponden a productos de un mismo registro sanitario. Se muestran los valores distintos, sin repetir filas idénticas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19950832 | FOLISTER HAIR LOTION (PROCAPS S.A.) | Solución tópica | Tetrinoína combinaciones; minoxidil |

Las formas farmacéuticas registradas para tretinoína en Colombia incluyen solución tópica, crema tópica y cápsula blanda.

## Consideraciones de Seguridad

- **Población pediátrica**: Varias de las enfermedades predichas son juveniles. El uso sistémico de tretinoína en niños plantearía preocupaciones de toxicidad esquelética y teratogenicidad.
- **Toxicidad esquelética de los retinoides**: Los retinoides sistémicos, con uso prolongado, se asocian con cambios esqueléticos de tipo espondiloartropatía (osificación similar a DISH). Esto es contradictorio con varias de las indicaciones predichas.
- **Interacciones farmacológicas**: No se identificaron interacciones fármaco-fármaco. Las 7 entradas de la consulta corresponden a dianas farmacológicas (receptores), no a fármacos que interactúan.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico específico entre la tretinoína y la nodulosis reumatoide. Además, la seguridad esquelética de los retinoides sistémicos es un riesgo importante en enfermedades articulares.

**Para avanzar se necesita:**
- Obtener del INVIMA el prospecto con advertencias y contraindicaciones, hoy sin datos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación clínica del registro colombiano, que hoy solo dice "combinaciones".
- Realizar una búsqueda dirigida de literatura sobre tretinoína y nodulosis reumatoide.
- Como referencia, entre las 10 predicciones solo la **osteoartritis** (puesto 7) tiene literatura relacionada, nivel L4 y la etiqueta "Research Question". Esa evidencia es mecanística y con señales contradictorias: el ácido retinoico endógeno parece antiinflamatorio, pero un estudio de 2025 describe un modelo de osteoartritis inducida por ácido retinoico. Cualquier hipótesis requeriría administración local o a dosis bajas y un marco de seguridad claro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

