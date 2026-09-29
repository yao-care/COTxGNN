---
layout: default
title: Eculizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: De Inhibidor del Complemento C5 a Hematopoyesis Cíclica

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal que inhibe la proteína C5 del complemento. El registro colombiano no detalla su indicación original, pero la literatura recuperada lo asocia con enfermedades mediadas por complemento como la hemoglobinuria paroxística nocturna (HPN) y el síndrome hemolítico urémico atípico (SHUa).
El modelo TxGNN predice que podría ser efectivo para **hematopoyesis cíclica**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección específica. Se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de INVIMA solo repite el nombre del principio activo) |
| Nueva Indicación Predicha | Hematopoyesis cíclica |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, eculizumab es un inhibidor del complemento C5 que bloquea la activación terminal del complemento. Su eficacia se ha documentado en enfermedades causadas por complemento descontrolado, como la HPN, el SHUa y la miastenia gravis.

La hematopoyesis cíclica es un trastorno de la producción de neutrófilos, generalmente ligado a variantes del gen *ELANE*. No se ha establecido ningún mecanismo impulsado por el complemento en esta enfermedad. Por eso, aunque el puntaje del modelo es alto, **no hay un vínculo mecanístico plausible** que lo respalde.

Es probable que la predicción refleje patrones del grafo de conocimiento, y no una relación biológica demostrada. Debe tratarse como una hipótesis sin validar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 13 registros sanitarios en total. Los datos recibidos muestran 2 registros únicos, cuyas entradas estaban repetidas:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20164753 | ELIZARIA® 10 MG/ML | Solución concentrada para infusión | No especificada en el registro |
| 20254329 | BKEMV® 300 MG | Solución concentrada para infusión | No especificada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como nota de contexto, eculizumab aumenta el riesgo de infección meningocócica. Esto sería una preocupación importante en pacientes con neutropenia, que es el cuadro de las indicaciones predichas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura que la respalden (nivel L5). Además, no existe un mecanismo conocido que conecte la inhibición de C5 con la neutropenia cíclica. El riesgo de infecciones graves en pacientes neutropénicos refuerza la cautela.

Los otros nueve candidatos del ranking (neutropenias congénitas, deficiencia de p14 y trastorno de liberación plaquetaria) tampoco tienen respaldo clínico. Las publicaciones asociadas a algunos de ellos tratan de HPN, SHUa o miastenia gravis, y coinciden por el nombre del fármaco, no por la enfermedad.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y una hipótesis biológica que vincule el complemento con la neutropenia cíclica
- Advertencias y contraindicaciones del prospecto de INVIMA, ya que la evaluación de seguridad no puede avanzar sin ellas
- Búsqueda dirigida de estudios preclínicos o reportes de caso que relacionen la inhibición de C5 con la producción de neutrófilos
- Confirmación de la indicación aprobada de cada registro sanitario

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

